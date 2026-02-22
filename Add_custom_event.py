import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Sprites with Custom Color Change Event")

clock = pygame.time.Clock()

CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)

class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def change_color(self):
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.image.fill(self.color)

sprite1 = MySprite(200, 250, 100, 100, (255, 0, 0))
sprite2 = MySprite(500, 250, 100, 100, (0, 0, 255))

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == CHANGE_COLOR:
            sprite1.change_color()
            sprite2.change_color()

    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()