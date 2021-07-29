import pygame

#設定長寬
WIN_WIDTH = 1024
WIN_HEIGHT = 600

BTN_WIDTH = 80
BTN_HEIGHT = 80

HP_WIDTH = 40
HP_HEIGHT = 40

FPS = 30

# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


# initialization
pygame.init()

# load image (background, enemy, buttons)

# background
background_image = pygame.transform.scale(pygame.image.load("Map.png"), (WIN_WIDTH, WIN_HEIGHT))

# enemy
enemy_image = pygame.transform.scale(pygame.image.load("enemy.png"), (50, 50))

# hp
hp_image = pygame.transform.scale(pygame.image.load("hp.png"), (HP_WIDTH, HP_HEIGHT))

hpg_image = pygame.transform.scale(pygame.image.load("hp_gray.png"), (HP_WIDTH, HP_HEIGHT))

# buttons
muse_image = pygame.transform.scale(pygame.image.load("muse.png"), (75, 75))

sound_image = pygame.transform.scale(pygame.image.load("sound.png"), (75, 75))

continue_image = pygame.transform.scale(pygame.image.load("continue.png"), (75, 75))

pause_image = pygame.transform.scale(pygame.image.load("pause.png"), (75, 75))


# Set the height and width of the screen

size = [WIN_WIDTH, WIN_HEIGHT]

screen = pygame.display.set_mode(size)


# set window caption.

pygame.display.set_caption("My first game")


# clock

done = False

# 管理屏幕更新的速度
clock = pygame.time.Clock()

# 設定timer字體大小
font = pygame.font.Font(None, 30)

class Game:

    def __init__(self):

        # window
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        # hp
        self.hp = 7
        self.max_hp = 10
        pass

    def game_run(self):
        pygame.init()

        # game loop
        done = False
        frame_rate = 60
        start_time = 90
        frame_count = 0  # 變數要丟在function裡面 但若放在while裡面每一次計算都會重新歸零

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            # draw background
            self.window.blit(background_image, (0, 0))

            # draw enemy and health bar
            self.window.blit(enemy_image, (20, 275))
            pygame.draw.rect(self.windowㄙ ,(255,0,0),[20,270,50,5]) # [ x, y, 寬, 長 ]

            # draw menu (and buttons)
            pygame.draw.rect(self.window, (0, 0, 0), [0, 0, 1024, 75])

            self.window.blit(hp_image, (412, 0))
            self.window.blit(hp_image, (452, 0))
            self.window.blit(hp_image, (492, 0))
            self.window.blit(hp_image, (532, 0))
            self.window.blit(hp_image, (572, 0))
            self.window.blit(hp_image, (412, 35))
            self.window.blit(hp_image, (452, 35))
            self.window.blit(hpg_image, (492, 35))
            self.window.blit(hpg_image, (532, 35))
            self.window.blit(hpg_image, (572, 35))
            self.window.blit(muse_image, (724, 0))
            self.window.blit(sound_image, (799, 0))
            self.window.blit(continue_image, (874, 0))
            self.window.blit(pause_image, (949, 0))


            # draw time
            pygame.draw.rect(self.window,(0,0,0),[0,560,85,40])

            # 計算總秒數
            total_seconds = frame_count // frame_rate

            # 計算分鐘數
            minutes = total_seconds // 60

            # 餘數求秒數
            seconds = total_seconds % 60

            # output
            output_string = "{0:02}:{1:02}".format(minutes, seconds)


            text = font.render(output_string, True, WHITE)
            self.window.blit(text, [17, 572])  # timer位置

            frame_count += 1

            # 限制每秒幀數
            clock.tick(frame_rate)

            pygame.display.update()

if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()
