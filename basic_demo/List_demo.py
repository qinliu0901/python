#!/usr/bin/env python3
# -*- coding: utf-8 -*-

names = ['mike','gretchen','sarah','jane']
print('hello,' + names[1].title() + ',can you eat supper with me?')
names[0] = 'SEVEN'
print('hello,' + names[0].title() + ',can you eat supper with me?')
names.insert(0,'carmie') # 列表开头插入
names.insert(-1,'judy') # 列表末尾插入
print(names[2].title()) # title()方法的对象是列表中的字符串，而不是列表,首字母大写
names.append('sansa') # 末尾添加
print(names)
poped_names = names.pop() # 末尾弹出，弹出后赋值给一个变量之后还可以使用
print('sorry,' + poped_names + ',I can not invite you eat supper')

poped_names = names.pop()
poped_names = names.pop(2) # 弹出索引为2的元素
del names[1] # 删除后不能使用
names.sort() # 首字母正向排序
names.sort(reverse=True) # 反向排序
names.reverse() # 列表倒过来输出
print(sorted(names)) # 临时排序，是一个函数
len(names)
dimension = (200,10)
# dimension[0] = 20 # 元组不可以修改里面的元素
dimension = (20,5) # 可以给存储元素的变量赋值
print(dimension)



