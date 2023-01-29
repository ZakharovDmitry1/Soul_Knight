import pygame
from screeninfo import get_monitors

WIDTH: int = 700
HEIGHT: int = 600

TILE_SIZE: int = 50

MAP_WIDTH: int = 100
MAP_HEIGHT: int = 100

MIN_ROOM_SIZE: int = 15
MIN_LEAF_SIZE: int = 20

MAP_UPDATE_TIME: float = 0.5
TIME_UPDATE_MOBS: float = 0.2

FPS: int = 50

MOB_RADIUS: int = 20
TIME_MOVE_MOBS: float = 0.001

MONITOR_WIDTH: int = get_monitors()[0].width
MONITOR_HEIGHT: int = get_monitors()[0].height

all_sprites: pygame.sprite.Group = pygame.sprite.Group()
tiles_group: pygame.sprite.Group = pygame.sprite.Group()
walls_group: pygame.sprite.Group = pygame.sprite.Group()
player_group: pygame.sprite.Group = pygame.sprite.Group()
weapons_group: pygame.sprite.Group = pygame.sprite.Group()
healthbar_group: pygame.sprite.Group = pygame.sprite.Group()
mobs_group: pygame.sprite.Group = pygame.sprite.Group()
#engry_mobs_group: pygame.sprite.Group = pygame.sprite.Group()