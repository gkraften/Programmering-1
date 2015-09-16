import pygame

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("ÅÄÖÖ")

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (23, 62, 145), (10, 10, 100, 100), 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()