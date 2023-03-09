import copy
import os
import queue
import random
import sys
import pygame
import pytmx as pytmx
from PIL import Image, ImageDraw
from pytmx import TiledMap

import player
from animation_sprite import Tile
from functions import load_image
from player import Player
from settings import *
from anim import *


class StartMap:
    def __init__(self, screen: pygame.Surface):
        self.map: TiledMap = pytmx.load_pygame(r"NewProject/mymap.tmx")
        self.height: int = self.map.height
        self.width: int = self.map.width
        self.tile_size = self.map.tilewidth

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