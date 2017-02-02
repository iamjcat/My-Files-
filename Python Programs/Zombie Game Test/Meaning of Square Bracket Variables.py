import random
import time

width = 800
height = 600

x1 = 400
x2 = 400
y1 = 300
y2 = 300

moveX1 = 0
moveX2 = 0
moveY1 = 0
moveY2 = 0

block = 30
healthBlock = 40

randHealthX = round(random.randrange(0, width - 20))
randHealthY = round(random.randrange(0, height - 20))

(a, b) = ((x1, y1, block, block), (randHealthX, randHealthY, healthBlock, healthBlock))

print 'a[0] is x1 and equals to', a[0]
print 'a[1] is y1 and equals to', a[1]
print 'a[2] is block and equals to', a[2]
print 'a[3] is block and equals to', a[3]
print '-------------------------------------------------------------------------------'
print 'b[0] is randHealthX and equals to', b[0]
print 'b[1] is randHealthY and equals to', b[1]
print 'b[2] is healthBlock and equals to', b[2]
print 'b[3] is healthBlock and equals to', b[3]

time.sleep(100000) 
