# -*- coding: utf-8 -*-
"""
@author: qinliu
1.未使用的最小的ID

你需要管理大量数据，使用零基础和非负ID来使每个数据项都是唯一的！
因此，需要一个方法来计算下一个新数据项返回最小的未使用ID...
注意：给定的已使用ID数组可能未排序。
出于测试原因，可能存在重复的ID，但你无需查找或删除它们！

"""

# DAY4-1


class Test:

    @staticmethod
    def assert_equals(fun, res):
        assert fun == res, 'error'


def next_id(arr):
    minId = 0
    while minId in arr:
        minId += 1
    return minId


# leoxin

def next_id(array):
    if not array:
        return 0

    sorted_arr = set(sorted(array))
    array = set(range(0, max(array) + 1))
    gap = array - sorted_arr
    if gap:
        return min(gap)
    else:
        return 0 if 0 not in sorted_arr else max(sorted_arr) + 1


Test.assert_equals(next_id([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 11)
Test.assert_equals(next_id([5, 4, 3, 2, 1]), 0)
Test.assert_equals(next_id([0, 1, 2, 3, 5]), 4)
Test.assert_equals(next_id([0, 0, 0, 0, 0, 0]), 1)
Test.assert_equals(next_id([]), 0)
# DAY4-2
import math


def get_middle(aimStr):
    return aimStr[math.ceil(len(aimStr) / 2) - 1: math.floor(len(aimStr) / 2) + 1]


Test.assert_equals(get_middle('test'), 'es')
