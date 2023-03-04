import copy
import os
import queue
import random
import sys
import pygame
from PIL import Image, ImageDraw

import player
from animation_sprite import Tile
from functions import load_image
from player import Player
from settings import *
from anim import *


class StartMap:
    def __init__(self, file_path: str):
        self.map: list[list] = []
        assert os.path.exists(file_path)
        with open(file_path, 'r') as file_map:
            for i in file_map.read().split('\n'):
                self.map.append([j for j in i])
        for i in range(self.map.__len__()):
            for j in range(self.map[i].__len__()):
                if self.map[i][j] == '.':
                    all_sprites.add(Tile(f'v1.1 dungeon crawler 16X16 pixel pack/tiles/floor/floor_{random.randint(1, 10)}.png',
                                         j, i, resize=TILE_SIZE))
                elif self.map[i][j] == '#':
                    walls_group.add(Tile(f'v1.1 dungeon crawler 16X16 pixel pack/tiles/wall/wall_{random.randint(1, 3)}.png',
                                         j, i, resize=TILE_SIZE))
                elif self.map[i][j] == '@':
                    self.player = Player(j, i)
                    player_group.add(Player(j, i))

    def destroy(self):
        for i in all_sprites:
            i.kill()
        for i in tiles_group:
            i.kill()
        for i in walls_group:
            i.kill()
        for i in player_group:
            i.kill()
        for i in weapons_group:
            i.kill()
        for i in bar_group:
            i.kill()
        for i in mobs_group:
            i.kill()
        for i in bullets_group:
            i.kill()
        for i in dead_enemy_group:
            i.kill()