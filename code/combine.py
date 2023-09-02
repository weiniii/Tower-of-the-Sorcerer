import pygame
from pygame.locals import *
import time
import random
import char
import numpy as np

def getmat(name):
    mat = np.zeros((9,16))
    a = 0

    with open(name,'r') as rf:
        k = rf.read()
        for m in range(0,9):
            for n in range(0,16):
                mat[m,n] += int(k[a])
                a += 1
            a += 1
    return mat        
    
def drawmap(mat):            
    for m in range(0,9):
        for n in range(0,16):
            if mat[m,n] == 1:
                sc.blit(pp12,(80*n,80*m))
            else:
                pass
            
def wall(mat,xr,yr,xk,yk):
    if mat[yr+yk,xr+xk] == 0:
        xr += xk
        yr += yk
    else:
        pass
        
    return xr,yr

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
        a = random.randint(5,635)
        b = random.randint(5,475)
        m += 1
        n += 1
        j += 5
    else:
        pass
    return a,b,m,n,j

def switchmap(xr,yr,xk,yk,k,entry,exit):
    if exit[1] == 8:
        if xr == exit[0] and yr+yk == exit[1]+1:
            k += 1
            xr = exit[0]
            yr = 0
    elif exit[0] == 15:
        if xr+xk == exit[0]+1 and yr == exit[1]:
            k += 1
            xr = 0
            yr = exit[1]
    elif exit[1] == 0:
        if xr == exit[0] and yr+yk == exit[1]-1:
            k += 1
            xr = exit[0]
            yr = 8
    elif exit[0] == 0:
        if xr+xk == exit[0]-1 and yr == exit[1]:
            k += 1
            xr = 15
            yr = exit[1]
            
    if entry[0] == 0:
        if xr+xk == entry[0]-1 and yr == entry[1]:
            k -= 1
            xr = 15
            yr = entry[1]
    elif entry[1] == 0:
        if xr == entry[0] and yr+yk == entry[1]-1:
            k -= 1
            xr = entry[0]
            yr = 8
    elif entry[0] == 15:
        if xr+xk == entry[0]+1 and yr == entry[1]:
            k += 1
            xr = 0
            yr = entry[1]
    elif entry[1] == 8:
        if xr == entry[0] and yr+yk == entry[1]+1:
            k += 1
            xr = entry[0]
            yr = 0       
    return xr,yr,k

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
con = 0

pygame.init()
size = [1280,720]
sc = pygame.display.set_mode(size,FULLSCREEN)
clock = pygame.time.Clock()

dd1 = pygame.image.load('new.png')
pp1 = pygame.transform.scale(dd1, (50,50))

dd2 = pygame.image.load('continue.png')
pp2 = pygame.transform.scale(dd2, (50,50))

dd3 = pygame.image.load('exit.png')
pp3 = pygame.transform.scale(dd3, (50,50))

dd4 = pygame.image.load('setting.png')
pp4 = pygame.transform.scale(dd4, (60,60))

dd5 = pygame.image.load('book.png')
pp5 = pygame.transform.scale(dd5, (65,65))

dd6 = pygame.image.load('setting2.png')
pp6 = pygame.transform.scale(dd6, (60,60))

dd7 = pygame.image.load('book2.png')
pp7 = pygame.transform.scale(dd7, (65,65))

dd8 = pygame.image.load('att1.png')
pp8 = pygame.transform.scale(dd8, (80,80))

dd9 = pygame.image.load('att2.png')
pp9 = pygame.transform.scale(dd9, (80,80))

dd10 = pygame.image.load('start.png')
pp10 = pygame.transform.scale(dd10, (60,60))

dd11 = pygame.image.load('load.png')
pp11 = pygame.transform.scale(dd11, (60,60))

dd12 = pygame.image.load('block.png')
pp12 = pygame.transform.scale(dd12,(80,80))

dd13 = pygame.image.load('information1.png')
pp13 = pygame.transform.scale(dd13,(60,60))

dd14 = pygame.image.load('information2.png')
pp14 = pygame.transform.scale(dd14,(60,60))

