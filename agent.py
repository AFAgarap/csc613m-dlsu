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

__version__ = '1.0.0'
__author__ = 'Abien Fred Agarap'

import random
from utils.markers import BEACON
from utils.markers import FACE_EAST
from utils.markers import FACE_NORTH
from utils.markers import FACE_SOUTH
from utils.markers import FACE_WEST
from utils.markers import PIT

random.seed(1024)


class Miner(object):
    def __init__(self, row, col, num_rotate, num_move):
        self.row = row
        self.col = col
        self.marker = FACE_SOUTH
        self.num_rotate = num_rotate
        self.num_move = num_move
        self.visited_nodes = [[row, col]]

    def forward(self, cells, grid):
        while True:
            self.rotate(cells)

            if self.marker == FACE_SOUTH and 0 <= self.row < (cells - 1) and grid[self.row + 1][self.col] != '-':
                self.row += 1
                break
            elif self.marker == FACE_EAST and 0 <= self.col < (cells - 1) and grid[self.row][self.col + 1] != '-':
                self.col += 1
                break
            elif self.marker == FACE_WEST and self.col > 0 and grid[self.row][self.col - 1] != '-':
                self.col -= 1
                break
            elif self.marker == FACE_NORTH and self.row > 0 and grid[self.row - 1][self.col] != '-':
                self.row -= 1
                break

            if 0 < self.row < (cells - 1) and 0 < self.col < (cells - 1) and \
               (grid[self.row + 1][self.col] == '-' and
                grid[self.row - 1][self.col] == '-' and
                grid[self.row][self.col + 1] == '-' and
                grid[self.row][self.col - 1] == '-'):
                return True
            elif self.row == 0 and self.col < (cells - 1) and \
                 ((grid[self.row][self.col + 1] == '-' and
                   grid[self.row][self.col - 1] == '-' and
                   grid[self.row + 1][self.col] == '-') or
                  (grid[self.row + 1][self.col] == '-' and
                   grid[self.row][self.col + 1] == '-') or
                  (grid[self.row][self.col - 1] == '-' and
                   grid[self.row + 1][self.col] == '-')):
                return True
            elif self.row == (cells - 1) and \
                 ((grid[self.row - 1][self.col] == '-' and
                   grid[self.row][self.col + 1] == '-') or
                  (grid[self.row][self.col + 1] == '-' and
                   grid[self.row][self.col - 1] == '-' and
                   grid[self.row - 1][self.col] == '-') or
                  (grid[self.row][self.col - 1] == '-' and
                   grid[self.row - 1][self.col] == '-')):
                return True
            elif self.col == 0 and self.row < (cells - 1) and \
                 ((grid[self.row][self.col + 1] == '-' and
                   grid[self.row + 1][self.col] == '-' and
                   grid[self.row - 1][self.col] == '-') or
                  (grid[self.row + 1][self.col] == '-' and
                   grid[self.row][self.col + 1] == '-') or
                  (grid[self.row - 1][self.col] == '-' and
                   grid[self.row][self.col + 1])):
                return True
            elif self.col == (cells - 1) and \
                 ((grid[self.row][self.col - 1] == '-' and
                   grid[self.row + 1][self.col] == '-' and
                   grid[self.row - 1][self.col] == '-') or
                  (grid[self.row - 1][self.col] == '-' and
                   grid[self.row][self.col - 1] == '-') or
                  (grid[self.row + 1][self.col] == '-' and
                   grid[self.row][self.col - 1] == '-')):
                return True

        self.visited_nodes.append([self.row, self.col])
        self.num_move += 1

    def rotate(self, cells):
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
        if self.row == 0 and self.col < (cells - 1):
            row_peek, col_peek = None, None
            row_values = [cell for cell in grid[self.row]]
            print('row : {}'.format(row_values))
            col_values = [row[self.col] for row in grid]
            print('col : {}'.format(col_values))
            if self.col > 0:
                for index in range(self.col, -1, -1):
                    if row_values[index] == PIT or row_values[index] == BEACON:
                        row_peek = row_values[index]
                        break
            else:
                for index
            for row_value in row_values:
                if row_value == PIT or row_value == BEACON:
                    row_peek = row_value
                    break
            for col_value in col_values:
                if col_value == PIT or col_value == BEACON:
                    col_peek = col_value
                    break
            self.row = 0
            self.col = 7
            return row_peek, col_peek
#        elif (0 < self.row < (cells - 1)) and (0 < self.col < (cells - 1)):
#            north_peek, south_peek, west_peek, east_peek = None, None, None, None
#            east_values = [east_cell for east_cell in grid[self.row:]]
#            west_values = [west_cell for west_cell in grid[ : self.row + 1]]
#            # print(west_values)
#            for east_value in east_values[self.row]:
#                print(east_value, end=' ')
#                if east_value == PIT or east_value == BEACON:
#                    east_peek = east_value
#                    print(east_peek)
#                    break
