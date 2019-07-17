from environment import after_action_state
from environment import check_game_status
from environment import tomark
from math import inf as infinity
import random
import time


class BaseAgent(object):
    def __init__(self, mark):
        self.mark = mark

    def act(self, board, state, available_actions):

        depth = len(available_actions)
        available_actions_ = list(available_actions)

        if depth == 0 or check_game_status(board) >= 0:
            return

        if len(available_actions) == 9:
            return self.lookup_table(board, available_actions_)
        else:
            board = list(board)
            action = self.minimax(board, available_actions, self.mark)[0]
            new_state = after_action_state(state, action)
            game_status = check_game_status(new_state[0])
            if game_status == 1:
                return action
            else:
                return self.lookup_table(board, available_actions_)

    def minimax(self, board, available_actions, player):
        depth = len(available_actions)

        if player == self.mark:
            best = [-1, -infinity]
        else:
            best = [-1, +infinity]

        if self.mark == 'X':
            human = 'O'
        elif self.mark == 'O':
            human = 'X'

        if depth == 0 or check_game_status(board) >= 0:
            score = self.evaluate(board)
            return [-1, score]

        for action in available_actions:
            board[action] = 1 if player == self.mark else 2
            available_actions.remove(action)
            score = self.minimax(board, available_actions, human if player == self.mark else player)
            board[action] = 0
            score[0] = action

            if player == self.mark:
                if score[1] > best[1]:
                    best = score
            else:
                if score[1] < best[1]:
                    best = score
        return best

    def evaluate(self, board):
        if check_game_status(board) == 2:
            return -1
        elif check_game_status(board) == 1:
            return 1
        else:
            return 0

    def lookup_table(self, board, available_actions):
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
