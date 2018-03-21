#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Gretchen Liu

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""一个飞船类,方便创建飞船编组"""
	def __init__(self, ai_settings, screen):
		"""初始化飞船设置初始位置"""
		super().__init__()
		self.screen = screen # 加self的可以供类中所有方法使用
		self.ai_settings = ai_settings

		# 加载飞船图像并获取外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# 将每艘新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# 在飞船的属性center中存储小数值,rect的centerx属性只能存储整数值
		self.center = float(self.rect.centerx)

		# 移动标志
		self.moving_right = False
		self.moving_left = False


	def update(self):
		"""根据移动调整飞船的位置，更新飞船的center值"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center +=self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -=self.ai_settings.ship_speed_factor

		self.rect.centerx = self.center
	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""让飞船在屏幕上居中"""
		self.center = self.screen_rect.centerx