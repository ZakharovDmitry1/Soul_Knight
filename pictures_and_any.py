import os
import sys

import pygame

from functions import load_image

tile_images = {
    'wall': load_image('Any_Pictures/walls/box.png'),
    'empty': load_image('maps/map.png')
}
player_image = load_image('Any_Pictures/mobs/m_slime.png')

tile_width = tile_height = 50
