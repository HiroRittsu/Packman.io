from Keyboard import *


class Enemy:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.speed_x = 0
        self.speed_y = 0
        self.animation = False
        self.split_x = 0
        self.split_y = 0
        self.size_x = 0
        self.size_y = 0
        self.anim_no = 0
        self.max_anim = 0
        self.draw = False

    def set_animation(self, split_x, split_y, step):
        self.animation = True
        self.split_x = split_x
        self.split_y = split_y
        self.size_x = self.width / split_x
        self.size_y = self.height / split_y
        self.max_anim = split_x * split_y
        self.step = step

    def move(self, screen, speed_x, speed_y):
        self.x += speed_x
        self.y += speed_y

    def update(self, screen):
        if self.draw:
            if self.animation:
                screen.blit(pygame.transform.scale(self.image, (self.width, self.height)), [self.x, self.y],
                            [int(self.size_x * int(self.anim_no)), 0, int(self.size_x), int(self.size_y)])
                self.anim_no += self.step
                if self.anim_no >= self.max_anim:
                    self.anim_no = 0
            else:
                screen.blit(self.image, [self.x, self.y])
