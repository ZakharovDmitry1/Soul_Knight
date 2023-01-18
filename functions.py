import os
import sys

import pygame

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def load_image(name: str):
    if not os.path.isfile(name):
        print(f"файл с именем '{name}' не найден")
        sys.exit()
    return pygame.image.load(name)
