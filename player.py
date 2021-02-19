import pygame
from images import *
from UI.levelWins import index


with open("currentLevel", "r") as f:
    try:
        index = int(f.readline())

    except Exception as e:
        print(e)

if index == 1:
    bg = pygame.image.load('background/maxresdefault2.jpg')
else:
    bg = pygame.image.load('background/maxresdefault.jpg')



class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.standing = True
        self.left = False
        self.right = False
        self.walkCount = 0
        self.onPlatform = False
        self.isJump = False
        self.jumpCount = 10
        self.health = 100
        # win.blit(walkRight[0], (self.x, self.y))

    def draw(self, win):
        win.blit(bg, (0, 0))

        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                if self.isJump:
                    win.blit(walkLeft[0], (self.x, self.y))
                else:
                    win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
            elif self.right:
                if self.isJump:
                    win.blit(walkRight[0], (self.x, self.y))
                else:
                    win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1

        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            elif self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        if self.health <= 0:
            gameover(win)
        pygame.display.update()

    def getY(self):
        return self.y

    def getX(self):
        return self.x

