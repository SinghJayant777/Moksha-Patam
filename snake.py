import pygame
from pygame.locals import *
import time
import random

pygame.init()

black = (0, 0, 0)
red = (255, 0, 0)
blue = (51, 153, 255)
green = (51, 102, 0)
yellow = (255, 255, 0)

win_width = 1320
win_height = 640

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake & Ladder")

snake = 10
snake_speed = 10

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("calibri", 40)
score_font = pygame.font.SysFont("comicsansms", 50)

def user_score(score):
    number = score_font.render("Score: " + str(score), True, blue)
    text_rect = number.get_rect()
    text_rect.center = (win_width / 2, 20)
    window.blit(number, text_rect)

def game_snake(snake, snake_length_list):
    for i, segment in enumerate(snake_length_list):
        # Check if the current segment is the snake head
        if i == len(snake_length_list) - 1:
            pygame.draw.rect(window, red, [segment[0], segment[1], snake, snake])
        else:
            pygame.draw.rect(window, green, [segment[0], segment[1], snake, snake])

def message(msg):
    text = font_style.render(msg, True, red)
    text_rect = text.get_rect()
    text_rect.center = (win_width / 2, win_height / 2)
    window.blit(text, text_rect)

def game_loop():
    gameOver = False
    gameClose = False

    x1 = win_width / 2
    y1 = win_height / 2

    x1_change = 0
    y1_change = 0

    snake_length_list = []
    snake_length = 1

    foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0

    while not gameOver:

        while gameClose == True:
            window.fill(black)
            message("You lost !! Press 'P' to play again and 'Q' to quit the game")
            user_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameClose = False
                    gameOver = True
                if event.type == pygame.KEYDOWN:
                    if event.key == K_q:
                        gameClose = False
                        gameOver = True
                    if event.key == K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True

            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                if event.key == K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                if event.key == K_UP:
                    x1_change = 0
                    y1_change = -snake
                if event.key == K_DOWN:
                    x1_change = 0
                    y1_change = snake

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            gameClose = True

        x1 += x1_change
        y1 += y1_change

        window.fill(black)
        pygame.draw.rect(window, yellow, [foodx, foody, snake, snake])
        snake_size = []
        snake_size.append(x1)
        snake_size.append(y1)
        snake_length_list.append(snake_size)

        if len(snake_length_list) > snake_length:
            del snake_length_list[0]

        game_snake(snake, snake_length_list)
        user_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0
            snake_length += 1

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
