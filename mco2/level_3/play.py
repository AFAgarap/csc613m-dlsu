#!/usr/bin/env python
import os
import sys
import random
import logging
import json
from collections import defaultdict
import click
from tqdm import tqdm as _tqdm

tqdm = _tqdm

from gym_tictactoe.env import TicTacToeEnv
from gym_tictactoe.env import set_log_level_by
from gym_tictactoe.env import agent_by_mark
from gym_tictactoe.env import next_mark
from gym_tictactoe.env import check_game_status
from gym_tictactoe.env import after_action_state
from gym_tictactoe.env import O_REWARD
from gym_tictactoe.env import X_REWARD
from human_agent import HumanAgent


DEFAULT_VALUE = 0
EPISODE_CNT = 17000
BENCH_EPISODE_CNT = 3000
MODEL_FILE = "best_td_agent.dat"
EPSILON = 0.08
ALPHA = 0.4
CWD = os.path.dirname(os.path.abspath(__file__))


st_values = {}
st_visits = defaultdict(lambda: 0)


def reset_state_values():
    global st_values, st_visits
    st_values = {}
    st_visits = defaultdict(lambda: 0)


def set_state_value(state, value):
    st_visits[state] += 1
    st_values[state] = value


def best_val_indices(values, fn):
    best = fn(values)
    return [i for i, v in enumerate(values) if v == best]


class TDAgent(object):
    def __init__(self, mark, epsilon, alpha):
        self.mark = mark
        self.alpha = alpha
        self.epsilon = epsilon
        self.episode_rate = 1.0

    def act(self, state, ava_actions):
        return self.egreedy_policy(state, ava_actions)

    def egreedy_policy(self, state, ava_actions):
        """Returns action by Epsilon greedy policy.

        Return random action with epsilon probability or best action.

        Args:
            state (tuple): Board status + mark
            ava_actions (list): Available actions

        Returns:
            int: Selected action.
        """
        logging.debug("egreedy_policy for '{}'".format(self.mark))
        e = random.random()
        if e < self.epsilon * self.episode_rate:
            logging.debug("Explore with eps {}".format(self.epsilon))
            action = self.random_action(ava_actions)
        else:
            logging.debug("Exploit with eps {}".format(self.epsilon))
            action = self.greedy_action(state, ava_actions)
        return action

    def random_action(self, ava_actions):
        return random.choice(ava_actions)

    def greedy_action(self, state, ava_actions):
        """Return best action by current state value.

        Evaluate each action, select best one. Tie-breaking is random.

        Args:
            state (tuple): Board status + mark
            ava_actions (list): Available actions

        Returns:
            int: Selected action
        """
        assert len(ava_actions) > 0

        ava_values = []
        for action in ava_actions:
            nstate = after_action_state(state, action)
            nval = self.ask_value(nstate)
            ava_values.append(nval)
            vcnt = st_visits[nstate]
            logging.debug(
                "  nstate {} val {:0.2f} visits {}".format(nstate, nval, vcnt)
            )

        # select most right action for 'O' or 'X'
        if self.mark == "O":
            indices = best_val_indices(ava_values, max)
        else:
            indices = best_val_indices(ava_values, min)

        # tie breaking by random choice
        aidx = random.choice(indices)
        logging.debug(
            "greedy_action mark {} ava_values {} indices {} aidx {}".format(
                self.mark, ava_values, indices, aidx
            )
        )

        action = ava_actions[aidx]

        return action

    def ask_value(self, state):
        """Returns value of given state.

        If state is not exists, set it as default value.

        Args:
            state (tuple): State.

        Returns:
            float: Value of a state.
        """
        if state not in st_values:
            logging.debug("ask_value - new state {}".format(state))
            gstatus = check_game_status(state[0])
            val = DEFAULT_VALUE
            # win
            if gstatus > 0:
                val = O_REWARD if self.mark == "O" else X_REWARD
            set_state_value(state, val)
        return st_values[state]

    def backup(self, state, nstate, reward):
        """Backup value by difference and step size.

        Execute an action then backup Q by best value of next state.

        Args:
            state (tuple): Current state
            nstate (tuple): Next state
            reward (int): Immediate reward from action
        """
        logging.debug(
            "backup state {} nstate {} reward {}".format(state, nstate, reward)
        )

        val = self.ask_value(state)
        nval = self.ask_value(nstate)
        diff = nval - val
        val2 = val + self.alpha * diff

        logging.debug("  value from {:0.2f} to {:0.2f}".format(val, val2))
        set_state_value(state, val2)


@click.group()
@click.option("-v", "--verbose", count=True, help="Increase verbosity.")
@click.pass_context
def cli(ctx, verbose):
    global tqdm

    set_log_level_by(verbose)
    if verbose > 0:
        tqdm = lambda x: x  # NOQA


