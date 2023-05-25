import pygame as pg
from random import randint, choice
import time
import math

pg.init()

WIDTH = 1200
HEIGHT = 800
screen = pg.display.set_mode((WIDTH, HEIGHT))
center_x = WIDTH // 2
center_y = HEIGHT // 2
pg.display.set_caption("Backgammon RK")
clock = pg.time.Clock()

background_img = pg.image.load("image/bg_board.png")
background_rect = background_img.get_rect()
bg_screen = screen.get_rect()

current_player = 1

is_double = False

dice_image1 = pg.image.load("image/dice/DICE1.png")
dice_rect1 = dice_image1.get_rect()
dice_image2 = pg.image.load("image/dice/DICE2.png")
dice_rect2 = dice_image1.get_rect()
dice_image3 = pg.image.load("image/dice/DICE3.png")
dice_rect3 = dice_image1.get_rect()
dice_image4 = pg.image.load("image/dice/DICE4.png")
dice_rect4 = dice_image1.get_rect()
dice_image5 = pg.image.load("image/dice/DICE5.png")
dice_rect5 = dice_image1.get_rect()
dice_image6 = pg.image.load("image/dice/DICE6.png")
dice_rect6 = dice_image1.get_rect()

rotate_dice = dice_image6
rotate_dice2 = dice_image1

dice_list = [dice_image1, dice_image2, dice_image3, dice_image4, dice_image5, dice_image6]

position_saber = (25, 670)
saber_white_1 = pg.image.load("image/fishka_white/white_1.png")
saber_rect1 = saber_white_1.get_rect()
saber_white_2 = pg.image.load("image/fishka_white/white_2.png")
saber_rect2 = saber_white_2.get_rect()
saber_white_3 = pg.image.load("image/fishka_white/white_3.png")
saber_rect3 = saber_white_3.get_rect()
saber_white_4 = pg.image.load("image/fishka_white/white_4.png")
saber_rect4 = saber_white_4.get_rect()
saber_white_5 = pg.image.load("image/fishka_white/white_5.png")
saber_rect5 = saber_white_5.get_rect()
saber_white_6 = pg.image.load("image/fishka_white/white_6.png")
saber_rect6 = saber_white_1.get_rect()
saber_white_7 = pg.image.load("image/fishka_white/white_7.png")
saber_rect7 = saber_white_1.get_rect()
saber_white_8 = pg.image.load("image/fishka_white/white_8.png")
saber_rect8 = saber_white_1.get_rect()
saber_white_9 = pg.image.load("image/fishka_white/white_9.png")
saber_rect9 = saber_white_1.get_rect()
saber_white_10 = pg.image.load("image/fishka_white/white_10.png")
saber_rect10 = saber_white_1.get_rect()
saber_white_11 = pg.image.load("image/fishka_white/white_11.png")
saber_rect11 = saber_white_1.get_rect()
saber_white_12 = pg.image.load("image/fishka_white/white_12.png")
saber_rect12 = saber_white_1.get_rect()
saber_white_13 = pg.image.load("image/fishka_white/white_13.png")
saber_rect13 = saber_white_1.get_rect()
saber_white_14 = pg.image.load("image/fishka_white/white_14.png")
saber_rect14 = saber_white_1.get_rect()
saber_white_15 = pg.image.load("image/fishka_white/white_15.png")
saber_rect15 = saber_white_1.get_rect()

saber_white_list = [saber_white_1, saber_white_2, saber_white_3, saber_white_4, saber_white_5, saber_white_6]
saber_white_rect = [saber_rect1, saber_rect2, saber_rect3, saber_rect4, saber_rect5, saber_rect6]

animation_running = False
animation_duration = 8.0
result_text = ""


def draw_result(result):
    global result_text
    result_text = result
    # Очистка экрана
    screen.blit(background_img, background_rect)
    screen.blit(saber_white_1, position_saber)
    screen.blit(saber_white_2, (position_saber[0], position_saber[1] - 30))
    screen.blit(saber_white_3, (position_saber[0], position_saber[1] - 60))
    screen.blit(saber_white_4, (position_saber[0], position_saber[1] - 90))
    screen.blit(saber_white_5, (position_saber[0], position_saber[1] - 120))
    screen.blit(saber_white_6, (position_saber[0], position_saber[1] - 150))
    screen.blit(saber_white_7, (position_saber[0] + 56, position_saber[1]))
    screen.blit(saber_white_8, (position_saber[0] + 115, position_saber[1]))
    screen.blit(saber_white_9, (position_saber[0] + 115, position_saber[1] - 30))
    screen.blit(saber_white_10, (position_saber[0] + 115, position_saber[1] - 60))
    screen.blit(saber_white_11, (position_saber[0] + 115, position_saber[1] - 90))
    screen.blit(saber_white_12, (position_saber[0] + 115, position_saber[1] - 120))
    screen.blit(saber_white_13, (position_saber[0] + 115, position_saber[1] - 150))
    screen.blit(saber_white_14, (position_saber[0], position_saber[1] - 180))
    screen.blit(saber_white_15, (position_saber[0], position_saber[1] - 210))

    # Отображение результата на доске
    font = pg.font.Font(None, 36)
    text = font.render("Результат: " + result, True, (38, 221, 56))

    screen.blit(text, (810, 0))

    # Обновление экрана
    pg.display.flip()


