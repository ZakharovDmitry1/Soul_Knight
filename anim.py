import threading
import time

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
        self.way_pos: int = -1

    def set_way(self, way):
        self.way = way
        self.way_pos = 0

    def run(self, dtime: float):
        if not self.is_moving:
            return
        if time.time() - self.timer_move_way_pos > dtime and 0 <= self.way_pos < self.way.__len__() - 1:
            self.rect = self.rect.move(self.way[self.way_pos + 1][0] - self.way[self.way_pos][0],
                                       self.way[self.way_pos + 1][1] - self.way[self.way_pos][1])
            self.timer_move_way_pos = time.time()
            self.way_pos += 1
        # dx = self.way[self.way_pos + 1][0] - self.way[self.way_pos][0]
        # dy = self.way[self.way_pos + 1][1] - self.way[self.way_pos][1]
        # if time.time() - self.timer_move > dtime / 10 and 0 <= self.way_pos < self.way.__len__() - 1:
        #     self.rect = self.rect.move(self.way[self.way_pos + 1][0] - self.way[self.way_pos][0],
        #                                self.way[self.way_pos + 1][1] - self.way[self.way_pos][1])


class FlyingCreature(EngryMob):
    def __init__(self, x: int, y: int):
        super(FlyingCreature, self).__init__(
            'v1.1 dungeon crawler 16X16 pixel pack/enemies/flying creature/fly_anim_spritesheet2.png',
            [[0] * 4 for _ in range(1)], x, y, 10, 50)
