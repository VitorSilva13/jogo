# Cores
import pygame

COLOR_PURPLE = (28, 14, 64)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 128, 0)

# vidas
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
    'Player1': 600,
    'Player1Shot': 1,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
    'Enemy1': 50,
    'Enemy2': 30,

}

# danos
ENTITY_DAMAGE = {
    'level1bg0': 0,
    'level1bg1': 0,
    'level1bg2': 0,
    'level1bg3': 0,
    'level2bg0': 0,
    'level2bg1': 0,
    'level2bg2': 0,
    'level2bg3': 0,
    'level2bg4': 0,
    'Player1': 1,
    'Player1Shot': 35,
    'Enemy1Shot': 25,
    'Enemy2Shot': 25,
    'Enemy1': 1,
    'Enemy2': 1,

}

ENTITY_KILLS = {
    'level1bg0': 0,
    'level1bg1': 0,
    'level1bg2': 0,
    'level1bg3': 0,
    'level2bg0': 0,
    'level2bg1': 0,
    'level2bg2': 0,
    'level2bg3': 0,
    'level2bg4': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Enemy1Shot': 0,
    'Enemy2Shot': 0,
    'Enemy1': 1,
    'Enemy2': 1,
}

# Eventos
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'level1bg0': 0,
    'level1bg1': 1,
    'level1bg2': 2,
    'level1bg3': 3,
    'level2bg0': 0,
    'level2bg1': 1,
    'level2bg2': 2,
    'level2bg3': 3,
    'level2bg4': 4,
    'Player1': 3,
    'Player1Shot': 5,
    'Enemy1': 2,
    'Enemy2': 1,
    'Enemy1Shot': 2,
    'Enemy2Shot': 2,

}

# Menu
MENU_OPTION = ('PRESS ENTER',
               'EXIT')
# tiros speed
ENTITY_SHOT_DELAY = {
    'Player1': 18,
    'Enemy1': 50,
    'Enemy2': 52
}

# Spawn time
SPAWN_TIME = 2000
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 60000
# dimensão tela
WIN_WIDTH = 576
WINDOW_HEIGHT = 324
