import random
import sys
import pygame
import numpy as np

pygame.init()
taille = 1000
screen = pygame.display.set_mode([taille, taille])
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
            elif event.key == pygame.K_UP:
                print("↑")
                [x, y] = snake[0]
                rect = [x, y, width, height]
                pygame.draw.rect(screen, noir, rect)
                for i in range(2):
                    snake[2][i] += direction[i]
                print(direction)
                serpent(snake)
            elif event.key == pygame.K_DOWN:
                print("↓")
            elif event.key == pygame.K_LEFT:
                print("←")
            elif event.key == pygame.K_RIGHT:
                print("→")

    # damier
    width = 20
    height = 20
    # red = 255
    # green = 255
    # blue = 255
    # color = [red, green, blue]
    # x,y= 0,0
    # for i in range (taille//20):
    # for j in range (taille//20):
    # rect = [x, y, width, height]
    # pygame.draw.rect(screen, color, rect)
    # y+=40
    # if (i+1)%2==0:
    # y=0
    # else:
    # y=20
    # x+=20

    # serpent

    snake = [
        [10, 20],
        [30, 20],
        [50, 20],
    ]

    colorS = [255, 0, 0]

    def serpent(snake):
        for i in range(3):
            [xS, yS] = snake[i]
            rectS = [xS, yS, width, height]
            pygame.draw.rect(screen, colorS, rectS)
        return ()

    serpent(snake)
    noir = [0, 0, 0]

    def colorier_noir(l):
        noir = [0, 0, 0]
        [x, y] = l
        rect = [x, y, width, height]
        pygame.draw.rect(screen, noir, rect)
        return ()

    # serpent qui bouge
    direction = [20, 0]
    # colorier_noir(snake[0])
    # [x,y]=snake[0]
    # rect=[x,y,width,height]
    # pygame.draw.rect(screen, noir, rect)
    # for i in range (2):
    # snake[2][i]+=direction[i]
    # print(snake)
    # serpent(snake)
    # elif event.key == pygame.K_DOWN:
    # print('down')

    pygame.display.update()
    # clock.tick(1)
