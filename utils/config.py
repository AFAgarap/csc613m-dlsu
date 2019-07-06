from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = '1.0.0'
__author__ = 'Abien Fred Agarap'


def use_config_1():
    pit_xy = [[0, 3], [2, 2], [2, 6], [5, 2]]
    beacon_xy = [[4, 0], [0, 4]]
    gold_row, gold_col = 4, 4
    return pit_xy, beacon_xy, gold_row, gold_col


def use_config_2():
    pit_xy = [[21, 0], [21, 1], [20, 2]]
    beacon_xy = [[22, 0], [31, 1]]
    gold_row, gold_col = 22, 1
    return pit_xy, beacon_xy, gold_row, gold_col

