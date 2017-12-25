#!/usr/bin/env python3
# -*- coding: utf-8 -*-


####### python basic grammers
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
# dimension[0] = 20 # tuple元组不可以修改里面的元素
dimension = (20,5) # 可以给存储元素的变量赋值
print(dimension)


####### if语句
users = ['admin','sarah','gretchen','sansa','aiya']
if users:
    for user in users:
        if user == 'admin':
            print('hello ' + user + ',would like to see a movie')
        else:
            print('hello,' + user + ',thank you')
else:
    print('we need more users')


####### 字典与列表的嵌套
friend_1 = {
    'first_name': 'male',
    'last_name': 'aiya',
    'age': 18,
    'city': 'beijing',
}
friend_2 = {
    'first_name': 'gretchen',
    'last_name': 'aiya',
    'age': 20,
    'city': 'beijing',
}
friend_3 = {
    'first_name': 'seven',
    'last_name': 'jane',
    'age': 22,
    'city': 'shanghai',
}
friends = [friend_1,friend_2,friend_3]
for friend in friends:
    print(friend)

cities = {
    'beijing':{'country': 'china','population': 70,'fact': 'every one loves hot pot'},
    'paris': {'country': 'french', 'population': 50, 'fact': 'every one loves cake'},
    'new york': {'country': 'america', 'population': 50, 'fact': 'every one loves hamburger'},
}
# 依次将每个键存储在city中（以上三个键），city_info包含城市信息字典，含有三个键
for city,city_info in cities.items():
    print('\ncity: ' + city.title())
    print('In ' + city_info['country'].title() + ', '+ city_info['fact'])


####### while loop




