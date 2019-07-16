from environment import after_action_state
from environment import check_game_status
from environment import tomark
import random


class BaseAgent(object):
    def __init__(self, mark):
        self.mark = mark

    def act(self, state, available_actions):
        for action in available_actions:
            new_state = after_action_state(state, action)
            game_status = check_game_status(new_state[0])
            if game_status > 0:
                if tomark(game_status) == self.mark:
                    return action
        return random.choice(available_actions)


class HumanAgent(object):
    def __init__(self, mark):
        self.mark = mark

    def act(self, available_actions):
        while True:
            uloc = input("Enter location[1-9], q for quit: ")
            if uloc.lower() == 'q':
                return None
            try:
                action = int(uloc) - 1
                if action not in available_actions:
                    raise ValueError()
            except ValueError:
                print("Illegal location: '{}'".format(uloc))
            else:
                break

        return action
