import pygame

from animation_sprite import AnimationSprite
from weapons import Weapon
from settings import *


class Anim(AnimationSprite):
    def __init__(self, sheet: str, list_for_sprites: list[list], x: int, y: int, speed: int = 10, hp: int = 100):
        super(Anim, self).__init__(sheet, list_for_sprites, x, y)
        self.is_moving: bool = False
        self.speed: int = speed
        self.armor = None
        self.weapon = None
        self.hp: int = hp

    def move(self, dx: int, dy: int):
        self.rect = self.rect.move(dx * self.speed, dy * self.speed)

    def set_damage(self, hp: int):
        self.hp -= hp
        if self.hp < 0:
            self.kill()

    def attack(self):
        if self.weapon is not None:
            self.weapon.attak_animation()

    def set_armor(self, armor):
        self.armor = armor

    def set_weapon(self, weapon: Weapon):
        self.weapon = weapon
        self.weapon.move(self.rect.x + TILE_SIZE * 4 // 6, self.rect.y + TILE_SIZE * 4 // 6)

class FlyingCreature(Anim):
    def __init__(self, x: int, y: int):
        sheet = 'v1.1 dungeon crawler 16X16 pixel pack/enemies/flying creature/fly_anim_spritesheet.png'
        list_for_sprites = [[0] * 4 for _ in range(1)]
        speed = 10
        hp = 50
        super(FlyingCreature, self).__init__(sheet, list_for_sprites, x, y, speed, hp)




