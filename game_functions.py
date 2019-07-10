import sys

import pygame

def check_events(ship):
    """响应案件和鼠标事件"""
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #向右移动飞船
                ship.rect.centerx += 1




def update_screen(ai_setting,screen,ship):
    """更新屏幕上的图像并切换到新屏幕"""
    #每次循环都重新画屏幕
    screen.fill(ai_setting.bg_color)
    ship.blitme()

    #让最近绘制的屏幕可见
    pygame.display.flip()
