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
from utils.markers import FACE_EAST
from utils.markers import FACE_NORTH
from utils.markers import FACE_SOUTH
from utils.markers import FACE_WEST

random.seed(42)


class Miner(object):
    def __init__(self, row, col, num_rotate):
        self.row = row
        self.col = col
        self.marker = FACE_SOUTH
        self.num_rotate = num_rotate

    def forward(self, cells):
        if self.marker == FACE_SOUTH and 0 <= self.row < (cells - 1):
            self.row += 1
        elif self.marker == FACE_EAST and 0 <= self.col < (cells - 1):
            self.col += 1
        elif self.marker == FACE_WEST and self.col > 0:
            self.col -= 1
        elif self.marker == FACE_NORTH and self.row > 0:
            self.row -= 1

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

    def scan(self):
        pass

    def search(self):
        pass

    def manhattan(self):
        pass
