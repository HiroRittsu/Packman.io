# Credit the Invent With Python book (http://inventwithpython.com)
# for doRectsOverlap and isPointInsideRect functions
# used to detect collisions in our game

########################################
from pg_init import *
from random import randint


def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or
                (isPointInsideRect(a.left, a.bottom, b)) or
                (isPointInsideRect(a.right, a.top, b)) or
                (isPointInsideRect(a.right, a.bottom, b))):
            return True

    return False


# used the by the doRectsOverlap function (won't be called directly from game code)
def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False


class MovingRectangle:
    def __init__(self, x, y, width, height, speed_x, speed_y, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # (x, y) are measured from the center, so have to subtract width/2 and height/2 from the coordinates
        self.rect = pygame.Rect(x - width / 2, y - height / 2, width, height)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color
        self.ticks = 0  # to prevent continous speed update in case of collision

    def update_rect(self):
        # (x, y) are measured from the center, so have to subtract width/2 and height/2 from the coordinates
        self.rect.x = self.x - self.width / 2
        self.rect.y = self.y - self.height / 2

    def update(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
        # updates the hitbox
        self.update_rect()


class MovingSphere():
    def __init__(self, x, y, radius, speed_x, speed_y, color):
        self.x = x
        self.y = y
        self.radius = radius
        # (x, y) are measured from the center, so have to subtract 1 radius from the coordinates
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color
        self.ticks = 0  # to prevent continous speed update in case of collision

    def update_rect(self):
        # (x, y) are measured from the center, so have to subtract 1 radius from the coordinates
        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius

    def update(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
        # updates the hitbox
        self.update_rect()


def compute_ball_velocity(ball, target_rect):
    if doRectsOverlap(ball.rect, target_rect):
        speed_boost = 1
        temp_ball = MovingSphere(
            ball.x, ball.y, ball.radius, ball.speed_x, ball.speed_y, [0, 0, 0])
        while doRectsOverlap(temp_ball.rect, target_rect):
            if temp_ball.speed_y * ball.speed_y > 0:
                temp_ball.speed_x = ball.speed_x * speed_boost
                temp_ball.speed_y = -ball.speed_y * speed_boost
            else:
                temp_ball.speed_x = -ball.speed_x * speed_boost
                temp_ball.speed_y = ball.speed_y * speed_boost
            temp_ball.update()
            speed_boost = speed_boost * 1.1
        if temp_ball.speed_x * ball.speed_x > 0:
            return ball.speed_x, -ball.speed_y
        else:
            return -ball.speed_x, ball.speed_y
    else:
        return ball.speed_x, ball.speed_y


def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return (red, green, blue)
