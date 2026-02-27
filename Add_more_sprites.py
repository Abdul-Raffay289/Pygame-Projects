import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Player vs Enemies")
clock = pygame.time.Clock()
player = pygame.Rect(370,500,60,60)
player_speed = 6
enemies = []
for i in range(7):
    enemy = pygame.Rect(random.randint(0,740),random.randint(0,200),60,60)
    enemies.append(enemy)
enemy_speed = 3
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < 740:
        player.x += player_speed
    if keys[pygame.K_UP] and player.y > 0:
        player.y -= player_speed
    if keys[pygame.K_DOWN] and player.y < 540:
        player.y += player_speed
    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.y > 600:
            enemy.x = random.randint(0,740)
            enemy.y = random.randint(-200,-60)
        if player.colliderect(enemy):
            print("Game Over!")
            running = False
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,255,0),player)
    for enemy in enemies:
        pygame.draw.rect(screen,(255,0,0),enemy)
    pygame.display.update()
pygame.quit()