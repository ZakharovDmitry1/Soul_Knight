import time

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

        self.width_image: int = width_image
        self.cooldown: float = cooldown
        self.damage: int = damage
        self.sheet: Surface = sheet

        self.rows: int = rows
        self.columns: int = columns

        self.column: int = column

        self.rect = pygame.Rect(0, 0, self.sheet.get_height() // self.rows,
                                self.sheet.get_height() // self.rows)

        self.frames: list = []
        self.cur_frame: int = 0
        self.cut_sheet()
        self.image: pygame.Surface = self.frames[self.cur_frame]

    def attak_animation(self):
        for i in range(len(self.frames)):
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            time.sleep(0.1)

    def cut_sheet(self):
        for i in range(self.columns):
            frame_location = (self.rect.w * i, self.rect.h * (self.column - 1))
            self.frames.append(self.sheet.subsurface(
                pygame.Rect(frame_location, self.rect.size)))

    def move(self, dx: int, dy: int):
        self.rect = self.rect.move(dx, dy)

    def attack(self):
        for i in mobs_group:
            if pygame.sprite.collide_rect(self, i):
                i.set_damage(self.damage)


class Stick(Weapon):
    def __init__(self):
        super(Stick, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', 11, 4, 10, 50, 0.5, 30)
        pass


class Bow(Weapon):
    def __init__(self):
        super(Bow, self).__init__()


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__()


class Gun(Weapon):
    def __init__(self):
        super(Gun, self).__init__()
