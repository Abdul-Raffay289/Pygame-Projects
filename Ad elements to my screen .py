import pygame,sys
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Pygame Screen Elements")
WHITE=(255,255,255)
BLUE=(0,120,255)
RED=(220,50,50)
BLACK=(0,0,0)
font=pygame.font.SysFont("arial",36)
text_surface=font.render("Hello Pygame!",True,BLACK)
text_rect=text_surface.get_rect(center=(400,50))
rect1=pygame.Rect(100,150,200,100)
rect2=pygame.Rect(450,300,150,150)
clock=pygame.time.Clock()
running=True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill(WHITE)
    pygame.draw.rect(screen,BLUE,rect1)
    pygame.draw.rect(screen,RED,rect2,3)
    screen.blit(text_surface,text_rect)
    pygame.display.flip()
pygame.quit()
sys.exit()