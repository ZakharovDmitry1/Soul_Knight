import os.path
import threading
import time
from pprint import pprint

import pygame as pygame

from bullets import Bullet
from functions import load_image
from generation_map import Map
from camera import Camera
from settings import *

pygame.init()
clock = pygame.time.Clock()

def start_game():
    pygame.display.set_caption("Soul_Knight")
    screen = pygame.display.set_mode((MONITOR_WIDTH, MONITOR_HEIGHT))
    map = Map((MAP_WIDTH, MAP_HEIGHT))
    player = map.generate_level()
    running: bool = True
    time_move_mobs: float = time.time()
    player_group.add(player)
    camera = Camera()
    time_update: float = time.time()

    while running:
        if time.time() - time_move_mobs >= TIME_MOVE_MOBS * 20:
            time_move_mobs = time.time()
            for i in mobs_group:
                i.run()

        if time.time() - time_update > MAP_UPDATE_TIME:
            map.create_way()
            time_update = time.time()
            for i in mobs_group:
                if pygame.sprite.collide_rect(player, i):
                    i.attack(player)
                    i.is_moving = False
                else:
                    i.is_moving = True

        player.weapon.attak_animation()

        # for i in mobs_group:
        #     i.run(TIME_UPDATE_MOBS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                player.player_attack(event.pos)
                print(map.get_real_pos(event.pos)[0] // TILE_SIZE, map.get_real_pos(event.pos)[1] // TILE_SIZE)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pass
                #print(map.get_pos(event.pos))

            if event.type == pygame.MOUSEMOTION:
                player.weapon.set_rotate(player.weapon.rect.center, event.pos)
                #print(player.weapon.rect.center)
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT] and keys[pygame.K_UP]) or (keys[pygame.K_w] and keys[pygame.K_d]):
            player.move(0.35, -0.35)
        elif (keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]) or (keys[pygame.K_d] and keys[pygame.K_s]):
            player.move(0.35, 0.35)
        elif (keys[pygame.K_DOWN] and keys[pygame.K_LEFT]) or (keys[pygame.K_s] and keys[pygame.K_a]):
            player.move(-0.35, 0.35)
        elif (keys[pygame.K_LEFT] and keys[pygame.K_UP]) or (keys[pygame.K_a] and keys[pygame.K_w]):
            player.move(-0.35, -0.35)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.move(-0.5, 0)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.move(0.5, 0)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.move(0, 0.5)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            player.move(0, -0.5)
        if keys[pygame.K_ESCAPE]:
            running = False
        if keys[pygame.K_q]:
            pygame.display.iconify()
        # map.create_way()


        screen.fill((255, 255, 255))

        all_sprites.draw(screen)
        all_sprites.update()
        walls_group.draw(screen)
        player_group.draw(screen)
        weapons_group.draw(screen)
        bar_group.draw(screen)
        bar_group.update()
        mobs_group.draw(screen)
        bullets_group.draw(screen)
        dead_enemy_group.draw(screen)

        clock.tick(FPS)
        camera.update(player)
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        pygame.display.flip()


start_game()
