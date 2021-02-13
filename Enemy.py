import pygame
from images import *


class Enemy(object):
    def __init__(self, x, y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 4
        self.health = 10
        self.walkCount = 32
        self.visible = True
        self.hitbox = (self.x + 5, self.y + 2, 31, 57)

    def draw(self, win):
        self.move()

        if self.visible:
            if self.walkCount + 1 > 30:
                self.walkCount = 0

            win.blit(walkKnight[self.walkCount // 2], (self.x, self.y))
            self.walkCount += 1
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            pygame.draw.rect(win, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 5 * (10 - self.health), 10))
         # if player.health <= 0:
         #     gameover(win)

    def move(self):
        if self.x + self.vel < 1000:
            self.x += self.vel
        else:
            self.x = 0
            self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
