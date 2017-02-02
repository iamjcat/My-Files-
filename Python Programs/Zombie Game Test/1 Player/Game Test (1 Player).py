import pygame   
import time   
import random   
 
pygame.init() 
 
black = (  0,   0,   0)   
white = (255, 255, 255)   
gray = (100, 100, 100)   
red = (255,   0,   0)   
blue = (  0,   0, 255)   
green = (  0, 255,   0)   
yellow = (255, 255,   0)   
purple = (255,   0, 255)   
orange = (255, 128,   0) 
 
width = 800 
height = 600  
 
window = pygame.display.set_mode((width,height)) 
pygame.display.set_caption("Game Test") 
 
RED = pygame.image.load('Red.png') 
healthPack = pygame.image.load('Health.png') 
 
clock = pygame.time.Clock() 
FPS = 30 
 
block = 30 
healthBlock = 40 
 
direction = "down" 
def red_sprite_direction(x, y): 
    pygame.draw.rect(window, white, [x + 35,y + 5,block,block]) 
    if direction == "right": 
        face = pygame.transform.rotate(RED, 180) 
        window.blit(face, (x, y))   
    if direction == "left": 
        face = RED 
        window.blit(face, (x, y))   
    if direction == "up": 
        face = pygame.transform.rotate(RED, 270) 
        window.blit(face, (x + 35, y - 30)) 
    if direction == "down": 
        face = pygame.transform.rotate(RED, 90) 
        window.blit(face, (x + 35, y - 30)) 
 
def sprite_collision(a, b): #collision function, the square brackets are unknown to me  
    return \
    a[0]+30 < b[0] + b[2] and \
    a[0]+30 + a[2] > b[0] and \
    a[1] < b[1] + b[3] and \
    a[1] + a[3] > b[1] 

def randHealthGen():
	randHealthX = round(random.randrange(0, width - healthBlock))  
	randHealthY = round(random.randrange(0, height - healthBlock))
	return randHealthX,randHealthY
 
def red_sprite_loop(): 
    global direction 
    gameExit=False 
    x,y = width/2,height/2 
    moveX,moveY = 0,0 
    randHealthX = 415 
    randHealthY = 250 
    while not gameExit: 
        for event in pygame.event.get(): 
            if (event.type == pygame.QUIT): 
                gameExit = True 
 
            if (event.type == pygame.KEYDOWN): 
                if (event.key == pygame.K_a): 
                    direction = "left" 
                    moveX = -10 
                if (event.key == pygame.K_d): 
                    direction = "right" 
                    moveX = 10 
                if (event.key == pygame.K_w): 
                    direction = "up" 
                    moveY = -10 
                if (event.key == pygame.K_s): 
                    direction = "down" 
                    moveY = 10 
                if (event.key == pygame.K_ESCAPE): 
                    gameExit = True 
             
            if (event.type==pygame.KEYUP): 
                if (event.key == pygame.K_a) or (event.key == pygame.K_d): 
                    moveX=0 
                if (event.key == pygame.K_w) or (event.key == pygame.K_s): 
                    moveY=0 
                     
        if x+50 < 0:#edge collisions  
            moveX = 1 
        elif x+50 >= width: 
            moveX = -1 
        elif y+25 >= height: 
            moveY = -1 
        elif y-5 < 0: 
            moveY = 1 
             
        x += moveX 
        y += moveY 
         
        window.fill(white) 
 
        #healthBlock = 40 
 
        #pygame.draw.rect(window, black, [randHealthX, randHealthY, healthBlock, healthBlock]) 
        window.blit(healthPack, (randHealthX, randHealthY))  
 
        red_sprite_direction(x, y) 
 
        pygame.display.update() 
 
        #if randHealthX + healthBlock >= x >= randHealthX and randHealthY + healthBlock >= y >= randHealthY: 
            #randHealthX = round(random.randrange(0, width - healthBlock))  
            #randHealthY = round(random.randrange(0, height - healthBlock)) 
        #elif randHealthX + healthBlock >= x + block >= randHealthX and randHealthY + healthBlock >= y >= randHealthY: 
            #randHealthX = round(random.randrange(0, width - healthBlock))  
            #randHealthY = round(random.randrange(0, height - healthBlock)) 
        #elif randHealthX + healthBlock >= x >= randHealthX and randHealthY + healthBlock >= y + block >= healthBlock: 
            #randHealthX = round(random.randrange(0, width - healthBlock))  
            #randHealthY = round(random.randrange(0, height - healthBlock)) 
        #elif randHealthX + healthBlock >= x + block >= randHealthX and randHealthX + healthBlock >= y + block >= randHealthY: 
            #randHealthX = round(random.randrange(0, width - healthBlock))  
            #randHealthY = round(random.randrange(0, height - healthBlock))     #Evidence of debugging the collisions  
             
        #if x >= randHealthX + healthBlock and y <= randHealthY + healthBlock: 
            #print("*contact*")  
            #randHealthX = round(random.randrange(0, width - healthBlock))  
            #randHealthY = round(random.randrange(0, height - healthBlock)) 
        #elif y + block >= randHealthY and y + block <= randHealthY + healthBlock: 
            #randHealthX = round(random.randrange(0, width - healthBlock))  
            #randHealthY = round(random.randrange(0, height - healthBlock)) 
             
        #if x < randHealthX + healthBlock and x > randHealthX - block and y < randHealthY + healthBlock and y > randHealthY - block: 
            #randHealthX = round(random.randrange(0, width - healthBlock))  
            #randHealthY = round(random.randrange(0, height - healthBlock)) 
 
         
 
        if sprite_collision((x, y, block, block), (randHealthX, randHealthY, healthBlock, healthBlock)):   
            randHealthX,randHealthY = randHealthGen()
 
        clock.tick(FPS) 
         
 
    pygame.quit() 
    quit() 
 
red_sprite_loop()  
