import pygame


class Projectile(object):
    def __init__(self, x, y, vel, radius, facing):
        self.x = x
        self.y = y
        self.vel = vel
        self.radius = radius
        self.facing = facing

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)
