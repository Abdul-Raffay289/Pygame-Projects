import pygame
def main():
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
    display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Color Changing Sprite')
    colors = {'Red' : pygame.Color('Red'),
    'Yellow' : pygame.Color('Yellow'),
    'Green' : pygame.Color('Green'),
    'Blue' : pygame.Color('Blue'),
    'White' : pygame.Color('White')}
    current_color = ['White']
    x, y = 30, 30
    sprite.width, sprite.height()