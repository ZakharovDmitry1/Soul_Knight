import threading
import time
from typing import Any

import pygame

from anim import Anim
from healthbar import Healthbar
from settings import *
from weapons import *


class Player(Anim):
    def __init__(self, pos_x: int, pos_y: int, hp: int = 100, speed: int = 22):
        self.sheet: str = 'v1.1 dungeon crawler 16X16 pixel pack/heroes/knight/knight_sprite.png'

        self.real_pos_x: int = pos_x * TILE_SIZE
        self.real_pos_y: int = pos_y * TILE_SIZE

        self.defence = DEFENCE

        self.columns: int = 4
        self.rows: int = 2

        self.list_for_sprites = [[0] * 6 for _ in range(4)]
        super(Player, self).__init__(self.sheet, self.list_for_sprites, pos_x, pos_y, speed, hp)
        self.rect = self.image.get_rect().move(
            TILE_SIZE * pos_x + TILE_SIZE // 4, TILE_SIZE * pos_y + TILE_SIZE // 7)
        self.set_weapon(Gun())
        self.hp_bar: Healthbar = Healthbar(self.hp)
        self.mob_radius: int = MOB_RADIUS

        self.time_damage: float = 0

    def move(self, dx: int, dy: int):
        super(Player, self).move(dx, dy)
        self.real_pos_x += dx * self.speed
        self.real_pos_y += dy * self.speed
        if self.weapon is not None:
            self.weapon.move(dx * self.speed, dy * self.speed)
        if dx > 0:
            self.cur_column = 3
        elif dx < 0:
            self.cur_column = 2
        elif dy != 0:
            if self.cur_column == 0:
                self.cur_column = 2
            if self.cur_column == 1:
                self.cur_column = 3

        if pygame.sprite.spritecollideany(self, walls_group):
            super(Player, self).move(-dx, -dy)
            self.real_pos_x -= dx * self.speed
            self.real_pos_y -= dy * self.speed
            if self.weapon is not None:
                self.weapon.move(-dx * self.speed, -dy * self.speed)

    def player_attack(self):
        self.weapon.attack_animation = True
        self.weapon.attak_animation()
        for i in mobs_group:
            if pygame.sprite.collide_rect(self.weapon, i):
                i.set_damage(self.weapon.damage)

    def set_damage(self, hp: int):
        self.time_damage = time.time()
        self.hp_bar.set_damage(hp)
        if self.defence > 0:
            self.defence -= hp
            if self.defence < 0:
                self.defence = 0
        else:
            self.hp -= hp

    def healing(self):
        self.defence += self.hp_bar.defence.full_defence // 5
        if self.defence > DEFENCE:
            self.defence = DEFENCE
        self.hp_bar.defence.defence += self.hp_bar.defence.full_defence // 5
        if self.hp_bar.defence.defence > DEFENCE:
            self.hp_bar.defence.defence = DEFENCE
        self.hp_bar.defence.reset_bar()

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update()
        if time.time() - self.time_damage > 5:
            self.healing()
            self.time_damage = time.time()
        self.hp_bar.health = self.hp
        if self.cur_column == 2:
            self.cur_column = 0
        elif self.cur_column == 3:
            self.cur_column = 1
