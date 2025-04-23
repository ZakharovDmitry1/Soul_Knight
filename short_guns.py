import pygame

from functions import load_image
from weapons import Gun, ShortGun


class Gun26(ShortGun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 8, 0), (32, 32)))
        super(Gun26, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=8, columns=11, column=1,
                                       width_image=50, damage=2, cooldown=0.7, bullet=image, max_columns=4, kill_time=0.5)


class Gun27(ShortGun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 7, 0), (32, 32)))
        super(Gun27, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=8, columns=11, column=2,
                                       width_image=50, damage=2, cooldown=0.7, bullet=image, max_columns=8, kill_time=0.7)


class Gun28(ShortGun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 6, 0), (32, 32)))
        super(Gun28, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=8, columns=11, column=3,
                                       width_image=50, damage=2, cooldown=0.7, bullet=image, max_columns=3, kill_time=0.3)


class Gun29(ShortGun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 5, 0), (32, 32)))
        super(Gun29, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=8, columns=11, column=4,
                                       width_image=50, damage=2, cooldown=0.7, bullet=image, max_columns=3, kill_time=0.4)


class Gun30(ShortGun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 4, 0), (32, 32)))
        super(Gun30, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=8, columns=11, column=5,
                                       width_image=50, damage=2, cooldown=0.5, bullet=image, max_columns=8, kill_time=0.8)


class Gun31(ShortGun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 3, 0), (32, 32)))
        super(Gun31, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=8, columns=11, column=6,
                                       width_image=50, damage=1, cooldown=0.5, bullet=image, max_columns=7, kill_time=0.8)


class Gun32(ShortGun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 2, 0), (32, 32)))
        super(Gun32, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=8, columns=11, column=7,
                                       width_image=50, damage=1, cooldown=0.5, bullet=image, max_columns=4, kill_time=0.8)


class Gun33(ShortGun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 9, 0), (32, 32)))
        super(Gun33, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=8, columns=11, column=8,
                                       width_image=50, damage=1, cooldown=0.5, bullet=image, max_columns=3, kill_time=0.9)


class Gun34(ShortGun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun34, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=8, columns=11, column=9,
                                       width_image=50, damage=1, cooldown=0.5, bullet=image, max_columns=4, kill_time=0.7)
