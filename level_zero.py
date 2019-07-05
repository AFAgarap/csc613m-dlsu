from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = '1.0.0'
__author__ = 'Abien Fred Agarap'

import random

random.seed(42)

pit = 'P'
gold = 'G'
beacon = 'B'
miner = 'v'

miner_row, miner_col = 0, 0

while True:
    pit_row = random.randint(1, 7)
    pit_col = random.randint(1, 7)
    gold_row = random.randint(1, 7)
    gold_col = random.randint(1, 7)
    beacon_row = random.randint(1, 7)
    beacon_col = random.randint(1, 7)
    if pit_row != gold_row != beacon_row and pit_col != gold_col != beacon_col:
        break

grid = [['_' for _ in range(8)] for _ in range(8)]
grid[miner_row][miner_col] = miner
grid[pit_row][pit_col] = pit
grid[gold_row][gold_col] = gold
grid[beacon_row][beacon_col] = beacon


def print_grid(new_miner_row, new_miner_col):
    grid[new_miner_row][new_miner_col] = miner

    for row in grid:
        print('{}'.format(row))

while True:

    print('miner\t:\t[{}][{}]\ngold\t:\t[{}][{}]\npit\t:\t[{}][{}]'.format(miner_row, miner_col, gold_row, gold_col, pit_row, pit_col))

    rotate = random.randint(1, 4)

    if rotate == 1:
        miner = 'v'
    elif rotate == 2:
        miner = '>'
    elif rotate == 3:
        miner = '<'
    elif rotate == 4:
        miner = '^'

    old_miner_row, old_miner_col = miner_row, miner_col

    if miner == 'v':
        if miner_row >= 0 and miner_row < 7:
            old_miner_row = miner_row
            miner_row += 1
    elif miner == '>':
        if miner_col >= 0 and miner_col < 7:
            old_miner_col = miner_col
            miner_col += 1
    elif miner == '<':
        if miner_col > 0 and miner_col > -1:
            old_miner_col = miner_col
            miner_col -= 1
    elif miner == '^':
        if miner_row > 0 and miner_row > -1:
            old_miner_row = miner_row
            miner_row -= 1

    grid[old_miner_row][old_miner_col] = '-'
    print_grid(miner_row, miner_col)
    print()

    if (miner_row == gold_row) and (miner_col == gold_col):
        print('success')
        break
