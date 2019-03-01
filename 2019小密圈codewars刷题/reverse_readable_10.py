# -*- coding: utf-8 -*-
"""
@author: qinliu
1.反转一个数字
给定一个数字，写一个函数来输出其反向数字。（例如，给出123答案是321）
数字应该保留他们的标志; 即反转时负数仍应为负数。
比如:
 123 ->  321
-456 -> -654

2.检查ip
编写一种算法，以十进制格式识别有效的IPv4地址。如果IP由四个八位字节组成，其值在0和之间255，则应视为有效。
该函数的输入保证是单个字符串。
例子：有效输入
1.2.3.4
123.45.67.89

请注意，前导零（例如01.02.03.04）被视为无效。
"""
class Test:

    @staticmethod
    def assert_equals(fun, res):
        assert fun == res, 'error'

# Day 10-1

def reverse_number(n):
    if n>=0:
        a = list(str(n))
        a.reverse()
        return int(''.join(a))
    else:
        n = abs(n)
        return -reverse_number(n)
# RamblerW
# def reverse_number(n):
#     # 数字 -> 字符串->反转->转字符串
#     return int(('-' if n < 0 else '') + ''.join(list(reversed(str(abs(n))))))

Test.assert_equals(reverse_number(-456), -654)

# Day 10-2
def is_valid_IP(string):
    s = string.split('.')
    if len(s) != 4:
        return False
    for i in s:
        try:
            if i.count(' ') or str(int(i)) != i or int(i) > 255 or int(i) < 0:
                return False
        except:
            return False    
    return True
# 在try中发生异常的才会到except中去。
Test.assert_equals(is_valid_IP('12.255.56.1'),     True)
Test.assert_equals(is_valid_IP(''),                False)
Test.assert_equals(is_valid_IP('abc.def.ghi.jkl'), False)
Test.assert_equals(is_valid_IP('123.456.789.0'),   False)
Test.assert_equals(is_valid_IP('12.34.56'),        False)
Test.assert_equals(is_valid_IP('12.34.56 .1'),     False)
Test.assert_equals(is_valid_IP('12.34.56.-1'),     False)
Test.assert_equals(is_valid_IP('123.045.067.089'), False)
Test.assert_equals(is_valid_IP('127.1.1.0'),        True)

"""Notes: try语句按照如下方式工作；

首先，执行try子句（在关键字try和关键字except之间的语句）
如果没有异常发生，忽略except子句，try子句执行后结束。
如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。
如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。"""



