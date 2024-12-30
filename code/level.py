#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.EntityMediator import EntityMediator
from code.const import COLOR_WHITE, WINDOW_HEIGHT, EVENT_ENEMY, SPAWN_TIME, COLOR_GREEN, EVENT_TIMEOUT, TIMEOUT_STEP, \
    TIMEOUT_LEVEL
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_kills: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + "bg"))
        player = (EntityFactory.get_entity('Player1'))
        player.kills = player_kills[0]
        self.entity_list.append(player)
        self.timeout = TIMEOUT_LEVEL
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_kills: list[int]):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(16, f'Vida : {ent.health} | kills:{ent.kills}', COLOR_GREEN, (10, 30))

            # Check all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End pygame
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_kills[0] = ent.kills
                        return True

            found_player = False
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    found_player = True

            if not found_player:
                return False

            # text
            self.level_text(16, f'{self.name} - Sobreviva: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(16, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WINDOW_HEIGHT - 35))
            self.level_text(16, f'Atirar:Shift', COLOR_WHITE, (10, WINDOW_HEIGHT - 20))
            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)  # collision
            EntityMediator.verify_health(entity_list=self.entity_list)  # health

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
