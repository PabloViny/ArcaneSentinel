import random

from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:


    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                list_bg.append(Background('Level1Bg', (0, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(80, WIN_HEIGHT - 100)))
            case 'Enemy1-2':
                return Enemy('Enemy1-2', (WIN_WIDTH + 10, random.randint(80, WIN_HEIGHT - 100)))
            case 'Enemy1-3':
                return Enemy('Enemy1-3', (WIN_WIDTH + 10, random.randint(80, WIN_HEIGHT - 100)))
            case 'Enemy1-4':
                return Enemy('Enemy1-4', (WIN_WIDTH + 10, random.randint(80, WIN_HEIGHT - 100)))