# C
import pygame

C_GREEN = (80, 250, 123)
C_WHITE = (240, 240, 240)
C_YELLOW = (255, 255, 0)
C_YELLOW2 = (255, 255, 140)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
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
}
ENTITY_HEALTH = {
    'Level1Bg': 999,
    'Level2Bg': 999,
    'Level3Bg': 999,
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
}

ENTITY_SHOT_DELAY = {
    'Player1': 40,
    'Player2': 40,
    'Enemy1-4':200,
}

ENTITY_DAMAGE = {
    'Level1Bg': 0,
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
    'Enemy2Shot': 15,
}

ENTITY_SCORE = {
    'Level1Bg': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 50,
    'Enemy1Shot': 0,
    'Enemy1-2':50,
    'Enemy1-3': 175,
    'Enemy1-4': 200,
    'Enemy1-4Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
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

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
