from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = '1.0.0'
__author__ = 'Abien Fred Agarap'

from agent import Miner
import os
import random
import shutil
import time
from utils.config import use_config_1
from utils.markers import *

random.seed(42) # solved in 24 moves
# random.seed(8) # solved in 70 moves
columns = shutil.get_terminal_size().columns

# miner_row, miner_col = 0, 0
success = False
move = 0

pit_xy, beacon_xy, gold_row, gold_col = use_config_1()


def setup_environment(miner, cells=8):

    grid = [['*' for _ in range(cells)] for _ in range(cells)]

    for coordinates in pit_xy:
        grid[coordinates[0]][coordinates[1]] = PIT

    for coordinates in beacon_xy:
        grid[coordinates[0]][coordinates[1]] = BEACON

    grid[gold_row][gold_col] = GOLD
    grid[miner.row][miner.col] = miner.marker

    return grid


def print_grid(new_miner_row, new_miner_col, miner):
    grid[new_miner_row][new_miner_col] = miner.marker
    os.system('figlet -c -w {} Miner'.format(columns))
    print('CSC613M Introduction to Intelligent Systems'.center(columns))
    print('DLSU 3rd Trimester A.Y. 2018-2019'.center(columns))
    print()
    for row in grid:
        row_text = ''
        for cell in row:
            row_text += cell + ' '
        print(row_text.center(columns), end='')
        print()


miner = Miner(row=0, col=0)

while success == False:

    grid = setup_environment(miner)

    miner.rotate()
    move += 1

    old_miner_row, old_miner_col = miner.row, miner.col

    miner.forward()
    move += 1
#    rotate = random.randint(1, 4)
#
#    if rotate == 1:
#        MINER = FACE_SOUTH
#    elif rotate == 2:
#        MINER = FACE_EAST
#    elif rotate == 3:
#        MINER = FACE_WEST
#    elif rotate == 4:
#        MINER = FACE_NORTH

#    old_miner_row, old_miner_col = miner_row, miner_col


#    if MINER == FACE_SOUTH and miner_row >= 0 and miner_row < 7:
#        old_miner_row = miner_row
#        miner_row += 1
#        move += 1
#    elif MINER == FACE_EAST and miner_col >= 0 and miner_col < 7:
#        old_miner_col = miner_col
#        miner_col += 1
#        move += 1
#    elif MINER == FACE_WEST and miner_col > 0 and miner_col > -1:
#        old_miner_col = miner_col
#        miner_col -= 1
#        move += 1
#    elif MINER == FACE_NORTH and miner_row > 0 and miner_row > -1:
#        old_miner_row = miner_row
#        miner_row -= 1
#        move += 1

    time.sleep(0.5)

    os.system('clear')
    grid[old_miner_row][old_miner_col] = '*'
    print_grid(miner.row, miner.col, miner)
    print('miner\t:\t[{}][{}]\ngold\t:\t[{}][{}]\nmoves\t:\t{}'.format(miner.row, miner.col, gold_row, gold_col, move))
    print()

    if (miner.row == gold_row) and (miner.col == gold_col):
        print('success in {} moves'.format(move))
        success = True
    elif [miner.row, miner.col] in pit_xy:
        os.system('clear')
        move = 0
#        MINER = FACE_SOUTH
        miner = Miner(row=0, col=0)
        grid = setup_environment(miner)
#        miner_row, miner_col = 0, 0
#        grid[miner_row][miner_col] = miner.marker
        print_grid(miner.row, miner.col, miner)
        print('miner\t:\t[{}][{}]\ngold\t:\t[{}][{}]\nmoves\t:\t{}'.format(miner.row, miner.col, gold_row, gold_col, move))

