import pygame.key

from code.Const import WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT
from code.Entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)



    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 60:
            self.rect.centery -= 1
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT - 55:
            self.rect.centery += 1
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= 1
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += 1
