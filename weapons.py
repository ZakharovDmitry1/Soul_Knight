import math
import threading
import time
from typing import Any

import PIL
import pygame
from PIL import Image
from pygame import Surface

from functions import load_image
from settings import *


class Weapon(pygame.sprite.Sprite):
    def __init__(self, first_img: str, rows: int, columns: int, column: int,
                 width_image: int, cooldown: float, damage: int):
        super(Weapon, self).__init__(all_sprites, weapons_group)

        new_img = Image.open(first_img).convert('RGBA')
        new_img = new_img.resize(((int)(new_img.size[0] * (width_image / (new_img.size[1] / rows))),
                                  (int)(new_img.size[1] * (width_image / (new_img.size[1] / rows)))))
        new_img.save('cache/weapon.png')

        sheet = load_image('cache/weapon.png')

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

        self.rect = pygame.Rect(0, 0, self.sheet.get_height() // self.rows,
                                self.sheet.get_height() // self.rows)

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
        for i in range(self.columns):
            frame_location = (self.rect.w * i, self.rect.h * (self.column - 1))
            self.frames.append(self.sheet.subsurface(
                pygame.Rect(frame_location, self.rect.size)))

    def move(self, dx: int, dy: int):
        self.rect = self.rect.move(dx, dy)

    def blitRotate(self, angle: float):
        w, h = self.image.get_size()
        box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(angle) for p in box]
        min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
        self.rect.x = self.rect.x + min_box[0]
        self.rect.y = self.rect.y
        # self.rect = pygame.Rect(self.rect.center[0] + min_box[0], self.rect.center[1] - max_box[1]self.rect.center[1] - max_box[1])

        self.image = pygame.transform.rotate(self.frames[self.cur_frame], angle)
        # image_rect = self.image.get_rect(topleft=(
        #         self.rect.centerx - self.rect.bottom,
        #         self.rect.centery - self.rect.right))
        # offset_center_to_pivot = pygame.math.Vector2(self.rect.center) - image_rect.center
        #
        # rotated_offset = offset_center_to_pivot.rotate(-angle)
        # rotated_image_center = (self.rect.centerx - rotated_offset.x,
        #                         self.rect.centery - rotated_offset.y)
        # self.image = pygame.transform.rotate(self.image, angle)
        # self.rect = self.image.get_rect(center=rotated_image_center)

    def set_rotate(self, pos: tuple[float, float], target_pos: tuple[int, int]):
        vec1: tuple = (1, 0)
        vec2: tuple = (target_pos[0] - pos[0], target_pos[1] - pos[1])
        self.vec2 = vec2
        cos: float = vec2[0] / (math.sqrt(vec2[0] ** 2 + vec2[1] ** 2))
        angle: float = math.degrees(math.acos(cos))
        self.angle = angle
        if vec2[1] > 0:
            angle *= -1
        if vec2[0] < 0:
            self.image = pygame.transform.rotate(self.frames[self.cur_frame], -angle)
            self.image = pygame.transform.flip(self.image, False, True)
        else:
            self.image = pygame.transform.rotate(self.frames[self.cur_frame], angle)
        self.rect = self.image.get_rect(center=self.rect.center)


class Stick(Weapon):
    def __init__(self):
        super(Stick, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=11, columns=4, column=10,
                                    width_image=50, cooldown=0.5, damage=30)
        pass

    def attack(self, target: tuple[int, int]):
        pass



class Bow(Weapon):
    def __init__(self):
        super(Bow, self).__init__()


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__()


class Gun(Weapon):
    def __init__(self):
        super(Gun, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=11, columns=8, column=5,
                                  width_image=50, cooldown=0.5, damage=30)

    def update(self, *args: Any, **kwargs: Any) -> None:
        ...
