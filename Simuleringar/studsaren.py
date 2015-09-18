import pygame
from vector import Vector
from square import Square
import random

pygame.init()

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Studsaren")

square = Square(screen, random.randint(0, screen.get_size()[0] - 50), random.randint(0, screen.get_size()[1] - 50), 50, 50)
square.velocity = 200 * Vector(random.uniform(-10, 10), random.uniform(-10, 10)).normalized()

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    t = clock.get_time() / 1000

    width, height = screen.get_size()
    if square.pos.x <= 0 or square.pos.x >= width - square.w:
        square.velocity = Vector(-square.velocity.x, square.velocity.y)
    if square.pos.y <= 0 or square.pos.y >= height - square.h:
        square.velocity = Vector(square.velocity.x, -square.velocity.y)
    square.update(t)

    screen.fill((0, 0, 0))

    square.draw()

    pygame.display.flip()
    clock.tick(60)