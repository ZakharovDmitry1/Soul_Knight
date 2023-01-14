import threading

import pygame as pygame
from generation_map import Map
from player import Player
from camera import Camera
from settings import *


pygame.init()
pygame.display.set_caption("Soul_Knight")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
map = Map((MAP_WIDTH, MAP_HEIGHT))


def start_game():
    player, level_x, level_y = map.generate_level()
    player_group.add(player)
    running: bool = True
    camera = Camera()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                t1 = threading.Thread(target=player.weapon.attak_animation)
                t1.start()

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

        clock.tick(FPS)
        camera.update(player)
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        pygame.display.flip()



start_game()
