from settings import *


def destroy():
    for i in lava_group:
        i.kill()
    for i in all_sprites:
        i.kill()
    for i in tiles_group:
        i.kill()
    for i in walls_group:
        i.kill()
    for i in player_group:
        i.kill()
    for i in weapons_group:
        i.kill()
    for i in bar_group:
        i.kill()
    for i in mobs_group:
        i.kill()
    for i in bullets_group:
        i.kill()
    for i in dead_enemy_group:
        i.kill()
    for i in drop_weapons_group:
        i.kill()