# C
import pygame

COLOR_PURPLE = (28, 14, 64)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

# h
ENTITY_HEALTH = {
    'level1bg0': 999,
    'level1bg1': 999,
    'level1bg2': 999,
    'level1bg3': 999,
    'level2bg0': 999,
    'level2bg1': 999,
    'level2bg2': 999,
    'level2bg3': 999,
    'level2bg4': 999,

    'Player1': 300,
    'Enemy1': 50,
    'Enemy2': 30

}

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'level1bg0': 0,
    'level1bg1': 1,
    'level1bg2': 2,
    'level1bg3': 3,
    'level2bg0': 0,
    'level2bg1': 1,
    'level2bg2': 2,
    'level2bg3': 3,
    'Player1': 3,
    'Enemy1': 2,
    'Enemy2': 1,

}

# M
MENU_OPTION = ('LEVEL 1',
               'LEVEL 2',
               'OPTIONS',
               'SCORE',
               'EXIT')

# S
SPAWN_TIME = 4000
# W
WIN_WIDTH = 576
WINDOW_HEIGHT = 324
