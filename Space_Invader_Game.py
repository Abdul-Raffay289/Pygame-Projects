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