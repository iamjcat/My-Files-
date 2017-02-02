import pygame   
import time   
import random   
 
pygame.init() 
 
black = (  0,   0,   0)  #basic stuff  
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
 
RED = pygame.image.load('Red.png') #loads images  
BLUE = pygame.image.load('Blue.png')  
healthPack = pygame.image.load('Health.png') 
 
clock = pygame.time.Clock() 
FPS = 30 
 
block = 30 
healthBlock = 40 
 
def redPlayer (x1, y1, block):#squares that attaches to sprite   
    pygame.draw.rect(window, white, [x1 + 35,y1 + 5,block,block]) 
def bluePlayer (x2, y2, block): 
    pygame.draw.rect(window, white, [x2 + 35,y2 + 5,block,block]) 

def randHealthGen():
	randHealthX = round(random.randrange(0, width - healthBlock))  
	randHealthY = round(random.randrange(0, height - healthBlock))
	return randHealthX,randHealthY
     
     
 
 
redDirection = "left"  
blueDirection = "right"  
def sprite_direction(x1, y1, x2, y2):#turns the sprite if movement key pressed  
    redPlayer (x1, y1, block) 
    if redDirection == "left": 
        redFace = RED 
        window.blit(redFace, (x1, y1)) 
    if redDirection == "right": 
        redFace = pygame.transform.rotate(RED, 180) 
        window.blit(redFace, (x1, y1))   
    if redDirection == "up": 
        redFace = pygame.transform.rotate(RED, 270) 
        window.blit(redFace, (x1 + 35, y1 - 30)) 
    if redDirection == "down": 
        redFace = pygame.transform.rotate(RED, 90) 
        window.blit(redFace, (x1 + 35, y1 - 30)) 
 
    bluePlayer (x2, y2, block) 
    if blueDirection == "left": 
        blueFace = pygame.transform.rotate(BLUE, 180) 
        window.blit(blueFace, (x2, y2)) 
    if blueDirection == "right": 
        blueFace = BLUE 
        window.blit(blueFace, (x2 + 35, y2)) 
    if blueDirection == "up": 
        blueFace = pygame.transform.rotate(BLUE, 90) 
        window.blit(blueFace, (x2 + 35, y2 - 30)) 
    if blueDirection == "down": 
        blueFace = pygame.transform.rotate(BLUE, 270)  
        window.blit(blueFace, (x2 + 35, y2 + 10)) 
         
     
#the SQUARE BRACKETS refers to the POSITION of the VARIABLES in the NORMAL BRACKERTS below the def sprite_loop()!! 
# a[0] = x1 
# a[1] = y1 
# a[2] = block 
# b[0] = randHealthX 
# b[1] = randHealthY 
# b{2] = healthBlock 
 
# x1 < randHealthX + healthBlock  
# x1 + block > randHealthX 
# y1 < randHealthY + healthBlock 
# y1 + block > randHealthY 
 
# x1 < randHealthX + healthBlock and x1 + block > randHealthX and y1 + block > randHealthY and y1 + block > randHealthY 
def redHealth_collision(a, b): #collision function 
    return \
    a[0]+30 < b[0] + b[2] and \
    a[0]+30 + a[2] > b[0] and \
    a[1] < b[1] + b[2] and \
    a[1] + a[2] > b[1]
 
def blueHealth_collision(a, b): 
    return \
    a[0]+30 < b[0] + b[2] and \
    a[0]+30 + a[2] > b[0] and \
    a[1] < b[1] + b[2] and \
    a[1] + a[2] > b[1] 
 
 
def sprite_loop():#the main loop  
    global redDirection, blueDirection #initial sprite variables  
    gameExit=False 
    x1,y1,x2,y2 = width/2 - 150,height/2,width/2,height/2 
    moveX1,moveY1,moveX2,moveY2 = 0,0,0,0 
    randHealthX,randHealthY = 360,250  
    while not gameExit: 
        for event in pygame.event.get(): 
            if (event.type == pygame.QUIT): 
                gameExit = True 
 
            if (event.type == pygame.KEYDOWN):#movement for red player  
                if (event.key == pygame.K_a): 
                    redDirection = "left" 
                    moveX1 = -10 
                if (event.key == pygame.K_d): 
                    redDirection = "right" 
                    moveX1 = 10 
                if (event.key == pygame.K_w): 
                    redDirection = "up" 
                    moveY1 = -10 
                if (event.key == pygame.K_s): 
                    redDirection = "down" 
                    moveY1 = 10 
 
                if (event.key == pygame.K_UP):#movement for blue player  
                    blueDirection = "up" 
                    moveY2 = -10 
                if (event.key == pygame.K_DOWN): 
                    blueDirection = "down" 
                    moveY2 = 10 
                if (event.key == pygame.K_LEFT): 
                    blueDirection = "left" 
                    moveX2 = -10 
                if (event.key == pygame.K_RIGHT): 
                    blueDirection = "right" 
                    moveX2 = 10 
                 
                     
                if (event.key == pygame.K_ESCAPE):#quits game  
                    gameExit = True 
             
            if (event.type==pygame.KEYUP):#doesn't allow continuous movement if key pressed once  
                if (event.key == pygame.K_a) or (event.key == pygame.K_d): 
                    moveX1 = 0 
                if (event.key == pygame.K_w) or (event.key == pygame.K_s): 
                    moveY1 = 0 
                if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT): 
                    moveX2 = 0 
                if (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN): 
                    moveY2 = 0 
 
        if x1+50 < 0:#edge collisions  
            moveX1 = 1 
        elif x1+50 >= width: 
            moveX1 = -1 
        elif y1+25 >= height: 
            moveY1 = -1 
        elif y1-5 < 0: 
            moveY1 = 1 
 
        if x2+50 < 0: 
            moveX2 = 1 
        elif x2+50 >= width: 
            moveX2 = -1 
        elif y2+25 >= height: 
            moveY2 = -1 
        elif y2-5 < 0: 
            moveY2 = 1 
             
 
        x1 += moveX1 #converts spawn postion to movement  
        y1 += moveY1 
 
        x2 += moveX2 
        y2 += moveY2 
         
         
        window.fill(white) 
 
 
        window.blit(healthPack, (randHealthX, randHealthY))  
 
        sprite_direction(x1, y1, x2, y2) 
 
        pygame.display.update() 
        #print (event)  
                 
        if redHealth_collision((x1, y1, block, block), (randHealthX, randHealthY, healthBlock, healthBlock)):   
            randHealthX,randHealthY = randHealthGen()
 
        if blueHealth_collision((x2, y2, block, block), (randHealthX, randHealthY, healthBlock, healthBlock)):   
            randHealthX,randHealthY = randHealthGen()
 
        clock.tick(FPS) 
         
 
    pygame.quit() 
    quit() 
 
sprite_loop()  
