#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Gretchen Liu

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""一个外星人类"""
	def __init__(self, ai_settings, screen):
		"""初始化外星人设置初始位置"""
		super().__init__()
		self.screen = screen # 加self的可以供类中所有方法使用
		self.ai_settings = ai_settings

		# 加载外星人图像并获取外接矩形
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# 每个新外星人最初在左上角
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		# 存储外星人的准确位置
		self.x = float(self.rect.x)

	def check_edges(self):
		""" 如果外星人处于屏幕边缘就返回true"""
		screen_rect =self.screen.get_rect()
		if self.rect.right >= screen_rect.right: # right是右边界
			return True
		elif self.rect.left <=0:
			return True

	def update(self):
		"""向左右移动外星人"""
		self.x +=(self.ai_settings.alien_speed_factor * 
					self.ai_settings.fleet_direction)
		self.rect.x = self.x 

	def blitme(self):
		"""在指定位置绘制外星人"""
		self.screen.blit(self.image, self.rect)













