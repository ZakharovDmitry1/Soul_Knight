import threading

import pygame as pygame
from generation_map import Map
from player import Player
from camera import Camera
from settings import *
import numpy as np

pygame.init()
pygame.display.set_caption("Soul_Knight")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
map = Map((MAP_WIDTH, MAP_HEIGHT))


def start_game():
    player = map.generate_level()
    player_group.add(player)
    running: bool = True
    camera = Camera()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                player.attak()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pass
                print(map.get_pos(event.pos, (player.real_pos_x, player.real_pos_y), player.rect.size))

        # print(player.real_pos_x, player.real_pos_y)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.move(-1, 0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.move(1, 0)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.move(0, 1)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.move(0, -1)
        if keys[pygame.K_ESCAPE]:
            running = False

        screen.fill((255, 255, 255))

        all_sprites.draw(screen)
        all_sprites.update()
        player_group.draw(screen)
        weapons_group.draw(screen)
        healthbar_group.draw(screen)
        mobs_group.draw(screen)

        clock.tick(FPS)
        camera.update(player)
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        pygame.display.flip()


start_game()


def create_way(player: Player):
    x_pos, y_pos = map.get_pos((player.rect.x, player.rect.y), (player.real_pos_x, player.real_pos_y), player.rect.size)
    array: np.ndarray = np.zeros((player.mob_radius * 2 + 1, player.mob_radius * 2 + 1, 3), int)

    lx = x_pos - player.mob_radius
    rx = x_pos + player.mob_radius

    ly = y_pos - player.mob_radius
    ry = y_pos + player.mob_radius

    if lx < 0:
        lx = 0
    if rx > MAP_WIDTH:
        rx = MAP_WIDTH
    if ly < 0:
        ly = 0
    if ry > MAP_HEIGHT:
        ry = MAP_HEIGHT

    for i in range(lx, rx):
        for j in range(ly, ry):
            if map.map[i][j] == '#':
                array[lx - i][ly - j][0] = -1

    for mob in mobs_group:
        x, y = map.get_pos((mob.rect.x, mob.rect.y), (player.real_pos_x, player.real_pos_y), player.rect.size)
        if lx <= x <= rx and ly <= y <= ry:
            array[lx - x][ly - y][1] = 1

def bfs()





