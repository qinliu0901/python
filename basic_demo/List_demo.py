#!/usr/bin/env python3
# -*- coding: utf-8 -*-

names = ['mike','gretchen','sarah','jane']
print('hello,' + names[1].title() + ',can you eat supper with me?')
names[0] = 'SEVEN'
print('hello,' + names[0].title() + ',can you eat supper with me?')
names.insert(0,'carmie') # 列表开头插入
names.insert(-1,'judy') # 列表末尾插入
print(names[2].title()) # title()方法的对象是列表中的字符串，而不是列表
names.append('sansa')
print(names)
poped_names = names.pop()
print('sorry,' + poped_names + ',I can not invite you eat supper')

poped_names = names.pop()
poped_names = names.pop(2)
del names[1]
names.sort()
names.sort(reverse=True)
names.reverse()
print(sorted(names)) # 临时排序，是一个函数
len(names)
print(names)



