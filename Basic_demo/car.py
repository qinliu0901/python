#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Gretchen Liu

'''一个表示汽车的类'''



class Car():
	"""一次模拟汽车的简单尝试"""

	def __init__(self, make, model, year): 
		"""初始化汽车的属性"""
		self.make = make # 以self为前缀的变量都可供类中所有方法使用
		self.model = model # 可以通过类的任何实例来访问这些变量
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""打印描述性名称"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""打印汽车的里程"""
		print('This car has ' + str(self.odometer_reading) + 'miles on it.')

	def update_odometer(self,mileage):
		"""将里程数设为指定的值，拒绝里程表回调"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self,miles):
		"""将里程表读数增加指定的量"""
		self.odometer_reading = miles


# from car import Car

my_new_car = Car('audi', 'a5', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()