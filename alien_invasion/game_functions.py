#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Gretchen Liu


import sys
import pygame
from bullet import Bullet

# check_events包含形参ship
def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		# 向右移动飞船
		ship.moving_right =True
	elif event.key == pygame.K_LEFT:
		# 向左移动飞船
		ship.moving_left =True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
def fire_bullet(ai_settings, screen, ship, bullets):
	# 创建一个子弹并加入到bullets中
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)
				
def check_keyup_events(event, ship):
	"""响应松开"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right =False
	elif event.key == pygame.K_LEFT:
		ship.moving_left =False

def check_events(ai_settings, screen, ship, bullets):
	"""响应键盘和鼠标事件"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event, ai_settings, screen, ship, bullets)
			elif event.type == pygame.KEYUP:
				check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
	"""更新屏幕上的图像并切换到新屏幕"""
	# 每次循环时都重绘屏幕
	screen.fill(ai_settings.bg_color)
	# 在飞船和外星人后面重绘子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()

	# 让最近绘制的屏幕可见
	pygame.display.flip()
def update_bullets(bullets):
	"""更新子弹位置删除消失子弹"""
	bullets.update()
	# 删除消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <=0:
			bullets.remove(bullet)
