import pygame
from vector import Vector

pygame.init()

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Cancer")

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)