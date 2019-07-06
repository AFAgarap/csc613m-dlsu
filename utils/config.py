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

