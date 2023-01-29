import copy
import os
import queue
import random
import sys
import threading

import PIL
import numpy as np
import pygame
from PIL import Image, ImageDraw

import player
from animation_sprite import Tile
from functions import load_image
# from pictures_and_any import tile_images
from player import Player
from settings import *
from anim import *


class Map:
    def __init__(self, size: tuple[int, int]):
        self.size = size
        self.leafs: list[Leaf] = []
        root: Leaf = Leaf(0, 0, size[0], size[1])
        self.leafs.append(root)
        did_split: bool = True
        self.MIN_LEAF_SIZE = 15
        self.player = None

        while (did_split):
            did_split = False
            for l in self.leafs:
                if l.leftChild is None or l.rightChild is None:
                    if l.width > self.MIN_LEAF_SIZE or l.height > self.MIN_LEAF_SIZE or random.randint(0, 100) > 25:
                        if l.split():
                            self.leafs.append(l.leftChild)
                            self.leafs.append(l.rightChild)
                            did_split = True

        root.create_rooms()

        self.map = np.array([['#'] * self.size[0] for _ in range(self.size[1])], str)

        self.create_walls()
        self.create_player()
        self.generete_sprite_walls()

        with open('maps/mainMap.txt', 'w') as file:
            for i in self.map:
                file.write(''.join(i) + '\n')

    def generate_level(self) -> Player:
        new_player, x, y = None, None, None
        wall = Image.new('RGBA', (self.map[0].__len__() * TILE_SIZE, self.map.__len__() * TILE_SIZE), '#000000')

        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == '.':
                    newImage = Image.open(
                        f'v1.1 dungeon crawler 16X16 pixel pack/tiles/floor/floor_{random.randint(1, 10)}.png').convert(
                        'RGBA').resize((TILE_SIZE, TILE_SIZE))
                    wall.paste(newImage,
                               (x * TILE_SIZE, y * TILE_SIZE))
                elif self.map[y][x] == 'f':
                    mobs_group.add(FlyingCreature(x, y))
                    newImage = Image.open(
                        f'v1.1 dungeon crawler 16X16 pixel pack/tiles/floor/floor_{random.randint(1, 10)}.png').convert(
                        'RGBA').resize((TILE_SIZE, TILE_SIZE))
                    wall.paste(newImage,
                               (x * TILE_SIZE, y * TILE_SIZE))
                elif self.map[y][x] == 'g':
                    mobs_group.add(GoblinCreature(x, y))
                    newImage = Image.open(
                        f'v1.1 dungeon crawler 16X16 pixel pack/tiles/floor/floor_{random.randint(1, 10)}.png').convert(
                        'RGBA').resize((TILE_SIZE, TILE_SIZE))
                    wall.paste(newImage,
                               (x * TILE_SIZE, y * TILE_SIZE))
                elif self.map[y][x] == '@':
                    newImage = Image.open(
                        f'v1.1 dungeon crawler 16X16 pixel pack/tiles/floor/floor_{random.randint(1, 10)}.png').convert(
                        'RGBA').resize((TILE_SIZE, TILE_SIZE))
                    wall.paste(newImage,
                               (x * TILE_SIZE, y * TILE_SIZE))
                    self.player = Player(x, y)
        wall.save('maps/map.png')
        Tile('maps/map.png', 0, 0)
        # вернем игрока
        return self.player

    def generete_sprite_walls(self):
        map2: list[list[str]] = self.map.copy()

        for i in range(self.map.__len__()):
            for j in range(self.map[0].__len__()):
                if map2[i][j] == '#':
                    j1: int = j
                    i1: int = i
                    while j1 < map2[0].__len__() and map2[i1][j1] == '#':
                        j1 += 1
                    while True:
                        if i1 == map2.__len__():
                            break
                        f: bool = True
                        for n in range(j, j1):
                            if map2[i1][n] != '#':
                                f = False
                        if not f:
                            break
                        else:
                            i1 += 1
                    for x in range(i, i1):
                        for y in range(j, j1):
                            map2[x][y] = '.'
                    img: Image = PIL.Image.new('RGBA', (TILE_SIZE * (j1 - j), TILE_SIZE * (i1 - i)), (0, 0, 0, 0))

                    for x in range(j1 - j):
                        for y in range(i1 - i):
                            newImage: Image = Image.open(
                                f'v1.1 dungeon crawler 16X16 pixel pack/tiles/wall/wall_{random.randint(1, 2)}.png').convert(
                                'RGBA').resize((TILE_SIZE, TILE_SIZE))
                            img.paste(newImage, (x * TILE_SIZE, y * TILE_SIZE))
                    # img = img.rotate(90)
                    img.save('cache/wall.png')
                    walls_group.add(
                        Tile(f'cache/wall.png', j, i))

    def create_player(self):
        f = True
        for i in range(self.map.__len__()):
            for j in range(self.map[i].__len__()):
                if self.map[i][j] == '.' and self.map[i + 1][j] == '.' and self.map[i - 1][j] == '.' \
                        and self.map[i][j - 1] == '.' and self.map[i + 1][j - 1] == '.' and self.map[i - 1][
                    j - 1] == '.' and \
                        self.map[i + 1][j + 1] == '.' and self.map[i - 1][j + 1] == '.' and self.map[i][j + 1] == '.' \
                        and self.map[i][j - 2] == '.' and self.map[i][j - 3] == '.' \
                        and self.map[i][j + 2] == '.' and self.map[i][j + 3] == '.' \
                        and self.map[i - 2][j] == '.' and self.map[i - 3][j] == '.' \
                        and self.map[i + 2][j] == '.' and self.map[i + 3][j] == '.':
                    self.map[i][j] = '@'
                    f = False
                    break
            if not f:
                break

    def create_walls(self):
        for leaf in self.leafs:
            if leaf.halls.__len__() > 0:
                for i in range(leaf.halls[0][0], leaf.halls[0][0] + leaf.halls[0][2]):
                    for j in range(leaf.halls[0][1], leaf.halls[0][1] + leaf.halls[0][3]):
                        self.map[j][i] = '.'
                if leaf.halls.__len__() == 2:
                    for i in range(leaf.halls[1][0], leaf.halls[1][0] + leaf.halls[1][2]):
                        for j in range(leaf.halls[1][1], leaf.halls[1][1] + leaf.halls[1][3]):
                            self.map[j][i] = '.'
            if leaf.rightChild is not None or leaf.leftChild is not None:
                continue
            for i in range(leaf.x + leaf.roomPos[0] + 1, leaf.x + leaf.roomPos[0] + leaf.roomSize[0]):
                for j in range(leaf.y + leaf.roomPos[1] + 1, leaf.y + leaf.roomPos[1] + leaf.roomSize[1]):
                    self.map[j][i] = leaf.room_map[i - (leaf.x + leaf.roomPos[0] + 1)][
                        j - (leaf.y + leaf.roomPos[1] + 1)]

    def get_pos(self, rect_pos: tuple[int, int]) -> tuple[int, int]:
        x: int = rect_pos[0] + self.player.real_pos_x + self.player.rect.h // 2 - MONITOR_WIDTH // 2 - 20
        y: int = rect_pos[1] + self.player.real_pos_y + self.player.rect.w // 2 - MONITOR_HEIGHT // 2 - 20
        return x // TILE_SIZE, y // TILE_SIZE

    def get_real_pos(self, mouse_pos: tuple[int, int]) -> tuple[int, int]:
        x: int = mouse_pos[0] + self.player.real_pos_x + self.player.rect.h // 2 - MONITOR_WIDTH // 2 - 20
        y: int = mouse_pos[1] + self.player.real_pos_y + self.player.rect.w // 2 - MONITOR_HEIGHT // 2 - 20
        return x, y

    def get_pos_for_map(self, pos: tuple[int, int]) -> tuple[int, int]:
        return pos[0] * TILE_SIZE + TILE_SIZE // 2, pos[1] * TILE_SIZE + TILE_SIZE // 2

    def create_way(self):
        y_pos, x_pos = self.get_pos(
            (self.player.rect.x + self.player.rect.h // 2, self.player.rect.y + self.player.rect.w // 2))

        lx = x_pos - self.player.mob_radius
        rx = x_pos + self.player.mob_radius

        ly = y_pos - self.player.mob_radius
        ry = y_pos + self.player.mob_radius

        arr_pos_x = self.player.mob_radius + 1
        arr_pos_y = self.player.mob_radius + 1

        if lx < 0:
            arr_pos_x += lx
            lx = 0
        if rx >= MAP_HEIGHT:
            rx = MAP_HEIGHT - 1
        if ly < 0:
            arr_pos_y += ly
            ly = 0
        if ry >= MAP_WIDTH:
            ry = MAP_WIDTH - 1

        self.array: np.ndarray = np.zeros(((rx - lx) + 3, (ry - ly) + 3), int)

        for i in range(lx, rx + 1):
            for j in range(ly, ry + 1):
                if self.map[i][j] == '#':
                    self.array[i - lx + 1][j - ly + 1] = -1

        for i in range(ry - ly + 3):
            self.array[0][i] = -1
            self.array[(rx - lx) + 2][i] = -1

        for i in range(rx - lx + 3):
            self.array[i][0] = -1
            self.array[i][(ry - ly) + 2] = -1

        self.voln(arr_pos_x, arr_pos_y, lx, rx, ly, ry)

    def voln(self, pos_x: int, pos_y: int, lx: int, rx: int, ly: int, ry: int):
        my_queue = queue.Queue()
        my_queue.put((pos_x, pos_y))
        self.array[pos_x][pos_y] = 1
        while not my_queue.empty():
            pos = my_queue.get()
            for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = pos[0] + i[0], pos[1] + i[1]
                if self.array[new_x][new_y] == 0 and self.array[pos[0]][pos[1]] < self.player.mob_radius:
                    self.array[new_x][new_y] = self.array[pos[0]][pos[1]] + 1
                    my_queue.put((new_x, new_y))

        # for i in self.array:
        #     for j in i:
        #         print(j, end='\t')
        #     print()

        for mob in mobs_group:
            y, x = self.get_pos((mob.rect.x + mob.rect.h // 2, mob.rect.y + mob.rect.w // 2))
            if lx <= x <= rx and ly <= y <= ry:
                pos: list = [x, y]
                a, b = self.get_real_pos((mob.rect.x + mob.rect.h // 2, mob.rect.y + mob.rect.w // 2))
                my_lst: list[tuple[int, int]] = [self.get_real_pos((mob.rect.x + mob.rect.h // 2, mob.rect.y + mob.rect.w // 2))]
                if self.array[pos[0] - lx][pos[1] - ly] <= 0:
                    continue
                flag = True
                while flag:
                    t = False
                    for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        new_y, new_x = pos[1] + i[1], pos[0] + i[0]
                        #print(self.array[new_x][new_y])
                        if self.array[new_x - lx][new_y - ly] == self.array[pos[0] - lx][pos[1] - ly] - 1:
                            my_lst.append(self.get_pos_for_map((new_y, new_x)))
                            pos[0] = new_x
                            pos[1] = new_y
                            break
                    if self.array[pos[0] - lx][pos[1] - ly] == 1:
                        flag = False
                my_lst.append(self.get_real_pos((self.player.rect.x + self.player.rect.h // 2,
                                                 self.player.rect.y + self.player.rect.w // 2)))
                #mob.run(my_lst)
                #mob.set_way(my_lst)
                mob.set_way(my_lst)

        self.array = None


class Leaf:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.room = None
        self.leftChild = None
        self.rightChild = None
        self.halls: list[tuple] = []
        self.MIN_LEAF_SIZE: int = MIN_LEAF_SIZE
        self.room_map = None

    def create_rooms(self):
        if self.leftChild is not None or self.rightChild is not None:
            if self.leftChild is not None:
                self.leftChild.create_rooms()
            if self.rightChild is not None:
                self.rightChild.create_rooms()
            if self.leftChild is not None and self.rightChild is not None:
                self.createHall(self.leftChild.getRoom(), self.rightChild.getRoom())
        else:
            self.roomSize: tuple = (random.randint(MIN_ROOM_SIZE, self.width - 2),
                                    random.randint(MIN_ROOM_SIZE, self.height - 2))
            self.roomPos: tuple = \
                (random.randint(1, self.width - self.roomSize[0] - 1),
                 random.randint(1, self.height - self.roomSize[1] - 1))
            self.room = (self.roomPos[0] + self.x, self.roomPos[1] + self.y,
                         self.roomSize[0], self.roomSize[1])
            self.room_map = [[''] * self.roomSize[1] for _ in range(self.roomSize[0])]
            for i in range(self.roomSize[0]):
                for j in range(self.roomSize[1]):
                    if random.randint(0, 100) == 0:
                        self.room_map[i][j] = 'f'
                    elif random.randint(0, 100) == 1:
                        self.room_map[i][j] = 'g'
                    else:
                        self.room_map[i][j] = '.'

    def split(self) -> bool:
        if self.leftChild is not None or self.rightChild is not None:
            return False
        splitH: bool = random.randint(0, 10) > 5
        if self.width > self.height and self.width / self.height >= 1.25:
            splitH = False
        elif self.width <= self.height and self.height / self.width >= 1.25:
            splitH = True
        max: int = 0
        if splitH:
            max = self.height - self.MIN_LEAF_SIZE
        else:
            max = self.width - self.MIN_LEAF_SIZE
        if max <= self.MIN_LEAF_SIZE:
            return False
        split: int = random.randint(self.MIN_LEAF_SIZE, max)
        if splitH:
            self.leftChild = Leaf(self.x, self.y, self.width, split)
            self.rightChild = Leaf(
                self.x, self.y + split, self.width, self.height - split)
        else:
            self.leftChild = Leaf(self.x, self.y, split, self.height)
            self.rightChild = Leaf(
                self.x + split, self.y, self.width - split, self.height)
        return True

    def getRoom(self) -> tuple[int]:
        if self.room is not None:
            return self.room
        else:
            if self.leftChild is not None:
                lRoom = self.leftChild.getRoom()
            if self.rightChild is not None:
                rRoom = self.rightChild.getRoom()
            if lRoom is None and rRoom is not None:
                return None
            elif rRoom is None:
                return lRoom
            elif lRoom is None:
                return rRoom
            elif random.randint(0, 100) > 50:
                return lRoom
            else:
                return rRoom

    def createHall(self, l: tuple[int], r: tuple[int]) -> None:
        point1 = Pair(random.randint(l[0] + 3, l[0] + l[2] - 3),
                      random.randint(l[1] + 3, l[1] + l[3] - 3))
        point2 = Pair(random.randint(r[0] + 3, r[0] + r[2] - 3),
                      random.randint(r[1] + 3, r[1] + r[3] - 3))
        w: int = point2.first - point1.first
        h: int = point2.second - point1.second

        coridor: int = 3
        # ширина коридора

        if w < 0:
            if h < 0:
                if random.randint(0, 100) < 50:
                    self.halls.append((point2.first, point1.second, abs(w), coridor))
                    self.halls.append((point2.first, point2.second, coridor, abs(h)))
                else:
                    self.halls.append((point2.first, point2.second, abs(w), coridor))
                    self.halls.append((point1.first, point2.second, coridor, abs(h)))
            elif h > 0:
                if random.randint(0, 100) < 50:
                    self.halls.append((point2.first, point1.second, abs(w), coridor))
                    self.halls.append((point2.first, point1.second, coridor, abs(h)))
                else:
                    self.halls.append((point2.first, point2.second, abs(w), coridor))
                    self.halls.append((point1.first, point1.second, coridor, abs(h)))
            else:
                self.halls.append((point2.first, point2.second, abs(w), coridor))
        elif w > 0:
            if h < 0:
                if random.randint(0, 100) < 50:
                    self.halls.append((point1.first, point2.second, abs(w), coridor))
                    self.halls.append((point1.first, point2.second, coridor, abs(h)))
                else:
                    self.halls.append((point1.first, point1.second, abs(w), coridor))
                    self.halls.append((point2.first, point2.second, coridor, abs(h)))
            elif h > 0:
                if random.randint(0, 100) < 50:
                    self.halls.append((point1.first, point1.second, abs(w), coridor))
                    self.halls.append((point2.first, point1.second, coridor, abs(h)))
                else:
                    self.halls.append((point1.first, point2.second, abs(w), coridor))
                    self.halls.append((point1.first, point1.second, coridor, abs(h)))
            else:
                self.halls.append((point1.first, point1.second, abs(w), coridor))
        else:
            if h < 0:
                self.halls.append((point2.first, point2.second, coridor, abs(h)))
            elif h > 0:
                self.halls.append((point1.first, point1.second, coridor, abs(h)))
