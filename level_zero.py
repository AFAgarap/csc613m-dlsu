from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = '1.0.0'
__author__ = 'Abien Fred Agarap'

import os
import random
import shutil
import time

random.seed(42)
columns = shutil.get_terminal_size().columns

pit = 'P'
gold = 'G'
beacon = 'B'
miner = 'v'

miner_row, miner_col = 0, 0
success = False
move = 0

# config 1
pit_xy = [[0, 3], [2, 2], [2, 6], [5, 2]]
beacon_xy = [[4, 0], [0, 4]]
gold_row, gold_col = 4, 4
# config 1

# config 2
#pit_xy = [[21, 0], [21, 1], [20, 2]]
#beacon_xy = [[22, 0], [31, 1]]
#gold_row, gold_col = 22, 1
# config 2

def setup_environment(cells=8):

    grid = [['*' for _ in range(cells)] for _ in range(cells)]

    for coordinates in pit_xy:
        grid[coordinates[0]][coordinates[1]] = pit

    for coordinates in beacon_xy:
        grid[coordinates[0]][coordinates[1]] = beacon

    grid[gold_row][gold_col] = gold
    grid[miner_row][miner_col] = miner

    return grid


def print_grid(new_miner_row, new_miner_col):
    grid[new_miner_row][new_miner_col] = miner
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
        miner = 'v'
    elif rotate == 2:
        miner = '>'
    elif rotate == 3:
        miner = '<'
    elif rotate == 4:
        miner = '^'

    move += 1

    old_miner_row, old_miner_col = miner_row, miner_col

    if miner == 'v' and miner_row >= 0 and miner_row < 7:
        old_miner_row = miner_row
        miner_row += 1
        move += 1
    elif miner == '>' and miner_col >= 0 and miner_col < 7:
        old_miner_col = miner_col
        miner_col += 1
        move += 1
    elif miner == '<' and miner_col > 0 and miner_col > -1:
        old_miner_col = miner_col
        miner_col -= 1
        move += 1
    elif miner == '^' and miner_row > 0 and miner_row > -1:
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
        miner = 'v'
        grid = setup_environment()
        miner_row, miner_col = 0, 0
        grid[miner_row][miner_col] = miner
        print_grid(miner_row, miner_col)
        print('miner\t:\t[{}][{}]\ngold\t:\t[{}][{}]\nmoves\t:\t{}'.format(miner_row, miner_col, gold_row, gold_col, move))

