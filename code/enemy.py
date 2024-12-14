#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.EnemyShot import EnemyShot
from code.PlayerShot import PlayerShot
from code.const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shoot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shoot_delay -= 1
        if self.shoot_delay == 0:
            self.shoot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(f'{self.name}Shot', (self.rect.centerx, self.rect.centery))
