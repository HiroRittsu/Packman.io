from Keyboard import *


class Cherry:
    def __init__(self, x, y, speed_x, speed_y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.draw = True

    def move(self, screen, speed_x, speed_y):
        self.x += speed_x
        self.y += speed_y

    def update(self, screen):
        if self.draw:
            self.move(screen, self.speed_x, self.speed_y)
            screen.blit(pygame.transform.scale(self.image, (self.width, self.height)), [self.x, self.y])


class Watch:
    def __init__(self, x, y, speed_x, speed_y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.draw = True

    def move(self, screen, speed_x, speed_y):
        self.x += speed_x
        self.y += speed_y

    def update(self, screen):
        if self.draw:
            self.move(screen, self.speed_x, self.speed_y)
            screen.blit(pygame.transform.scale(self.image, (self.width, self.height)), [self.x, self.y])