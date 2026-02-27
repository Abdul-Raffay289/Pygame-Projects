import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Two Rectangles Game")

clock = pygame.time.Clock()

player = pygame.Rect(100, 250, 60, 60)
enemy = pygame.Rect(500, 250, 60, 60)

player_speed = 5

running = True
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed
    
    player.x = max(0, min(screen_width - player.width, player.x))
    player.y = max(0, min(screen_height - player.height, player.y))
    
    screen.fill((30, 30, 30))
    
    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)
    
    pygame.display.flip()

pygame.quit()
sys.exit()