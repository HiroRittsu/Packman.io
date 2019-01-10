from Keyboard import *


class Player:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.speed_x = 0
        self.speed_y = 0
        self.size_x = 0
        self.size_y = 0
        self.anim_no = 0.0
        self.max_anim = 0
        self.rate = 1

        self.Controller = Keyboard()

    def change_size(self, rate):
        self.rate = rate

    def set_animation(self, split_x, split_y, step):
        self.animation = True
        self.split_x = split_x
        self.split_y = split_y
        self.size_x = self.width / split_x
        self.size_y = self.height / split_y
        self.max_anim = split_x * split_y
        self.step = step

    def update(self, screen):
        self.calc_speed(screen)
        if self.animation:
            screen.blit(pygame.transform.scale(self.image, (int(self.width * self.rate), int(self.height * self.rate))),
                        [self.x, self.y],
                        [int(self.size_x * int(self.anim_no) * self.rate), 0, int(self.size_x * self.rate),
                         int(self.size_y * self.rate)])
            self.anim_no += self.step
            if self.anim_no >= self.max_anim:
                self.anim_no = 0
        else:
            screen.blit(self.image, [self.x, self.y])

    def calc_speed(self, screen):
        input = self.Controller.get_input()
        if input == Controller.Input.Left:
            self.speed_y += -0.1 / self.rate
        elif input == Controller.Input.Right:
            self.speed_y += 0.1 / self.rate
        elif input == Controller.Input.Null:
            # 減速
            self.speed_y += (-0.1 * (self.speed_y / 5)) / self.rate

        # 範囲制限
        if self.y + self.speed_y > screen.get_height() - (self.height * self.rate):
            self.speed_y = 0
            self.y = screen.get_height() - (self.height * self.rate) - 0.1
        if self.y + self.speed_y < 0:
            self.speed_y = 0
            self.y = 0

        self.x += self.speed_x
        self.y += self.speed_y
