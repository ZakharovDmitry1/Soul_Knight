from typing import Any

import pygame

from anim import Anim
from healthbar import Healthbar
from pictures_and_any import player_image, tile_width, tile_height
from settings import *
from weapons import Stick


class Player(Anim):
    def __init__(self, pos_x: int, pos_y: int, hp: int = 100, speed: int = 22):
        self.sheet: str = player_image
        self.columns: int = 4
        self.rows: int = 2
        self.list_for_sprites = [[0] * 6 for _ in range(4)]
        super(Player, self).__init__(self.sheet, self.list_for_sprites, pos_x, pos_y, speed, hp)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.set_weapon(Stick())
        self.hp_bar: Healthbar = Healthbar(self.hp)

    def move(self, dx: int, dy: int):
        super(Player, self).move(dx, dy)
        if self.weapon is not None:
            self.weapon.move(dx * self.speed, dy * self.speed)
        if dx > 0:
            self.cur_column = 3
        elif dx < 0:
            self.cur_column = 2
        elif dy != 0:
            if self.cur_column == 0:
                self.cur_column = 2
            else:
                self.cur_column = 3

        if pygame.sprite.spritecollideany(self, walls_group):
            super(Player, self).move(-dx, -dy)
            if self.weapon is not None:
                self.weapon.move(-dx * self.speed, -dy * self.speed)

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update()
        if self.cur_column == 2:
            self.cur_column = 0
        elif self.cur_column == 3:
            self.cur_column = 1