@cli.command(help="Learn and save the model.")
@click.option(
    "-p",
    "--episode",
    "max_episode",
    default=EPISODE_CNT,
    show_default=True,
    help="Episode count.",
)
@click.option(
    "-e",
    "--epsilon",
    "epsilon",
    default=EPSILON,
    show_default=True,
    help="Exploring factor.",
)
@click.option(
    "-a", "--alpha", "alpha", default=ALPHA, show_default=True, help="Step size."
)
@click.option(
    "-f",
    "--save-file",
    default=MODEL_FILE,
    show_default=True,
    help="Save model data as file name.",
)
def learn(max_episode, epsilon, alpha, save_file):
    _learn(max_episode, epsilon, alpha, save_file)


def _learn(max_episode, epsilon, alpha, save_file):
    """Learn by episodes.

    Make two TD agent, and repeat self play for given episode count.
    Update state values as reward coming from the environment.

    Args:
        max_episode (int): Episode count.
        epsilon (float): Probability of exploration.
        alpha (float): Step size.
        save_file: File name to save result.
    """
    reset_state_values()

    env = TicTacToeEnv()
    agents = [TDAgent("O", epsilon, alpha), TDAgent("X", epsilon, alpha)]

    start_mark = "O"
    for i in tqdm(range(max_episode)):
        episode = i + 1
        env.show_episode(False, episode)

        # reset agent for new episode
        for agent in agents:
            agent.episode_rate = episode / float(max_episode)

        env.set_start_mark(start_mark)
        state = env.reset()
        _, mark = state
        done = False
        while not done:
            agent = agent_by_mark(agents, mark)
            ava_actions = env.available_actions()
            env.show_turn(False, mark)
            action = agent.act(state, ava_actions)

            # update (no rendering)
            nstate, reward, done, info = env.step(action)
            agent.backup(state, nstate, reward)

            if done:
                env.show_result(False, mark, reward)
                # set terminal state value
                set_state_value(state, reward)

            _, mark = state = nstate

        # rotate start
        start_mark = next_mark(start_mark)

    # save states
    save_model(save_file, max_episode, epsilon, alpha)


def save_model(save_file, max_episode, epsilon, alpha):
    with open(save_file, "wt") as f:
        # write model info
        info = dict(type="td", max_episode=max_episode, epsilon=epsilon, alpha=alpha)
        # write state values
        f.write("{}\n".format(json.dumps(info)))
        for state, value in st_values.items():
            vcnt = st_visits[state]
            f.write("{}\t{:0.3f}\t{}\n".format(state, value, vcnt))


def load_model(filename):
    with open(filename, "rb") as f:
        # read model info
        info = json.loads(f.readline().decode("ascii"))
        for line in f:
            elms = line.decode("ascii").split("\t")
            state = eval(elms[0])
            val = eval(elms[1])
            vcnt = eval(elms[2])
            st_values[state] = val
            st_visits[state] = vcnt
    return info


@cli.command(help="Play with human.")
@click.option(
    "-f", "--load-file", default=MODEL_FILE, show_default=True, help="Load file name."
)
@click.option(
    "-n",
    "--show-number",
    is_flag=True,
    default=False,
    show_default=True,
    help="Show location number when play.",
)
def play(load_file, show_number):
    _play(load_file, HumanAgent("O"), show_number)


def _play(load_file, vs_agent, show_number):
    """Play with learned model.

    Make TD agent and adversarial agnet to play with.
    Play and switch starting mark when the game finished.
    TD agent behave no exploring action while in play mode.

    Args:
        load_file (str):
        vs_agent (object): Enemy agent of TD agent.
        show_number (bool): Whether show grid number for visual hint.
    """
    load_model(load_file)
    env = TicTacToeEnv(show_number=show_number)
    td_agent = TDAgent("X", 0, 0)  # prevent exploring
    start_mark = "O"
    agents = [vs_agent, td_agent]

    while True:
        # start agent rotation
        env.set_start_mark(start_mark)
        state = env.reset()
        _, mark = state
        done = False

        # show start board for human agent
        if mark == "O":
            env.render(mode="human")

        while not done:
            agent = agent_by_mark(agents, mark)
            human = isinstance(agent, HumanAgent)

            env.show_turn(True, mark)
            ava_actions = env.available_actions()
            if human:
                action = agent.act(ava_actions)
                if action is None:
                    sys.exit()
            else:
                action = agent.act(state, ava_actions)

            state, reward, done, info = env.step(action)

            env.render(mode="human")
            if done:
                env.show_result(True, mark, reward)
                break
            else:
                _, mark = state

        # rotation start
        start_mark = next_mark(start_mark)


if __name__ == "__main__":
    cli()
