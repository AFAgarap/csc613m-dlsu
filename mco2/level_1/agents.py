from environment import after_action_state
from environment import check_game_status
from environment import tomark
import random


class BaseAgent(object):
    def __init__(self, mark):
        self.mark = mark

    def act(self, board, state, available_actions):
        for action in available_actions:
            new_state = after_action_state(state, action)
            game_status = check_game_status(new_state[0])
            if game_status > 0:
                if tomark(game_status) == self.mark:
                    return action
        if board[0] == 2 and board[4] == 2 and board[8] == 0:
            return 8
        elif board[0] == 2 and board[1] == 2 and board[2] == 0:
            return 2
        elif board[0] == 2 and board[3] == 2 and board[6] == 0:
            return 6
        elif board[3] == 2 and board[4] == 2 and board[5] == 0:
            return 5
        elif board[6] == 2 and board[7] == 2 and board[8] == 0:
            return 8
        elif board[0] == 2 and board[2] == 2 and board[1] == 0:
            return 1
        elif board[0] == 2 and board[8] == 2 and board[4] == 0:
            return 4
        elif board[0] == 2 and board[6] == 2 and board[3] == 0:
            return 3
        elif board[3] == 2 and board[5] == 2 and board[4] == 0:
            return 4
        elif board[6] == 2 and board[8] == 2 and board[7] == 0:
            return 7
        elif board[2] == 2 and board[8] == 2 and board[5] == 0:
            return 5
        else:
            return random.choice(available_actions)


class HumanAgent(object):
    def __init__(self, mark):
        self.mark = mark

    def act(self, available_actions):
        while True:
            uloc = input("Enter location[1-9], q for quit: ")
            if uloc.lower() == "q":
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
