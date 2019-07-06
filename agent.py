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
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.marker = FACE_SOUTH

    def forward(self):
        if self.marker == FACE_SOUTH and 0 <= self.row < 7:
            self.row += 1
        elif self.marker == FACE_EAST and 0 <= self.col < 7:
            self.col += 1
        elif self.marker == FACE_WEST and self.col > 0 and self.col > -1:
            self.col -= 1
        elif self.marker == FACE_NORTH and self.row > 0 and self.row > -1:
            self.row -= 1

    def rotate(self):
        face = random.randint(1, 4)

        if face == 1:
            self.marker = FACE_SOUTH
        elif face == 2:
            self.marker = FACE_EAST
        elif face == 3:
            self.marker = FACE_WEST
        elif face == 4:
            self.marker = FACE_NORTH

