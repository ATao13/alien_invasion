import sys

import pygame

from setting import Settings

from ship import Ship

import game_functions as func

def run_game():
    #初始化游戏并建立一个屏幕对象
    pygame.init()
    #建立一个设置的对象
    ai_setting = Settings()
    #建立屏幕对象
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    bg_color = ai_setting.bg_color
    #设置标题
    pygame.display.set_caption("Test")
    #建立飞船的对象
    ship = Ship(screen)
   

    #开始游戏的主循环
    while True:
            #检查鼠标和键盘
            func.check_events(ship)
            #重置屏幕
            func.update_screen(ai_setting,screen,ship)
       


run_game()


