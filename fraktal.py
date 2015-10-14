import pygame
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __rmul__(self, other):
        return Vector(self.x*other, self.y*other)

    def __truediv__(self, other):
        return (1/other) * self

    def __neg__(self):
        return -1 * self

    def normalized(self):
        return self / self.length()

    def coordinates(self):
        return (self.x, self.y)

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Träd")

def draw_tree(x, y, length, level):
    v1 = length * Vector(x + 3, y + 3).normalized()
    v2 = length * Vector(x - 3, y + 3).normalized()
    pygame.draw.line(screen, (0, 0, 0), (x, y), v1.coordinates())
    pygame.draw.line(screen, (0, 0, 0), (x, y), v2.coordinates())

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    draw_tree(400, 300, 100, 1)

    pygame.display.flip()

pygame.quit()