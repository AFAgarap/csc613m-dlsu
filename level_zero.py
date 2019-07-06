# Copyright 2019 Abien Fred Agarap
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Implementation of random strategy for finding the gold."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = '1.0.0'
__author__ = 'Abien Fred Agarap'

from agent import Miner
from environment import display
from environment import setup
import os
import random
import shutil
import time


random.seed(42)  # solved in 24 moves
# random.seed(8)  # solved in 70 moves
columns = shutil.get_terminal_size().columns

success = False
move = 0
# pit_xy, beacon_xy, gold_row, gold_col = use_config_1()


# def setup_environment(miner, cells=8):
#
#     grid = [['*' for _ in range(cells)] for _ in range(cells)]
#
#     for coordinates in pit_xy:
#         grid[coordinates[0]][coordinates[1]] = PIT
#
#     for coordinates in beacon_xy:
#         grid[coordinates[0]][coordinates[1]] = BEACON
#
#     grid[gold_row][gold_col] = GOLD
#     grid[miner.row][miner.col] = miner.marker
#
#     return grid
#
#
# def print_grid(miner):
#
#     grid[miner.row][miner.col] = miner.marker
#
#     os.system('figlet -c -w {} Miner'.format(columns))
#     print('CSC613M Introduction to Intelligent Systems'.center(columns))
#     print('DLSU 3rd Trimester A.Y. 2018-2019'.center(columns))
#     print()
#
#     for row in grid:
#         row_text = ''
#         for cell in row:
#             row_text += cell + ' '
#         print(row_text.center(columns), end='')
#         print()


miner = Miner(row=0, col=0)

while not success:

    grid, pit_xy, beacon_xy, gold_row, gold_col = setup(miner)

    miner.rotate()
    move += 1

    grid[miner.row][miner.col] = '*'

    miner.forward()
    move += 1

    time.sleep(4e-1)

    os.system('clear')

    display(grid, miner)
    print('miner\t:\t[{}][{}]\ngold\t:\t[{}][{}]\nmoves\t:\t{}'.format(miner.row, miner.col, gold_row, gold_col, move))
    print()

    if (miner.row == gold_row) and (miner.col == gold_col):
        print('success in {} moves'.format(move))
        success = True
    elif [miner.row, miner.col] in pit_xy:
        os.system('clear')
        move = 0
        miner = Miner(row=0, col=0)
        grid, pit_xy, beacon_xy, gold_row, gold_col = setup(miner)
        display(grid, miner)
        print('miner\t:\t[{}][{}]\ngold\t:\t[{}][{}]\nmoves\t:\t{}'.format(miner.row, miner.col, gold_row, gold_col, move))
