# -*- coding: utf-8 -*-
"""
@author: qinliu
1.有序字符数

计算每个字符的出现次数，并按照出现的顺序将其作为元组列表返回。
例如给你一个字符串"abracadabra"，统计里面的字符按照下面的格式输出:

ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
2.缩写双字名称

编写一个函数将名称转换为首字母。这个kata严格地用两个词，它们之间有一个空格。
输出应该是两个大写字母，并用点分隔它们。
它应该如下所示：

    Sam Harris` => `S.H
    Patrick Feeney` => `P.F
"""

# Day01-1自己的版本
str = input('请输入一串字符：')
str_1 = ""
for i in str:
    if i not in str_1:
        str_1 += i

ordered_count = {}
ordered_count[str] = [(i, str.count(i)) for i in str_1]
print(ordered_count[str])


# Ramblerw版本
def ordered_count(str):
    dict = {}
    for char in str:
        # 如果字符在字典中不存在，则追加；存在，则+1
        dict[char] = dict[char] + 1 if char in dict else 1
    return list(zip(dict.keys(), dict.values()))


if __name__ == '__main__':
    str = input('请输入一串字符：')
    ordered_count(str)


# Day01-2

str = input('请输入一字符串：')

def abbrevName(str):
	strResult = ""
	for word in str.split(" "):
	    strResult += word[0].upper() + "."
	return "%s => %s"%(str, strResult[:-1])

