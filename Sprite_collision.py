import pygame

import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400

MOVEMENT_SPEED = 5

FONT_SIZE = 72

pygame.init()

BACKGROUND_IMAGE  = pygame.transform.scale(
    pygame.image.load('GAME BACKGROUND IMAGE.avif').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT))

FONT = pygame.font.SysFont("Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.Image = pygame.Surface([width, height])
        self.Image.fill(
            pygame.Color('Yellow'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def Move(self, change_x, change_y):
        self.rect.x = max(
                          min(self.rect.x + change_x, SCREEN_WIDTH - self.rect.width), 0)

        self.rect.y = max(
                          min(self.rect.y + change_y, SCREEN_HEIGHT - self.rect.height), 0)

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.pygame.display.set_caption("Sprite Collision")

ALL_SPRITES = pygame.sprite.Group()

SPRITE_1 = Sprite(pygame.color('Yellow'), 20, 30)

SPRITE_1.rect.x, SPRITE_1.rect.y = random.randint(0, SCREEN_WIDTH - SPRITE_1.rect.width), 

random.randint(0, SCREEN_HEIGHT - SPRITE_1.rect.height)

ALL_SPRITES.add(SPRITE_1)



SPRITE_2 = Sprite(pygame.color('Green'), 20, 30)

SPRITE_2.rect.x, SPRITE_2.rect.y = random.randint(0, SCREEN_WIDTH - SPRITE_2.rect.width), 

random.randint(0, SCREEN_HEIGHT - SPRITE_2.rect.height)

ALL_SPRITES.add(SPRITE_2)

RUNNING, WON = True, False

CLOCK = clock.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            RUNNING = False
    if not WON:
        KEYS = pygame.key.get_pressed()
        change_x = (KEYS[pygame.K_RIGHT] - KEYS[pygame.K_LEFT])*MOVEMENT_SPEED

        change_y = (KEYS[pygame.K_DOWN] - KEYS[pygame.K_UP])*MOVEMENT_SPEED

        if SPRITE_1.rect.colliderect(SPRITE_2.rect):
            ALL_SPRITES.remove(SPRITE_2)

            WON = True

screen.blit(background_image, (0, 0))
all_sprites.draw(screen)
if won:
    win_text = font.render("You win!", True, pygame.Color('black'))
    screen.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2,
    (SCREEN_HEIGHT - win_text.get_height()) // 2))

pygame.display.flip()
clock.tick(90)

pygame.quit()