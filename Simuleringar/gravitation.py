import pygame
from vector import Vector
from square import Square
import random

pygame.init()

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Gravitation")

square = Square(screen, 325, 0, 50, 50)
square.acceleration = Vector(0, 200)

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    t = clock.get_time() / 1000

    if square.pos.y >= screen.get_size()[1] - 50:
        square.pos = Vector(325, screen.get_size()[1] - 50)
        square.velocity = -square.velocity/1.2
        if abs(square.velocity) <= 10:
            square.velocity = Vector(0, 0)
            square.acceleration = Vector(0, 0)
    square.update(t)

    screen.fill((0, 0, 0))

    square.draw()

    pygame.display.flip()
    clock.tick(60)