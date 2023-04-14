import time
from typing import Any

import pygame.sprite
from pygame import Surface

from functions import load_image
from settings import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, texture: Surface, start_pos: tuple[int, int], end_pos: tuple[int, int], speed: int, damage: int,
                 rotate: float = 0, resize=-1, kill_time: float = 100):
        self.start_time = time.time()
        self.kill_time = kill_time
        self.damage: int = damage
        super(Bullet, self).__init__(bullets_group, all_sprites)

        if resize != -1:
            self.image: Surface = pygame.transform.rotate(pygame.transform.scale(texture, (resize, resize)), rotate)
        else:
            self.image: Surface = pygame.transform.rotate(texture, rotate)



        self.rect: pygame.rect.Rect = self.image.get_rect()
        self.rect.move_ip(start_pos)

        self.update_time: float = 0.1 / speed
        self.current_time: float = time.time()
        self.vector_move = pygame.math.Vector2(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]).normalize()
        self.dx = self.vector_move.x
        self.dy = self.vector_move.y

    def update(self, *args: Any, **kwargs: Any) -> None:
        if time.time() - self.start_time > self.kill_time:
            self.kill()
        if time.time() - self.current_time > self.update_time:
            self.rect.move_ip(self.dx * 20, self.dy * 20)
            self.current_time = time.time()
            for i in mobs_group:
                if pygame.sprite.collide_rect(self, i):
                    i.set_damage(self.damage)
                    self.kill()
            if pygame.sprite.spritecollideany(self, walls_group):
                self.kill()
