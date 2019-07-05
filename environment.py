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

start = 0

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

print('miner\t:\t[{}][{}]\ngold\t:\t[{}][{}]\npit\t:\t[{}][{}]'.format(miner_row, miner_col, gold_row, gold_col, pit_row, pit_col))

def print_grid(miner_row, miner_col, new_miner_row, new_miner_col):
    grid[miner_row][miner_col] = '-'
    grid[new_miner_row][new_miner_col] = miner

    for row in grid:
        print('{}'.format(row))

while (miner_row != gold_row) and (miner_col != gold_col):
    if miner_row < 8:
        new_miner_row = miner_row + 1
    if miner_col < 8:
        new_miner_col = miner_col + 1
    if miner_row > 0:
        new_miner_row = miner_row - 1
    if miner_col > 0:
        new_miner_row = miner_row - 1
    print_grid(miner_row, miner_col, new_miner_row, new_miner_col)
    print()
    if (miner_row == gold_row) and (miner_col == gold_col):
        print('success')