#tree = pygame.image.load('tree.png')
rose = 255,228,225
bacc = 220,238,238
white = 255,255,255 
blue = 0,0,200
green = 255,100,255
acc = 255,250,250
maincolor = 32,80,230
color1 = 179,153,255
color2 = 179,153,255
color3 = 179,153,255

k = 1
#判別地圖

xr = 1
yr = 1
#主角位置

xk = 0
yk = 0
#主角位移量

qu = 0
#判斷Quit按鍵

yp = 644
yl = 46
#關於欄伸縮的Y座標及Y長度

yyqu = 0
#判斷關於伸縮欄長度

ypos1 = 560
ypos2 = 565
#按下QUIT鍵後的位置

sc.fill(bacc)
pygame.display.update()

a1 = 340
b1 = 55
c1 = (size[0]-a1)/2
d1 = 320

a2 = 295
b2 = 55
c2 = (size[0]-a2)/2
d2 = 440

a3 = 140
b3 = 55
c3 = (size[0]-a3)/2
d3 = 560

pos = (0,0)
pa = (0,0,0)
pb = (0,0,0)
pc = (0,0,0)
pd = (0,0,0)
pe = (0,0,0)
pf = (0,0,0)
pg = (0,0,0)

done = False
while not done:
    
    sc.fill(bacc)
    pygame.draw.rect(sc,bacc,[c1,d1,a1,b1])
    pygame.draw.rect(sc,bacc,[c2,d2,a2,b2])
    pygame.draw.rect(sc,bacc,[c3,d3,a3,b3])
    pygame.draw.rect(sc,maincolor,[369,275,542,6])
    
    keys = pygame.key.get_pressed()
    
    pk = pygame.font.SysFont("Arial",130)
    pkk = pk.render('Main Menu',1,maincolor)
    sc.blit(pkk,(400,175))
    
    p1 = pygame.font.SysFont("Arial",95)
    p11 = p1.render('New Game',1,color1)
    sc.blit(p11,(467,320))
    
    p2 = pygame.font.SysFont("Arial",95)
    p22 = p2.render('Continue',1,color2)
    sc.blit(p22,(490,440))
    
    p3 = pygame.font.SysFont("Arial",95)
    p33 = p3.render('Quit',1,color3)
    sc.blit(p33,(570,560))
    
    if c1 <= pos[0] <= c1+a1 and d1 <= pos[1] <= d1+b1:
        q1,w1,e1 = pa
        color1 = 140,230,0
        sc.blit(pp1,(407,325))
        sc.blit(pp1,(815,325))
        if q1 == 1:
            checkmenu = 0
            newgame = 1
            while newgame!=0:
                sc.fill(white)
                keys = pygame.key.get_pressed()

                if k == 1:
                    mat = getmat('map1.txt')
                    drawmap(mat)
                    xr,yr,k = switchmap(xr,yr,xk,yk,k,[0,0],[14,8])
                if k == 2:
                    mat = getmat('map2.txt')
                    drawmap(mat)
                    xr,yr,k = switchmap(xr,yr,xk,yk,k,[14,0],[13,8])
                if k == 3:
                    mat = getmat('map3.txt')
                    drawmap(mat)
                    xr,yr,k = switchmap(xr,yr,xk,yk,k,[13,0],[1,8])
                if k == 4:
                    mat = getmat('map4.txt')
                    drawmap(mat)
                    xr,yr,k = switchmap(xr,yr,xk,yk,k,[1,0],[13,8])
                if k == 5:
                    mat = getmat('map5.txt')
                    drawmap(mat)
                    xr,yr,k = switchmap(xr,yr,xk,yk,k,[13,0],[0,7])
                if k == 6:
                    mat = getmat('map6.txt')
                    drawmap(mat)
                    xr,yr,k = switchmap(xr,yr,xk,yk,k,[15,7],[2,8])
                if k == 7:
                    mat = getmat('map7.txt')
                    drawmap(mat)
                    xr,yr,k = switchmap(xr,yr,xk,yk,k,[2,0],[15,6])
                if k == 8:
                    mat = getmat('map8.txt')
                    drawmap(mat)
                    xr,yr,k = switchmap(xr,yr,xk,yk,k,[0,6],[5,8])
                if k == 9:
                    mat = getmat('map9.txt')
                    drawmap(mat)
                    xr,yr,k = switchmap(xr,yr,xk,yk,k,[5,0],[4,8])
                if k == 10:
                    mat = getmat('map10.txt')
                    drawmap(mat)
                    xr,yr,k = switchmap(xr,yr,xk,yk,k,[4,0],[12,8])
                if k == 11:
                    mat = getmat('map11.txt')
                    drawmap(mat)
                    xr,yr,k = switchmap(xr,yr,xk,yk,k,[12,0],[1,8])
                if k == 12:
                    mat = getmat('map12.txt')
                    drawmap(mat)
                    xr,yr,k = switchmap(xr,yr,xk,yk,k,[1,0],[6,8])
                if k == 13:
                    mat = getmat('map13.txt')
                    drawmap(mat)
                    xr,yr,k = switchmap(xr,yr,xk,yk,k,[6,0],[15,4])
                if k == 14:
                    mat = getmat('map14.txt')
                    drawmap(mat)
                    xr,yr,k = switchmap(xr,yr,xk,yk,k,[0,4],[15,4])
                if k == 15:
                    mat = getmat('map15.txt')
                    drawmap(mat)
                    xr,yr,k = switchmap(xr,yr,xk,yk,k,[0,4],[15,8])
                        
                if checkmenu%2 == 0:
                    if keys[pygame.K_d]:
                        xk = 1
                        yk = 0
                        if xr+xk > 15:
                            pass
                        else:
                            xr,yr = wall(mat,xr,yr,xk,yk)
                            xk = 0
                            yk = 0

                    if keys[pygame.K_a]:
                        xk = -1
                        yk = 0
                        if xr+xk < 0:
                            pass
                        else:
                            xr,yr = wall(mat,xr,yr,xk,yk)
                            xk = 0
                            yk = 0

                    if keys[pygame.K_s]:
                        xk = 0
                        yk = 1
                        if yr+yk > 8:
                            pass
                        else:
                            xr,yr = wall(mat,xr,yr,xk,yk)
                            xk = 0
                            yk = 0

                    if keys[pygame.K_w]:
                        xk = 0
                        yk = -1
                        if yr+yk < 0:
                            pass
                        else:
                            xr,yr = wall(mat,xr,yr,xk,yk)
                            xk = 0
                            yk = 0

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                    if keys[pygame.K_z]:
                        newgame = 0
                    if event.type == MOUSEMOTION:
                        pos = pygame.mouse.get_pos()
                        
                    if event.type ==  MOUSEBUTTONDOWN:
                        menu = pygame.mouse.get_pressed()

                pygame.draw.rect(sc,green,(80*xr,80*yr,80,80))

                pl = pygame.font.SysFont("Arial",30)
                pll = pl.render(str(pos[0])+','+str(pos[1]),1,blue)
                
                gamenum1 = pygame.font.SysFont("Arial",30)
                gamenum2 = pl.render(str(k),1,rose)
                sc.blit(gamenum2,(10,10))
                
                if checkmenu%2 == 1:
                    pygame.draw.rect(sc,rose,(0,0,1280,720))
                    
                if 1210 <= pos[0] <= 1270 and 10 <= pos[1] <= 70:
                    m1,m2,m3 = menu
                    sc.blit(pp14,(1212,10))
                    if m1 == 1:
                        checkmenu += 1
                        menu = (0,0,0)
                    else:
                        pass
                else:
                    sc.blit(pp13,(1212,10))
                    menu = (0,0,0)
              
                sc.blit(pll,(1100,700)) 
                pygame.display.update()

                clock.tick(25)
            pa = (0,0,0)
        else:
            pass
    else:
        color1 = 179,153,255
        pa = (0,0,0)
        
    if c2 <= pos[0] <= c2+a2 and d2 <= pos[1] <= d2+b2:
        q2,w2,e2 = pb
        color2 = 140,230,0
        sc.blit(pp2,(430,445))
        sc.blit(pp2,(797,445))
        if q2 == 1:
            #按鈕動作
            pb = (0,0,0)
        else:
            pass
    else:
        color2 = 179,153,255
        pb = (0,0,0)
        
    if c3 <= pos[0] <= c3+a3 and d3 <= pos[1] <= d3+b3:
        q3,w3,e3 = pc
        color3 = 140,230,0
        sc.blit(pp3,(507,565))
        sc.blit(pp3,(721,565))
        if q3 == 1:
            #按鈕動作
            qu = 1
            pc = (0,0,0)
        else:
            pass
    else:
        color3 = 179,153,255
        pc = (0,0,0)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if keys[pygame.K_q]:
            done = True
            
        if event.type == MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            
        if event.type ==  MOUSEBUTTONDOWN:
            pa = pygame.mouse.get_pressed()
            pb = pygame.mouse.get_pressed()
            pc = pygame.mouse.get_pressed()
            pd = pygame.mouse.get_pressed()
            pe = pygame.mouse.get_pressed()
            pf = pygame.mouse.get_pressed()
            pg = pygame.mouse.get_pressed()
    
    sc.blit(pp4,(1200,640))
    sc.blit(pp5,(15,635))
    
    if qu == 1:
        color3 = 140,230,0
        pygame.draw.rect(sc,bacc,[0,310,1280,410])
        if ypos1 > 320 and ypos2 > 325:
            sc.blit(p33,(570,ypos1))
            sc.blit(pp3,(507,ypos2))
            sc.blit(pp3,(721,ypos2))
            ypos1 -= 4
            ypos2 -= 4
            pd = (0,0,0)
            pe = (0,0,0)
        else:
            maincolor1 = 75,75,75
            maincolor2 = 75,75,75
            sc.blit(p33,(570,320))
            sc.blit(pp3,(507,325))
            sc.blit(pp3,(721,325))
            sc.blit(pp8,(400,450))
            sc.blit(pp8,(820,450))
            
            if (400 <= pos[0] <= 480 and 450 <= pos[1] <= 530) or (390 <= pos[0] <= 492 and 553 <= pos[1] <= 583):
                q4,w4,e4 = pd
                sc.blit(pp9,(400,450))
                maincolor1 = 140,230,0
                if q4 == 1:
                    #按鈕動作
                    done = True
                    pd = (0,0,0)
                else:
                    pass
            else:
                pd = (0,0,0)
                
            if (820 <= pos[0] <= 900 and 450 <= pos[1] <= 530) or (782 <= pos[0] <= 950 and 553 <= pos[1] <= 583):
                q5,w5,e5 = pe
                sc.blit(pp9,(820,450))
                maincolor2 = 140,230,0
                if q5 == 1:
                    #按鈕動作
                    qu = 0
                    ypos1 = 560
                    ypos2 = 565
                    pe = (0,0,0)
                else:
                    pass
            else:
                pe = (0,0,0)
            
            att1 = pygame.font.SysFont("Arial",60)
            atte1 = att1.render('QUIT',1,maincolor1)
            sc.blit(atte1,(390,550))
            att2 = pygame.font.SysFont("Arial",60)
            atte2 = att2.render('RETURN',1,maincolor2)
            sc.blit(atte2,(780,550))
        
    if 1200 <= pos[0] <= 1260 and 640 <= pos[1] <= 696:
        sc.blit(pp6,(1200,640))
    if (15 <= pos[0] <= 68) and (640 <= pos[1] <= 695) and yyqu == 0:     
        if yp >= 464:
            pygame.draw.rect(sc,acc,[20,yp,56,yl])
            pygame.draw.circle(sc,acc,(48,686),28)
            pygame.draw.circle(sc,acc,(48,yp),28)
            sc.blit(pp7,(15,635))
            yp -= 8
            yl += 8
        else:
            yyqu = 1
    elif ((pos[0] < 15) or (pos[0] > 68)) or ((pos[1] < 640) or (pos[1] > 695)) and yyqu == 0:
        yp = 644
        yl = 46
                
    if (20 <= pos[0] <= 76) and (436 <= pos[1] <= 714) and yp == 460:
        pygame.draw.rect(sc,acc,[20,yp+4,56,yl+4])
        pygame.draw.circle(sc,acc,(48,686),28)
        pygame.draw.circle(sc,acc,(48,yp+4),28)
        sc.blit(pp7,(15,635))
        sc.blit(pp11,(25,545))
        sc.blit(pp10,(18,455))
        
        if 20 <= pos[0] <= 76 and 454 <= pos[1] <= 514:
            q6,w6,e6 = pf
            if q6 == 1:
                #按鈕動作
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
                qq = 0
                a = random.randint(5,1275)
                b = random.randint(5,715)
                con = 0
                testt = 1
                while testt!=0:
                    sc.fill(white)
                    keys = pygame.key.get_pressed()
    
                    x = xxcheck(x,aa/2)
                    y = yycheck(y,bb/2)
    
                    if keys[pygame.K_d]:
                        if n <= 10:
                            if z == -7:
                                pass
                            else:
                                w = 0
                                z = 7
            
                            if tt == 0:
                                tt = 1
                                qq = time.clock()
                            else:
                                pass
                        else:
                            pass
        
                    if keys[pygame.K_a]:
                        if n <= 10:
                            if z == 7:
                                pass
                            else:
                                w = 0
                                z = -7
            
                            if tt == 0:
                                tt = 1
                                qq = time.clock()
                            else:
                                pass
                        else:
                            pass
        
                    if keys[pygame.K_s]:
                        if n <= 10:
                            if w == -7:
                                pass
                            else:
                                z = 0
                                w = 7
                        
                            if tt == 0:
                                tt = 1
                                qq = time.clock()
                            else:
                                pass
                        else:
                            pass
        
                    if keys[pygame.K_w]:
                        if n <= 10:
                            if w == 7:
                                pass
                            else:
                                z = 0
                                w = -7
            
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
                            testt = 0
                        if keys[pygame.K_z]:
                            testt = 0
                            con += time.clock()-qq
                        
                    clock.tick(60+j)
                pf = (0,0,0)
            else:
                pass
        else:
            pf = (0,0,0)
            
        if 20 <= pos[0] <= 76 and 550 <= pos[1] <= 600:
            q7,w7,e7 = pg
            if q7 == 1:
                #按鈕動作
                testt = 1
                qq = time.clock()
                while testt!=0:
                    sc.fill(white)
                    keys = pygame.key.get_pressed()
    
                    x = xxcheck(x,aa/2)
                    y = yycheck(y,bb/2)
    
                    if keys[pygame.K_d]:
                        if n <= 10:
                            if z == -7:
                                pass
                            else:
                                w = 0
                                z = 7
            
                            if tt == 0:
                                tt = 1
                                qq = time.clock()
                            else:
                                pass
                        else:
                            pass
        
                    if keys[pygame.K_a]:
                        if n <= 10:
                            if z == 7:
                                pass
                            else:
                                w = 0
                                z = -7
            
                            if tt == 0:
                                tt = 1
                                qq = time.clock()
                            else:
                                pass
                        else:
                            pass
        
                    if keys[pygame.K_s]:
                        if n <= 10:
                            if w == -7:
                                pass
                            else:
                                z = 0
                                w = 7
                    
                            if tt == 0:
                                tt = 1
                                qq = time.clock()
                            else:
                                pass
                        else:
                            pass
            
                    if keys[pygame.K_w]:
                        if n <= 10:
                            if w == 7:
                                pass
                            else:
                                z = 0
                                w = -7
            
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
                        con = 0
                        a = random.randint(5,1275)
                        b = random.randint(5,715)
                
                    (a,b,m,n,j) = touchx(x,y,a,b,m,n,j,aa,bb)
    
                    if m == 10 and n == 10:
                        n += 1
                        z = 0
                        w = 0
                        a = -10
                        b = -10
                        qq = con+time.clock()-qq
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
                            testt = 0
                        if keys[pygame.K_z]:
                            testt = 0
                            con += time.clock()-qq
                        
                    clock.tick(60+j) 
                pg = (0,0,0)
            else:
                pass
        else:
            pg = (0,0,0)
            
    elif ((pos[0] <= 20) or (76 <= pos[0])) or ((pos[1] <= 436) or (714 <= pos[1])) and yyqu == 1:
        yp = 644
        yl = 46
        yyqu = 0
        
    pl = pygame.font.SysFont("Arial",30)
    pll = pl.render(str(pos[0])+','+str(pos[1]),1,blue)
    sc.blit(pll,(1100,700))    
    
    #sc.blit(tree,(100,300))
    pygame.display.update()                 
            
    clock.tick(50)                   
pygame.quit()