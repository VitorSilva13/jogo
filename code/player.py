#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.PlayerShot import PlayerShot
from code.const import ENTITY_SPEED, WINDOW_HEIGHT, WIN_WIDTH, ENTITY_SHOT_DELAY
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shoot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_w] and self.rect.top > 0:  # subir
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_s] and self.rect.bottom < WINDOW_HEIGHT:  # descer
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_a] and self.rect.left > 0:  # esquerda
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_d] and self.rect.right < WIN_WIDTH:  # direita
            self.rect.centerx += ENTITY_SPEED[self.name]

        pass

    def shoot(self):
        self.shoot_delay -= 1
        if self.shoot_delay == 0:
            self.shoot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_LSHIFT]:
                return PlayerShot(f'{self.name}Shot', (self.rect.centerx, self.rect.centery))
