
import pygame

from functions import load_image
from weapons import Gun


class Gun1(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun1, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=1,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=3)
class Gun2(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun2, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=2,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=3)

class Gun3(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun3, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=3,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=3)

class Gun4(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun4, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=4,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=3)

class Gun5(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun5, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=5,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=3)
class Gun6(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun6, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=6,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=3)

class Gun7(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun7, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=7,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=3)

class Gun8(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun8, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=8,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=3)

class Gun9(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun9, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=9,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=4)
class Gun10(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun10, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=10,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=3)

class Gun11(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun11, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=11,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=3)

class Gun12(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun12, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=12,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=3)

class Gun13(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun13, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=13,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=3)
class Gun14(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun14, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=14,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=4)

class Gun15(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun15, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=15,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=3)

class Gun16(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun16, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=16,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=3)

class Gun17(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun17, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=17,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=3)
class Gun18(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun18, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=18,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=4)

class Gun19(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun19, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=19,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=4)

class Gun20(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun20, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=20,
                                       width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=4)


class Gun21(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun21, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=21,
                                   width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=4)


class Gun22(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun22, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=22,
                                   width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=4)


class Gun23(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun23, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=23,
                                   width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=4)


class Gun24(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun24, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=24,
                                   width_image=70, damage=10, cooldown=0.5, bullet=image, max_columns=5)


class Gun25(Gun):
    def __init__(self):
        image = load_image('RoguelikeWeapons/Bullets 2-Sheet.png').subsurface(pygame.rect.Rect((32 * 1, 0), (32, 32)))
        super(Gun25, self).__init__('RoguelikeWeapons/Weapons 1-Sheet.png', rows=8, columns=25, column=25,
                                   width_image=70, damage=10, cooldown=3, bullet=image, max_columns=8)
