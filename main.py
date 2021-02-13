import subprocess
import time
from images import ghosts, walkKnight, walkRight, walkLeft
import pygame
# from gameGUI import Ui_MainWindow
from subprocess import call
from button import Button
from player import Player
from Enemy import Enemy
from AeroEnemy import AeroEnemy
from Projectile import Projectile
from Platform import Platform


aeroEnemy = [AeroEnemy(100, 240, 64, 64)]
enemies = [Enemy(200, 620, 64, 64)]
player = Player(680, 620, 64, 64)
platforms = [Platform(500, 540, 200, 25, (0, 255, 0)), Platform(100, 500, 200, 25, (0, 255, 0)),
             Platform(550, 400, 200, 25, (0, 221, 0))]
bullets = []
bg = pygame.image.load('background/spacebg.jpg')


def gameover(win):
    font1 = pygame.font.SysFont('comimcsans', 100)
    text = font1.render('GAME OVER', 1, (255, 0, 0))
    win.blit(text, ((1000 // 2) - (text.get_width() // 2), (700 // 2) - 50))

    pygame.display.update()
    i = 0
    while i < 400:
        pygame.time.delay(10)
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    pygame.quit()


def main():
    pygame.init()
    win = pygame.display.set_mode((1000, 720))
    pygame.display.set_caption("First game")
    clock = pygame.time.Clock()
    shootFreq = 0

    print("ye")
    font = pygame.font.SysFont('comicsans', 30, True)

    running = True
    index = 0

    font1 = pygame.font.SysFont('comimcsans', 18)
    text = font1.render('Health: ', True, (0, 0, 0))

    def endScreen():
        font2 = pygame.font.SysFont('comimcsans', 100)
        text2 = font2.render('You Win !', True, (255, 0, 0))
        win.blit(text2, ((500 // 2) - (text.get_width() // 2), (500 // 2) - 50))

        pygame.display.update()
        i = 0

        while i < 150:
            pygame.time.delay(10)
            i += 1
        pygame.quit()
        subprocess.call("python " + "gameGUI.py")
        quit()

    def redrawGameWindow():
        win.blit(bg, (0, 0))
        player.draw(win)

        for airEnemy in aeroEnemy:
            airEnemy.draw(win)

        for gob in enemies:
            gob.draw(win)

        for bullet in bullets:
            bullet.draw(win)

        for platform in platforms:
            platform.draw(win)
        # draw health
        win.blit(text, (25, 25))

        pygame.draw.rect(win, (0, 255, 0), (90, 25, player.health, 10))
        pygame.display.update()

    first = True
    breakLoop = False
    isBreak = False
    charAirEnemyLeft = True
    charEnemyLeft = True
    while running:
        # check if game is finished
        for gob in enemies:
            if gob.visible:
                charEnemyLeft = True
                break
            else:
                charEnemyLeft = False

        for airEnemy in aeroEnemy:
            if airEnemy.visible:
                charAirEnemyLeft = True
                break
            else:
                charAirEnemyLeft = False

        if not charAirEnemyLeft and not charEnemyLeft:
            print("bye bye")
            endScreen()

        # check if enemy attacked player
        for gob in enemies:
            if gob.visible:
                if abs(player.x - gob.x) < 30 and abs(player.y - gob.y) < 15:
                    player.health -= 1
        if player.health <= 0:
            gameover(win)

        c = 0

        if shootFreq > 0:
            shootFreq += 1
        if shootFreq > 5:
            shootFreq = 0

        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for bullet in bullets:
            if bullet.x > 1000 - bullet.vel or bullet.x < bullet.vel:
                bullets.pop(bullets.index(bullet))

            else:
                for gob in enemies:
                    if bullet.x in range(gob.x, gob.x + 20) and gob.visible:
                        if bullet.y + bullet.radius > gob.hitbox[1]:
                            gob.hit()
                            bullets.pop(bullets.index(bullet))
                for airEnemy in aeroEnemy:
                    if bullet.x in range(airEnemy.x, airEnemy.x + 20) and airEnemy.visible:
                        if abs(bullet.y + bullet.radius - airEnemy.hitbox[1]) < 35:
                            airEnemy.hit()
                            print(airEnemy.hitbox[1], bullet.y)
                    bullet.x += 5 * bullet.facing

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shootFreq == 0:

            if player.left:
                facing = -1
            elif player.right:
                facing = 1
            else:
                facing = 1
            if len(bullets) < 6:
                bullets.append(
                    Projectile(round(player.x + player.width // 2), round(player.y + player.height // 2), 5, 4, facing))

        if keys[pygame.K_LEFT] and player.x > player.vel:
            player.x -= player.vel
            player.left = True
            player.right = False
            player.standing = False
        elif keys[pygame.K_RIGHT] and player.y < 1000 - player.vel:
            player.x += player.vel
            player.left = False
            player.right = True
            player.standing = False

        else:
            player.walkCount = 0
            player.standing = True

        if not player.isJump:
            if keys[pygame.K_UP]:
                player.isJump = True
        elif player.onPlatform and player.isJump:

            if player.jumpCount >= -10:
                if player.jumpCount < 0:
                    for i in range(int((player.jumpCount ** 2) * 0.5)):
                        player.y -= - 1
                        for platform in platforms:
                            if player.y == (platform.y - platform.width * 2) and player.x in range(platform.x,
                                                                                                   platform.x + platform.length) and platform != \
                                    platforms[index]:
                                index = platforms.index(platform)
                                player.jumpCount = 10
                                player.isJump = False
                                isBreak = True
                                player.y -= 5
                            if isBreak:
                                break
                else:
                    for i in range(int((player.jumpCount ** 2) * 0.5)):
                        player.y -= 1
                        for platform in platforms:
                            if player.y == (platform.y - platform.width * 2) and player.x in range(platform.x,
                                                                                                   platform.x + platform.length) and platform != \
                                    platforms[index]:
                                index = platforms.index(platform)

                                player.jumpCount = 10
                                player.isJump = False
                                isBreak = True
                                player.y -= 5
                            if isBreak:
                                break
                        if isBreak:
                            break
                if not isBreak:
                    player.jumpCount -= 1
                isBreak = False

            else:
                player.jumpCount = 10
                player.isJump = False

        # jump and check if on platform
        else:

            if player.jumpCount >= -10:
                if player.jumpCount < 0:
                    for i in range(int((player.jumpCount ** 2) * 0.5)):
                        player.y -= - 1
                        for platform in platforms:
                            if player.y == (platform.y - platform.width * 2) and player.x in range(platform.x,
                                                                                                   platform.x + platform.length):
                                index = platforms.index(platform)
                                player.isJump = False
                                player.onPlatform = True
                                breakLoop = True
                                player.jumpCount = 10
                                break
                        if breakLoop:
                            break

                else:
                    for i in range(int((player.jumpCount ** 2) * 0.5)):
                        player.y -= 1
                        for platform in platforms:
                            if player.y == (platform.y - platform.width * 2) and player.x in range(platform.x,
                                                                                                   platform.x + platform.length):
                                index = platforms.index(platform)
                                print(platforms.index(platform))
                                player.isJump = False
                                player.onPlatform = True
                                player.jumpCount = 10
                                breakLoop = True
                                break
                        if breakLoop:
                            break
                if not breakLoop:
                    player.jumpCount -= 1
            else:
                player.jumpCount = 10
                player.isJump = False

        breakLoop = False
        redrawGameWindow()
        if first:
            player.draw(win)
            first = False
        if player.onPlatform:
            c = 0
            breakout = False
            if platforms[index].x - 32 > player.x and not player.isJump or player.x > platforms[index].x + platforms[
                index].length - 16 and not player.isJump:
                print('beamed', player.isJump)

                while player.y < 620:

                    player.y += 0.5

                    c += 0.5
                    for platform in platforms:
                        if player.y == (platform.y - platform.width * 2) and player.x in \
                                range(platform.x,
                                      platform.x + platform.length):
                            breakout = True
                            index = platforms.index(platform)
                            player.onPlatform = True

                    if c > 450 or breakout:
                        break
                if not breakout:
                    player.onPlatform = False
                    player.jumpCount = 10
                    player.isJump = False

    pygame.quit()


if __name__ == '__main__':
    main()
