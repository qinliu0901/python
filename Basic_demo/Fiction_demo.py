#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Gretchen Liu

# 函数定义def fiction()+调用fiction(),实参传递给形参
def make_sanwhichs(*toppings):
	'''概述三明治'''
	print('\nmaking a sanwhich with the following toppings:')
	for topping in toppings:
		print('-' + topping)
make_sanwhichs('meat','cheese','tomato')

def make_car(store,size,**car_info):
	'''创建一个字典，包含有关汽车的一切'''
	profile = {}
	profile['store_name'] = store
	profile['size'] = size
	for key,value in car_info.items():
		profile[key] = value
	return profile

car = make_car('apple','4',color = 'yellow',tow_package = True)
print(car)