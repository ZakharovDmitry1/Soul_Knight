import math
import time

from boss_map import BossMap
from camera import Camera
from golem import SkeletonKing
from music import SONG_MAIN_PLAY
from player import Player
from settings import *

def len_to_points(a: tuple[float, float], b: tuple[float, float]):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def boss_window(clock):
    pygame.display.set_caption("Soul_Knight")
    screen = pygame.display.set_mode((MONITOR_WIDTH, MONITOR_HEIGHT))
    map = BossMap()
    player = Player(7, 7)
    running: bool = True
    time_move_mobs: float = time.time()
    player_group.add(player)
    camera = Camera()
    time_update: float = time.time()
    SONG_MAIN_PLAY.play(1000)

    boss = SkeletonKing(10, 10)

    boss_group.add(boss)

    while running:
        player.weapon.attak_animation()
        # for i in mobs_group:
        #     i.run(TIME_UPDATE_MOBS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                player.player_attack(event.pos)
                boss.attack_fire()
                for drop in drop_weapons_group:
                    if drop.rect.collidepoint(event.pos) and len_to_points(event.pos, player.rect.center) < 80:
                        player.set_weapon(drop.kill_drop_weapon())

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pass
                # print(map.get_pos(event.pos))

            if event.type == pygame.MOUSEMOTION:
                player.weapon.set_rotate(player.weapon.rect.center, event.pos)
                # print(player.weapon.rect.center)
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT] and keys[pygame.K_UP]) or (keys[pygame.K_w] and keys[pygame.K_d]):
            player.move(0.35, -0.35)
        elif (keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]) or (keys[pygame.K_d] and keys[pygame.K_s]):
            player.move(0.35, 0.35)
        elif (keys[pygame.K_DOWN] and keys[pygame.K_LEFT]) or (keys[pygame.K_s] and keys[pygame.K_a]):
            player.move(-0.35, 0.35)
        elif (keys[pygame.K_LEFT] and keys[pygame.K_UP]) or (keys[pygame.K_a] and keys[pygame.K_w]):
            player.move(-0.35, -0.35)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.move(-0.5, 0)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.move(0.5, 0)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.move(0, 0.5)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            player.move(0, -0.5)
        if keys[pygame.K_ESCAPE]:
            running = False
        if keys[pygame.K_q]:
            pygame.display.iconify()
        # map.create_way()

        for i in bullets_group:
            if i.rect.colliderect(boss.rect):
                boss.set_damage(i.damage)
                i.kill()
                print(i.damage)


        screen.fill((44, 49, 54))
        all_sprites.update()
        all_sprites.draw(screen)
        walls_group.draw(screen)
        player_group.draw(screen)
        weapons_group.draw(screen)
        bar_group.draw(screen)
        bar_group.update()
        mobs_group.draw(screen)
        bullets_group.draw(screen)
        dead_enemy_group.draw(screen)
        drop_weapons_group.draw(screen)
        boss_group.draw(screen)

        clock.tick(FPS)
        camera.update(player)
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        pygame.display.flip()
    map.destroy()
    SONG_MAIN_PLAY.stop()