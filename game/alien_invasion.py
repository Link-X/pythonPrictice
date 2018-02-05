import pygame
from setting import Setting
from ship import Ship
import game_functions as gf
def run_game():
  #  初始化游戏并创建一个屏幕对象
  pygame.init()
  sets = Setting()

  screen = pygame.display.set_mode((sets.screen_width, sets.screen_height))
  pygame.display.set_caption(sets.title)

  # 创建一个飞船
  ship = Ship(screen)

  #  开始游戏的主循环
  while True:
    #  监视键盘和鼠标事件
    gf.check_envets(ship)
    ship.update()
    gf.update_screen(sets, screen, ship)

run_game()