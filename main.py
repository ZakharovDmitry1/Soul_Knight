import threading
import time

import pygame as pygame
from generation_map import Map
from player import Player
from camera import Camera
from settings import *
import numpy as np
import time as tm

pygame.init()
pygame.display.set_caption("Soul_Knight")
screen = pygame.display.set_mode((MONITOR_WIDTH, MONITOR_HEIGHT))
clock = pygame.time.Clock()
map = Map((MAP_WIDTH, MAP_HEIGHT))
player = map.generate_level()
running: bool = True


def start_game():
    global running
    player_group.add(player)
    camera = Camera()
    time_update: float = time.time()

    while running:
        if time.time() - time_update > MAP_UPDATE_TIME:
            map.create_way()
            time_update = time.time()
            for i in mobs_group:
                if pygame.sprite.collide_rect(player, i):
                    i.attack(player)
                    i.is_moving = False
                else:
                    i.is_moving = True

        for i in mobs_group:
            i.run(TIME_UPDATE_MOBS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                player.attak()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                map.create_way()

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
        if keys[pygame.K_q]:
            pygame.display.iconify()
        # map.create_way()


        screen.fill((255, 255, 255))

        all_sprites.draw(screen)
        all_sprites.update()
        player_group.draw(screen)
        weapons_group.draw(screen)
        healthbar_group.draw(screen)
        healthbar_group.update()
        mobs_group.draw(screen)

        clock.tick(FPS)
        camera.update(player)
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        pygame.display.flip()


start_game()
