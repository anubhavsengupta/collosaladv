from Enemy import Enemy
from images import ghosts

class AeroEnemy(Enemy):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.vel = 5
        self.walkCount = 24
        self.visible = True
        self.hitbox = (self.x + 5, self.y + 2, 31, 57)

    def draw(self, win):
        self.move()

        if self.visible:
            if self.walkCount + 1 > 24:
                self.walkCount = 0
            win.blit(ghosts[self.walkCount // 4], (self.x, self.y))
            self.walkCount += 1

    def move(self):
        if self.x + self.vel > 0:
            self.x -= self.vel
        else:
            self.x = 1000
            self.walkCount = 0

    def hit(self):
        self.visible = False