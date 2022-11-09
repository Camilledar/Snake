# import random
# import sys
# import pygame
# import numpy as np

# pygame.init()
# taille = 800
# screen = pygame.display.set_mode([taille, taille])
# clock = pygame.time.Clock()
# snake = [
#     [700, 20],
#     [720, 20],
#     [740, 20],
# ]

# width = 20
# height = 20

# fps = 10

# # palette de couleurs
# red = 50
# green = 0
# blue = 150
# color = [red, green, blue]
# colorS = [200, 0, 0]
# blanc = [255, 255, 255]
# noir = [0, 0, 0]
# colorFruit = [255, 255, 255]
# COLORS = {"case": color, "background": noir, "snake": colorS, "fruit": colorFruit}

# # générer fruit
# xF, yF = random.randint(0, taille / 20 - 1), random.randint(0, taille / 20 - 1)
# pygame.draw.rect(screen, COLORS["fruit"], [xF * 20, yF * 20, width, height])

# # damier
# x, y = 0, 0
# for i in range(taille // 20):
#     for j in range(taille // 20):
#         rect = [x, y, width, height]
#         pygame.draw.rect(screen, COLORS["case"], rect)
#         y += 40
#     if (i + 1) % 2 == 0:
#         y = 0
#     else:
#         y = 20
#     x += 20

# # Direction
# UP = [0, -1]
# DOWN = [0, 1]
# LEFT = [-1, 0]
# RIGHT = [1, 0]
# direction = LEFT

# # sortie
# def exit():
#     pygame.quit()
#     sys.exit()
#     return

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
                direction = UP
            elif event.key == pygame.K_DOWN:
                print("↓")
                direction = DOWN
            elif event.key == pygame.K_LEFT:
                print("←")
                direction = LEFT
            elif event.key == pygame.K_RIGHT:
                print("→")
                direction = RIGHT

    # effacer la queue
    queue = snake[-1]
    if ((queue[0] + queue[1]) / 20) % 2 == 0:
        pygame.draw.rect(screen, COLORS["case"], [queue[0], queue[1], width, height])
        pygame.display.update()
    else:
        pygame.draw.rect(
            screen, COLORS["background"], [queue[0], queue[1], width, height]
        )
        pygame.display.update()
    # modifier la liste snake
    for i in range(1, len(snake)):
        snake[len(snake) - i] = snake[len(snake) - i - 1]
    snake[0] = [snake[0][0] + direction[0] * 20, snake[0][1] + direction[1] * 20]
    # colorier le serpent
    for i in range(len(snake)):
        xS, yS = snake[i]
        rectS = [xS, yS, width, height]
        pygame.draw.rect(screen, COLORS["snake"], rectS)
        pygame.display.update()
    # regénérer le fruit et grandir
    if snake[0] == [xF * 20, yF * 20]:
        xF, yF = random.randint(0, taille / 20 - 1), random.randint(0, taille / 20 - 1)
        COLORS["fruit"] = [
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        ]

        pygame.draw.rect(screen, COLORS["fruit"], [xF * 20, yF * 20, width, height])
        snake.append(snake[-1])
        print(snake)
    # test d'echec:
    for i in range(1, len(snake)):
        if snake[0] == snake[i]:
            pygame.quit()
            sys.exit()
    if not (snake[0][0] in np.arange(0, taille, 20)) or not (
        snake[0][1] in np.arange(0, taille, 20)
    ):
        pygame.quit()
        sys.exit()
    pygame.display.update()
    clock.tick(fps)
