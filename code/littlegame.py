import pygame
from pygame.locals import *
import random
import time

pygame.init()
size = [1280,720]
sc = pygame.display.set_mode(size,FULLSCREEN)
clock = pygame.time.Clock()

def xxcheck(x,aa):
    if x+13-aa > size[0]:
        x = -13+aa
    elif x < -13+aa:
        x = size[0]-13+aa
    return x
        
def yycheck(y,bb):
    if y+13-bb > size[1]:
        y = -13+bb
    elif y < -13+bb:
        y = size[1]-13+bb
    return y

def touchx(x,y,a,b,m,n,j,aa,bb):
    
    if x <= a <= x+26-aa and y <= b <= y+26-bb:
        a = random.randint(5,1275)
        b = random.randint(5,715)
        m += 1
        n += 1
        j += 4
    else:
        pass
    return a,b,m,n,j

aa = 0
bb = 0
j = 0
tt = 0
m = 0
n = 0
a = random.randint(5,635)
b = random.randint(5,475)
x = 10
y = 10
z = 0
w = 0
white = 255,255,255 
blue = 0,0,200
green = 255,100,255

sc.fill(white)
pygame.display.update()

done = False
while not done:
    
    sc.fill(white)
    keys = pygame.key.get_pressed()
    
    x = xxcheck(x,aa/2)
    y = yycheck(y,bb/2)
    
    if keys[pygame.K_d]:
        if n <= 10:
            if z == -10:
                pass
            else:
                w = 0
                z = 10
            
            if tt == 0:
                tt = 1
                qq = time.clock()
            else:
                pass
        else:
            pass
        
    if keys[pygame.K_a]:
        if n <= 10:
            if z == 10:
                pass
            else:
                w = 0
                z = -10
            
            if tt == 0:
                tt = 1
                qq = time.clock()
            else:
                pass
        else:
            pass
        
    if keys[pygame.K_s]:
        if n <= 10:
            if w == -10:
                pass
            else:
                z = 0
                w = 10
        
            if tt == 0:
                tt = 1
                qq = time.clock()
            else:
                pass
        else:
            pass
        
    if keys[pygame.K_w]:
        if n <= 10:
            if w == 10:
                pass
            else:
                z = 0
                w = -10
            
            if tt == 0:
                tt = 1
                qq = time.clock()
            else:
                pass
        else:
            pass
        
    if keys[pygame.K_q]:
            z = 0
            w = 0
            
    if keys[pygame.K_f]:
            tt = 0
            x = 10
            y = 10
            m = 0
            n = 0
            z = 0
            w = 0
            j = 0
            aa = 0
            bb = 0
            a = random.randint(5,1275)
            b = random.randint(5,715)
    
    (a,b,m,n,j) = touchx(x,y,a,b,m,n,j,aa,bb)
    
    if m == 10 and n == 10:
        n += 1
        z = 0
        w = 0
        a = -10
        b = -10
        qq = time.clock()-qq
        rr = round(qq,2)

    if m == 10:
        pl = pygame.font.SysFont("Arial",50)
        pll = pl.render(str(rr),1,blue)
        sc.blit(pll,(625,350))
    
    if m == 5:
        aa = 6
        bb = 6
    
    x += z
    y += w
    
    pf = pygame.font.SysFont("Arial",40)
    pt = pf.render(str(m),1,blue)    
    
    mylist = [x,y,26-aa,26-bb]
    pygame.draw.rect(sc,green,mylist)
    pygame.draw.circle(sc,blue,(a,b),5)
    sc.blit(pt,(1230,680))
    pygame.display.update()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if keys[pygame.K_z]:
            done = True
            
    clock.tick(32+j)
pygame.quit()