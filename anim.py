import threading
import time
from typing import Any

import pygame

from animation_sprite import AnimationSprite
from functions import Pair
from weapons import Weapon
from settings import *


class Anim(AnimationSprite):
    def __init__(self, sheet: str, list_for_sprites: list[list], x: int, y: int, speed: int = 10, hp: int = 100):
        super(Anim, self).__init__(sheet, list_for_sprites, x, y, TILE_SIZE * 3 // 2)
        self.is_moving: bool = True
        self.speed: int = speed
        self.armor = None
        self.weapon = None
        self.hp: int = hp

    def move(self, dx: int, dy: int):
        if self.is_moving:
            self.rect = self.rect.move(dx * self.speed, dy * self.speed)

    def set_damage(self, hp: int):
        self.hp -= hp
        if self.hp < 0:
            self.kill()

    def attack(self, target: AnimationSprite):
        if self.weapon is not None:
            self.weapon.attack()
        else:
            target.set_damage(10)

    def set_armor(self, armor):
        self.armor = armor

    def set_weapon(self, weapon: Weapon):
        self.weapon = weapon
        self.weapon.move(self.rect.x + TILE_SIZE * 4 // 6, self.rect.y + TILE_SIZE * 4 // 6)

    def kill(self) -> None:
        super(Anim, self).kill()
        if self.weapon is not None:
            self.weapon.kill()


class EngryMob(Anim):
    def __init__(self, sheet: str, list_for_sprites: list[list[int]], x: int, y: int, speed: int, hp: int):
        super(EngryMob, self).__init__(sheet, list_for_sprites, x, y, speed, hp)
        self.way: list[tuple[int, int]] = []
        self.timer_move_way_pos: float = time.time()
        self.timer_move: float = time.time()
        self.way_pos: int = -1
        self.count_move: int = 0
        self.max_count_move: int = 6

    def set_way(self, way):
        self.way = way
        self.way_pos = 0

    def simple_move(self, dx: float, dy: float):
        self.rect = self.rect.move(dx, dy)

    def run(self):
        if not self.is_moving:
            return
        self.count_move += 1
        if self.count_move > self.max_count_move:
            self.count_move = 0
            self.way_pos += 1
        if 0 <= self.way_pos < self.way.__len__() - 1:
            dx = self.way[self.way_pos + 1][0] - self.way[self.way_pos][0]
            dy = self.way[self.way_pos + 1][1] - self.way[self.way_pos][1]
            self.simple_move(dx / self.max_count_move, dy / self.max_count_move)


class AnimationMoveAnim(EngryMob):
    def __init__(self, sheet: str, list_for_sprites: list[list], x: int, y: int, speed: int = 10, hp: int = 100):
        super(AnimationMoveAnim, self).__init__(sheet, list_for_sprites, x, y, speed, hp)

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update()
        if self.cur_column == 2:
            self.cur_column = 0
        elif self.cur_column == 3:
            self.cur_column = 1

    def simple_move(self, dx: int, dy: int):
        super().simple_move(dx, dy)
        if self.weapon is not None:
            self.weapon.move(dx, dy)
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
            super(AnimationMoveAnim, self).simple_move(-dx, -dy)
            if self.weapon is not None:
                self.weapon.move(-dx, -dy)


class FlyingCreature(EngryMob):
    def __init__(self, x: int, y: int):
        super(FlyingCreature, self).__init__(
            'v1.1 dungeon crawler 16X16 pixel pack/enemies/flying creature/fly_anim_spritesheet2.png',
            [[0] * 4 for _ in range(1)], x, y, speed=10, hp=50)


class GoblinCreature(AnimationMoveAnim):
    def __init__(self, x: int, y: int):
        super(GoblinCreature, self).__init__(
            'v1.1 dungeon crawler 16X16 pixel pack/enemies/goblin/goblin.png',
            [[0] * 6 for _ in range(4)], x, y, speed=10, hp=50)
