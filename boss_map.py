import csv
import json

from animation_sprite import Tile
from settings import *


class BossMap:
    def __init__(self):
        self.map: list[list[int]] = []
        with open('boss_map.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for index, row in enumerate(reader):
                self.map.append(list(map(int, row)))
        with open('tiles_for_start_map.json', 'r') as readfile:
            self.tiles_for_start_map: dict = json.load(readfile)
        for i in range(self.map.__len__()):
            for j in range(self.map[0].__len__()):
                if 5 <= self.map[i][j] <= 19:
                    walls_group.add(Tile(self.tiles_for_start_map[str(self.map[i][j])], j, i, resize=64))
                elif 20 <= self.map[i][j] <= 48:
                    tiles_group.add(Tile(self.tiles_for_start_map[str(self.map[i][j])], j, i, resize=64))
                elif self.map[i][j] == 49:
                    lava_group.add(Tile(self.tiles_for_start_map[str(self.map[i][j])], j, i, resize=64))

    def destroy(self):
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
