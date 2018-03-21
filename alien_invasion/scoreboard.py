#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Gretchen Liu

import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
	"""显示得分信息的类"""
	def __init__(self, ai_settings, screen, stats):
		"""初始化显示得分信息涉及的属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		# 显示得分信息时的字体设置
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		# 准备初始当前得分和最高得分图像,文本装换为图像
		self.prep_score()
		self.prep_hign_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		"""将得分转换为一幅渲染的图像"""
		# 将得分圆整，为10的倍数,round()让小数精确到小数点后几位
		rounded_score = int(round(self.stats.score, -1)) # python3可不要int
		score_str = "{:,}".format(rounded_score)
		self.score_img = self.font.render(score_str, True, self.text_color, 
			self.ai_settings.bg_color)

		# 将得分放在右上角
		self.score_rect = self.score_img.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_hign_score(self):
		"""将最高得分转换为一幅渲染的图像"""
		# 将得分圆整，为10的倍数,round()让小数精确到小数点后几位
		hign_score = int(round(self.stats.hign_score, -1)) # python3可不要int
		hign_score_str = "{:,}".format(hign_score)
		self.hign_score_img = self.font.render(hign_score_str, True, 
			self.text_color, self.ai_settings.bg_color)

		# 将最高得分放在顶部中央
		self.hign_score_rect = self.hign_score_img.get_rect()
		self.hign_score_rect.centerx = self.screen_rect.centerx
		self.hign_score_rect.top = self.score_rect.top

	def prep_level(self):
		"""将等级转换为一幅渲染的图像"""
		self.level_img = self.font.render(str(self.stats.level), True, self.text_color, 
			self.ai_settings.bg_color)

		# 将等级放在得分下面
		self.level_rect = self.level_img.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ships(self):
		"""显示还剩下多少飞船"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)

# 蓝瘦ing，
	def show_score(self):
		"""在屏幕上显示得分，将图像放在score_rect指定的位置"""
		self.screen.blit(self.score_img, self.score_rect)
		self.screen.blit(self.hign_score_img, self.hign_score_rect)
		self.screen.blit(self.level_img, self.level_rect)
		self.ships.draw(self.screen)
