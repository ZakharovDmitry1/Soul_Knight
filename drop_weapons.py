import pygame.sprite
from PIL import Image
from pygame.surface import Surface

from functions import load_image
from settings import all_sprites, drop_weapons_group
from weapons import Weapon
from guns import *


class DropWeapon(pygame.sprite.Sprite):
    def __init__(self, path_img: str, columns: int, rows: int, column: int, width_image: int, pos: tuple[int, int]):
        super(DropWeapon, self).__init__(all_sprites, drop_weapons_group)

        new_img = Image.open(path_img).convert('RGBA')
        new_img = new_img.resize(((int)(rows * width_image),
                                  (int)(columns * width_image)))
        new_img.save('cache/weapon.png')

        sheet = load_image('cache/weapon.png')

        self.width_image: int = width_image
        self.sheet: Surface = sheet

        self.rows: int = rows
        self.columns: int = columns

        self.column: int = column

        self.rect = pygame.Rect(pos[0], pos[1], width_image,
                                width_image)
        frame_location = (0, self.rect.h * (self.column - 1))
        self.image: pygame.Surface = self.sheet.subsurface(
            pygame.Rect(frame_location, self.rect.size))

    def kill_drop_weapon(self) -> Weapon:
        p = self.column
        self.kill()
        return eval(f'Gun{p}()')
