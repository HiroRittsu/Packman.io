# coding=utf-8
import random
from Bar import *
from pg_engine import *
from pg_init import *
from Controller import *  # new import
from EMG import *  # new import
from Engine import *
from Player import *
from Enemy import *
from threading import Timer

MAX_TIME = 60
BG_IMAGE_INDEX = 0


class game:

    def __init__(self):
        # タイマースレッド起動
        # self.timer = Timer(MAX_TIME, self.end)

        self.enemies = []
        self.bg_image = []
        self.start()
        self.running = True
        while self.running:
            for event in pygame.event.get():
                # checks if you've exited the game
                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    # プログラム終了
                    pygame.quit()
                    # self.timer.cancel()
                    sys.exit(0)

            self.update()
            pygame.display.update()
            pygame.time.delay(16)  # 30 FPS

    def start(self):
        # プレイヤー
        self.player = Player(150, 300, 1030, 100, pygame.image.load('packman.png'))
        self.player.change_size(0.5)
        self.player.set_animation(8, 1, 0.2)
        self.status_bar = Status(self.player.x, self.player.y, 100, 100, self.player.hp)
        self.timer_bar = Timer_Bar(0, 0, 250, 250, MAX_TIME)
        self.time_count = MAX_TIME
        for i in range(1801):
            self.bg_image.append(pygame.image.load('./backimg/t' + str("{0:04d}".format(i)) + '.bmp'))

        # self.timer.start()

    def end(self):
        self.running = False
        # self.timer.cancel()
        finish_run = True
        # 画面初期化
        screen.fill(pygame.color.THECOLORS['black'])
        # フォントの作成
        font = pygame.font.SysFont(None, 50)
        font.set_underline(True)
        # テキストを描画したSurfaceを作成、描画
        game_over = pygame.image.load('gameover.png')
        screen.blit(game_over,
                    [(screen.get_width() / 2) - (game_over.get_rect().size[0] / 2),
                     (screen.get_height() / 2) - (game_over.get_rect().size[1] / 2)])
        text = font.render("Your Score  " + str(self.player.point), True, (0, 255, 0))
        text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 170))
        screen.blit(text, text_rect)

        if self.time_count <= 0:
            # time upの場合
            font.set_underline(False)
            text = font.render("Time UP!", True, (255, 0, 255))
        if self.player.hp <= 0:
            # hpが尽きた場合
            font.set_underline(False)
            text = font.render("You are Killed!", True, (255, 0, 255))
        text_rect = text.get_rect(center=(screen.get_width() / 2, 75))
        screen.blit(text, text_rect)

        pygame.display.update()

        while finish_run:
            for event in pygame.event.get():
                # checks if you've exited the game
                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    finish_run = False

        pygame.quit()
        sys.exit(0)

    def update(self):
        global BG_IMAGE_INDEX
        # playerの体力確認
        if self.player.hp <= 0:
            self.end()
        # 時間の確認
        if self.time_count <= 0:
            self.end()

        # 画面初期化
        screen.fill(pygame.color.THECOLORS['black'])

        # background_image
        screen.blit(self.bg_image[BG_IMAGE_INDEX], [0, 0])
        if BG_IMAGE_INDEX >= 1800:
            BG_IMAGE_INDEX = 0
        BG_IMAGE_INDEX += 1

        #######################################################################
        # 衝突、範囲判定
        delete_index = []
        self.player.damaged = False
        for i in range(len(self.enemies)):
            over = is_over(self.player, self.enemies[i])
            if over == 1:
                self.player.change_size(self.player.rate + self.enemies[i].cost / 100.0)
                self.player.point += self.enemies[i].cost
                # モンスター削除
                delete_index.append(i)
            elif over == -1:
                # ダメージ
                self.player.hp -= 0.5
                self.player.damaged = True

            if is_outside(screen, self.enemies[i]):
                # モンスター削除
                delete_index.append(i)
        for i in delete_index:
            del self.enemies[i]

        if self.player.damaged:
            # ダメージ点滅
            if self.player.draw:
                self.player.draw = False
            else:
                self.player.draw = True
        else:
            self.player.draw = True

        #######################################################################
        # 敵の出現
        if np.random.choice([True, False], p=[0.07, 0.93]):
            # スポーン
            cost_list = []
            for c in range(4):
                cost_list.append(c + 1)
            cost = np.random.choice(cost_list, p=[0.35, 0.35, 0.2, 0.1])
            self.enemies.append(
                Enemy(screen.get_width() + 100, random.randint(0, screen.get_height()), float(-4 / cost), 0, 500,
                      100, pygame.image.load('./monster/m' + str(random.randint(0, 19) + 1) + '.png'), cost))
            self.enemies[-1].set_animation(5, 1, random.uniform(0, 1))
            self.enemies[-1].change_size(self.enemies[-1].cost / 4.0)

        for i in range(len(self.enemies)):
            self.enemies[i].update(screen)

        #######################################################################
        # アイテムの出現
        if np.random.choice([True, False], p=[0.01, 0.99]):
            np.random.choice([True, False], p=[0.01, 0.99])
            pass

        #######################################################################
        # プレイヤーの更新
        self.player.update(screen)
        self.status_bar.update(self.player)
        # score
        font = pygame.font.SysFont(None, 25)
        text = font.render("score  " + str(self.player.point), True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.player.x, self.player.y - 70))
        screen.blit(text, text_rect)

        ##時間表示
        self.time_count -= 0.016
        self.timer_bar.update(screen, self.time_count)


if __name__ == '__main__':
    g = game()
