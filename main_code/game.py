import pygame
import random

pygame.init()
windows = pygame.display.set_mode((400, 400))

pygame.display.set_caption("2D Dota")

x = 300
y = 0
player_y = 200
width = 16
height = 16
speed = 5

clock = pygame.time.Clock()

background = pygame.image.load('img/back.jpg')
background = pygame.transform.scale(background, (400, 400))
player_car = pygame.image.load('img/car.png')
player_car = pygame.transform.scale(player_car, (54, 114))
player_car.set_colorkey('White')

enemy_car = pygame.image.load('img/enemy_car_1.png')
enemy_car_start_x = random.randrange(80, 300)
enemy_car_start_y = 0
enemy_car_speed = 5
enemy_car_width = 49
enemy_car_height = 100

run = True

left = False
right = False
up = False
down = False


def drawing_window():
    if left:
        windows.blit(player_car, (x, player_y))

    elif right:
        windows.blit(player_car, (x, player_y))

    elif up:
        windows.blit(player_car, (x, player_y))

    elif down:
        windows.blit(player_car, (x, player_y))

    else:
        windows.blit(player_car, (x, player_y))

    windows.blit(enemy_car, (enemy_car_start_x, enemy_car_start_y))

    pygame.display.update()


while run:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    rel_y = y % background.get_rect().height
    windows.blit(background, (0, rel_y - background.get_rect().height))

    if rel_y > 0:
        windows.blit(background, (0, rel_y))
    y += speed // 2

    enemy_car_start_y += speed // 3

    if keys[pygame.K_a] and x > 54 // 2 + 5:
        x -= speed
        left = True
        right = False
        down = False
        up = False

    elif keys[pygame.K_d] and x < 395 - 54 * 1.5:
        x += speed
        left = False
        right = True
        down = False
        up = False

    elif keys[pygame.K_w] and player_y > 5:
        player_y -= speed
        up = True
        down = False
        left = False
        right = False

    elif keys[pygame.K_s] and player_y < 400 - 114:
        player_y += speed
        up = False
        down = True
        left = False
        right = False
    else:
        left = False
        right = False
        down = False
        up = False

    drawing_window()
    # windows.blit(player_car, (250, 200))
    pygame.display.update()
    speed += 0.001
    clock.tick(144)
pygame.quit()
