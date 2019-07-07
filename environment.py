from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = '1.0.0'
__author__ = 'Abien Fred Agarap'

import os
import shutil
from utils.config import use_config_1
from utils.markers import BEACON
from utils.markers import GOLD
from utils.markers import PIT

columns = shutil.get_terminal_size().columns
pit_xy, beacon_xy, gold_row, gold_col = use_config_1()
# pit_xy, beacon_xy, gold_row, gold_col = use_config_2()


def setup(miner, cells):

    grid = [['*' for _ in range(cells)] for _ in range(cells)]

    for coordinates in pit_xy:
        grid[coordinates[0]][coordinates[1]] = PIT

    for coordinates in beacon_xy:
        grid[coordinates[0]][coordinates[1]] = BEACON

    grid[gold_row][gold_col] = GOLD
    grid[miner.row][miner.col] = miner.marker

    return grid, pit_xy, beacon_xy, gold_row, gold_col


def display(grid, miner, num_fail):

    grid[miner.row][miner.col] = miner.marker

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

    print('\t|\tminer\t:\t[{}][{}]\t\t|'.format(miner.row, miner.col).center(columns // 3))
    print('\t|\tgold\t:\t[{}][{}]\t\t|'.format(gold_row, gold_col).center(columns // 3))
    print('\t|\t{:<6s}\t:\t{}\t\t|'.format('moves', miner.num_move).center(columns // 3))
    print('\t|\trotate\t:\t{}\t\t|'.format(miner.num_rotate).center(columns // 3))
    print('\t|\tfail\t:\t{}\t\t|'.format(num_fail).center(columns // 3))
