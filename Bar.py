# coding=utf-8
import math

import pygame

from pg_init import screen


class Status:
    def __init__(self, x, y, width, height, max):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max = max

    def update(self, player):
        bar_rate = player.rate * 2
        pygame.draw.arc(screen, pygame.Color(0, 255, 0, 0),
                        (player.x - self.width * bar_rate / 2, player.y - self.height * bar_rate / 2,
                         self.width * bar_rate, self.height * bar_rate), math.pi / 2.0,
                        math.pi * (2 * (player.hp / 100.0)) + math.pi / 2.0, 7)
