import pygame
from vector import Vector
import random
import math

class Planet:
    def __init__(self, radius, x, y, density, color=(255, 255, 255)):
        self.mass = density*math.pi*radius**2
        self.pos = Vector(x, y)
        self.radius = radius
        self.color = color
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

    def apply_force(self, force):
        self.acceleration += force/self.mass

    def update(self, time):
        self.velocity += time*self.acceleration
        self.pos += time*self.velocity
        self.acceleration = Vector(0, 0)

        if abs(self.velocity) > 500:
            self.velocity = Vector(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("Planeter")

planets = []
for i in range(int(screen.get_size()[0]/120)):
    planets.append(Planet(random.randint(30, 60), random.randint(60, screen.get_size()[0] - 60), random.randint(60, screen.get_size()[1] - 60), 3))

moon = Planet(10, screen.get_size()[0]/2 - 200, screen.get_size()[1]/2, 1, (255, 0, 0))

clock = pygame.time.Clock()
done = False
acc = Vector(0, 0)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                moon.velocity = -acc
            if event.key == pygame.K_ESCAPE:
                done = True

    t = clock.get_time() / 1000

    width, height = screen.get_size()
    if moon.pos.x <= moon.radius or moon.pos.x >= width - moon.radius:
        if moon.pos.x <= moon.radius:
            moon.pos.x = moon.radius
        if moon.pos.x >= width - moon.radius:
            moon.pos.x = width - moon.radius
        moon.velocity = Vector(-moon.velocity.x, moon.velocity.y)
    if moon.pos.y <= moon.radius or moon.pos.y >= height - moon.radius:
        if moon.pos.y <= moon.radius:
            moon.pos.y = moon.radius
        if moon.pos.y >= height - moon.radius:
            moon.pos.y = height - moon.radius
        moon.velocity = Vector(moon.velocity.x, -moon.velocity.y)

    for planet in planets:
        distance = planet.pos - moon.pos
        distance_len = abs(distance)
        force_amp = 50*planet.mass*moon.mass/distance_len**2
        angle = math.atan2(distance.y, distance.x)
        force = force_amp*Vector(math.cos(angle), math.sin(angle))
        moon.apply_force(force)

        if distance_len <= planet.radius + moon.radius:
            hit_plane1 = Vector(-distance.y, distance.x)
            hit_plane2 = -hit_plane1
            hit_angle1 = math.acos((hit_plane1*moon.velocity)/(abs(hit_plane1)*abs(moon.velocity)))
            hit_angle2 = math.acos((hit_plane2*moon.velocity)/(abs(hit_plane2)*abs(moon.velocity)))
            hit_angle = 0
            if hit_angle1 < hit_angle2:
                hit_angle = hit_angle1
            else:
                hit_angle = hit_angle2
            moon.velocity = moon.velocity.rotated(2*hit_angle)
            direction = -distance.normalized()
            moon.pos += (planet.radius - distance_len)*direction + moon.radius*direction.normalized()
    acc = moon.acceleration
    moon.update(t)

    screen.fill((0, 0, 0))

    for planet in planets:
        planet.draw(screen)
    moon.draw(screen)

    pygame.draw.line(screen, (0, 255, 0), list(moon.pos), list(moon.pos + moon.velocity), 2)
    pygame.draw.line(screen, (255, 0, 255), list(moon.pos), list(moon.pos + acc), 2)

    pygame.display.flip()
    clock.tick(100)