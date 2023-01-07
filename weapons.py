import pygame
from pygame import Surface

from functions import load_image
from settings import *


class Weapon(pygame.sprite.Sprite):
    def __init__(self, sheet: Surface, rows: int, columns: int, width_image: int, cooldown: float, damage: int):
        super(Weapon, self).__init__(all_sprites, weapons_group)

        self.x = None
        self.y = None

        self.width_image: int = width_image
        self.cooldown: float = cooldown
        self.damage: int = damage
        self.sheet: Surface = sheet

        self.rows: int = rows
        self.columns: int = columns

        self.rect = pygame.Rect(0, 0, self.sheet.get_width() // self.columns,
                                self.sheet.get_height() // 12)

        self.frames: list = []
        self.cur_frame: int = 0
        self.animation()
        self.image: pygame.Surface = self.frames[self.cur_frame]

    # def set_coords(self, x: int, y: int):
    #     self.x = x
    #     self.y = y

    def animation(self):
        for i in range(self.columns):
            frame_location = (self.rect.w * i, self.rect.h * (self.rows - 1))
            self.frames.append(self.sheet.subsurface(
                pygame.Rect(frame_location, self.rect.size)))

    def move(self, dx: int, dy: int):
        self.rect = self.rect.move(dx, dy)


class Stick(Weapon):
    def __init__(self):
        super(Stick, self).__init__(load_image('RoguelikeWeapons/Weapons 3-Sheet.png'), 3, 11, 27, 0.5, 10)
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
