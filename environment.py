from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = '1.0.0'
__author__ = 'Abien Fred Agarap'

import random

grid = [['_' for _ in range(8)] for _ in range(8)]
grid[0][1] = 'P'

for row in grid:
    print('{}'.format(row))
