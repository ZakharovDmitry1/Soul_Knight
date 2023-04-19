import pygame

from functions import load_image
from weapons import ShortGun


class ShortGun1(ShortGun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 9, 0), (32, 32)))
        super(ShortGun, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=8, columns=11, column=1,
                                       width_image=50, damage=2, cooldown=0.5, bullet=image, max_columns=4)


class ShortGun2(ShortGun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 9, 0), (32, 32)))
        super(ShortGun, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=8, columns=11, column=2,
                                       width_image=50, damage=2, cooldown=0.5, bullet=image, max_columns=8)


class ShortGun3(ShortGun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 9, 0), (32, 32)))
        super(ShortGun, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=8, columns=11, column=3,
                                       width_image=50, damage=2, cooldown=0.5, bullet=image, max_columns=3)


class ShortGun4(ShortGun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 9, 0), (32, 32)))
        super(ShortGun, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=8, columns=11, column=4,
                                       width_image=50, damage=2, cooldown=0.5, bullet=image, max_columns=3)


class ShortGun5(ShortGun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 9, 0), (32, 32)))
        super(ShortGun, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=8, columns=11, column=5,
                                       width_image=50, damage=2, cooldown=0.5, bullet=image, max_columns=8)


class ShortGun6(ShortGun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 9, 0), (32, 32)))
        super(ShortGun, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=8, columns=11, column=6,
                                       width_image=50, damage=2, cooldown=0.5, bullet=image, max_columns=7)


class ShortGun7(ShortGun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 9, 0), (32, 32)))
        super(ShortGun, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=8, columns=11, column=7,
                                       width_image=50, damage=2, cooldown=0.5, bullet=image, max_columns=4)


class ShortGun8(ShortGun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 9, 0), (32, 32)))
        super(ShortGun, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=8, columns=11, column=8,
                                       width_image=50, damage=2, cooldown=0.5, bullet=image, max_columns=3)


class ShortGun9(ShortGun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 3-Sheet.png').subsurface(pygame.rect.Rect((32 * 9, 0), (32, 32)))
        super(ShortGun, self).__init__('RoguelikeWeapons/Weapons 2-Sheet.png', rows=8, columns=11, column=9,
                                       width_image=50, damage=2, cooldown=0.5, bullet=image, max_columns=4)
