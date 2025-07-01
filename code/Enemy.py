import random

from code.EnemyShot import EnemyShot
from code.Entity import Entity

from code.Const import WIN_WIDTH, ENTITY_SPEED, ENTITY_SHOT_DELAY


class Enemy(Entity):

    def __init__(self, name, position):
        super().__init__(name, position)
        if (self.name == 'Enemy1-4') or (self.name == 'Enemy2-3'):
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]



    def move(self):
        if (self.name == 'Enemy1-4') or (self.name == 'Enemy2-3'):
            if self.rect.centerx >= WIN_WIDTH - random.randrange(30,100, 10):
                self.rect.centerx -= ENTITY_SPEED[self.name]
        else:
            self.rect.centerx -= ENTITY_SPEED[self.name]


    def shoot(self):
        if (self.name == 'Enemy1-4') or (self.name == 'Enemy2-3'):
            self.shot_delay -= 1
            if self.shot_delay == 0:
                self.shot_delay = ENTITY_SHOT_DELAY[self.name]
                if self.name == 'Enemy1-4':
                    return EnemyShot(f'{self.name}Shot', position=(self.rect.centerx - 30, self.rect.centery - 20))
                else:
                    return EnemyShot(f'{self.name}Shot', position=(self.rect.centerx - 30, self.rect.centery - 35))
