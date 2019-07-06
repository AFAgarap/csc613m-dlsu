from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = '1.0.0'
__author__ = 'Abien Fred Agarap'

import os
import random

random.seed(42)

pit = 'P'
gold = 'G'
beacon = 'B'
miner = 'v'

miner_row, miner_col = 0, 0

# config 1

# pit_xy = [[0, 3], [2, 2], [2, 6], [5, 2]]

# pit_row_0 = 0
# pit_col_0 = 3
#
# pit_row_1 = 2
# pit_col_1 = 2
#
# pit_row_2 = 2
# pit_col_2 = 6
#
# pit_row_3 = 5
# pit_col_3 = 2

# beacon_xy = [[4, 0], [0, 4]]

# beacon_row_0 = 4
# beacon_col_0 = 0

# beacon_row_1 = 0
# beacon_col_1 = 4
gold_row, gold_col = 4, 4
# config 1

# config 2
pit_xy = [[21, 0], [21, 1], [20, 2]]
beacon_xy = [[22, 0], [31, 1]]
gold_row, gold_col = 22, 1
# config 2

# while True:
#     pit_row = random.randint(1, 7)
#     pit_col = random.randint(1, 7)
#     gold_row = random.randint(1, 7)
#     gold_col = random.randint(1, 7)
#     beacon_row = random.randint(1, 7)
#     beacon_col = random.randint(1, 7)
#     if pit_row != gold_row != beacon_row and pit_col != gold_col != beacon_col:
#         break

def setup_environment():

    grid = [['_' for _ in range(32)] for _ in range(32)]
    grid[miner_row][miner_col] = miner

    for coordinates in pit_xy:
        grid[coordinates[0]][coordinates[1]] = pit

    grid[gold_row][gold_col] = gold

    for coordinates in beacon_xy:
        grid[coordinates[0]][coordinates[1]] = beacon

    return grid

def print_grid(new_miner_row, new_miner_col):
    grid[new_miner_row][new_miner_col] = miner

    for row in grid:
        print('{}'.format(row))

success = False
move = 0

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

    if miner == 'v':
        if miner_row >= 0 and miner_row < 7:
            old_miner_row = miner_row
            miner_row += 1
            move += 1
    elif miner == '>':
        if miner_col >= 0 and miner_col < 7:
            old_miner_col = miner_col
            miner_col += 1
            move += 1
    elif miner == '<':
        if miner_col > 0 and miner_col > -1:
            old_miner_col = miner_col
            miner_col -= 1
            move += 1
    elif miner == '^':
        if miner_row > 0 and miner_row > -1:
            old_miner_row = miner_row
            miner_row -= 1
            move += 1

    grid[old_miner_row][old_miner_col] = '-'
    print('miner\t:\t[{}][{}]\ngold\t:\t[{}][{}]'.format(miner_row, miner_col, gold_row, gold_col))
    print_grid(miner_row, miner_col)
    print()

    if (miner_row == gold_row) and (miner_col == gold_col):
        print('success in {} moves'.format(move))
        success = True
    elif [miner_row, miner_col] in pit_xy:
        os.system('clear')
        print('reset')
        move = 0
        miner = 'v'
        grid = setup_environment()
        miner_row, miner_col = 0, 0
        grid[miner_row][miner_col] = miner

