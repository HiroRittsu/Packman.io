# coding=utf-8
import pygame

from pg_init import screen


class Status:
    def __init__(self, x, y, width, height, max):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max = max

    def calc_bar(self):
        pass

    def update(self, player):
        p_width = player.size_x * player.rate
        p_height = player.size_y * player.rate
        bar_rate = player.rate * 2
        pygame.draw.arc(screen, pygame.Color(0, 255, 0, 0),
                        (player.x - self.width * bar_rate / 2, player.y - self.height * bar_rate / 2,
                         self.width * bar_rate, self.height * bar_rate), 0.1, 10, 7)
