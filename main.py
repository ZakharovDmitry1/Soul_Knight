import pygame as pygame
from main_windows.start_game import start_game
from pygame import mixer

from main_windows.start_window import start_first_window

pygame.init()
clock = pygame.time.Clock()
mixer.init()



clock = start_first_window(clock)
start_game(clock)
clock = start_first_window(clock)
