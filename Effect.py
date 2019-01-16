from Keyboard import *


class Effect:
    def __init__(self, player, width, height, image_dir, image_number, step):
        self.x = player.x
        self.y = player.y
        self.width = width
        self.height = height
        self.image_dir = image_dir
        self.draw = True
        self.image_count = 1.0
        self.image_number = image_number
        self.step = step

    def update(self, screen, player):
        if self.draw:
            if self.image_count <= self.image_number:
                screen.blit(
                    pygame.transform.scale(
                        pygame.image.load(
                            self.image_dir + 'frame-' + str("{0:02d}".format(int(self.image_count))) + '.gif'),
                        (self.width, self.height)), [player.x - self.width / 2, player.y - self.height / 2])
                self.image_count += self.step

    def can_animation(self):
        if self.image_count <= self.image_number:
            return True
        else:
            return False
