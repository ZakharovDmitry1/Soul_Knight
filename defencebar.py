import pygame


class DefenceBar(pygame.sprite.Sprite):
    def __init__(self):
        super(DefenceBar, self).__init__(healthbar_group)
        self.health: int = health
        self.full_health: int = health
        self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/HP/Value/HP_Value_5.png')
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(0, 20)