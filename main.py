import pygame
import time
import random

pygame.init()

canvas_width = 800
canvas_height = 600
dis = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption('Joguinho da cobrinha')
# Color Constants
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 255, 102)

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [canvas_width / 3, canvas_height / 3])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])


def game_loop():
    game_over = False
    game_close = False
    points = 0

    snake_block = 10

    x1 = canvas_width / 2
    y1 = canvas_height / 2

    x1_change = 0
    y1_change = 0

    clock = pygame.time.Clock()
    snake_speed = 15

    snake_list = []
    lenght_of_snake = 1

    foodx = round(random.randrange(0, canvas_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, canvas_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            dis.fill(blue)
            message("You Lost. Press Q-Quit o R-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= canvas_width or x1 < 0 or y1 >= canvas_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > lenght_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, canvas_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, canvas_height - snake_block) / 10.0) * 10.0
            lenght_of_snake += 1

        clock.tick(snake_speed)

    #message("You lost", red)

    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()

game_loop()

