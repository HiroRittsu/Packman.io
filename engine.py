import pygame

from Enemy import *
from Player import *


def is_over(player: Player, enemy: Enemy):
    p_width = (player.size_x * player.rate)
    p_height = (player.size_y * player.rate)
    e_width = (enemy.size_x * enemy.rate)
    e_height = (enemy.size_y * enemy.rate)

    if p_width / 2 < (p_width / 2 + e_width / 2) - abs(
            (player.x + p_width / 2) - (enemy.x + e_width / 2)) and p_height / 2 < (
            p_height / 2 + e_height / 2) - abs((player.y + p_height / 2) - (enemy.y + e_height / 2)):
        return True
    else:
        return False


def is_outside(screen, enemy: Enemy):
    if enemy.x < 0:
        return True
    else:
        return False
