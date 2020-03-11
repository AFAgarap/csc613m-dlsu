from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = "1.0.0"
__author__ = "Abien Fred Agarap"

from agents import BaseAgent
from agents import HumanAgent
from environment import agent_by_mark
from environment import next_mark
from environment import TicTacToeEnv
import random
import sys


def play():
    first_move = random.randint(1, 100)

    env = TicTacToeEnv(False)
    human = HumanAgent("X")
    machine = BaseAgent("O")
    agents = [human, machine]
    start_mark = "O" if first_move % 2 == 0 else "X"

    while True:
        env.set_start_mark(start_mark)
        state = env.reset()
        _, mark = state
        done = False
        env.render()

        while not done:
            agent = agent_by_mark(agents, mark)
            human = isinstance(agent, HumanAgent)
            env.show_turn(True, mark)
            available_actions = env.available_actions()
            if human:
                action = agent.act(available_actions)
                if action is None:
                    sys.exit()
            else:
                action = agent.act(state, available_actions)

            state, reward, done, info = env.step(action)

            env.render(mode="human")
            if done:
                env.show_result(True, mark, reward)
                break
            else:
                _, mark = state

        start_mark = next_mark(start_mark)


if __name__ == "__main__":
    play()
