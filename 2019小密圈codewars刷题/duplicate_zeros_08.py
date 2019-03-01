# -*- coding: utf-8 -*-
"""
@author: qinliu
1.计算重复字母出现的次数

编写一个函数，该函数将返回在输入字符串中出现多次(不同的不区分大小写的)字母字符和数字的计数。可以假定输入字符串仅包含字母（大写和小写）和数字。

例如:
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

2.把0挪到队尾

编写一个算法，该算法采用数组并将所有零移动到最后，保留其他元素的顺序。
例如：
move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

"""
def duplicate_count(str):
    a = {}
    s = str.lower()
    for i in s:
        if not a.get(i):
            a[i] = s.count(i)
    return len([j for j in a.values() if j >= 2])

assert duplicate_count('abcde') == 0
assert duplicate_count("aabbcde") == 2
assert duplicate_count("aabBcde") == 2
assert duplicate_count("ABBA") == 2


def move_zeros(array):
    list = []
    s = []
    for i in array:
        if i == 0 and str(i) != 'False':
            s.append(0)
        else:
            list.append(i)
    return list + s

# 黄帮主
l = [i for i in array if isinstance(i, bool) or i != 0]
return l + [0]*(len(array) - len(l))

# Notes

""" isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type().
isinstance() 与 type() 区别：
type() 不会认为子类是一种父类类型，不考虑继承关系
isinstance() 会认为子类和父类是相同类型，考虑继承关系
如果要判断两个类型是否相同推荐使用 isinstance()."""

assert move_zeros([0,1,None,2,False,1,0]) == [1,None,2,False,1,0,0]
assert move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]) == [9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
assert move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]) == ["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
assert move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]) == ["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0]
assert move_zeros([0,1,None,2,False,1,0]) == [1,None,2,False,1,0,0]
assert move_zeros(["a","b"]) == ["a","b"]
assert move_zeros(["a"]) == ["a"]
assert move_zeros([0,0]) == [0,0]
assert move_zeros([0]) == [0]
assert move_zeros([False]) == [False]
assert move_zeros([]) == []