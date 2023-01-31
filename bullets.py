import time
from typing import Any

import pygame.sprite
from pygame import Surface

from functions import load_image
from settings import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, texture: Surface, start_pos: tuple[int, int], end_pos: tuple[int, int], speed: int, resize=-1):
        super(Bullet, self).__init__(bullets_group, all_sprites)
        self.image: Surface = texture
        self.rect: pygame.rect.Rect = self.image.get_rect().move(start_pos)

        self.update_time: float = 0.03 / speed
        self.current_time: float = time.time()
        self.vector_move = pygame.math.Vector2(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]).normalize()
        self.dx = self.vector_move.x
        self.dy = self.vector_move.y

    def update(self, *args: Any, **kwargs: Any) -> None:
        if time.time() - self.current_time > self.update_time:
            self.rect.move_ip(self.dx * 7, self.dy * 7)
            self.current_time = time.time()
            for i in mobs_group:
                if pygame.sprite.collide_rect(self, i):
                    i.kill()
            if pygame.sprite.spritecollideany(self, walls_group):
                self.kill()
