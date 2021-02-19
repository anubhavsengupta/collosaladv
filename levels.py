from subprocess import call
from button import Button
from player import Player
from Enemy import Enemy
from AeroEnemy import AeroEnemy
from Projectile import Projectile
from Platform import Platform
import pygame
index = 0
with open("currentLevel", "r") as f:
    try:
        index = int(f.readline())
        print(index)
    except Exception as e:
        print(e)
if index == 1:
    level = [[AeroEnemy(100, 240, 64, 64)], [Enemy(200, 580, 64, 64), Enemy(300, 580, 64, 64)], Player(680, 580, 64, 64),
             [Platform(480, 540, 200, 25, (0, 255, 0)), Platform(100, 500, 200, 25, (0, 255, 0)),
              Platform(550, 400, 200, 25, (0, 221, 0))], pygame.image.load('background/maxresdefault2.jpg')]
else:

    level = [[AeroEnemy(100, 240, 64, 64)], [Enemy(200, 620, 64, 64)], Player(680, 620, 64, 64),
             [Platform(500, 540, 200, 25, (0, 255, 0)), Platform(100, 500, 200, 25, (0, 255, 0)),
              Platform(550, 400, 200, 25, (0, 221, 0))], pygame.image.load('background/maxresdefault.jpg')]
