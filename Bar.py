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
                        math.pi * (2 * (player.hp / self.max)) + math.pi / 2.0, 7)


class Timer_Bar:
    def __init__(self, x, y, width, height, max):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max = max

    def update(self, screen, time):
        pygame.draw.circle(screen, pygame.Color(100, 100, 100, 100),
                           (screen.get_width(), screen.get_height()), 135)
        pygame.draw.arc(screen, (0, 0, 0),
                        (screen.get_width() - self.width / 2, screen.get_height() - self.height / 2, self.width,
                         self.height), math.pi / 2.0, 2 * math.pi + math.pi / 2.0, 25)
        if time > 0:
            pygame.draw.arc(screen, (255, 0, 0),
                            (screen.get_width() - self.width / 2, screen.get_height() - self.height / 2, self.width,
                             self.height), math.pi / 2.0, (math.pi / 2.0) * time / self.max + math.pi / 2.0, 25)
            font = pygame.font.SysFont(None, 40)
            text = font.render("{:.2f}".format(time), True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width() - 45, screen.get_height() - 35))
            screen.blit(text, text_rect)
