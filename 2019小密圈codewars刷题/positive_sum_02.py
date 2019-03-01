# -*- coding: utf-8 -*-
"""
@author: qinliu
1.求表达式中正数的和

你得到一组数字，返回所有正数的总和。

示例[1,-4,7,12]=>1 + 7 + 12 = 20

注意：如果没有要求的总和，则默认值为0。

"""

# 自己的版本


# def positive_sum(arr):
#     s = 0
#     if len(arr) == 0:
#         return 0
#     for i in arr:
#         if i > 0:
#             s += i
#         else:
#             s += 0
#     return s


# 改进版
def positive_sum(arr):
    s = 0
    return sum([i for i in arr if i > 0])


assert positive_sum([1, 2, -2, 5]) == 8
assert positive_sum([1, 2, 3, 4, 5]) == 15
assert positive_sum([-1, -2, -3, -4, -5]) == 0
