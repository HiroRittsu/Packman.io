from pg_engine import *
from Controller import *  # new import
from EMG import *  # new import
from engine import *
from Player import *
from Enemy import *


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
        self.player = Player(150, 300, 1030, 100, pygame.image.load('packman.png'))
        self.player.set_animation(8, 1, 0.8)

    def update(self):
        self.player.change_size(0.1)
        # 画面初期化
        screen.fill(pygame.color.THECOLORS['black'])
        self.player.update(screen)


if __name__ == '__main__':
    g = game()
