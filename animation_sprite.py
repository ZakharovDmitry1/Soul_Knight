import os.path
import sys
import time
from abc import abstractmethod
from typing import Any

import pygame.sprite
from PIL import Image

from functions import load_image
from pictures_and_any import tile_images, tile_width, tile_height
from settings import all_sprites, tiles_group


class AnimationSprite(pygame.sprite.Sprite):
    def __init__(self, sheet: pygame.Surface, columns: int, rows: int, x: int, y: int):
        super().__init__(all_sprites)
        self.frames: list = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame: int = 0
        self.image: pygame.Surface = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.timer: float = time.perf_counter()

    @abstractmethod
    def set_row(self):
        pass

    def cut_sheet(self, sheet: pygame.Surface, columns: int, rows: int):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // 2)
        for i in range(columns):
            frame_location = (self.rect.w * i, self.rect.h * (rows - 1))
            self.frames.append(sheet.subsurface(
                pygame.Rect(frame_location, self.rect.size)))

    def update(self, *args: Any, **kwargs: Any) -> None:
        # print(self.timer - time.perf_counter())
        if abs(self.timer - time.perf_counter()) > 1:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
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
        self.mask: pygame.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
