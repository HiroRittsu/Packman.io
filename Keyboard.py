import pygame
from Controller import Controller
import os


class Keyboard(Controller):
    def __init__(self):
        Controller.__init__(self)
        pass

    def get_input(self, **kwargs):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] & keys[pygame.K_RIGHT]:
            return Controller.Input.Launch

        if keys[pygame.K_LEFT]:
            return Controller.Input.Left

        if keys[pygame.K_RIGHT]:
            return Controller.Input.Right

        if keys[pygame.K_UP]:
            return Controller.Input.Up

        if keys[pygame.K_DOWN]:
            return Controller.Input.Down

        return Controller.Input.Null

    def close(self):
        os._exit(0)
