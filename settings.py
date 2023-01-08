import pygame
from screeninfo import get_monitors

WIDTH: int = 700
HEIGHT: int = 600

TILE_SIZE: int = 50

MAP_WIDTH: int = 50
MAP_HEIGHT: int = 50

FPS: int = 50

MONITOR_WIDTH: int = get_monitors()[0].width
MONITOR_HEIGHT: int = get_monitors()[0].height

all_sprites: pygame.sprite.Group = pygame.sprite.Group()
tiles_group: pygame.sprite.Group = pygame.sprite.Group()
walls_group: pygame.sprite.Group = pygame.sprite.Group()
player_group: pygame.sprite.Group = pygame.sprite.Group()
weapons_group: pygame.sprite.Group = pygame.sprite.Group()
healthbar_group: pygame.sprite.Group = pygame.sprite.Group()