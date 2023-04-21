import math
import random
import threading
import time
from abc import abstractmethod


import PIL
import pygame
from PIL import Image
from pygame import Surface

from bullets import Bullet
from functions import load_image
from music import GUN_ATTACK
from settings import *


class Weapon(pygame.sprite.Sprite):
    def __init__(self, first_img: str, rows: int, columns: int, column: int,
                 width_image: int, cooldown: float, damage: int, max_columns: int, bullet: Surface):
        super(Weapon, self).__init__(all_sprites, weapons_group)
        self.max_columns: int = max_columns

        new_img = Image.open(first_img).convert('RGBA')
        new_img = new_img.resize(((int)(rows * width_image),
                                  (int)(columns * width_image)))
        new_img.save('cache/weapon.png')

        sheet = load_image('cache/weapon.png')
        self.bullet: Surface = bullet

        self.time_attack: float = time.time()

        self.x = None
        self.y = None

        self.angle: float = 0
        self.reflection: bool = False

        self.attack_animation = False

        self.width_image: int = width_image
        self.cooldown: float = cooldown
        self.damage: int = damage
        self.sheet: Surface = sheet

        self.rows: int = rows
        self.columns: int = columns

        self.time_animation: float = time.time()

        self.column: int = column

        self.rect = pygame.Rect(0, 0, width_image,
                                width_image)

        self.frames: list = []
        self.cur_frame: int = 0
        self.cut_sheet()
        self.image: pygame.Surface = self.frames[self.cur_frame]

        self.vec2: tuple[int, int] = (0, 0)

    def attak_animation(self):
        if not self.attack_animation:
            return
        if time.time() - self.time_animation < 0.1:
            return

        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        if self.cur_frame == 0:
            self.attack_animation = False
            return
        if self.vec2[1] > 0 and self.angle > 0:
            self.angle *= -1
        if self.vec2[0] < 0:
            self.image = pygame.transform.rotate(self.frames[self.cur_frame], -self.angle)
            self.image = pygame.transform.flip(self.image, False, True)
        else:
            self.image = pygame.transform.rotate(self.frames[self.cur_frame], self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.time_animation = time.time()

    def cut_sheet(self):
        for i in range(self.max_columns):
            frame_location = (self.rect.w * i, self.rect.h * (self.column - 1))
            self.frames.append(self.sheet.subsurface(
                pygame.Rect(frame_location, self.rect.size)))

    def move(self, dx: int, dy: int):
        self.rect = self.rect.move(dx, dy)

    # def blitRotate(self, angle: float):
    #     w, h = self.image.get_size()
    #     box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    #     box_rotate = [p.rotate(angle) for p in box]
    #     min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    #     max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
    #     self.rect.x = self.rect.x + min_box[0]
    #     self.rect.y = self.rect.y
    #     # self.rect = pygame.Rect(self.rect.center[0] + min_box[0], self.rect.center[1] - max_box[1]self.rect.center[1] - max_box[1])
    #
    #     self.image = pygame.transform.rotate(self.frames[self.cur_frame], angle)

    def set_rotate(self, pos: tuple[float, float], target_pos: tuple[int, int]):
        vec1: tuple = (1, 0)
        vec2: tuple = (target_pos[0] - pos[0], target_pos[1] - pos[1])
        self.vec2 = vec2
        cos: float = vec2[0] / (math.sqrt(vec2[0] ** 2 + vec2[1] ** 2))
        angle: float = math.degrees(math.acos(cos))
        self.angle = angle
        if vec2[1] > 0:
            self.angle *= -1
        if vec2[0] < 0:
            self.image = pygame.transform.rotate(self.frames[self.cur_frame], -self.angle)
            self.image = pygame.transform.flip(self.image, False, True)
        else:
            self.image = pygame.transform.rotate(self.frames[self.cur_frame], self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def attack(self, target: tuple[int, int]) -> bool:
        if time.time() - self.time_attack < self.cooldown:
            return False
        else:
            self.time_attack = time.time()
        return True


class Stick(Weapon):
    def __init__(self):
        super(Stick, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=11, columns=4, column=10,
                                    width_image=50, cooldown=0.5, damage=30)
        pass

    def attack(self, target: tuple[int, int]):
        pass


class ShortGun(Weapon):
    def __init__(self, first_img: str, rows: int, columns: int, column: int,
                 width_image: int, cooldown: float, damage: int, max_columns: int, bullet: Surface):
        super(ShortGun, self).__init__(first_img, rows=rows, columns=columns, column=column,
                                       width_image=width_image, cooldown=cooldown, damage=damage, bullet=bullet,
                                       max_columns=max_columns)

    def attack(self, target: tuple[int, int]):
        if not super().attack(target):
            return
        GUN_ATTACK.play(0)
        for i in range(10):
            vec = [target[0] - self.rect.x, target[1] - self.rect.y]
            angle = random.uniform(-0.15, 0.15)
            rotatedX = vec[0] * math.cos(angle) - vec[1] * math.sin(angle)
            rotatedY = vec[0] * math.sin(angle) + vec[1] * math.cos(angle)
            Bullet(self.bullet, (self.rect.x, self.rect.y), (rotatedX + self.rect.x, rotatedY + self.rect.y),
                   random.randint(5, 16), self.damage, rotate=self.angle, resize=40, kill_time=0.4)


class Bow(Weapon):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 9, 0), (32, 32)))
        super(ShortGun, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=11, columns=8, column=4,
                                       width_image=50, damage=2, cooldown=0.5, bullet=image, max_columns=3)


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__()


class Gun(Weapon):
    def __init__(self, first_img: str, rows: int, columns: int, column: int,
                 width_image: int, cooldown: float, damage: int, max_columns: int, bullet: Surface):
        super(Gun, self).__init__(first_img, rows=rows, columns=columns, column=column,
                                  width_image=width_image, cooldown=cooldown, damage=damage, bullet=bullet,
                                  max_columns=max_columns)


    def attack(self, target: tuple[int, int]):
        if not super().attack(target):
            return
        GUN_ATTACK.play(0)
        Bullet(self.bullet, (self.rect.x, self.rect.y), target, 10, self.damage, rotate=self.angle, resize=40)

    def update(self, *args, **kwargs) -> None:
        ...
