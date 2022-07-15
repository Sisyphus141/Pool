from re import X
import pygame, sys
color1 = (1, 1, 1)
pygame.init()
clock = pygame.time.Clock()
        ##450, 800
res = (550, 900)

screen = pygame.display.set_mode(res)
pygame.display.set_caption("POOL")
loop = True 
light_green = (1, 50, 32)


ball1 = pygame.image.load('./assets/ball1.png')
ball2 = pygame.image.load('./assets/ball2.png')
ball3 = pygame.image.load('./assets/ball3.png')
ball4 = pygame.image.load('./assets/ball4.png')
ball5 = pygame.image.load('./assets/ball5.png')
ball6 = pygame.image.load('./assets/ball6.png')
ball7 = pygame.image.load('./assets/ball7.png')
ball8 = pygame.image.load('./assets/ball8.png')
ball9 = pygame.image.load('./assets/ball9.png')
ball10 = pygame.image.load('./assets/ball10.png')
ball11 = pygame.image.load('./assets/ball11.png')
ball12 = pygame.image.load('./assets/ball12.png')
ball13 = pygame.image.load('./assets/ball13.png')
ball14 = pygame.image.load('./assets/ball14.png')
ball15 = pygame.image.load('./assets/ball15.png')


class ball(pygame.sprite.Sprite):
    def __init__(self, pic):
        super().__init__()

        self.image = (pic)
        self.rect = self.image.get_rect()




ball1 = ball(ball1)

ballSet = pygame.sprite.Group()
ballSet.add(ball1)


while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    screen.blit(screen, (0,0))
    ballSet.draw(screen)
    clock.tick(60)