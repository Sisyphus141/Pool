import pygame, sys 
loop = True 



class ball(pygame.sprite.Sprite):
    def __init__(self, pic):
        super().__init__()

        self.image = pygame.image.load(pic)
        self.rect = self.image.get_rect()


pygame.init()
clock = pygame.time.Clock()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))




ball = ball('./assets/ball2.jpg')

ballSet = pygame.sprite.Group()
ballSet.add(ball)

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    screen.blit(screen, (0,0))
    ballSet.draw(screen)
    clock.tick(60)