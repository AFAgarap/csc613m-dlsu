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
"""Configurations for the miner environment."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = '1.0.0'
__author__ = 'Abien Fred Agarap'


def get_speed(rate):
    assert -1 <= rate <= 3, \
        'Expected value for speed : [-1 <= speed <= 3], \
        but given {}.'.format(rate)
    if rate == 0:
        return 5e-1
    elif rate == 1:
        return 3e-1
    elif rate == 2:
        return 1e-1
    elif rate == 3:
        return 1e-4
    elif rate == -1:
        return 0


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


def use_config_3():
    pit_xy = [[8, 17], [9, 17], [10, 18], [10, 19], [10, 21], [0, 19]]
    beacon_xy = [[0, 26], [8, 20]]
    gold_row, gold_col = 0, 20
    return pit_xy, beacon_xy, gold_row, gold_col


def use_config_4():
    pit_xy = [[15, 19], [15, 20], [15, 21], [15, 23], [16, 18], [16, 24], [17, 19], [17, 20], [17, 21], [17, 23]]
    beacon_xy = [[16, 21], [16, 23]]
    gold_row, gold_col = 16, 19
    return pit_xy, beacon_xy, gold_row, gold_col
