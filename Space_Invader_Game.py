import math
import random
import pygame

#Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

#Initialize Pygame
pygame.init()

#Creating The Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Background
background = pygame.image.load('Background.png')

#Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('UFO.png')
pygame.display.set_icon(icon)

#Player
playerIMG = pygame.image.load('Rocket.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

#Enemy
enemyIMG = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
numbers_of_enemies = 6

#Creating enemies
for i in range(numbers_of_enemies):
    enemyIMG.append(pyagme.image.load('Enemy-removebg-preview.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))

    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Bullet
bulletIMG = pygame.load.image('Bullet.png')
bullet_X = 0
bullet_y = PLAYER_START_Y
bullet_X_change = 0
bullet_Y_change = BULLET_SPEED_Y
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font("freesonbold.ttf", 32)
textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font("freesonbold.ttf", 64)

def show_score(x, y):
    score = pygame.render("score" +str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    score = pygame.render("Game Over", True, (255, 255, 255))
    screen.blit(score, (200, 200))

def player(x, y):
    # Draw the player on the screen
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    # Draw an enemy on the screen
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    # Fire a bullet from the player's position
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    # Check if there is a collision between the enemy and a bullet
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

# Game Loop
running = True
while running:
    scree.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5

            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_X = playerX
                fire_bullet(bullet_X, bullet_y)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0
        # Player Movement
        playerX += playerX_change
        playerX = max(0, min(playerX, SCREEN_WIDTH - 64))  # 64 is the size of the player