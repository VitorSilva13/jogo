#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def update(self, ):
        pass

    def move(self, ):
        pass
