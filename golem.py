import math
import time
from typing import Any

import pygame
from pygame.surface import Surface

from anim import Anim
from animation_sprite import AnimationSprite
from bullets import Bullet
from functions import load_image
from settings import *


class SkeletonKing(pygame.sprite.Sprite):
    def __init__(self, pos_x: int, pos_y: int, hp: int = 100, speed: int = 22):
        super(SkeletonKing, self).__init__(boss_group, all_sprites)
        self.list_for_sprites:[list[list[Surface]]] = \
            [[load_image('Roguelike Dungeon - Asset Bundle/Sprites/Bosses/Skeleton King/SkeletonKing_Walk_0.png'),
             load_image('Roguelike Dungeon - Asset Bundle/Sprites/Bosses/Skeleton King/SkeletonKing_Walk_1.png'),
             load_image('Roguelike Dungeon - Asset Bundle/Sprites/Bosses/Skeleton King/SkeletonKing_Walk_2.png'),
             load_image('Roguelike Dungeon - Asset Bundle/Sprites/Bosses/Skeleton King/SkeletonKing_Walk_3.png')]]
        self.timer: float = time.time()
        self.cur_frame: int = 0
        self.cur_column: int = 0
        self.rect = pygame.rect.Rect(0, 0, 250, 200)
        self.rect = self.rect.move(pos_x * TILE_SIZE, pos_y * TILE_SIZE)
        self.hp: int = hp
        self.speed: int = speed

        self.texture_fire: Surface = load_image(
            'Roguelike Dungeon - Asset Bundle/Sprites/Bosses/Goblin King/Projectile/GoblinKing_Projectile_01.png')

        self.image: pygame.Surface = self.list_for_sprites[self.cur_column][self.cur_frame]

        self.list_x = [math.cos(math.pi / 8 * i) + math.sin(math.pi / 8 * i) for i in range(16)]
        self.list_y = [math.sin(math.pi / 8 * i) - math.cos(math.pi / 8 * i) for i in range(16)]

    def update(self, *args: Any, **kwargs: Any) -> bool:
        # print(self.timer - time.perf_counter())
        if abs(self.timer - time.perf_counter()) > 0.75:
            self.cur_frame = (self.cur_frame + 1) % len(self.list_for_sprites[self.cur_column])
            self.image = self.list_for_sprites[self.cur_column][self.cur_frame]
            self.timer: float = time.perf_counter()
            return True
        return False

    def set_damage(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()

    def attack_fire(self):
        for i in range(16):
            Bullet(self.texture_fire, self.rect.center, (self.rect.centerx + self.list_x[i], self.rect.centery + self.list_y[i]), speed=20, damage=10, resize=200)






    def move(self, dx: float, dy: float):
        if time.time() - self.timer < TIME_MOVE_MOBS:
            return

    def healing(self):
        pass

class DeadSkeletonKing(pygame.sprite.Sprite):
    pass

