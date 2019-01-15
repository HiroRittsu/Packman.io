import pygame

from Enemy import *
from Player import *


def is_over_enemy(player, enemy):
    p_width = (player.size_x * player.rate)
    p_height = (player.size_y * player.rate)
    e_width = (enemy.size_x * enemy.rate)
    e_height = (enemy.size_y * enemy.rate)

    if p_width / 2 < (p_width / 2 + e_width / 2) - abs(player.x - (enemy.x + e_width / 2)) and p_height / 2 < (
            p_height / 2 + e_height / 2) - abs(player.y - (enemy.y + e_height / 2)):
        if p_width > e_width and p_height > e_height:
            return 1
        else:
            return -1
    else:
        return 0


def is_over_item(player, item):
    p_width = (player.size_x * player.rate)
    p_height = (player.size_y * player.rate)
    e_width = item.width
    e_height = item.height

    if p_width / 2 < (p_width / 2 + e_width / 2) - abs(player.x - (item.x + e_width / 2)) and p_height / 2 < (
            p_height / 2 + e_height / 2) - abs(player.y - (item.y + e_height / 2)):
        return True
    else:
        return False


def is_outside(screen, enemy):
    if enemy.x + enemy.size_x * enemy.rate < 0:
        return True
    else:
        return False
