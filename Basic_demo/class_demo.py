#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Gretchen Liu

# A restaurant class 
class restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(self.restaurant_name + ' is a %s restaurant'%self.cuisine_type)

	def open_restaurant(self):
		print(self.restaurant_name + ' is opening')

	def read_number(self):
		print('there are ' + str(self.number_served) + ' people ate at this restaurant')

	def increment_number_served(self, numbers):
		'''将用餐人数增加指定的量'''
		self.number_served += numbers

restaurants = restaurant('Seven days','French')
restaurants.describe_restaurant()
restaurants.open_restaurant()
restaurants.number_served = 23 # 直接访问属性，也可以通过方法修改属性值
restaurants.increment_number_served(100)
restaurants.read_number()
