import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame Screen")
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLUE)
    pygame.display.update()
pygame.quit()
sys.exit()
