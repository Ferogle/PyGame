import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))  # creating a new window in pygame
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.png')
# player info
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
player_Change = 0

# enemy info
enemyImg = pygame.image.load('monster.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(0, 100)
enemy_Change = 4

# bullet dynamics
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bullet_YChange = 10
bullet_State = "Ready"
score = 0

def playerPos(x, y):
    screen.blit(playerImg, (x, y))


def enemyPos(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_State
    bullet_State = "fired"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = (enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2
    if distance <= 729:
        return True
    else:
        return False
    # game loop
    # makes sure that window is never closed until we quit


running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # this is for quit button to function
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_Change = -5
            if event.key == pygame.K_RIGHT:
                player_Change = 5
            if event.key == pygame.K_SPACE:
                if bullet_State is "Ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_Change = 0

    playerX += player_Change

    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    enemyX += enemy_Change
    if enemyX <= 0:
        enemy_Change = 4
        enemyY += 40
    if enemyX >= 736:
        enemy_Change = -4
        enemyY += 40
    if bulletY <= 0:
        bulletY = 480
        bullet_State = "Ready"
    if bullet_State is "fired":
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_YChange
    if isCollision(enemyX,enemyY,bulletX,bulletY):
        bulletY = 480
        bullet_State = "Ready"
        score+=1
        print(score)
        enemyX = random.randint(0, 736)
        enemyY = random.randint(0, 100)
    playerPos(playerX, playerY)
    enemyPos(enemyX, enemyY)
    pygame.display.update()  # update any change done to the game window
