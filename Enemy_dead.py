import random
import time
from animation_sprite import AnimationSprite


class EnemyDead(AnimationSprite):
    def __init__(self, pos_x: int, pos_y: int):
        super(EnemyDead, self).__init__(
            'v1.1 dungeon crawler 16X16 pixel pack/effects (new)/enemy_afterdead_explosion_anim_spritesheet.png',
            [[0] * 4 for _ in range(1)], 0, 0, resize_len=random.randint(40, 64))
        self.rect.centerx = pos_x
        self.rect.centery = pos_y
        self.count: int = 0

    def update(self, *args, **kwargs) -> None:
        f: bool = super(EnemyDead, self).update()
        if f:
            self.count += 1
        if self.count == self.list_for_sprites[0].__len__():
            self.kill()
