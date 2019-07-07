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

import argparse
from agent import Miner
from environment import display
from environment import setup
import os
import time
from utils.config import get_speed


def parse_args():
    parser = argparse.ArgumentParser(description='Miner')
    group = parser.add_argument_group('Arguments')
    group.add_argument('-c', '--cells', required=False, type=int, default=8,
            help='the size of the environment')
    group.add_argument('-x', '--speed', required=False, type=int, default=1,
            help='the speed of display refresh')
    arguments = parser.parse_args()
    return arguments


def main(arguments):

    cells = arguments.cells
    speed = get_speed(arguments.speed)
    move = 0
    num_fail = 0

    miner = Miner(row=0, col=0, num_rotate=0)

    while True:

        grid, pit_xy, beacon_xy, gold_row, gold_col = setup(miner, cells=cells)
        miner.rotate(cells=cells)
        grid[miner.row][miner.col] = '*'
        miner.forward(cells=cells)
        move += 1

        time.sleep(speed)

        os.system('clear')

        display(grid, miner)
        print('miner\t:\t[{}][{}]\ngold\t:\t[{}][{}]\nmoves\t:\t{}\nrotate\t:\t{}\nFail\t:\t{}'.format(miner.row,
            miner.col, gold_row, gold_col, move, miner.num_rotate, num_fail))
        print()

        if (miner.row == gold_row) and (miner.col == gold_col):
            print('success in {} moves'.format(move))
            break
        elif [miner.row, miner.col] in pit_xy:
            os.system('clear')
            num_fail += 1
            move = 0
            miner = Miner(row=0, col=0, num_rotate=0)
            grid, pit_xy, beacon_xy, gold_row, gold_col = setup(miner, cells=cells)
            display(grid, miner)
            print('miner\t:\t[{}][{}]\ngold\t:\t[{}][{}]\nmoves\t:\t{}\nrotate\t:\t{}\nFail\t:\t{}'.format(miner.row,
                miner.col, gold_row, gold_col, move, miner.num_rotate, num_fail))


if __name__ == '__main__':
    arguments = parse_args()
    main(arguments)
