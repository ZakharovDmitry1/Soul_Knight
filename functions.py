import os
import sys

import pygame


def load_image(name: str):
    if not os.path.isfile(name):
        print(f"файл с именем '{name}' не найден")
        sys.exit()
    return pygame.image.load(name)
