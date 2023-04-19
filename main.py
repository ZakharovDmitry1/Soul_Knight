import math
import os.path
import threading
import time
from pprint import pprint

import pygame as pygame

from boss_map import BossMap
from bullets import Bullet
from functions import load_image
from generation_map import Map
from camera import Camera
from golem import SkeletonKing
from music import *
from player import Player
from settings import *
from start_map import StartMap
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()
mixer.init()


def len_to_points(a: tuple[float, float], b: tuple[float, float]):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def destroy():
    for i in lava_group:
        i.kill()
    for i in all_sprites:
        i.kill()
    for i in tiles_group:
        i.kill()
    for i in walls_group:
        i.kill()
    for i in player_group:
        i.kill()
    for i in weapons_group:
        i.kill()
    for i in bar_group:
        i.kill()
    for i in mobs_group:
        i.kill()
    for i in bullets_group:
        i.kill()
    for i in dead_enemy_group:
        i.kill()
    for i in drop_weapons_group:
        i.kill()


def boss_window():
    pygame.display.set_caption("Soul_Knight")
    screen = pygame.display.set_mode((MONITOR_WIDTH, MONITOR_HEIGHT))
    map = BossMap()
    player = Player(7, 7)
    running: bool = True
    time_move_mobs: float = time.time()
    player_group.add(player)
    camera = Camera()
    time_update: float = time.time()
    SONG_MAIN_PLAY.play(1000)

    boss = SkeletonKing(10, 10)

    boss_group.add(boss)

    while running:
        player.weapon.attak_animation()
        # for i in mobs_group:
        #     i.run(TIME_UPDATE_MOBS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                player.player_attack(event.pos)
                boss.attack_fire()
                for drop in drop_weapons_group:
                    if drop.rect.collidepoint(event.pos) and len_to_points(event.pos, player.rect.center) < 80:
                        player.set_weapon(drop.kill_drop_weapon())

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pass
                # print(map.get_pos(event.pos))

            if event.type == pygame.MOUSEMOTION:
                player.weapon.set_rotate(player.weapon.rect.center, event.pos)
                # print(player.weapon.rect.center)
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

        # for i in bullets_group:
        #     if i.rect.colliderect(boss.rect):
        #         boss.set_damage(i.damage)
        #         i.kill()
        #         print(i.damage)


        screen.fill((44, 49, 54))
        all_sprites.update()
        all_sprites.draw(screen)
        walls_group.draw(screen)
        player_group.draw(screen)
        weapons_group.draw(screen)
        bar_group.draw(screen)
        bar_group.update()
        mobs_group.draw(screen)
        bullets_group.draw(screen)
        dead_enemy_group.draw(screen)
        drop_weapons_group.draw(screen)
        boss_group.draw(screen)

        clock.tick(FPS)
        camera.update(player)
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        pygame.display.flip()
    map.destroy()
    SONG_MAIN_PLAY.stop()


def start_first_window():
    pygame.display.set_caption("Soul_Knight")
    screen = pygame.display.set_mode((MONITOR_WIDTH, MONITOR_HEIGHT))
    map = StartMap()
    player = Player(7, 7)
    running: bool = True
    time_move_mobs: float = time.time()
    player_group.add(player)
    camera = Camera()
    time_update: float = time.time()
    SONG_START_PLAY.play(1000)

    while running:
        if time.time() - time_move_mobs >= TIME_MOVE_MOBS:
            time_move_mobs = time.time()
            for i in mobs_group:
                i.run()

        if time.time() - time_update > MAP_UPDATE_TIME:
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
                for drop in drop_weapons_group:
                    if drop.rect.collidepoint(event.pos) and len_to_points(event.pos, player.rect.center) < 80:
                        player.set_weapon(drop.kill_drop_weapon())

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pass
                # print(map.get_pos(event.pos))

            if event.type == pygame.MOUSEMOTION:
                player.weapon.set_rotate(player.weapon.rect.center, event.pos)
                # print(player.weapon.rect.center)
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

        if mobs_group.empty():
            running = False


        for i in lava_group:
            if i.rect.collidepoint(player.rect.center):
                running = False

        screen.fill((44, 49, 54))
        all_sprites.update()
        all_sprites.draw(screen)
        walls_group.draw(screen)
        player_group.draw(screen)
        weapons_group.draw(screen)
        bar_group.draw(screen)
        bar_group.update()
        mobs_group.draw(screen)
        bullets_group.draw(screen)
        dead_enemy_group.draw(screen)
        drop_weapons_group.draw(screen)

        clock.tick(FPS)
        camera.update(player)
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        pygame.display.flip()
    map.destroy()
    SONG_START_PLAY.stop()


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
    SONG_MAIN_PLAY.play(1000)

    while running:
        if time.time() - time_move_mobs >= TIME_MOVE_MOBS:
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
                for drop in drop_weapons_group:
                    if drop.rect.collidepoint(event.pos) and len_to_points(event.pos, player.rect.center) < 80:
                        player.set_weapon(drop.kill_drop_weapon())

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pass
                # print(map.get_pos(event.pos))

            if event.type == pygame.MOUSEMOTION:
                player.weapon.set_rotate(player.weapon.rect.center, event.pos)
                # print(player.weapon.rect.center)
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

        if mobs_group.__len__() == 0:
            running = False

        screen.fill((44, 49, 54))
        all_sprites.update()
        all_sprites.draw(screen)
        walls_group.draw(screen)
        player_group.draw(screen)
        weapons_group.draw(screen)
        bar_group.draw(screen)
        bar_group.update()
        mobs_group.draw(screen)
        bullets_group.draw(screen)
        dead_enemy_group.draw(screen)
        drop_weapons_group.draw(screen)

        clock.tick(FPS)
        camera.update(player)
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        pygame.display.flip()
    destroy()
    SONG_MAIN_PLAY.stop()



start_first_window()
start_game()
# boss_window()
start_first_window()
