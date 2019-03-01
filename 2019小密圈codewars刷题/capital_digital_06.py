# -*- coding: utf-8 -*-
"""
@author: qinliu
1.找到大写字母

写一个函数capitals()给你一串字符串，找到里面的大写字母，并返回它们的index.

比如：
capitals('CodEWaRs')输出为 [0,3,4,6] 
https://www.codewars.com/kata/find-the-capitals-1

2.递归数字总和

写一个函数叫digital_root,给定一个数字，递归遍历数字从个位，十位，百位...以此相加计算总和。
则以这种方式继续减少，直到产生一位数字。这仅适用于自然数

比如:
digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6
"""

# DAY6-1


def capitals(chars):
    return [chars.index(i) for i in chars if 'A' <= i <= 'Z']
# return [chars.index(i) for i in chars if i.isupper()]

assert capitals('CodEWaRs') == [0, 3, 4, 6]
assert capitals('You are the best') == [0]


# DAY6-2
# leoxin

# def digital_root(num):
#     if len(str(num)) == 1:
#         print("=>", num)
#         return num
#     else:
#         arr = list(str(num))
#         print("=>", "+".join(arr))
#         s = sum(map(int,arr))
#         if len(str(s)) > 1:
#             print("=>", s, "...")
#         digital_root(s)

 """九余数定理法:对于十进制数，只要这个数能除尽3/9则他个位数字之和也能除尽3/9
对于十进制数，例如这个数是abcd,他表示的大小就是 x=1000*a+100*b+10*c+d ,

我们对他进行转化x=999*a+99*b+9*c+(a+b+c+d)

                x=9(99*a+9b+c)+(a+b+c+d)

因为9一定能除尽3和9，所以对于x，只要(a+b+c+d)能除尽3和9，则x也能除尽3和9."""

def digital_root(num):
    if num == 0:
        return 0
    return num % 9 == 0 and 9 or num % 9

print(digital_root(19))