def animate_cube():
    start_time = time.time()
    end_time = start_time + 8  # Длительность анимации в секундах

    current_time = time.time() - start_time
    progress = min(current_time / animation_duration, 1.0)
    angle_x = progress * 360
    angle_y = progress * 360
    angle_z = progress * 360

    result = str(randint(1, 6)) + ", " + str(randint(1, 6))

    while time.time() < end_time:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False

        screen.blit(background_img, background_rect)
        screen.blit(saber_white_1, position_saber)
        screen.blit(saber_white_2, (position_saber[0], position_saber[1] - 30))
        screen.blit(saber_white_3, (position_saber[0], position_saber[1] - 60))
        screen.blit(saber_white_4, (position_saber[0], position_saber[1] - 90))
        screen.blit(saber_white_5, (position_saber[0], position_saber[1] - 120))
        screen.blit(saber_white_6, (position_saber[0], position_saber[1] - 150))
        screen.blit(saber_white_7, (position_saber[0] + 56, position_saber[1]))
        screen.blit(saber_white_8, (position_saber[0] + 115, position_saber[1]))
        screen.blit(saber_white_9, (position_saber[0] + 115, position_saber[1] - 30))
        screen.blit(saber_white_10, (position_saber[0] + 115, position_saber[1] - 60))
        screen.blit(saber_white_11, (position_saber[0] + 115, position_saber[1] - 90))
        screen.blit(saber_white_12, (position_saber[0] + 115, position_saber[1] - 120))
        screen.blit(saber_white_13, (position_saber[0] + 115, position_saber[1] - 150))
        screen.blit(saber_white_14, (position_saber[0], position_saber[1] - 180))
        screen.blit(saber_white_15, (position_saber[0], position_saber[1] - 210))

        # Генерация случайных чисел для вращения кубика
        smooth_angle_x = math.sin(math.radians(angle_x)) * 90
        smooth_angle_y = math.sin(math.radians(angle_y)) * 90
        smooth_angle_z = math.sin(math.radians(angle_z)) * 90



        # Вращение поверхности кубика
        rotate_dice = pg.transform.rotate(choice(dice_list), smooth_angle_x)
        rotate_dice = pg.transform.rotate(rotate_dice, smooth_angle_y)
        rotate_dice = pg.transform.rotate(rotate_dice, smooth_angle_z)

        rotate_dice2 = pg.transform.rotate(choice(dice_list), smooth_angle_x)
        rotate_dice2 = pg.transform.rotate(rotate_dice2, smooth_angle_y)
        rotate_dice2 = pg.transform.rotate(rotate_dice2, smooth_angle_z)

        # Отрисовка кубика на экране
        screen.blit(rotate_dice, (WIDTH // 2, HEIGHT // 2))
        screen.blit(rotate_dice2, ((WIDTH // 2) + 80, HEIGHT // 2))

        # Обновление экрана
        pg.display.flip()
        pg.time.wait(10)

    draw_result(result)

    return True, result


running = True
while running:
    clock.tick(5)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            if not animation_running:
                animation_running = True
                result = animate_cube()

                if result:
                    print("Анимация завершена! Результат получен.")
                else:
                    print("Анимация прервана.")
                    animation_running = False

        screen.blit(background_img, background_rect)
        screen.blit(saber_white_1, position_saber)
        screen.blit(saber_white_2, (position_saber[0], position_saber[1] - 30))
        screen.blit(saber_white_3, (position_saber[0], position_saber[1] - 60))
        screen.blit(saber_white_4, (position_saber[0], position_saber[1] - 90))
        screen.blit(saber_white_5, (position_saber[0], position_saber[1] - 120))
        screen.blit(saber_white_6, (position_saber[0], position_saber[1] - 150))
        screen.blit(saber_white_7, (position_saber[0] + 56, position_saber[1]))
        screen.blit(saber_white_8, (position_saber[0] + 115, position_saber[1]))
        screen.blit(saber_white_9, (position_saber[0] + 115, position_saber[1] - 30))
        screen.blit(saber_white_10, (position_saber[0] + 115, position_saber[1] - 60))
        screen.blit(saber_white_11, (position_saber[0] + 115, position_saber[1] - 90))
        screen.blit(saber_white_12, (position_saber[0] + 115, position_saber[1] - 120))
        screen.blit(saber_white_13, (position_saber[0] + 115, position_saber[1] - 150))
        screen.blit(saber_white_14, (position_saber[0], position_saber[1] - 180))
        screen.blit(saber_white_15, (position_saber[0], position_saber[1] - 210))
        clock.tick(30)

    if result_text:
        draw_result(result=result_text)

    pg.display.flip()
    pg.display.update()

pg.quit()
