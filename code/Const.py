# C
import pygame

C_GREEN = (80, 250, 123)
C_WHITE = (240, 240, 240)
C_YELLOW = (255, 255, 0)
C_YELLOW2 = (255, 255, 140)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg': 0,
    'Level2Bg': 0,
    'Player1': 3,
    'Player1Shot': 2,
    'Player2': 3,
    'Player2Shot': 2,
    'Enemy1': 1,
    'Enemy1-2': 2,
    'Enemy1-3': 2,
    'Enemy1-4': 1,
    'Enemy1-4Shot': 2,
    'Enemy2': 1,
    'Enemy2-2': 2,
    'Enemy2-3': 2,
    'Enemy2-3Shot': 2,
}
ENTITY_HEALTH = {
    'Level1Bg': 999,
    'Level2Bg': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1-2': 50,
    'Enemy1-3': 50,
    'Enemy1-4': 50,
    'Enemy1-4Shot': 1,
    'Enemy2': 60,
    'Enemy2-2': 100,
    'Enemy2-3': 100,
    'Enemy2-3Shot': 1,
}

ENTITY_SHOT_DELAY = {
    'Player1': 30,
    'Player2': 50,
    'Enemy1-4': 200,
    'Enemy2-3': 100,
}

ENTITY_DAMAGE = {
    'Level1Bg': 0,
    'Level2Bg': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1-2': 1,
    'Enemy1-3': 1,
    'Enemy1-4': 1,
    'Enemy1-4Shot': 80,
    'Enemy2': 1,
    'Enemy2-2': 1,
    'Enemy2-3': 1,
    'Enemy2-3Shot': 100,
}

ENTITY_SCORE = {
    'Level1Bg': 0,
    'Level2Bg': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 50,
    'Enemy1-2': 50,
    'Enemy1-3': 175,
    'Enemy1-4': 200,
    'Enemy1-4Shot': 0,
    'Enemy2': 50,
    'Enemy2-2': 50,
    'Enemy2-3': 175,
    'Enemy2-3Shot': 0,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 3000

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 5000  # 20s

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 120),
             'Label': (WIN_WIDTH / 2, 110),
             'Name': (WIN_WIDTH / 2, 170),
             0: (WIN_WIDTH / 2, 170),
             1: (WIN_WIDTH / 2, 225),
             2: (WIN_WIDTH / 2, 280),
             }
