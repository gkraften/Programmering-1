from vector import Vector
import pygame
import math

class Square:
    def __init__(self, screen, x, y, w, h, color=(255, 255, 255)):
        self.screen = screen
        self.pos = Vector(x, y)
        self.w = w
        self.h = h
        self.color = color
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.pos.x, self.pos.y, self.w, self.h))

    def update(self, time):
        self.velocity += time*self.acceleration
        self.pos += time*self.velocity
