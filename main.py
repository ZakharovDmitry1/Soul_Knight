import sys
import threading
import time

import pygame as pygame
from PyQt5.QtGui import QPixmap

from bullets import Bullet
from functions import load_image
from generation_map import Map
from camera import Camera
from settings import *
from PyQt5.QtWidgets import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(MONITOR_WIDTH, MONITOR_HEIGHT)
        self.setWindowTitle('Заставка')
        self.btn = QPushButton('Начать игру', self)
        self.btn.resize(200, 100)
        self.label = QLabel()
        self.label.resize(MONITOR_WIDTH, MONITOR_HEIGHT)
        pixmap = QPixmap()
        pixmap.load(r'C:\Users\79082\PycharmProjects\Soul_Knight\main_image.png')
        self.label.setPixmap(pixmap)
        self.btn.move(MONITOR_WIDTH // 2 - 100, MONITOR_HEIGHT // 4 * 3 - 50)
        self.btn.clicked.connect(self.count)

    def count(self):
        self.close()


def start_main_window():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


start_main_window()


def start_game():
    pygame.init()
    pygame.display.set_caption("Soul_Knight")
    screen = pygame.display.set_mode((MONITOR_WIDTH, MONITOR_HEIGHT))
    clock = pygame.time.Clock()
    map = Map((MAP_WIDTH, MAP_HEIGHT))
    player = map.generate_level()
    running: bool = True
    time_move_mobs: float = time.time()
    running, time_move_mobs
    player_group.add(player)
    camera = Camera()
    time_update: float = time.time()

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
            if player.hp <= 0:
                return

        player.weapon.attak_animation()

        # for i in mobs_group:
        #     i.run(TIME_UPDATE_MOBS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                player.player_attack(event.pos)

            if event.type == pygame.MOUSEMOTION:
                player.weapon.set_rotate(player.weapon.rect.center, event.pos)
                # print(player.weapon.rect.center)

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
