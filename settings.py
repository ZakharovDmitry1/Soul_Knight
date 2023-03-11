import pygame
from screeninfo import get_monitors

WIDTH: int = 700
HEIGHT: int = 600

TILE_SIZE: int = 50

MAP_WIDTH: int = 100
MAP_HEIGHT: int = 100

MIN_ROOM_SIZE: int = 15
MIN_LEAF_SIZE: int = 20

MAP_UPDATE_TIME: float = 1
TIME_UPDATE_MOBS: float = 0.2
TIME_UPDATE_MOBS_ANIMATION: float = 0.07

FPS: int = 70

MOB_RADIUS: int = 25
TIME_MOVE_MOBS: float = 0.01

DEFENCE: int = 400

MONITOR_WIDTH: int = get_monitors()[0].width
MONITOR_HEIGHT: int = get_monitors()[0].height

all_sprites: pygame.sprite.Group = pygame.sprite.Group()
tiles_group: pygame.sprite.Group = pygame.sprite.Group()
walls_group: pygame.sprite.Group = pygame.sprite.Group()
player_group: pygame.sprite.Group = pygame.sprite.Group()
weapons_group: pygame.sprite.Group = pygame.sprite.Group()
bar_group: pygame.sprite.Group = pygame.sprite.Group()
mobs_group: pygame.sprite.Group = pygame.sprite.Group()
bullets_group: pygame.sprite.Group = pygame.sprite.Group()
dead_enemy_group: pygame.sprite.Group = pygame.sprite.Group()
#engry_mobs_group: pygame.sprite.Group = pygame.sprite.Group()