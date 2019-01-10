# coding=utf-8
import random
from Bar import *
from pg_engine import *
from Controller import *  # new import
from EMG import *  # new import
from Engine import *
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
        self.player.change_size(0.5)
        self.player.set_animation(8, 1, 0.2)
        self.status_bar = Status(self.player.x, self.player.y, 100, 100, 50)

    def update(self):
        # 画面初期化
        screen.fill(pygame.color.THECOLORS['black'])

        # 衝突、範囲判定
        delete_index = []
        for i in range(len(self.enemies)):
            over = is_over(self.player, self.enemies[i])
            if over == 1:
                self.player.change_size(self.player.rate + self.enemies[i].cost / 10.0)
                # モンスター削除
                delete_index.append(i)
            elif over == -1:
                if self.player.damaged:
                    pass
                self.player.damaged = True

            if is_outside(screen, self.enemies[i]):
                # モンスター削除
                delete_index.append(i)
        for i in delete_index:
            del self.enemies[i]

        # 敵の出現
        if np.random.choice([True, False], p=[0.05, 0.95]):
            # スポーン
            cost = random.randint(1, 4)
            self.enemies.append(
                Enemy(screen.get_width() + 100, random.randint(0, screen.get_height()), float(-4 / cost), 0, 500,
                      100, pygame.image.load('./monster/m' + str(random.randint(0, 19) + 1) + '.png'), cost))
            self.enemies[-1].set_animation(5, 1, random.uniform(0, 1))
            self.enemies[-1].change_size(self.enemies[-1].cost / 4.0)

        for i in range(len(self.enemies)):
            self.enemies[i].update(screen)

        # プレイヤーの更新
        self.player.update(screen)

        self.status_bar.update(self.player)


if __name__ == '__main__':
    g = game()
