import pygame.sprite

from functions import load_image
from settings import healthbar_group, all_sprites


class Healthbar(pygame.sprite.Sprite):
    def __init__(self, health: int):
        super(Healthbar, self).__init__(healthbar_group)
        self.health: int = health
        self.full_health: int = health
        self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/HP/Value/HP_Value_5.png')
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(0, 20)

    def reset_bar(self):
        if self.health / self.full_health > 4 / 5:
            self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/HP/Value/HP_Value_5.png')
        elif self.health / self.full_health > 3 / 5:
            self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/HP/Value/HP_Value_4.png')
        elif self.health / self.full_health > 2 / 5:
            self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/HP/Value/HP_Value_3.png')
        elif self.health / self.full_health > 1 / 5:
            self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/HP/Value/HP_Value_2.png')
        elif self.health / self.full_health > 0 / 5:
            self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/HP/Value/HP_Value_1.png')
        else:
            self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/HP/Value/HP_Value_0.png')


