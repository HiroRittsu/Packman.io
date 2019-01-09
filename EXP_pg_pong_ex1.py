from pg_engine import *
from Controller import *  # new import
from EMG import *  # new import
from engine import *


class game:

    def __init__(self):
        self.start()
        self.running = True
        while self.running:
            for event in pygame.event.get():
                # checks if you've exited the game
                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    self.running = False

            self.update()
            pygame.display.update()
            pygame.time.delay(16)  # 30 FPS

        pygame.quit()

    def start(self):
        self.player = Player(150, 300, 460, 188, pygame.image.load('invader1.jpeg'))
        self.player.set_animation(2, 1, 0.1)

    def update(self):
        # 画面初期化
        screen.fill(pygame.color.THECOLORS['black'])
        self.player.update(screen)


if __name__ == '__main__':
    g = game()
