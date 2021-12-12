import random
import pygame
import sys

from pygame import *
from easygui import *


SIDE = 1000

# мяч
ball_size = 20
ball_position = [0, 0]
ball_speed = [0, 0]
x_speed = 0
y_speed = 0

# ракетка
racket_width = 10
racket_height = 120

racket_width_hf = racket_width // 2
racket_height_hf = racket_height // 2

racket1_move = 0
racket2_move = 0
racket3_move = 0
racket4_move = 0

racket1_position = [0, 0]
racket2_position = [0, 0]
racket3_position = [0, 0]
racket4_position = [0, 0]

# счёт
score_left = 0
score_right = 0
score_up = 0
score_down = 0
score_index = 0

# политра
LINES = (48, 71, 94)
BALL = (240, 84, 84)
STICK = (232, 232, 232)
BACK = (34, 40, 49)


def ball_setup():
    global ball_position, ball_speed, x_speed, y_speed

    ball_position = [SIDE // 2, SIDE // 2]
    x_speed = random.randrange(-4, 4)
    y_speed = random.randrange(-3, 3)

    while x_speed == y_speed or x_speed == 0 or y_speed == 0:
        x_speed = random.randrange(-4, 4)
        y_speed = random.randrange(-3, 3)

    ball_speed = [x_speed, -y_speed]


def setup():
    global racket1_position, racket2_position, racket3_position, racket4_position, racket1_move, racket2_move, \
        score_left, score_right, score_up, score_down

    # место спавна
    racket1_position = [racket_width_hf - 1, SIDE // 2]
    racket2_position = [SIDE + 1 - racket_width_hf, SIDE // 2]
    racket3_position = [4, SIDE // 2]
    racket4_position = [SIDE - 4, SIDE // 2]

    score_left = 0
    score_right = 0
    score_up = 0
    score_down = 0

    ball_setup()


def score_counting():
    global score_left, score_right, score_up, score_down

    if score_index == 1:
        score_left += 1
    elif score_index == 2:
        score_up += 1
    elif score_index == 3:
        score_right += 1
    elif score_index == 4:
        score_down += 1


def drawing(canvas):
    global racket1_position, racket2_position, racket3_position, racket4_position, ball_position, ball_speed, \
        score_left, score_right, score_up, score_down, score_index

    # заливка фона
    canvas.fill(BACK)
    # линии поля игроков
    pygame.draw.line(canvas, LINES, [racket_width, 0], [racket_width, SIDE], 1)  # левая граница
    pygame.draw.line(canvas, LINES, [SIDE - racket_width, 0], [SIDE - racket_width, SIDE], 1)  # правая граница
    pygame.draw.line(canvas, LINES, [0, racket_width], [SIDE, racket_width], 1)
    pygame.draw.line(canvas, LINES, [0, SIDE - racket_width], [SIDE, SIDE - racket_width], 1)

    # форма ракетки (прямоугольник по 4-м точкам)
    pygame.draw.polygon(
        canvas,
        STICK,
        [
            [racket1_position[0] - racket_width_hf, racket1_position[1] - racket_height_hf],
            [racket1_position[0] - racket_width_hf, racket1_position[1] + racket_height_hf],
            [racket1_position[0] + racket_width_hf, racket1_position[1] + racket_height_hf],
            [racket1_position[0] + racket_width_hf, racket1_position[1] - racket_height_hf],
        ],
        0,
    )

    pygame.draw.polygon(
        canvas,
        STICK,
        [
            [racket2_position[0] - racket_width_hf, racket2_position[1] - racket_height_hf],
            [racket2_position[0] - racket_width_hf, racket2_position[1] + racket_height_hf],
            [racket2_position[0] + racket_width_hf, racket2_position[1] + racket_height_hf],
            [racket2_position[0] + racket_width_hf, racket2_position[1] - racket_height_hf],
        ],
        0,
    )

    pygame.draw.polygon(
        canvas,
        STICK,
        [
            [racket3_position[1] + racket_height_hf, racket3_position[0] - racket_width_hf],
            [racket3_position[1] + racket_height_hf, racket3_position[0] + racket_width_hf],
            [racket3_position[1] - racket_height_hf, racket3_position[0] + racket_width_hf],
            [racket3_position[1] - racket_height_hf, racket3_position[0] - racket_width_hf],
        ],
        0,
    )

    pygame.draw.polygon(
        canvas,
        STICK,
        [
            [racket4_position[1] - racket_height_hf, racket4_position[0] - racket_width_hf],
            [racket4_position[1] - racket_height_hf, racket4_position[0] + racket_width_hf],
            [racket4_position[1] + racket_height_hf, racket4_position[0] + racket_width_hf],
            [racket4_position[1] + racket_height_hf, racket4_position[0] - racket_width_hf],
        ],
        0,
    )

    # отрисовка передвижений ракеток
    if racket_height_hf < racket1_position[1] < SIDE - racket_height_hf:
        racket1_position[1] += racket1_move
    elif racket1_position[1] == racket_height_hf and racket1_move > 0:
        racket1_position[1] += racket1_move
    elif racket1_position[1] == SIDE - racket_height_hf and racket1_move < 0:
        racket1_position[1] += racket1_move

    if racket_height_hf < racket2_position[1] < SIDE - racket_height_hf:
        racket2_position[1] += racket2_move
    elif racket2_position[1] == racket_height_hf and racket2_move > 0:
        racket2_position[1] += racket2_move
    elif racket2_position[1] == SIDE - racket_height_hf and racket2_move < 0:
        racket2_position[1] += racket2_move

    if racket_height_hf < racket3_position[1] < SIDE - racket_height_hf:
        racket3_position[1] += racket3_move
    elif racket3_position[1] == racket_height_hf and racket3_move > 0:
        racket3_position[1] += racket3_move
    elif racket3_position[1] == SIDE - racket_height_hf and racket3_move < 0:
        racket3_position[1] += racket3_move

    if racket_height_hf < racket4_position[1] < SIDE - racket_height_hf:
        racket4_position[1] += racket4_move
    elif racket4_position[1] == racket_height_hf and racket4_move > 0:
        racket4_position[1] += racket4_move
    elif racket4_position[1] == SIDE - racket_height_hf and racket4_move < 0:
        racket4_position[1] += racket4_move

    # нарисовать мяч
    pygame.draw.circle(canvas, BALL, ball_position, 20, 0)

    # отрисовка передвижения мяча
    ball_position[0] += int(ball_speed[0])
    ball_position[1] += int(ball_speed[1])

    # положение очков на экране
    FONT = 'microsofttaile'
    font_size = pygame.font.SysFont(FONT, 28)

    score_1 = font_size.render("SCORE 1: " + str(score_left), 1, (247, 219, 240))
    canvas.blit(score_1, (50, 40))

    score_2 = font_size.render("SCORE 2: " + str(score_right), 1, (247, 219, 240))
    canvas.blit(score_2, (50, 70))

    score_3 = font_size.render("SCORE 3: " + str(score_up), 1, (247, 219, 240))
    canvas.blit(score_3, (50, 100))

    score_4 = font_size.render("SCORE 4: " + str(score_down), 1, (247, 219, 240))
    canvas.blit(score_4, (50, 130))


# отбивание
def back_off():
    global ball_position, ball_speed, score_left, score_right, score_up, score_down, score_index

    if int(ball_position[0]) <= ball_size + racket_width and int(ball_position[1]) in range(
            racket1_position[1] - racket_height_hf - 10, racket1_position[1] + racket_height_hf + 10):
        ball_speed[0] = -ball_speed[0]
        ball_speed[0] *= 1.15  # увеличении скорости после отбития
        ball_speed[1] *= 1.15  # увеличении скорости после отбития
        score_index = 1
        sound(True)
    elif int(ball_position[0]) <= ball_size + racket_width:
        sound(False)
        score_counting()
        ball_setup()
        score_index = 0

    if int(ball_position[0]) >= SIDE - ball_size - racket_width and int(ball_position[1]) in range(
            racket2_position[1] - racket_height_hf - 10, racket2_position[1] + racket_height_hf + 10):
        ball_speed[0] = -ball_speed[0]
        ball_speed[0] *= 1.15
        ball_speed[1] *= 1.15
        score_index = 2
        sound(True)
    elif int(ball_position[0]) >= SIDE + 1 - ball_size - racket_width:
        sound(False)
        score_counting()
        ball_setup()
        score_index = 0

    if int(ball_position[1]) <= ball_size + racket_width and int(ball_position[0]) in range(
            racket3_position[1] - racket_height_hf - 10, racket3_position[1] + racket_height_hf + 10):
        ball_speed[1] = -ball_speed[1]
        ball_speed[0] *= 1.15
        ball_speed[1] *= 1.15
        score_index = 3
        sound(True)
    elif int(ball_position[1]) <= ball_size + racket_width - 1:
        sound(False)
        score_counting()
        ball_setup()
        score_index = 0

    if int(ball_position[1]) >= SIDE - ball_size - racket_width - 15 and int(ball_position[0]) in range(
            racket4_position[1] - racket_height_hf - 10, racket4_position[1] + racket_height_hf + 10):
        ball_speed[1] = -ball_speed[0]
        ball_speed[0] *= 1.15
        ball_speed[1] *= 1.15
        score_index = 4
        sound(True)
    elif int(ball_position[1]) >= SIDE - ball_size - racket_width + 15:
        sound(False)
        score_counting()
        ball_setup()
        score_index = 0


def pc_logic():
    global ball_position, racket2_move, racket3_move, racket4_move
    racket2_position[1] = ball_position[1]
    racket3_position[1] = ball_position[0]
    racket4_position[1] = ball_position[0]


# кнопка нажаьа - двигайся
def key_on(action):
    global racket1_move, racket2_move, racket3_move, racket4_move

    if action.key == K_w:
        racket1_move = -10  # скорость смещения
    if action.key == K_s:
        racket1_move = 10  # скорость смещения

    if action.key == K_UP:
        racket2_move = -10  # скорость смещения
    if action.key == K_DOWN:
        racket2_move = 10  # скорость смещения

    if action.key == K_a:
        racket3_move = -10  # скорость смещения
    if action.key == K_d:
        racket3_move = 10  # скорость смещения

    if action.key == K_LEFT:
        racket4_move = -10  # скорость смещения
    if action.key == K_RIGHT:
        racket4_move = 10  # скорость смещения


# кнопка поднята - скорость 0
def key_off(action):
    global racket1_move, racket2_move, racket3_move, racket4_move

    if action.key in (K_s, K_w):
        racket1_move = 0
    if action.key in (K_UP, K_DOWN):
        racket2_move = 0
    if action.key in (K_a, K_d):
        racket3_move = 0
    if action.key in (K_LEFT, K_RIGHT):
        racket4_move = 0


def sound(mode):
    if mode:
        pygame.mixer.init()
        pygame.mixer.music.load("Blip.wav")
        pygame.mixer.music.play()
    if not mode:
        pygame.mixer.init()
        pygame.mixer.music.load("Game over.wav")
        pygame.mixer.music.play()


def key_on_solo(action):
    global racket1_move, racket2_move, racket3_move, racket4_move

    if action.key == K_w:
        racket1_move = -10  # скорость смещения
    if action.key == K_s:
        racket1_move = 10  # скорость смещения


def key_off_solo(act):
    global racket1_move

    if act.key in (K_s, K_w):
        racket1_move = 0


pygame.init()
fps = pygame.time.Clock()

# стартовый экран
menu = 'menu.png'
game_mode = ['локальный мультиплеер', 'против ботов']
res = buttonbox(msg='', title='Pong 44', image=menu, choices=game_mode)
print(res)

setup()

# экран игры
window = pygame.display.set_mode((SIDE, SIDE))
pygame.display.set_caption("Pong4four")

while True:
    if res == 'локальный мультиплеер':
        drawing(window)
        back_off()

        for event in pygame.event.get():

            if event.type == KEYDOWN:
                key_on(event)
            elif event.type == KEYUP:
                key_off(event)
            elif event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fps.tick(60)
    if res == 'против ботов':
        drawing(window)
        back_off()
        pc_logic()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                key_on_solo(event)
            elif event.type == KEYUP:
                key_off_solo(event)
            elif event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fps.tick(60)
