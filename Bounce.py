import pygame
import random
pygame.init()
#Custom Event
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT+1
Background_COLOR_CHANGE_EVENT = pygame.USEREVENT+2
#Background Color
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')
#Sprite Colorpython Bounce.py
Yellow = pygame.Color('yellow')
Magenta = pygame.Color('magenta')
Orange = pygame.Color('orange')
Green = pygame.Color('green')
#Object Class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = False
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(Background_COLOR_CHANGE_EVENT))
    def Color_Change(self):
        self.image.fill(random.choice([Yellow, Magenta, Orange, Green]))
def Change_Background_Color():
    global bg_color
    bg_color = random.choice([BLUE, DARKBLUE, LIGHTBLUE])
all_sprites_list = pygame.sprite.Group()
sp_1 = Sprite(Magenta, 20, 30)
sp_1.rect.x = random.randint(0, 480)
sp_1.rect.y = random.randint(0, 370)
all_sprites_list.add(sp_1)
screen = pygame.display.set_mode((500, 400))
bg_color = BLUE
screen.fill(bg_color)
exit = False
clock = pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp_1.Color_Change()
        elif event.type == Background_COLOR_CHANGE_EVENT:
            Change_Background_Color()
    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()