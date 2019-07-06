from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = '1.0.0'
__author__ = 'Abien Fred Agarap'

from config import use_config_1
from markers import *
import os
import random
import shutil
import time

random.seed(42)
columns = shutil.get_terminal_size().columns

miner_row, miner_col = 0, 0
success = False
move = 0

pit_xy, beacon_xy, gold_row, gold_col = use_config_1()


def setup_environment(cells=8):

    grid = [['*' for _ in range(cells)] for _ in range(cells)]

    for coordinates in pit_xy:
        grid[coordinates[0]][coordinates[1]] = PIT

    for coordinates in beacon_xy:
        grid[coordinates[0]][coordinates[1]] = BEACON

    grid[gold_row][gold_col] = GOLD
    grid[miner_row][miner_col] = MINER

    return grid


def print_grid(new_miner_row, new_miner_col):
    grid[new_miner_row][new_miner_col] = MINER
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


while success == False:

    grid = setup_environment()

    rotate = random.randint(1, 4)

    if rotate == 1:
        MINER = FACE_SOUTH
    elif rotate == 2:
        MINER = FACE_EAST
    elif rotate == 3:
        MINER = FACE_WEST
    elif rotate == 4:
        MINER = FACE_NORTH

    move += 1

    old_miner_row, old_miner_col = miner_row, miner_col

    if MINER == FACE_SOUTH and miner_row >= 0 and miner_row < 7:
        old_miner_row = miner_row
        miner_row += 1
        move += 1
    elif MINER == FACE_EAST and miner_col >= 0 and miner_col < 7:
        old_miner_col = miner_col
        miner_col += 1
        move += 1
    elif MINER == FACE_WEST and miner_col > 0 and miner_col > -1:
        old_miner_col = miner_col
        miner_col -= 1
        move += 1
    elif MINER == FACE_NORTH and miner_row > 0 and miner_row > -1:
        old_miner_row = miner_row
        miner_row -= 1
        move += 1

    time.sleep(0.5)

    os.system('clear')
    grid[old_miner_row][old_miner_col] = '*'
    print_grid(miner_row, miner_col)
    print('miner\t:\t[{}][{}]\ngold\t:\t[{}][{}]\nmoves\t:\t{}'.format(miner_row, miner_col, gold_row, gold_col, move))
    print()

    if (miner_row == gold_row) and (miner_col == gold_col):
        print('success in {} moves'.format(move))
        success = True
    elif [miner_row, miner_col] in pit_xy:
        os.system('clear')
        move = 0
        MINER = FACE_SOUTH
        grid = setup_environment()
        miner_row, miner_col = 0, 0
        grid[miner_row][miner_col] = MINER
        print_grid(miner_row, miner_col)
        print('miner\t:\t[{}][{}]\ngold\t:\t[{}][{}]\nmoves\t:\t{}'.format(miner_row, miner_col, gold_row, gold_col, move))

