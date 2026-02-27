import pygame
import sys

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Background and Sound Example")

# Load background image
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Load background music
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)  # -1 means loop forever

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.blit(background, (0, 0))

    pygame.display.update()

# Quit pygame
pygame.quit()
sys.exit()