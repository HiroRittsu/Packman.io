from pg_engine import *
from Controller import *  # new import
from EMG import *  # new import
from engine import *
from Player import *
from Enemy import *


class game:

    def __init__(self):
        self.enemies = []
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
        # プレイヤー
        self.player = Player(150, 300, 1030, 100, pygame.image.load('packman.png'))
        self.player.set_animation(8, 1, 0.8)
        # 敵
        for i in range(20):
            self.enemies.append(Enemy(screen.get_width() / 2 + i * 10, screen.get_height() / 2, 500, 100,
                                      pygame.image.load('./monster/m' + str(i + 1) + '.png')))

    def update(self):
        # 画面初期化
        screen.fill(pygame.color.THECOLORS['black'])

        self.player.change_size(0.1)
        self.player.update(screen)

        for i in range(20):
            self.enemies[i].draw = True
            self.enemies[i].set_animation(5, 1, 0.8)
            self.enemies[i].update(screen)



if __name__ == '__main__':
    g = game()
