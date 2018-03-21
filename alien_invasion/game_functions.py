#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Gretchen Liu


import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

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
	elif event.key == pygame.K_q:
		sys.exit()
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

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, 
		bullets):
	"""响应键盘和鼠标事件"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event, ai_settings, screen, ship, bullets)
			elif event.type == pygame.KEYUP:
				check_keyup_events(event, ship)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x,mouse_y = pygame.mouse.get_pos()
				check_play_button(ai_settings, screen, stats, sb, play_button, ship, 
					aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship,
		aliens, bullets, mouse_x, mouse_y):
	"""在玩家点击play按钮开始游戏"""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		# 重置游戏设置
		ai_settings.initialize_dynamic_settings()
		
		# 隐藏光标
		pygame.mouse.set_visible(False)
		# 重置游戏统计信息
		stats.reset_stats()
		stats.game_active = True				

		# 重置记分牌图像
		sb.prep_score()
		sb.prep_hign_score()
		sb.prep_level()
		sb.prep_ships()
		# 清空外星人列表和子弹列表
		aliens.empty()
		bullets.empty()

		# 创建一群新外星人，让飞船居中
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
		play_button):
	"""更新屏幕上的图像并切换到新屏幕"""
	# 每次循环时都重绘屏幕
	screen.fill(ai_settings.bg_color)
	# 在飞船和外星人后面重绘子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
	# 显示得分
	sb.show_score()
	# 如果游戏处于非活动状态，就绘制play按钮
	if not stats.game_active:
		play_button.draw_button()

	# 让最近绘制的屏幕可见
	pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""更新子弹位置删除消失子弹"""
	bullets.update()
	# 删除消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <=0:
			bullets.remove(bullet)

	check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, 
		aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, 
		aliens, bullets):
	# 检查是否有子弹击中了外星人，删除相应子弹外星人,两个true表示删除,两个组之间的
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	# 当有外星人击落时，加分，更新得分
	# 每个值都是一个列表，包含被同一颗子弹击中的所有外星人
	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
			sb.prep_score()
		check_hign_score(stats, sb)

	if len(aliens) == 0:
		# 删除现有子弹,加快游戏节奏，并新建一群外星人
		bullets.empty()
		ai_settings.increase_speed()
		# 提高等级
		stats.level +=1
		sb.prep_level()
		create_fleet(ai_settings, screen, ship, aliens)

def get_number_aliens_x(ai_settings, alien_width):
	"""计算一行可容纳多少个外星人"""
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
	"""计算可容纳多少行外星人"""
	available_space_y = (ai_settings.screen_height - 
							(3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	"""创建一个外星人"""
	# 外星人间距为外星人宽度
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
	"""创建外星人群"""
	# 创建第一个外星人，计算每行外星人数量
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, 
		alien.rect.height)
	# 创建外星人群
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number,
				row_number)

def check_fleet_edges(ai_settings, aliens):
	"""当有外星人到达边缘时"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	""" 整群外星人下移，并改变方向"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
	"""响应被外星人撞到的飞船"""
	if stats.ships_left >0:
		stats.ships_left -= 1

		# 更新记分牌
		sb.prep_ships()
		# 清空外星人列表和子弹列表
		aliens.empty()
		bullets.empty()
		# 创建一群新外星人，飞船放到屏幕低端中央
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)
 
def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens,bullets):
	"""检查是否有外星人到达屏幕底端"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
			break

def update_aliens(ai_settings, stats, sb, screen, ship, aliens,bullets):
	# 检查屏幕边缘，更新外星人的位置
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
	
	# 检查外星人和飞船之间的碰撞，精灵和编组之间的
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, sb, screen, ship, aliens,bullets)
	# 检查是否有外星人到达屏幕底端
	check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens,bullets)

def check_hign_score(stats, sb):
	"""检查是否诞生了新最高分"""
	if stats.score > stats.hign_score:
		stats.hign_score = stats.score
		sb.prep_hign_score()
