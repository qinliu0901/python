#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Gretchen Liu


import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	'''初始化游戏并定义一个屏幕对象'''
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')

	# 创建play按钮
	play_button = Button(ai_settings, screen, "Play")
	# 创建一个用于存储游戏统计信息的实例，创建记分牌
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	# 创建一艘飞船
	ship = Ship(ai_settings, screen)
	# 创建一个存储子弹的编组
	bullets = Group()
	# 创建外星人编组，外星人群
	aliens = Group()
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	'''开始游戏的主循环'''
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
			aliens, bullets) # 响应事件
		
		if stats.game_active:
			ship.update()# 更新飞船
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, 
				bullets)# 更新子弹
			gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens,
				bullets) # 更新外星人
		
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
			play_button) # 更新屏幕

run_game()



