#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Gretchen Liu

import pygame.font

class Button():
	"""开始游戏结束游戏的按钮"""
	def __init__(self, ai_settings, screen, msg):
		"""初始化按钮属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		# 设置按钮的尺寸和其它属性
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# 创建按钮的rect对象，并居中
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# 按钮的标签只需创建一次
		self.prep_msg(msg)

	def prep_msg(self, msg):
		"""将msg渲染为图像，使其在按钮上居中，文本msg转化为图像"""
		self.msg_image = self.font.render(msg, True, self.text_color, 
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		# 绘制一个用颜色填充的按钮，再绘制文本
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)