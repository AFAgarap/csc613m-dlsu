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
"""Class implementation for the miner agent."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = "1.0.0"
__author__ = "Abien Fred Agarap"

import random
from utils.markers import BEACON
from utils.markers import FACE_EAST
from utils.markers import FACE_NORTH
from utils.markers import FACE_SOUTH
from utils.markers import FACE_WEST
from utils.markers import GOLD
from utils.markers import PIT

random.seed(111)


class Miner(object):
    def __init__(self, row, col, num_rotate, num_move):
        self.row = row
        self.col = col
        self.marker = FACE_SOUTH
        self.num_rotate = num_rotate
        self.num_move = num_move
        self.visited_nodes = [[row, col]]

    def forward(self, cells, grid, level):
        if level == 0:
            self.rotate(cells)
            if self.marker == FACE_SOUTH and 0 <= self.row < (cells - 1):
                self.row += 1
            elif self.marker == FACE_EAST and 0 <= self.col < (cells - 1):
                self.col += 1
            elif self.marker == FACE_WEST and self.col > 0:
                self.col -= 1
            elif self.marker == FACE_NORTH and self.row > 0:
                self.row -= 1
        elif level == 1:
            while True:
                self.rotate(cells)
                if (
                    self.marker == FACE_SOUTH
                    and 0 <= self.row < (cells - 1)
                    and grid[self.row + 1][self.col] != "-"
                ):
                    self.row += 1
                    break
                elif (
                    self.marker == FACE_EAST
                    and 0 <= self.col < (cells - 1)
                    and grid[self.row][self.col + 1] != "-"
                ):
                    self.col += 1
                    break
                elif (
                    self.marker == FACE_WEST
                    and self.col > 0
                    and grid[self.row][self.col - 1] != "-"
                ):
                    self.col -= 1
                    break
                elif (
                    self.marker == FACE_NORTH
                    and self.row > 0
                    and grid[self.row - 1][self.col] != "-"
                ):
                    self.row -= 1
                    break
                if self.is_stuck(cells, grid):
                    return True
        elif level == 2:
            peek, marker = self.scan(cells, grid)
            if peek == -1:
                while True:
                    self.rotate(cells)
                    #                    self.rotate(cells, override=marker, peek=peek)
                    if (
                        self.marker == FACE_SOUTH
                        and 0 <= self.row < (cells - 1)
                        and grid[self.row + 1][self.col] != PIT
                    ):
                        self.row += 1
                        break
                    elif (
                        self.marker == FACE_EAST
                        and 0 <= self.col < (cells - 1)
                        and grid[self.row][self.col + 1] != PIT
                    ):
                        self.col += 1
                        break
                    elif (
                        self.marker == FACE_WEST
                        and self.col > 0
                        and grid[self.row][self.col - 1] != PIT
                    ):
                        self.col -= 1
                        break
                    elif (
                        self.marker == FACE_NORTH
                        and self.row > 0
                        and grid[self.row - 1][self.col] != PIT
                    ):
                        self.row -= 1
                        break
                    if self.is_stuck(cells, grid):
                        return True
            elif peek == 2:
                while True:
                    self.rotate(cells)
                    #                    self.rotate(cells, override=marker, peek=peek)
                    if (
                        self.marker == FACE_SOUTH
                        and 0 <= self.row < (cells - 1)
                        and grid[self.row + 1][self.col] != "-"
                    ):
                        self.row += 1
                        break
                    elif (
                        self.marker == FACE_EAST
                        and 0 <= self.col < (cells - 1)
                        and grid[self.row][self.col + 1] != "-"
                    ):
                        self.col += 1
                        break
                    elif (
                        self.marker == FACE_WEST
                        and self.col > 0
                        and grid[self.row][self.col - 1] != "-"
                    ):
                        self.col -= 1
                        break
                    elif (
                        self.marker == FACE_NORTH
                        and self.row > 0
                        and grid[self.row - 1][self.col] != "-"
                    ):
                        self.row -= 1
                        break
                    if self.is_stuck(cells, grid):
                        return True
            else:
                while True:
                    self.rotate(cells)
                    if (
                        self.marker == FACE_SOUTH
                        and 0 <= self.row < (cells - 1)
                        and grid[self.row + 1][self.col] != "-"
                    ):
                        self.row += 1
                        break
                    elif (
                        self.marker == FACE_EAST
                        and 0 <= self.col < (cells - 1)
                        and grid[self.row][self.col + 1] != "-"
                    ):
                        self.col += 1
                        break
                    elif (
                        self.marker == FACE_WEST
                        and self.col > 0
                        and grid[self.row][self.col - 1] != "-"
                    ):
                        self.col -= 1
                        break
                    elif (
                        self.marker == FACE_NORTH
                        and self.row > 0
                        and grid[self.row - 1][self.col] != "-"
                    ):
                        self.row -= 1
                        break
                    if self.is_stuck(cells, grid):
                        return True

        self.visited_nodes.append([self.row, self.col])
        self.num_move += 1

    def rotate(self, cells, override=0, peek=0):
        if peek != -1 and override != 0:
            if override == 1 and self.row < (cells - 1):
                self.marker = FACE_SOUTH
            elif override == 2 and self.col < (cells - 1):
                self.marker = FACE_EAST
            elif override == 3 and self.col > 0:
                self.marker = FACE_WEST
            elif override == 4 and self.row > 0:
                self.marker = FACE_NORTH
        elif peek == -1 and override != 0:
            while True:
                face = random.randint(1, 4)
                if face != override and face == 1 and self.row < (cells - 1):
                    self.marker = FACE_SOUTH
                    break
                elif face != override and face == 2 and self.col < (cells - 1):
                    self.marker = FACE_EAST
                    break
                elif face != override and face == 3 and self.col > 0:
                    self.marker = FACE_WEST
                    break
                elif face != override and face == 4 and self.row > 0:
                    self.marker = FACE_NORTH
                    break
        else:
            while True:
                face = random.randint(1, 4)
                if face == 1 and self.row < (cells - 1):
                    self.marker = FACE_SOUTH
                    break
                elif face == 2 and self.col < (cells - 1):
                    self.marker = FACE_EAST
                    break
                elif face == 3 and self.col > 0:
                    self.marker = FACE_WEST
                    break
                elif face == 4 and self.row > 0:
                    self.marker = FACE_NORTH
                    break
        self.num_rotate += 1

    def scan(self, cells, grid):
        if self.marker == FACE_SOUTH:
            grid_transpose = list(map(list, zip(*grid)))[self.row]
            for index, cell in enumerate(grid_transpose):
                if cell == BEACON:
                    return self.beacon_scan(grid_transpose[index + 1 :]), 1
                elif cell == PIT:
                    return -1, 1
        elif self.marker == FACE_EAST:
            row = grid[self.row][self.col :]
            for index, cell in enumerate(row):
                if cell == BEACON:
                    return self.beacon_scan(row[index + 1 :]), 2
                elif cell == PIT:
                    return -1, 2
        elif self.marker == FACE_WEST:
            row = grid[self.row][: self.col + 1]
            row_reversed = row[::-1]
            for index, cell in enumerate(row_reversed):
                if cell == BEACON:
                    return self.beacon_scan(row_reversed[index + 1 :]), 3
                elif cell == PIT:
                    return -1, 3
        elif self.marker == FACE_NORTH:
            grid_transpose_reversed = list(map(list, zip(*grid)))[self.row][::-1]
            for index, cell in enumerate(grid_transpose_reversed):
                if cell == BEACON:
                    return self.beacon_scan(grid_transpose_reversed[index + 1 :]), 4
                elif cell == PIT:
                    return -1, 4
        return 0, 0

    def beacon_scan(self, grid):
        for cell in grid:
            if cell == PIT:
                return -1
            elif cell == GOLD:
                return 2

    def is_stuck(self, cells, grid):
        if (
            0 < self.row < (cells - 1)
            and 0 < self.col < (cells - 1)
            and (
                grid[self.row + 1][self.col] == "-"
                and grid[self.row - 1][self.col] == "-"
                and grid[self.row][self.col + 1] == "-"
                and grid[self.row][self.col - 1] == "-"
            )
        ):
            return True
        elif (self.row == 0 and 0 <= self.col < (cells - 1)) and (
            (
                grid[self.row][self.col + 1] == "-"
                and grid[self.row + 1][self.col] == "-"
            )
            or (
                grid[self.row + 1][self.col] == "-"
                and grid[self.row][self.col + 1] == "-"
                and grid[self.row][self.col - 1] == "-"
            )
        ):
            return True
        elif (self.row == 0 and self.col == (cells - 1)) and (
            grid[self.row + 1][self.col] == "-" and grid[self.row][self.col - 1] == "-"
        ):
            return True
        elif (self.row == (cells - 1) and 0 <= self.col < (cells - 1)) and (
            (
                grid[self.row - 1][self.col] == "-"
                and grid[self.row][self.col + 1] == "-"
            )
            or (
                grid[self.row - 1][self.col] == "-"
                and grid[self.row][self.col - 1] == "-"
                and grid[self.row][self.col + 1] == "-"
            )
        ):
            return True
        elif (self.row == (cells - 1) and self.col == (cells - 1)) and (
            grid[self.row - 1][self.col] == "-" and grid[self.row][self.col - 1] == "-"
        ):
            return True
        elif (0 <= self.row < (cells - 1) and self.col == (cells - 1)) and (
            grid[self.row - 1][self.col] == "-"
            and grid[self.row + 1][self.col] == "-"
            and grid[self.row][self.col - 1] == "-"
        ):
            return True
        elif (0 <= self.row < (cells - 1) and self.col == 0) and (
            grid[self.row - 1][self.col] == "-"
            and grid[self.row + 1][self.col] == "-"
            and grid[self.row][self.col + 1] == "-"
        ):
            return True
