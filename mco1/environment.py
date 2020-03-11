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
"""Environment for gold miner."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = "1.0.0"
__author__ = "Abien Fred Agarap"

import os
import shutil
from utils.config import use_config_1
from utils.config import use_config_2
from utils.config import use_config_3
from utils.config import use_config_4
from utils.markers import BEACON
from utils.markers import GOLD
from utils.markers import PIT

columns = shutil.get_terminal_size().columns
# pit_xy, beacon_xy, gold_row, gold_col = use_config_1()
# pit_xy, beacon_xy, gold_row, gold_col = use_config_2()
# pit_xy, beacon_xy, gold_row, gold_col = use_config_3()
pit_xy, beacon_xy, gold_row, gold_col = use_config_4()


def setup(miner, cells):

    grid = [["*" for _ in range(cells)] for _ in range(cells)]

    for coordinates in pit_xy:
        grid[coordinates[0]][coordinates[1]] = PIT

    for coordinates in beacon_xy:
        grid[coordinates[0]][coordinates[1]] = BEACON

    grid[gold_row][gold_col] = GOLD
    grid[miner.row][miner.col] = miner.marker

    return grid, pit_xy, beacon_xy, gold_row, gold_col


def display(grid, miner, num_fail):

    grid[miner.row][miner.col] = miner.marker
    os.system("clear")
    os.system("figlet -c -w {} Miner".format(columns))
    print("CSC613M Introduction to Intelligent Systems".center(columns))
    print("DLSU 3rd Trimester A.Y. 2018-2019".center(columns))
    print()

    for row in grid:
        row_text = ""
        for cell in row:
            row_text += cell + " "
        print(row_text.center(columns), end="")
        print()

    num_move = "0{}".format(miner.num_move) if miner.num_move < 10 else miner.num_move
    num_rotate = (
        "0{}".format(miner.num_rotate) if miner.num_rotate < 10 else miner.num_rotate
    )
    num_fail = "0{}".format(num_fail) if num_fail < 10 else num_fail
    print(
        "\t|\tminer\t:\t[{}][{}]\t\t|".format(miner.row, miner.col).center(columns // 3)
    )
    print("\t|\tgold\t:\t[{}][{}]\t\t|".format(gold_row, gold_col).center(columns // 3))
    print("\t|\t{:<6s}\t:\t{}\t\t|".format("moves", num_move).center(columns // 3))
    print("\t|\trotate\t:\t{}\t\t|".format(num_rotate).center(columns // 3))
    print("\t|\t{:<7s}\t:\t{}\t\t|".format("fail", num_fail).center(columns // 3))


#     row_text = ''
#     for index, node in enumerate(miner.visited_nodes):
#         row_text += ' -> {},{}'.format(node[0], node[1]) if 0 < index < len(miner.visited_nodes) -1 else ' -> {},{}'.format(node[0], node[1])
#         print(row_text.center(columns), end='')
#         print()
