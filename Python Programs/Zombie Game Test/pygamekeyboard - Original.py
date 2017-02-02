import pygame

pygame.init()

window = pygame.display.set_mode((800,600))

pygame.display.set_caption("Window")

black = (0,0,0)
white=(255,255,255)

x,y=0,0

moveX,moveY=0,0

clock = pygame.time.Clock()

gameLoop=True
while gameLoop:

    for event in pygame.event.get():

        if (event.type==pygame.QUIT):
            gameLoop=False

        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_a):
                moveX = -5
            if (event.key==pygame.K_d):
                moveX = 5
            if (event.key==pygame.K_w):
                moveY = -5
            if (event.key==pygame.K_s):
                moveY = 5

        if (event.type==pygame.KEYUP):
            if (event.key==pygame.K_a):
                moveX=0
            if (event.key==pygame.K_d):
                moveX=0
            if (event.key==pygame.K_w):
                moveY=0
            if (event.key==pygame.K_s):
                moveY=0

    window.fill(white)

    x+=moveX
    y+=moveY

    pygame.draw.rect(window,black,(x,y,50,50))

    clock.tick(50)

    pygame.display.flip()

pygame.quit()
