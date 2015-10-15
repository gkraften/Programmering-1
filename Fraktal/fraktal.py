import pygame
import math
import time
from vector import Vector

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Träd")

def draw_tree(pos, length, level, angle, sep_angle=math.pi/6):
    v1 = Vector.from_polar(length, angle-sep_angle)
    v2 = Vector.from_polar(length, angle+sep_angle)
    p = Vector(*pos)
    pygame.draw.line(screen, (0, 0, 0), pos, (p + v1).coordinates())
    pygame.draw.line(screen, (0, 0, 0), pos, (p + v2).coordinates())

    level -= 1

    if level > 0:
        pos1 = p + v1
        pos2 = p + v2
        draw_tree(pos1.coordinates(), 0.7*length, level, math.atan2(v1.y, v1.x), sep_angle)
        draw_tree(pos2.coordinates(), 0.7*length, level, math.atan2(v2.y, v2.x), sep_angle)

done = False
n = 1
angle = math.pi/12 # 15°
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                angle += math.pi/24
            elif event.key == pygame.K_DOWN and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                angle -= math.pi/24
            elif event.key == pygame.K_UP:
                if n < 15:
                    n += 1
            elif event.key == pygame.K_DOWN:
                if n > 1:
                    n -= 1


    screen.fill((255, 255, 255))

    draw_tree((400, 450), 100, n, -math.pi/2, angle)

    pygame.display.flip()

pygame.quit()