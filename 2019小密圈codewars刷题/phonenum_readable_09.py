# -*- coding: utf-8 -*-
"""
@author: qinliu
1.创建一个电话号码

编写一个接受10个整数（0到9之间）数组的函数，它以电话号码的形式返回这些数字的字符串。
例如：
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"


2.人性化的可读性时间

编写一个函数，它以非负整数（秒）作为输入，并以人类可读的格式返回时间（HH:MM:SS）

- HH =小时，填充到2位数，范围：00 - 99
- MM =分钟，填充到2位数，范围：00 - 59
- SS =秒，填充到2位数，范围：00 - 59

最长时间永远不会超过359999（99:59:59）
"""
""" Day 09-1思路：按3,3,4取出三个列表，将每个列表中的数字转化为字符串再用join连接起来。"""
class Test:

    @staticmethod
    def assert_equals(fun, res):
        assert fun == res, 'error'


def create_phone_number(array):
    tel = {'area': array[:3], 'county': array[3:6], 'town': array[6:]}
    return "({}) {}-{}".format(''.join(list(map(str, tel['area']))), 
        ''.join(list(map(str, tel['county']))),''.join(list(map(str, tel['town']))))
# def create_phone_number(array):
#     arr = ''.join(map(str, array))
#     return "({}) {}-{}".format(arr[:3],arr[3:6],arr[6:])

# 小密圈活着
# return "({}{}{}) {}{}{}-{}{}{}{}".format(*array)

Test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
Test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
Test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")

""" Day 09-2思路：数字除以3600，再依据余数和商分情况讨论。{:0>2d}: >表示数字右对齐方式，2d表示两个宽度的10进制数显示"""
def make_readable(i):
    return "{:0>2d}:{:0>2d}:{:0>2d}".format(i//3600,i%3600//60,i%60) if i <= 359999 else "99:59:59"

Test.assert_equals(make_readable(0), "00:00:00")
Test.assert_equals(make_readable(60), "00:01:00")
Test.assert_equals(make_readable(86399), "23:59:59")

