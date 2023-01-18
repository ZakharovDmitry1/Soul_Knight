import os.path
import sys
import time
from abc import abstractmethod
from typing import Any

import pygame.sprite
from PIL import Image

from functions import load_image
from settings import all_sprites, tiles_group, TILE_SIZE


class AnimationSprite(pygame.sprite.Sprite):
    def __init__(self, sheet: str, list_for_sprites: list[list], x: int, y: int, resize_len=75):
        self.resize_len: int = 50
        newImage = Image.open(sheet).convert('RGBA').resize(
            (resize_len * list_for_sprites[0].__len__(), resize_len * list_for_sprites.__len__()))
        newImage.save('cache/wall2.png')
        self.full_img: pygame.surface.Surface = load_image('cache/wall2.png')
        super().__init__(all_sprites)
        self.list_for_sprites: list[list[pygame.surface.Surface]] = list_for_sprites
        self.cut_sheet(self.full_img, list_for_sprites)
        self.cur_frame: int = 0
        self.cur_column: int = 0
        self.image: pygame.Surface = self.list_for_sprites[self.cur_column][self.cur_frame]
        self.rect = self.rect.move(x * TILE_SIZE, y * TILE_SIZE)
        self.timer: float = time.perf_counter()

    @abstractmethod
    def set_row(self):
        pass

    def cut_sheet(self, sheet: pygame.Surface, list_for_sprites: list[list[pygame.surface.Surface]]):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // list_for_sprites[0].__len__(),
                                sheet.get_height() // self.list_for_sprites.__len__())
        for j in range(list_for_sprites.__len__()):
            for i in range(list_for_sprites[j].__len__()):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.list_for_sprites[j][i] = sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size))

    def update(self, *args: Any, **kwargs: Any) -> None:
        # print(self.timer - time.perf_counter())
        if abs(self.timer - time.perf_counter()) > 0.07:
            self.cur_frame = (self.cur_frame + 1) % len(self.list_for_sprites[self.cur_column])
            self.image = self.list_for_sprites[self.cur_column][self.cur_frame]
            self.timer: float = time.perf_counter()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type: str, pos_x: int, pos_y: int, colorkey: tuple = (0, 0, 0), resize: int = -1):
        super().__init__(tiles_group, all_sprites)
        self.image = load_image(tile_type)
        self.image.set_colorkey(colorkey)
        if resize != -1:
            newImage = Image.open(tile_type).convert('RGBA').resize((resize, resize))
            newImage.save('cache/wall.png')
            self.image = load_image('cache/wall.png')
            self.image.set_colorkey(colorkey)
        self.rect = self.image.get_rect().move(
            TILE_SIZE * pos_x, TILE_SIZE * pos_y)
