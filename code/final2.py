import pygame
from pygame.locals import *
import time
import random
import char
import numpy as np

def buyitem(k,gold,hpmp,mycharacter):
    if mycharacter.goldnd < gold:
        pass
    else:
        mycharacter.goldnd -= gold
        if k == 1:
            if mycharacter.hpnd + hpmp > mycharacter.HP:
                mycharacter.hpnd = mycharacter.HP
            else:
                mycharacter.hpnd += hpmp
        elif k == 2:
            if mycharacter.mpnd + hpmp > mycharacter.MP:
                mycharacter.mpnd = mycharacter.MP
            else:
                mycharacter.mpnd += hpmp

def isset(v): 
    try : 
        type (eval(v)) 
    except : 
        return  0  
    else : 
        return  1 

def getmatlast(name,mapx,mapy):
    mat = np.zeros((9,16))
    a = (mapy-1)*65+mapx-1

    with open(name,'r') as rf:
        k = rf.read()
        for m in range(0,9):
            for n in range(0,16):
                mat[m,n] += int(k[a])
                a += 1
            a += 49
    return mat       
    
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
    pygame.draw.rect(sc,skyblue,(0,0,1280,720))
    for m in range(0,9):
        for n in range(0,16):
            if mat[m,n] == 1:
                sc.blit(pp12,(80*n,80*m))
            elif mat[m,n] == 2:
                pygame.draw.rect(sc,(144,238,144),(80*n,80*m,80,80))
            elif mat[m,n] == 3:
                sc.blit(pp21,(80*n+10,80*m+10))
            elif mat[m,n] == 4:
                pygame.draw.rect(sc,(255,45,81),(80*n,80*m,80,80))
            elif mat[m,n] == 5:
                sc.blit(pp22,(80*n,80*m))
            elif mat[m,n] == 6:
                sc.blit(pp23,(80*n+10,80*m+10))
            elif mat[m,n] == 7:
                sc.blit(pp24,(80*n+10,80*m+10))
            elif mat[m,n] == 8:
                sc.blit(pp27,(80*n,80*m))
            elif mat[m,n] == 9:
                sc.blit(pp30,(80*n+10,80*m+10))
            else:
                pass   

def drawsquare(point):
    mylist = []
    pygame.draw.lines(sc,sblue,1,point,8)
    for i in point:
        x,y = i
        mylist.append((x-3,y-3,8,8))
    for j in mylist:
        pygame.draw.rect(sc,sblue,j)
        
def wall(mat,xr,yr,xk,yk,k,needbattle,fightcount,mapreturn,mapreturnreal):
    if mat[yr+yk,xr+xk] == 0:
        xr += xk
        yr += yk
    elif mat[yr+yk,xr+xk] == 2:
        mycharacter.create(k)
        xr += xk
        yr += yk
        
        g = random.randint(1,10)
        if g <= 6:
            needbattle += 1
            if mycharacter.DEXs < mycharacter.DEXmon:
                fightcount = 1
            elif mycharacter.DEXs > mycharacter.DEXmon:
                fightcount = 0
            else:
                h = random.randint(1,2)
                if h == 1:
                    fightcount = 1
                else:
                    fightcount = 0
        else:
            pass
    elif mat[yr+yk,xr+xk] == 3:
        pygame.mixer.music.load('drink.mp3')
        pygame.mixer.music.play(1,0)
        mycharacter.remain += random.randint(1,2)
        
        name = 'map'+str(k)+'.txt'
        drinkpos = (yr+yk)*17+xr+xk
        mapreturn.append((3,k,drinkpos))
        mapreturnreal.append((3,k,drinkpos))
        with open(name,'r+b') as f:
            f.seek(drinkpos)
            f.write(b'0')
            f.flush
            f.seek(0)
        xr += xk
        yr += yk   
    elif mat[yr+yk,xr+xk] == 4:
        xr += xk
        yr += yk
        if mycharacter.hpnd <= int(0.1*mycharacter.HP):
            mycharacter.hpnd = 0
        else:
            mycharacter.hpnd -= int(0.1*mycharacter.HP)
    elif mat[yr+yk,xr+xk] == 5:        
        if mycharacter.key > 0:
            pygame.mixer.music.load('door.mp3')
            pygame.mixer.music.play(0,0)
            name = 'map'+str(k)+'.txt'
            doorpos = (yr+yk)*17+xr+xk
            mapreturn.append((5,k,doorpos))
            mapreturnreal.append((5,k,doorpos))
            with open(name,'r+b') as f:
                f.seek(doorpos)
                f.write(b'0')
                f.flush
                f.seek(0)
            xr += xk
            yr += yk
            mycharacter.key -= 1
        else:
            pass
    elif mat[yr+yk,xr+xk] == 6:
        pygame.mixer.music.load('key.mp3')
        pygame.mixer.music.play(1,0)
        mycharacter.key += 1
        
        name = 'map'+str(k)+'.txt'
        keypos = (yr+yk)*17+xr+xk
        mapreturn.append((6,k,keypos))
        mapreturnreal.append((6,k,keypos))
        with open(name,'r+b') as f:
            f.seek(keypos)
            f.write(b'0')
            f.flush
            f.seek(0)
        xr += xk
        yr += yk
    elif mat[yr+yk,xr+xk] == 7:
        pygame.mixer.music.load('coin.mp3')
        pygame.mixer.music.play(0,0)
        mycharacter.create(k)
        mycharacter.goldnd += (10*mycharacter.goldmon)
        
        name = 'map'+str(k)+'.txt'
        coinpos = (yr+yk)*17+xr+xk
        mapreturn.append((7,k,coinpos))
        mapreturnreal.append((7,k,coinpos))
        with open(name,'r+b') as f:
            f.seek(coinpos)
            f.write(b'0')
            f.flush
            f.seek(0)
        xr += xk
        yr += yk
    else:
        pass
        
    return xr,yr,needbattle,fightcount,mapreturn,mapreturnreal

def walllast(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno):
    if (yr+yk+mapy-1)*65+xr+xk+mapx-1 == 261:
        wallpos = 260
        mapreturn.append((0,k,wallpos))
        mapreturnreal.append((0,k,wallpos))
        with open('map15.txt','r+b') as f:
            f.seek(wallpos)
            f.write(b'1')
            f.flush
            f.seek(0)
    else:
        pass
    
    if mat[yr+yk,xr+xk] == 0:
        mapx += xk
        mapy += yk
    elif mat[yr+yk,xr+xk] == 2:
        mycharacter.create(k)
        mapx += xk
        mapy += yk
        
        g = random.randint(1,10)
        if g <= 6:
            needbattle += 1
            if mycharacter.DEXs < mycharacter.DEXmon:
                fightcount = 1
            elif mycharacter.DEXs > mycharacter.DEXmon:
                fightcount = 0
            else:
                h = random.randint(1,2)
                if h == 1:
                    fightcount = 1
                else:
                    fightcount = 0
        else:
            pass
    elif mat[yr+yk,xr+xk] == 3:
        pygame.mixer.music.load('drink.mp3')
        pygame.mixer.music.play(1,0)
        mycharacter.remain += random.randint(1,2)
        
        name = 'map'+str(k)+'.txt'
        drinkpos = (yr+yk+mapy-1)*65+xr+xk+mapx-1
        mapreturn.append((3,k,drinkpos))
        mapreturnreal.append((3,k,drinkpos))
        with open(name,'r+b') as f:
            f.seek(drinkpos)
            f.write(b'0')
            f.flush
            f.seek(0)
        mapx += xk
        mapy += yk   
    elif mat[yr+yk,xr+xk] == 4:
        mapx += xk
        mapy += yk
        if mycharacter.hpnd <= int(0.1*mycharacter.HP):
            mycharacter.hpnd = 0
        else:
            mycharacter.hpnd -= int(0.1*mycharacter.HP)
    elif mat[yr+yk,xr+xk] == 5:        
        if mycharacter.key > 0:
            pygame.mixer.music.load('door.mp3')
            pygame.mixer.music.play(0,0)
            name = 'map'+str(k)+'.txt'
            doorpos = (yr+yk+mapy-1)*65+xr+xk+mapx-1
            mapreturn.append((5,k,doorpos))
            mapreturnreal.append((5,k,doorpos))
            with open(name,'r+b') as f:
                f.seek(doorpos)
                f.write(b'0')
                f.flush
                f.seek(0)
            xr += xk
            yr += yk
            mycharacter.key -= 1
        else:
            pass
    elif mat[yr+yk,xr+xk] == 6:
        pygame.mixer.music.load('key.mp3')
        pygame.mixer.music.play(1,0)
        mycharacter.key += 1
        
        name = 'map'+str(k)+'.txt'
        keypos = (yr+yk+mapy-1)*65+xr+xk+mapx-1
        mapreturn.append((6,k,keypos))
        mapreturnreal.append((6,k,keypos))
        with open(name,'r+b') as f:
            f.seek(keypos)
            f.write(b'0')
            f.flush
            f.seek(0)
        mapx += xk
        mapy += yk
    elif mat[yr+yk,xr+xk] == 7:
        pygame.mixer.music.load('coin.mp3')
        pygame.mixer.music.play(0,0)
        mycharacter.create(k)
        mycharacter.goldnd += (10*mycharacter.goldmon)
        
        name = 'map'+str(k)+'.txt'
        coinpos = (yr+yk+mapy-1)*65+xr+xk+mapx-1
        mapreturn.append((7,k,coinpos))
        mapreturnreal.append((7,k,coinpos))
        with open(name,'r+b') as f:
            f.seek(coinpos)
            f.write(b'0')
            f.flush
            f.seek(0)
        mapx += xk
        mapy += yk
    elif mat[yr+yk,xr+xk] == 9:
        g = random.randint(1,8)
        if g <= 6:
            if g == 1:
                pygame.mixer.music.load('coin.mp3')
                pygame.mixer.music.play(0,0)
                mycharacter.create(k)
                mycharacter.goldnd += (10*mycharacter.goldmon)
            elif g == 2:
                pygame.mixer.music.load('drink.mp3')
                pygame.mixer.music.play(1,0)
                mycharacter.remain += random.randint(1,2)
            elif g == 3 or g == 4:
                pygame.mixer.music.load('contral.mp3')
                pygame.mixer.music.play(0,0)
                contralyesno += 1
            else:
                pygame.mixer.music.load('water.mp3')
                pygame.mixer.music.play(0,0)
                inkyesno += 1
            name = 'map'+str(k)+'.txt'
            markpos = (yr+yk+mapy-1)*65+xr+xk+mapx-1
            mapreturn.append((9,k,markpos))
            mapreturnreal.append((9,k,markpos))
            with open(name,'r+b') as f:
                f.seek(markpos)
                f.write(b'0')
                f.flush
                f.seek(0)
            mapx += xk
            mapy += yk
        else:
            pygame.mixer.music.load('return.mp3')
            pygame.mixer.music.play(0,0)
            name = 'map'+str(k)+'.txt'
            markpos = (yr+yk+mapy-1)*65+xr+xk+mapx-1
            mapreturn.append((9,k,markpos))
            mapreturnreal.append((9,k,markpos))
            with open(name,'r+b') as f:
                f.seek(markpos)
                f.write(b'0')
                f.flush
                f.seek(0)
            mapx = 1
            mapy = 1
            xr = 1
            yr = 4
    else:
        pass
        
    return xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno

def walllast2(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno):
    if (yr+yk+mapy-1)*65+xr+xk+mapx-1 == 261:
        wallpos = 260
        mapreturn.append((0,k,wallpos))
        mapreturnreal.append((0,k,wallpos))
        with open('map15.txt','r+b') as f:
            f.seek(wallpos)
            f.write(b'1')
            f.flush
            f.seek(0)
    else:
        pass
    
    if mat[yr+yk,xr+xk] == 0:
        xr += xk
        yr += yk
    elif mat[yr+yk,xr+xk] == 2:
        mycharacter.create(k)
        xr += xk
        yr += yk
        
        g = random.randint(1,10)
        if g <= 6:
            needbattle += 1
            if mycharacter.DEXs < mycharacter.DEXmon:
                fightcount = 1
            elif mycharacter.DEXs > mycharacter.DEXmon:
                fightcount = 0
            else:
                h = random.randint(1,2)
                if h == 1:
                    fightcount = 1
                else:
                    fightcount = 0
        else:
            pass
    elif mat[yr+yk,xr+xk] == 3:
        pygame.mixer.music.load('drink.mp3')
        pygame.mixer.music.play(1,0)
        mycharacter.remain += random.randint(1,2)
        
        name = 'map'+str(k)+'.txt'
        drinkpos = (yr+yk+mapy-1)*65+xr+xk+mapx-1
        mapreturn.append((3,k,drinkpos))
        mapreturnreal.append((3,k,drinkpos))
        with open(name,'r+b') as f:
            f.seek(drinkpos)
            f.write(b'0')
            f.flush
            f.seek(0)
        xr += xk
        yr += yk   
    elif mat[yr+yk,xr+xk] == 4:
        xr += xk
        yr += yk
        if mycharacter.hpnd <= int(0.1*mycharacter.HP):
            mycharacter.hpnd = 0
        else:
            mycharacter.hpnd -= int(0.1*mycharacter.HP)
    elif mat[yr+yk,xr+xk] == 5:        
        if mycharacter.key > 0:
            pygame.mixer.music.load('door.mp3')
            pygame.mixer.music.play(0,0)
            name = 'map'+str(k)+'.txt'
            doorpos = (yr+yk+mapy-1)*65+xr+xk+mapx-1
            mapreturn.append((5,k,doorpos))
            mapreturnreal.append((5,k,doorpos))
            with open(name,'r+b') as f:
                f.seek(doorpos)
                f.write(b'0')
                f.flush
                f.seek(0)
            xr += xk
            yr += yk
            mycharacter.key -= 1
        else:
            pass
    elif mat[yr+yk,xr+xk] == 6:
        pygame.mixer.music.load('key.mp3')
        pygame.mixer.music.play(1,0)
        mycharacter.key += 1
        
        name = 'map'+str(k)+'.txt'
        keypos = (yr+yk+mapy-1)*65+xr+xk+mapx-1
        mapreturn.append((6,k,keypos))
        mapreturnreal.append((6,k,keypos))
        with open(name,'r+b') as f:
            f.seek(keypos)
            f.write(b'0')
            f.flush
            f.seek(0)
        xr += xk
        yr += yk
    elif mat[yr+yk,xr+xk] == 7:
        pygame.mixer.music.load('coin.mp3')
        pygame.mixer.music.play(0,0)
        mycharacter.create(k)
        mycharacter.goldnd += (10*mycharacter.goldmon)
        
        name = 'map'+str(k)+'.txt'
        coinpos = (yr+yk+mapy-1)*65+xr+xk+mapx-1
        mapreturn.append((7,k,coinpos))
        mapreturnreal.append((7,k,coinpos))
        with open(name,'r+b') as f:
            f.seek(coinpos)
            f.write(b'0')
            f.flush
            f.seek(0)
        xr += xk
        yr += yk
    elif mat[yr+yk,xr+xk] == 9:
        g = random.randint(1,8)
        if g <= 6:
            if g == 1:
                pygame.mixer.music.load('coin.mp3')
                pygame.mixer.music.play(0,0)
                mycharacter.create(k)
                mycharacter.goldnd += (10*mycharacter.goldmon)
            elif g == 2:
                pygame.mixer.music.load('drink.mp3')
                pygame.mixer.music.play(1,0)
                mycharacter.remain += random.randint(1,2)
            elif g == 3 or g == 4:
                pygame.mixer.music.load('contral.mp3')
                pygame.mixer.music.play(0,0)
                contralyesno += 1
            else:
                pygame.mixer.music.load('water.mp3')
                pygame.mixer.music.play(0,0)
                inkyesno += 1
            name = 'map'+str(k)+'.txt'
            markpos = (yr+yk+mapy-1)*65+xr+xk+mapx-1
            mapreturn.append((9,k,markpos))
            mapreturnreal.append((9,k,markpos))
            with open(name,'r+b') as f:
                f.seek(markpos)
                f.write(b'0')
                f.flush
                f.seek(0)
            xr += xk
            yr += yk
        else:
            pygame.mixer.music.load('return.mp3')
            pygame.mixer.music.play(0,0)
            name = 'map'+str(k)+'.txt'
            markpos = (yr+yk+mapy-1)*65+xr+xk+mapx-1
            mapreturn.append((9,k,markpos))
            mapreturnreal.append((9,k,markpos))
            with open(name,'r+b') as f:
                f.seek(markpos)
                f.write(b'0')
                f.flush
                f.seek(0)
            mapx = 1
            mapy = 1
            xr = 1
            yr = 4
    else:
        pass
        
    return xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno


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

def collide(ballx,bally,move,clen):
    if move == 1:
        if (ballx+clen >= 1280) and (bally-clen != 0):
            move = 2
        elif (ballx+clen != 1280) and (bally-clen <= 0):
            move = 4
        elif (ballx+clen >= 1280) and (bally-clen <= 0):
            move = 3
    if move == 2:
        if (ballx-clen <= 0) and (bally-clen != 0):
            move = 1
        elif (ballx-clen != 0) and (bally-clen <= 0):
            move = 3
        elif (ballx-clen <= 0) and (bally-clen <= 0):
            move = 4
    if move == 3:
        if (ballx-12 <= 0) and (bally+clen != 720):
            move = 4
        elif (ballx-12 != 0) and (bally+clen >= 720):
            move = 2
        elif (ballx-12 <= 0) and (bally+clen >= 720):
            move = 1
    if move == 4:
        if (ballx+clen >= 1280) and (bally+clen != 720):
            move = 3
        elif (ballx+clen != 1280) and (bally+clen >= 720):
            move = 1
        elif (ballx+clen >= 1280) and (bally+clen >= 720):
            move =  2    
    return move

def color(firstcolor):
    if firstcolor == 1:
        rgb = (255,0,0)
    elif firstcolor == 2:
        rgb = (0,255,0)
    elif firstcolor == 3:
        rgb = (0,0,255)
    elif firstcolor == 4:
        rgb = (255,255,0)
    elif firstcolor == 5:
        rgb = (255,0,255)
    elif firstcolor == 6:
        rgb = (0,255,255)
    return rgb

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

dd13 = pygame.image.load('warrior.png')
pp13 = pygame.transform.scale(dd13,(150,150))
ppp13 = pygame.transform.scale(dd13,(80,80))

dd14 = pygame.image.load('archer.png')
pp14 = pygame.transform.scale(dd14,(150,150))
ppp14 = pygame.transform.scale(dd14,(80,80))

dd15 = pygame.image.load('magician.png')
pp15 = pygame.transform.scale(dd15,(150,150))
ppp15 = pygame.transform.scale(dd15,(80,80))

dd16 = pygame.image.load('ninja.png')
pp16 = pygame.transform.scale(dd16,(150,150))
ppp16 = pygame.transform.scale(dd16,(80,80))

dd17 = pygame.image.load('warrior2.png')
pp17 = pygame.transform.scale(dd17,(150,150))

dd18 = pygame.image.load('archer2.png')
pp18 = pygame.transform.scale(dd18,(150,150))

dd19 = pygame.image.load('magician2.png')
pp19 = pygame.transform.scale(dd19,(150,150))

dd20 = pygame.image.load('ninja2.png')
pp20 = pygame.transform.scale(dd20,(150,150))

dd21 = pygame.image.load('drink.png')
pp21 = pygame.transform.scale(dd21,(60,60))

dd22 = pygame.image.load('door.png')
pp22 = pygame.transform.scale(dd22,(80,80))

dd23 = pygame.image.load('key.png')
pp23 = pygame.transform.scale(dd23,(60,60))

dd24 = pygame.image.load('coin.png')
pp24 = pygame.transform.scale(dd24,(60,60))

dd25 = pygame.image.load('slime.png')
pp25 = pygame.transform.scale(dd25,(70,70))

dd26 = pygame.image.load('slime2.png')
pp26 = pygame.transform.scale(dd26,(70,70))

dd27 = pygame.image.load('boss.png')
pp27 = pygame.transform.scale(dd27,(80,80))

dd28 = pygame.image.load('ink1.png')
pp28 = pygame.transform.scale(dd28,(500,500))

dd29 = pygame.image.load('ink2.png')
pp29 = pygame.transform.scale(dd29,(500,500))

dd30 = pygame.image.load('mark.png')
pp30 = pygame.transform.scale(dd30,(60,60))

#tree = pygame.image.load('tree.png')
gray1 = 105,105,105
gray2 = 192,192,192
gray3 = 220,220,220
rose = 255,228,225
strongred = 255,20,147
darkred = 178,34,34
skyblue = 224,255,255
sblue = 77,128,230
waterblue = 0,255,255
lightblue = 0,191,255
shell = 255,245,238
bacc = 220,238,238
white = 255,255,255 
blue = 0,0,200
green = 255,100,255
numm = 71,152,179
acc = 255,250,250
maincolor = 32,80,230
color1 = 179,153,255
color2 = 179,153,255
color3 = 179,153,255

charcolor1 = 25,25,25
charcolor2 = 25,25,25
charcolor3 = 25,25,25
charcolor4 = 25,25,25

yesnocolor1 = 220
yesnocolor2 = 240
yesnocolor3 = 240

surecolor1 = 220
surecolor2 = 240
surecolor3 = 240

choosecolor1 = 220
choosecolor2 = 240
choosecolor3 = 240

battlepluscolor = 71,152,179

numm1 = 71,152,179
numm2 = 71,152,179
numm3 = 71,152,179
numm4 = 71,152,179
numm5 = 71,152,179
numm6 = 71,152,179

battlecolor1 = 0,191,255
battlecolor2 = 0,191,255
battlecolor3 = 0,191,255
battlecolor4 = 0,191,255
battlecolor5 = 0,191,255
battlecolor6 = 0,191,255

battlechangecolor1 = 0
battlechangecolor2 = 0
battlechangecolor3 = 0
battlechangecolor4 = 0
battlechangecolor5 = 0
battlechangecolor6 = 0

mapx = 1
mapy = 1

mapxx = 1
mapyy = 1

#判別地圖
k = 1

#存檔判別地圖
kk = 1

#
deadtime = 0

#判斷墨跡
inkyesno = 0
inkyesnoo = 0

#判斷反向控制
contralyesno = 0
contralyesnoo = 0

moslist = []
moslistreal = []
for i in range(1,145):
    moslist.append(i)

#主角位置
xr = 1
yr = 1

#主角存檔位置
xrr = 1
yrr = 1

#主角位移量
xk = 0
yk = 0

#判斷新遊戲
createnew = 0

#判斷戰鬥
needbattle = 0

#地圖回復
mapreturn = []
mapreturnreal = []

#判斷能力點是否為雙位數
abilitylen1 = 205
abilitylen2 = 205
abilitylen3 = 205
abilitylen4 = 205
abilitylen5 = 205
abilitylen6 = 205

statuslen1 = 1050
statuslen2 = 1020
statuslen3 = 1050
statuslen4 = 1050
statuslen5 = 1050
statuslen6 = 1050
statuslen7 = 1050
statuslen8 = 1050
statuslen9 = 1050

monstatuslen1 = 260
monstatuslen2 = 670
monstatuslen3 = 655
monstatuslen4 = 670
monstatuslen5 = 650

faillen1 = -300
faillen2 = -300
faillen3 = -300
faillen4 = -300
faillen5 = -300
faillen6 = -300

#主角面相方向
charface = 1
charfacee = 1

#回血秒數計算
healcount = 0

#戰鬥順序
fightcount = 0

#戰鬥延時
battlecount = 0

#判斷選角選單
choosemenu = 0

#能力點選單
abilitymenu = 0

#道具選單
itemmenu = 0

#判斷戰鬥亮燈
changecolor1 = 0
changecolor2 = 0
changecolor3 = 0
changecolor4 = 0
changecolor5 = 0
changecolor6 = 0

#戰鬥道具選單
battleitemmenu = 0

itemcolor = 1

#遊戲選單
checkmenu = 0

#進入遊戲迴圈
newgame = 0

#選角確認按鈕
advenbutton = 0


#選角選單橫線長度
linelen = 200

#判斷能力點選單
abilitycolor = 1

#戰鬥勝利延時
battlewin = 0

#判斷是否有用技能
useskill = 0

#判斷顏色
suretime = 0
yesnotime = 0
choosetime = 0

picpos = 325
menupos1 = 320
menupos2 = 440
menupos3 = 560

#判斷Quit按鍵
qu = 0

#關於欄伸縮的Y座標及Y長度
yp = 644
yl = 46

#判斷關於伸縮欄長度
yyqu = 0

#按下QUIT鍵後的位置
ypos1 = 560
ypos2 = 565

#球位置
ballx = random.randint(50,1230)
bally = random.randint(50,670)

#球顏色
firstcolor = random.randint(1,6)
rr,gg,bb = color(firstcolor)

#球初始方向
move = random.randint(1,4)

#戰鬥選單寬度
battlelen = 0

#球半徑
circlelength = 16

#判斷選角亮燈
changecolor1,changecolor2,changecolor3,changecolor4 = (0,0,0,0)

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
ph = (0,0,0)
pi = (0,0,0)
pj = (0,0,0)
pk = (0,0,0)
pl = (0,0,0)

done = False
while not done:
    
    sc.fill(bacc)
    pygame.draw.rect(sc,bacc,[c1,d1,a1,b1])
    pygame.draw.rect(sc,bacc,[c2,d2,a2,b2])
    pygame.draw.rect(sc,bacc,[c3,d3,a3,b3])
    pygame.draw.rect(sc,maincolor,[299,275,682,6])
    sc.blit(pp4,(1200,640))
    sc.blit(pp5,(15,635))
    
    keys = pygame.key.get_pressed()
    pygame.mouse.set_visible(True)
    
    mainmenu1 = pygame.font.SysFont("algerian",130)
    mainmenu2 = mainmenu1.render('Main Menu',1,maincolor)
    sc.blit(mainmenu2,(300,132))
    
    p1 = pygame.font.SysFont("simhei",95)
    p11 = p1.render('New Game',1,color1)
    sc.blit(p11,(467,menupos1))
    
    p2 = pygame.font.SysFont("simhei",95)
    p22 = p2.render('Continue',1,color2)
    sc.blit(p22,(490,menupos2))
    
    p3 = pygame.font.SysFont("simhei",95)
    p33 = p3.render('Quit',1,color3)
    sc.blit(p33,(570,menupos3))
    
    if createnew == 1 and choosemenu == 0:
        color1 = 140,230,0
        sc.blit(pp1,(407,picpos))
        sc.blit(pp1,(815,picpos))
        if menupos1 < 720:
            picpos += 4
            menupos1 += 4
            menupos2 += 4
            menupos3 += 4
        else:
            areyousure1 = pygame.font.SysFont("stencil",85)
            areyousure2 = areyousure1.render('Are you sure ?',1,(surecolor1,surecolor2,surecolor3))
            sc.blit(areyousure2,(320,340))
            sureyes1 = pygame.font.SysFont("stencil",70)
            sureyes2 = sureyes1.render('Yes',1,(yesnocolor1,yesnocolor2,yesnocolor3))
            sc.blit(sureyes2,(410,500))
            sureno1 = pygame.font.SysFont("stencil",70)
            sureno2 = sureno1.render('No',1,(yesnocolor1,yesnocolor2,yesnocolor3))
            sc.blit(sureno2,(800,500))
            
            if surecolor1 != 140:
                surecolor1 -= 2
                surecolor3 -= 6
                suretime += 1
                if suretime%4 == 0:
                    surecolor2 -= 1
            else:
                if yesnocolor1 != 180:
                    pf = (0,0,0)
                    pg = (0,0,0)
                    yesnotime += 1
                    if yesnotime > 5:
                        yesnocolor1 -= 1
                    if yesnotime > 5:
                        yesnocolor2 -= 1
                    yesnocolor1 -= 2
                    yesnocolor2 -= 5
                    yesnocolor3 += 1
                else:
                    if 410 <= pos[0] <= 530 and 505 <= pos[1] <= 550:
                        q6,w6,e6 = pf
                        csureyes1 = pygame.font.SysFont("stencil",70)
                        csureyes2 = csureyes1.render('Yes',1,(140,230,0))
                        sc.blit(csureyes2,(410,500))
                        if q6 == 1:
                            #按鈕動作
                            choosemenu = 1
                            advenbutton = 0
                            charface = 1
                            mapx = 1
                            mapy = 1
                            k = 14
                            xr = 4
                            yr = 4
                            
                            for i in mapreturnreal:
                                aaa,bbb,ccc = i
                                name = 'map'+str(bbb)+'.txt'
                                with open(name,'r+b') as f:
                                    f.seek(ccc)
                                    if int(aaa) == 3:
                                        f.write(b'3')
                                    elif int(aaa) == 5:
                                        f.write(b'5')
                                    elif int(aaa) == 6:
                                        f.write(b'6')
                                    elif int(aaa) == 7:
                                        f.write(b'7')
                                    elif int(aaa) == 9:
                                        f.write(b'9')
                                    else:
                                        f.write(b'0')
                                    f.flush
                                    f.seek(0)
                            
                            pf = (0,0,0)
                        else:
                            pass
                    else:
                        pf = (0,0,0)
                        
                    if 803 <= pos[0] <= 890 and 504 <= pos[1] <= 550:
                        q7,w7,e7 = pg
                        csureno1 = pygame.font.SysFont("stencil",70)
                        csureno2 = csureno1.render('No',1,(140,230,0))
                        sc.blit(csureno2,(800,500))    
                        if q7 == 1:
                            #按鈕動作
                            createnew = 0
                            yesnocolor1 = 220
                            yesnocolor2 = 240
                            yesnocolor3 = 240
                            surecolor1 = 220
                            surecolor2 = 240
                            surecolor3 = 240
                            suretime = 0
                            yesnotime = 0
                            picpos = 325
                            menupos1 = 320
                            menupos2 = 440
                            menupos3 = 560
                            color1 = 179,153,255
                            pg = (0,0,0)
                        else:
                            pass
                    else:
                        pg = (0,0,0)
    
    if choosemenu == 1:
        pygame.draw.rect(sc,bacc,[0,0,1280,720])
        choose1 = pygame.font.SysFont("stencil",70)
        choose2 = choose1.render('Choose your character',1,(choosecolor1,choosecolor2,choosecolor3))
        sc.blit(choose2,(200,100))
        if choosecolor1 != 30:
            choosetime += 1
            choosecolor1 -= 9
            choosecolor2 -= 8
            if choosetime > 10:
                choosecolor1 -= 1
            if choosetime%2 == 1:
                choosecolor3 -= 1
        else:
            if linelen != 1080:
                ph = (0,0,0)
                pi = (0,0,0)
                pj = (0,0,0)
                pk = (0,0,0)
                linelen += 10
                pygame.draw.line(sc,maincolor,(200,170),(linelen,170),8)
            else:
                pygame.draw.line(sc,maincolor,(200,170),(1080,170),8)
                sc.blit(pp13,(200,300))
                sc.blit(pp14,(443,300))
                sc.blit(pp15,(686,300))
                sc.blit(pp16,(929,300))
                
                if 180 <= pos[0] <= 330 and 500 <= pos[1] <= 520:
                    q8,w8,e8 = ph
                    charcolor1 = 140,230,0
                    sc.blit(pp17,(200,300))
                    if q8 == 1:
                        #按鈕動作
                        advenbutton = 1
                        pl = (0,0,0)
                        ph = (0,0,0)
                else:
                    if changecolor1 == 0:
                        ph = (0,0,0)
                        charcolor1 = 25,25,25
                    elif changecolor1 == 1:
                        charcolor1 = 140,230,0
                    
                if 453 <= pos[0] <= 588 and 500 <= pos[1] <= 520:
                    q9,w9,e9 = pi
                    charcolor2 = 140,230,0
                    sc.blit(pp18,(443,300))
                    if q9 == 1:
                        #按鈕動作
                        advenbutton = 2
                        pl = (0,0,0)
                        pi = (0,0,0)
                else:
                    if changecolor2 == 0:
                        pi = (0,0,0)
                        charcolor2 = 25,25,25
                    elif changecolor2 == 1:
                        pi = (0,0,0)
                        charcolor2 = 140,230,0
                    
                if 685 <= pos[0] <= 847 and 500 <= pos[1] <= 520:
                    q10,w10,e10 = pj
                    charcolor3 = 140,230,0
                    sc.blit(pp19,(686,300))
                    if q10 == 1:
                        #按鈕動作
                        advenbutton = 3
                        pl = (0,0,0)
                        pj = (0,0,0)
                else:
                    if changecolor3 == 0:
                        pj = (0,0,0)
                        charcolor3 = 25,25,25
                    elif changecolor3 == 1:
                        charcolor3 = 140,230,0               
                    
                if 965 <= pos[0] <= 1056 and 500 <= pos[1] <= 520:
                    q11,w11,e11 = pk
                    charcolor4 = 140,230,0
                    sc.blit(pp20,(929,300))
                    if q11 == 1:
                        #按鈕動作
                        advenbutton = 4
                        pl = (0,0,0)
                        pk = (0,0,0)
                else:
                    if changecolor4 == 0:
                        pk = (0,0,0)
                        charcolor4 = 25,25,25
                    elif changecolor4 == 1:
                        charcolor4 = 140,230,0
                
                warrior1 = pygame.font.SysFont("jokerman",40)
                warrior2 = warrior1.render('warrior',1,charcolor1)
                sc.blit(warrior2,(180,470))
                archer1 = pygame.font.SysFont("jokerman",40)
                archer2 = archer1.render('archer',1,charcolor2)
                sc.blit(archer2,(453,470))
                magician1 = pygame.font.SysFont("jokerman",40)
                magician2 = magician1.render('magician',1,charcolor3)
                sc.blit(magician2,(681,470))
                ninja1 = pygame.font.SysFont("jokerman",40)
                ninja2 = ninja1.render('ninja',1,charcolor4)
                sc.blit(ninja2,(964,470))
        
        if advenbutton != 0:
            adventure1 = pygame.font.SysFont("stencil",50)
            adventure2 = adventure1.render('adventure',1,maincolor)
            sc.blit(adventure2,(500,600))
            
            advenlist = [(485,590),(485,650),(797,650),(797,590)]
            mylist = []
            pygame.draw.lines(sc,maincolor,1,advenlist,4)
            for i in advenlist:
                x,y = i
                mylist.append((x-1,y-1,4,4))
            for j in mylist:
                pygame.draw.rect(sc,maincolor,j)
                
            if advenbutton == 1:
                sc.blit(pp17,(200,300))
                changecolor1,changecolor2,changecolor3,changecolor4 = (1,0,0,0)
            elif advenbutton == 2:
                sc.blit(pp18,(443,300))
                changecolor1,changecolor2,changecolor3,changecolor4 = (0,1,0,0)
            elif advenbutton == 3:
                sc.blit(pp19,(686,300))
                changecolor1,changecolor2,changecolor3,changecolor4 = (0,0,1,0)
            elif advenbutton == 4:
                sc.blit(pp20,(929,300))
                changecolor1,changecolor2,changecolor3,changecolor4 = (0,0,0,1)
            
            if 485 <= pos[0] <= 797 and 590 <= pos[1] <= 650:
                    q11,w11,e11 = pl
                    if q11 == 1:
                        #按鈕動作
                        if advenbutton == 1:
                            mycharacter = char.warrior()
                            mycharacterold = char.warrior()
                            mycharacter.status()
                        elif advenbutton == 2:
                            mycharacter = char.archer()
                            mycharacterold = char.archer()
                            mycharacter.status()
                        elif advenbutton == 3:
                            mycharacter = char.magician()
                            mycharacterold = char.magician()
                            mycharacter.status()
                        elif advenbutton == 4:
                            mycharacter = char.ninja()
                            mycharacterold = char.ninja()
                            mycharacter.status()
                        
                        abilitymenu = 0
                        checkmenu = 0
                        newgame = 1
                        pl = (0,0,0)
                    else:
                        pl = (0,0,0)
    
    while newgame!=0:
        sc.fill(white)
        keys = pygame.key.get_pressed()
        mods = pygame.key.get_mods()
        pygame.mouse.set_visible(False)

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
            mat = getmatlast('map15.txt',mapx,mapy)
            drawmap(mat)
        
        if charface == 1:
            sc.blit(pp25,(80*xr+5,80*yr+5))
        else:
            sc.blit(pp26,(80*xr+5,80*yr+5))
        #pygame.draw.rect(sc,green,(80*xr+20,80*yr+20,40,40))  

        if checkmenu%2 == 1:
            pygame.draw.rect(sc,rose,(0,0,1280,720))
            pygame.draw.circle(sc,(rr,gg,bb),(ballx,bally),circlelength)
            if move == 4:
                ballx += 3
                bally += 3
            elif move == 3:
                ballx -= 3
                bally += 3
            elif move == 2:
                ballx -= 3
                bally -= 3
            elif move == 1:
                ballx += 3
                bally -= 3
            move = collide(ballx,bally,move,circlelength)

            if rr == 255 and gg < 255 and bb == 0:
                gg += 5
            if rr > 0 and gg == 255 and bb == 0:
                if rr > 100:
                    rr -= 5
                else:
                    rr -= 10
            if gg == 255 and bb < 255 and rr == 0:
                bb += 5
            if gg > 0 and bb == 255 and rr == 0:
                if gg > 100:
                    gg -= 5
                else:
                    gg -= 10
            if bb == 255 and rr < 255 and gg == 0:
                rr += 5
            if bb > 0 and rr == 255 and gg == 0:
                if bb > 100:
                    bb -= 5
                else:
                    bb -= 10

            drawsquare([(50,50),(50,573),(300,573),(300,50)])

            ability1 = pygame.font.SysFont("stencil",50)
            ability2 = ability1.render('ABILITY',1,sblue)
            sc.blit(ability2,(80,80))
            ability3 = pygame.font.SysFont("stencil",50)
            ability4 = ability3.render('POINT',1,sblue)
            sc.blit(ability4,(100,140))

            pygame.draw.line(sc,sblue,(80,195),(270,195),5)

            yline = [258,315,372,429,486,543]
            for i in yline:
                pygame.draw.line(sc,shell,(80,i),(270,i),3)

            hp1 = pygame.font.SysFont("stencil",40)
            hp2 = hp1.render('HP',1,lightblue)
            sc.blit(hp2,(90,220))
            mp1 = pygame.font.SysFont("stencil",40)
            mp2 = mp1.render('MP',1,lightblue)
            sc.blit(mp2,(90,277))
            str1 = pygame.font.SysFont("stencil",40)
            str2 = str1.render('STR',1,lightblue)
            sc.blit(str2,(80,334))
            intt1 = pygame.font.SysFont("stencil",40)
            intt2 = intt1.render('INT',1,lightblue)
            sc.blit(intt2,(80,391))
            dex1 = pygame.font.SysFont("stencil",40)
            dex2 = dex1.render('DEX',1,lightblue)
            sc.blit(dex2,(80,448))
            luk1 = pygame.font.SysFont("stencil",40)
            luk2 = luk1.render('LUK',1,lightblue)
            sc.blit(luk2,(80,505))

            if mycharacter.HPs >= 10:
                abilitylen1 = 195
            else:
                abilitylen1 = 205
            if mycharacter.MPs >= 10:
                abilitylen2 = 195
            else:
                abilitylen2 = 205
            if mycharacter.STRs >= 10:
                abilitylen3 = 195
            else:
                abilitylen3 = 205
            if mycharacter.INTs >= 10:
                abilitylen4 = 195
            else:
                abilitylen4 = 205
            if mycharacter.DEXs >= 10:
                abilitylen5 = 195
            else:
                abilitylen5 = 205
            if mycharacter.LUKs >= 10:
                abilitylen6 = 195
            else:
                abilitylen6 = 205

            mhp1 = pygame.font.SysFont("stencil",40)
            mhp2 = mhp1.render(str(mycharacter.HPs),1,numm1)
            sc.blit(mhp2,(abilitylen1,220))
            mmp1 = pygame.font.SysFont("stencil",40)
            mmp2 = mmp1.render(str(mycharacter.MPs),1,numm2)
            sc.blit(mmp2,(abilitylen2,277))
            mstr1 = pygame.font.SysFont("stencil",40)
            mstr2 = mstr1.render(str(mycharacter.STRs),1,numm3)
            sc.blit(mstr2,(abilitylen3,334))
            mintt1 = pygame.font.SysFont("stencil",40)
            mintt2 = mintt1.render(str(mycharacter.INTs),1,numm4)
            sc.blit(mintt2,(abilitylen4,391))
            mdex1 = pygame.font.SysFont("stencil",40)
            mdex2 = dex1.render(str(mycharacter.DEXs),1,numm5)
            sc.blit(mdex2,(abilitylen5,448))
            mluk1 = pygame.font.SysFont("stencil",40)
            mluk2 = mluk1.render(str(mycharacter.LUKs),1,numm6)
            sc.blit(mluk2,(abilitylen6,505))

            drawsquare([(795,50),(795,573),(1230,573),(1230,50)])
            status1 = pygame.font.SysFont("stencil",50)
            status2 = status1.render('STATUS',1,sblue)
            sc.blit(status2,(932,80))
            pygame.draw.line(sc,sblue,(830,135),(1200,135),5)

            yline = [193,243,293,343,393,443,493,543]
            for i in yline:
                pygame.draw.line(sc,shell,(830,i),(1200,i),3)

            slv1 = pygame.font.SysFont("stencil",40)
            slv2 = slv1.render('LV',1,lightblue)
            sc.blit(slv2,(840,155))
            sexp1 = pygame.font.SysFont("stencil",40)
            sexp2 = sexp1.render('EXP',1,lightblue)
            sc.blit(sexp2,(830,205))
            sgold1 = pygame.font.SysFont("stencil",40)
            sgold2 = sgold1.render('GOLD',1,lightblue)
            sc.blit(sgold2,(830,255))
            shp1 = pygame.font.SysFont("stencil",40)
            shp2 = shp1.render('HP',1,lightblue)
            sc.blit(shp2,(840,305))
            smp1 = pygame.font.SysFont("stencil",40)
            smp2 = smp1.render('MP',1,lightblue)
            sc.blit(smp2,(840,355))
            sstr1 = pygame.font.SysFont("stencil",40)
            sstr2 = sstr1.render('STR',1,lightblue)
            sc.blit(sstr2,(830,405))
            sintt1 = pygame.font.SysFont("stencil",40)
            sintt2 = sintt1.render('INT',1,lightblue)
            sc.blit(sintt2,(830,455))
            sdex1 = pygame.font.SysFont("stencil",40)
            sdex2 = sdex1.render('MISS',1,lightblue)
            sc.blit(sdex2,(830,505))

            mycharacter.status()
            if mycharacter.LV < 10:
                statuslen1 = 1050
            else:
                statuslen1 = 1038

            if mycharacter.goldnd < 10:
                statuslen2 = 1050
            elif mycharacter.goldnd < 100:
                statuslen2 = 1038
            elif mycharacter.goldnd < 1000:
                statuslen2 = 1026
            else:
                statuslen2 = 1014

            if mycharacter.STR < 10:
                statuslen3 = 1050
            elif mycharacter.STR < 100:
                statuslen3 = 1038
            else:
                statuslen3 = 1026

            if mycharacter.miss < 0.1:
                statuslen5 = 1025
            else:
                statuslen5 = 1013

            if mycharacter.INT < 10:
                statuslen4 = 1050
            elif mycharacter.INT < 100:
                statuslen4 = 1038
            else:
                statuslen4 = 1026

            if mycharacter.miss < 10:
                statuslen5 = 1038
            else:
                statuslen5 = 1026

            if mycharacter.expnd < 10:
                statuslen6 = 1051
            elif mycharacter.expnd < 100:
                statuslen6 = 1028
            elif mycharacter.expnd < 1000:
                statuslen6 = 1005
            elif mycharacter.expnd < 10000:
                statuslen6 = 982
            else:
                statuslen6 = 959

            if mycharacter.hpnd < 10:
                statuslen7 = 1051
            elif mycharacter.hpnd < 100:
                statuslen7 = 1028
            elif mycharacter.hpnd < 1000:
                statuslen7 = 1005
            else:
                statuslen7 = 982
                
            if mycharacter.mpnd < 10:
                statuslen8 = 1051
            elif mycharacter.mpnd < 100:
                statuslen8 = 1028
            elif mycharacter.mpnd < 1000:
                statuslen8 = 1005
            else:
                statuslen8 = 982

            statusnum = pygame.font.SysFont("stencil",40)
            nlv = statusnum.render(str(mycharacter.LV),1,numm)
            sc.blit(nlv,(statuslen1,155))
            nexpnd = statusnum.render(str(mycharacter.expnd),1,numm)
            sc.blit(nexpnd,(statuslen6,205))
            nexp = statusnum.render('/'+str(mycharacter.exp),1,numm)
            sc.blit(nexp,(1080,205))
            ngold = statusnum.render(str(mycharacter.goldnd),1,numm)
            sc.blit(ngold,(statuslen2,255))
            nhpnd = statusnum.render(str(mycharacter.hpnd),1,numm)
            sc.blit(nhpnd,(statuslen7,305))
            nhp = statusnum.render('/'+str(mycharacter.HP),1,numm)
            sc.blit(nhp,(1080,305))
            nmpnd = statusnum.render(str(mycharacter.mpnd),1,numm)
            sc.blit(nmpnd,(statuslen8,355))
            nmp = statusnum.render('/'+str(mycharacter.MP),1,numm)
            sc.blit(nmp,(1080,355))
            nstr = statusnum.render(str(mycharacter.STR),1,numm)
            sc.blit(nstr,(statuslen3,405))
            nint = statusnum.render(str(mycharacter.INT),1,numm)
            sc.blit(nint,(statuslen4,455))
            nmiss = statusnum.render(str(mycharacter.miss)+'%',1,numm)
            sc.blit(nmiss,(statuslen5,505))

            drawsquare([(350,50),(350,573),(745,573),(745,50)])
            if itemmenu%2 == 0:
                contral1 = pygame.font.SysFont("stencil",50)
                contral2 = contral1.render('CONTRAL',1,sblue)
                sc.blit(contral2,(440,80))
                pygame.draw.line(sc,sblue,(380,135),(715,135),5)

            if abilitymenu%2 == 0 and itemmenu%2 == 0:
                yline = [193,243,293,343,393,443,493,543]
                for i in yline:
                    pygame.draw.line(sc,shell,(380,i),(715,i),3)

                up1 = pygame.font.SysFont("stencil",40)
                up2 = up1.render('UP',1,lightblue)
                sc.blit(up2,(385,155))
                down1 = pygame.font.SysFont("stencil",40)
                down2 = down1.render('DOWN',1,lightblue)
                sc.blit(down2,(380,205))
                right1 = pygame.font.SysFont("stencil",40)
                right2 = right1.render('RIGHT',1,lightblue)
                sc.blit(right2,(380,255))
                left1 = pygame.font.SysFont("stencil",40)
                left2 = left1.render('LEFT',1,lightblue)
                sc.blit(left2,(380,305))
                heal1 = pygame.font.SysFont("stencil",40)
                heal2 = heal1.render('SKILL',1,lightblue)
                sc.blit(heal2,(380,355))
                item1 = pygame.font.SysFont("stencil",40)
                item2 = item1.render('ITEM',1,lightblue)
                sc.blit(item2,(380,405))
                save1 = pygame.font.SysFont("stencil",40)
                save2 = save1.render('SAVE',1,lightblue)
                sc.blit(save2,(380,455))
                menu1 = pygame.font.SysFont("stencil",40)
                menu2 = menu1.render('MENU',1,lightblue)
                sc.blit(menu2,(380,505))

                cup1 = pygame.font.SysFont("stencil",40)
                cup2 = cup1.render('W',1,numm)
                sc.blit(cup2,(605,155))
                cdown1 = pygame.font.SysFont("stencil",40)
                cdown2 = cdown1.render('S',1,numm)
                sc.blit(cdown2,(605,205))
                cright1 = pygame.font.SysFont("stencil",40)
                cright2 = cright1.render('D',1,numm)
                sc.blit(cright2,(605,255))
                cleft1 = pygame.font.SysFont("stencil",40)
                cleft2 = cleft1.render('A',1,numm)
                sc.blit(cleft2,(605,305))
                cheal1 = pygame.font.SysFont("stencil",40)
                cheal2 = cheal1.render('Q',1,numm)
                sc.blit(cheal2,(605,355)) 
                citem1 = pygame.font.SysFont("stencil",40)
                citem2 = citem1.render('G',1,numm)
                sc.blit(citem2,(605,405))
                csave1 = pygame.font.SysFont("stencil",40)
                csave2 = csave1.render('ALT+B',1,numm)
                sc.blit(csave2,(555,455))
                cmenu1 = pygame.font.SysFont("stencil",40)
                cmenu2 = menu1.render('CTRL+Z',1,numm)
                sc.blit(cmenu2,(545,505))

                manage1 = pygame.font.SysFont("stencil",23)
                manage2 = manage1.render('Press [P] to Manage',1,blue)
                sc.blit(manage2,(58,590))
        
            if itemmenu%2 == 1:
                store1 = pygame.font.SysFont("stencil",50)
                store2 = store1.render('STORE',1,sblue)
                sc.blit(store2,(470,75))
                pygame.draw.line(sc,sblue,(470,123),(625,123),5)
                pygame.draw.line(sc,sblue,(380,193),(715,193),5)
                
                item1 = pygame.font.SysFont("stencil",40)
                item2 = item1.render('ITEM',1,sblue)
                sc.blit(item2,(410,150))
                gold1 = pygame.font.SysFont("stencil",40)
                gold2 = gold1.render('GOLD',1,sblue)
                sc.blit(gold2,(595,150))
                
                hps1 = pygame.font.SysFont("stencil",40)
                hps2 = hps1.render('HP 1200',1,lightblue)
                sc.blit(hps2,(380,205))
                hpm1 = pygame.font.SysFont("stencil",40)
                hpm2 = hpm1.render('HP 2100',1,lightblue)
                sc.blit(hpm2,(380,255))
                hpl1 = pygame.font.SysFont("stencil",40)
                hpl2 = hpl1.render('HP 3200',1,lightblue)
                sc.blit(hpl2,(380,305))
                mps1 = pygame.font.SysFont("stencil",40)
                mps2 = mps1.render('MP 100',1,lightblue)
                sc.blit(mps2,(380,355))
                mpm1 = pygame.font.SysFont("stencil",40)
                mpm2 = mpm1.render('MP 300',1,lightblue)
                sc.blit(mpm2,(380,405))
                mpl1 = pygame.font.SysFont("stencil",40)
                mpl2 = mpl1.render('MP 500',1,lightblue)
                sc.blit(mpl2,(380,455))
                buy1 = pygame.font.SysFont("stencil",40)
                buy2 = buy1.render('BUY',1,lightblue)
                sc.blit(buy2,(380,505))
                
                return1 = pygame.font.SysFont("stencil",23)
                return2 = return1.render('Press [G] to RETURN',1,blue)
                sc.blit(return2,(420,590))
                
                if itemcolor%6 == 1:
                    ihps1 = pygame.font.SysFont("stencil",40)
                    ihps2 = ihps1.render('HP 1200',1,waterblue)
                    sc.blit(ihps2,(380,205))
                elif itemcolor%6 == 2:
                    ihpm1 = pygame.font.SysFont("stencil",40)
                    ihpm2 = ihpm1.render('HP 2100',1,waterblue)
                    sc.blit(ihpm2,(380,255))
                elif itemcolor%6 == 3:
                    ihpl1 = pygame.font.SysFont("stencil",40)
                    ihpl2 = ihpl1.render('HP 3200',1,waterblue)
                    sc.blit(ihpl2,(380,305))
                elif itemcolor%6 == 4:
                    imps1 = pygame.font.SysFont("stencil",40)
                    imps2 = imps1.render('MP 100',1,waterblue)
                    sc.blit(imps2,(380,355))
                elif itemcolor%6 == 5:
                    impm1 = pygame.font.SysFont("stencil",40)
                    impm2 = impm1.render('MP 300',1,waterblue)
                    sc.blit(impm2,(380,405))
                elif itemcolor%6 == 0:
                    impl1 = pygame.font.SysFont("stencil",40)
                    impl2 = impl1.render('MP 500',1,waterblue)
                    sc.blit(impl2,(380,455))

                yline = [243,293,343,393,443,493,543]
                for i in yline:
                    pygame.draw.line(sc,shell,(380,i),(715,i),3)
                
                bhps1 = pygame.font.SysFont("stencil",40)
                bhps2 = bhps1.render('40',1,numm)
                sc.blit(bhps2,(620,205))
                bhpm1 = pygame.font.SysFont("stencil",40)
                bhpm2 = bhpm1.render('200',1,numm)
                sc.blit(bhpm2,(605,255))
                bhpl1 = pygame.font.SysFont("stencil",40)
                bhpl2 = bhpl1.render('500',1,numm)
                sc.blit(bhpl2,(605,305))
                bmps1 = pygame.font.SysFont("stencil",40)
                bmps2 = bmps1.render('30',1,numm)
                sc.blit(bmps2,(620,355))
                bmpm1 = pygame.font.SysFont("stencil",40)
                bmpm2 = bmpm1.render('80',1,numm)
                sc.blit(bmpm2,(620,405)) 
                bmpl1 = pygame.font.SysFont("stencil",40)
                bmpl2 = bmpl1.render('130',1,numm)
                sc.blit(bmpl2,(605,455))
                bbuy1 = pygame.font.SysFont("stencil",40)
                bbuy2 = bbuy1.render('D',1,numm)
                sc.blit(bbuy2,(630,505))

            if abilitymenu%2 == 1:
                if abilitycolor%6 == 1:
                    ahp1 = pygame.font.SysFont("stencil",40)
                    ahp2 = ahp1.render('HP',1,waterblue)
                    sc.blit(ahp2,(90,220))
                elif abilitycolor%6 == 2:
                    amp1 = pygame.font.SysFont("stencil",40)
                    amp2 = amp1.render('MP',1,waterblue)
                    sc.blit(amp2,(90,277))
                elif abilitycolor%6 == 3:
                    astr1 = pygame.font.SysFont("stencil",40)
                    astr2 = astr1.render('STR',1,waterblue)
                    sc.blit(astr2,(80,334))
                elif abilitycolor%6 == 4:
                    aintt1 = pygame.font.SysFont("stencil",40)
                    aintt2 = aintt1.render('INT',1,waterblue)
                    sc.blit(aintt2,(80,391))
                elif abilitycolor%6 == 5:
                    adex1 = pygame.font.SysFont("stencil",40)
                    adex2 = adex1.render('DEX',1,waterblue)
                    sc.blit(adex2,(80,448))
                elif abilitycolor%6 == 0:
                    aluk1 = pygame.font.SysFont("stencil",40)
                    aluk2 = aluk1.render('LUK',1,waterblue)
                    sc.blit(aluk2,(80,505))

                yline = [193,243,293,343,443,493,543]
                for i in yline:
                    pygame.draw.line(sc,shell,(380,i),(715,i),3)

                up1 = pygame.font.SysFont("stencil",40)
                up2 = up1.render('UP',1,lightblue)
                sc.blit(up2,(385,155))
                down1 = pygame.font.SysFont("stencil",40)
                down2 = down1.render('DOWN',1,lightblue)
                sc.blit(down2,(380,205))
                right1 = pygame.font.SysFont("stencil",40)
                right2 = right1.render('PLUS',1,lightblue)
                sc.blit(right2,(380,255))
                left1 = pygame.font.SysFont("stencil",40)
                left2 = left1.render('MINUS',1,lightblue)
                sc.blit(left2,(380,305))
                heal1 = pygame.font.SysFont("stencil",40)
                heal2 = heal1.render('POINT',1,lightblue)
                sc.blit(heal2,(380,360))
                item1 = pygame.font.SysFont("stencil",40)
                item2 = item1.render('REMAIN',1,lightblue)
                sc.blit(item2,(380,405))
                save1 = pygame.font.SysFont("stencil",40)
                save2 = save1.render('SAVE',1,lightblue)
                sc.blit(save2,(380,455))
                menu1 = pygame.font.SysFont("stencil",40)
                menu2 = menu1.render('CANCEL',1,lightblue)
                sc.blit(menu2,(380,505))

                if mycharacter.remain < 10:
                    pointlen = 605
                else:
                    pointlen = 593

                cup1 = pygame.font.SysFont("stencil",40)
                cup2 = cup1.render('W',1,numm)
                sc.blit(cup2,(605,155))
                cdown1 = pygame.font.SysFont("stencil",40)
                cdown2 = cdown1.render('S',1,numm)
                sc.blit(cdown2,(605,205))
                cright1 = pygame.font.SysFont("stencil",40)
                cright2 = cright1.render('D',1,numm)
                sc.blit(cright2,(605,255))
                cleft1 = pygame.font.SysFont("stencil",40)
                cleft2 = cleft1.render('A',1,numm)
                sc.blit(cleft2,(605,305))
                cremain1 = pygame.font.SysFont("stencil",40)
                cremain2 = cremain1.render(str(mycharacter.remain),1,numm)
                sc.blit(cremain2,(pointlen,380))
                csave1 = pygame.font.SysFont("stencil",40)
                csave2 = csave1.render('CTRL+V',1,numm)
                sc.blit(csave2,(545,455))
                cmenu1 = pygame.font.SysFont("stencil",40)
                cmenu2 = menu1.render('P',1,numm)
                sc.blit(cmenu2,(605,505)) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                newgame = 0
            if event.type == pygame.KEYDOWN:
                if checkmenu%2 == 1:
                    if abilitymenu%2 == 0 and itemmenu%2 == 0:
                        if event.key == K_z and mods & pygame.KMOD_LCTRL:
                            yesnocolor1 = 220
                            yesnocolor2 = 240
                            yesnocolor3 = 240
                            surecolor1 = 220
                            surecolor2 = 240
                            surecolor3 = 240
                            choosecolor1 = 220
                            choosecolor2 = 240
                            choosecolor3 = 240

                            suretime = 0
                            yesnotime = 0

                            pa = (0,0,0)
                            pb = (0,0,0)
                            pc = (0,0,0)
                            pd = (0,0,0)
                            pe = (0,0,0)
                            pf = (0,0,0)
                            pg = (0,0,0)
                            ph = (0,0,0)
                            pi = (0,0,0)
                            pj = (0,0,0)
                            pk = (0,0,0)
                            pl = (0,0,0)

                            changecolor1,changecolor2,changecolor3,changecolor4 = (0,0,0,0)

                            linelen = 200
                            picpos = 325
                            menupos1 = 320
                            menupos2 = 440
                            menupos3 = 560
                            color1 = 179,153,255
                            createnew = 0
                            choosemenu = 0
                            newgame = 0
                            
                            for i in mapreturn:
                                aaa,bbb,ccc = i
                                name = 'map'+str(bbb)+'.txt'
                                with open(name,'r+b') as f:
                                    f.seek(ccc)
                                    if int(aaa) == 3:
                                        f.write(b'3')
                                    elif int(aaa) == 5:
                                        f.write(b'5')
                                    elif int(aaa) == 6:
                                        f.write(b'6')
                                    elif int(aaa) == 7:
                                        f.write(b'7')
                                    elif int(aaa) == 9:
                                        f.write(b'9')
                                    else:
                                        f.write(b'0')
                                    f.flush
                                    f.seek(0)
                            
                            k = kk
                            xr = xrr
                            yr = yrr
                            mapx = mapxx
                            mapy = mapyy
                            charface = charfacee
                            inkyesno = inkyesnoo
                            contralyesno = contralyesnoo
                            
                            mycharacter.HPs = mycharacterold.HPs
                            mycharacter.MPs = mycharacterold.MPs
                            mycharacter.STRs = mycharacterold.STRs
                            mycharacter.INTs = mycharacterold.INTs
                            mycharacter.DEXs = mycharacterold.DEXs
                            mycharacter.LUKs = mycharacterold.LUKs
                            mycharacter.LV = mycharacterold.LV
                            mycharacter.key = mycharacterold.key
                            mycharacter.remain = mycharacterold.remain
                            mycharacter.exp = mycharacterold.exp
                            mycharacter.expnd = mycharacterold.expnd
                            mycharacter.hpnd = mycharacterold.hpnd
                            mycharacter.mpnd = mycharacterold.mpnd
                            mycharacter.goldnd = mycharacterold.goldnd

                        if event.key == K_b and mods & pygame.KMOD_LALT:
                            mapreturn.clear()
                            kk = k
                            xrr = xr
                            yrr = yr
                            mapxx = mapx
                            mapyy = mapy
                            charfacee = charface
                            inkyesnoo = inkyesno
                            contralyesnoo = contralyesno
                            mycharacterold.HPs = mycharacter.HPs
                            mycharacterold.MPs = mycharacter.MPs
                            mycharacterold.STRs = mycharacter.STRs
                            mycharacterold.INTs = mycharacter.INTs
                            mycharacterold.DEXs = mycharacter.DEXs
                            mycharacterold.LUKs = mycharacter.LUKs
                            mycharacterold.LV = mycharacter.LV
                            mycharacterold.key = mycharacter.key
                            mycharacterold.remain = mycharacter.remain
                            mycharacterold.exp = mycharacter.exp
                            mycharacterold.expnd = mycharacter.expnd
                            mycharacterold.hpnd = mycharacter.hpnd
                            mycharacterold.mpnd = mycharacter.mpnd
                            mycharacterold.goldnd = mycharacter.goldnd
                    if abilitymenu%2 == 0:
                        if event.key == K_g:
                            itemcolor = 1
                            itemmenu += 1
                    if itemmenu%2 == 0:
                        if event.key == K_p:
                            abilitycolor = 1
                            abilitymenu += 1
                            numm1 = 71,152,179
                            numm2 = 71,152,179
                            numm3 = 71,152,179
                            numm4 = 71,152,179
                            numm5 = 71,152,179
                            numm6 = 71,152,179
                            if abilitymenu%2 == 0:
                                mycharacter.remain = pointstatus0
                                mycharacter.HPs = pointstatus1
                                mycharacter.MPs = pointstatus2
                                mycharacter.STRs = pointstatus3
                                mycharacter.INTs = pointstatus4
                                mycharacter.DEXs = pointstatus5
                                mycharacter.LUKs = pointstatus6

                            pointstatus0 = mycharacter.remain
                            pointstatus1 = mycharacter.HPs
                            pointstatus2 = mycharacter.MPs
                            pointstatus3 = mycharacter.STRs
                            pointstatus4 = mycharacter.INTs
                            pointstatus5 = mycharacter.DEXs
                            pointstatus6 = mycharacter.LUKs

                if abilitymenu%2 == 0 and needbattle%2 == 0 and itemmenu%2 ==0:
                    if event.key == K_m:
                        if mycharacter.hpnd > 0:
                            checkmenu += 1
                            firstcolor = random.randint(1,6)
                            rr,gg,bb = color(firstcolor)
                            move = random.randint(1,4)
                            ballx = random.randint(50,1230)
                            bally = random.randint(50,670)
                        else:
                            pass
                if checkmenu%2 == 0 and needbattle%2 == 0 and mycharacter.hpnd > 0:
                    if event.key == K_d:
                        healcount = 0
                        if contralyesno%2 == 0:
                            xk = 1
                            yk = 0
                            charface = 1
                            if k == 15:
                                if xr+xk == 14:
                                    if mapx < 49:
                                        xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                        xk = 0
                                        yk = 0
                                    else:
                                        xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast2(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                        xk = 0
                                        yk = 0
                                else:
                                    xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast2(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                    xk = 0
                                    yk = 0
                            else:
                                if xr+xk > 15:
                                    pass
                                else:
                                    xr,yr,needbattle,fightcount,mapreturn,mapreturnreal = wall(mat,xr,yr,xk,yk,k,needbattle,fightcount,mapreturn,mapreturnreal)
                                    xk = 0
                                    yk = 0
                        else:
                            xk = -1
                            yk = 0
                            charface = 2
                            if k == 15:
                                if xr+xk == 2:
                                    if mapx > 1:
                                        xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                        xk = 0
                                        yk = 0
                                    else:
                                        xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast2(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                        xk = 0
                                        yk = 0
                                else:
                                    xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast2(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                    xk = 0
                                    yk = 0
                            else:
                                if xr+xk < 0:
                                    pass
                                else:
                                    xr,yr,needbattle,fightcount,mapreturn,mapreturnreal = wall(mat,xr,yr,xk,yk,k,needbattle,fightcount,mapreturn,mapreturnreal)
                                    xk = 0
                                    yk = 0
                            
                        

                    if event.key == K_a:
                        healcount = 0
                        if contralyesno%2 == 0:
                            xk = -1
                            yk = 0
                            charface = 2
                            if k == 15:
                                if xr+xk == 2:
                                    if mapx > 1:
                                        xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                        xk = 0
                                        yk = 0
                                    else:
                                        xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast2(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                        xk = 0
                                        yk = 0
                                else:
                                    xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast2(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                    xk = 0
                                    yk = 0
                            else:
                                if xr+xk < 0:
                                    pass
                                else:
                                    xr,yr,needbattle,fightcount,mapreturn,mapreturnreal = wall(mat,xr,yr,xk,yk,k,needbattle,fightcount,mapreturn,mapreturnreal)
                                    xk = 0
                                    yk = 0
                        else:
                            xk = 1
                            yk = 0
                            charface = 1
                            if k == 15:
                                if xr+xk == 14:
                                    if mapx < 49:
                                        xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                        xk = 0
                                        yk = 0
                                    else:
                                        xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast2(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                        xk = 0
                                        yk = 0
                                else:
                                    xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast2(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                    xk = 0
                                    yk = 0
                            else:
                                if xr+xk > 15:
                                    pass
                                else:
                                    xr,yr,needbattle,fightcount,mapreturn,mapreturnreal = wall(mat,xr,yr,xk,yk,k,needbattle,fightcount,mapreturn,mapreturnreal)
                                    xk = 0
                                    yk = 0
                            
                        

                    if event.key == K_s:
                        healcount = 0
                        if contralyesno%2 == 0:
                            xk = 0
                            yk = 1
                            if k == 15:
                                if yr+yk == 7:
                                    if mapy < 28:
                                        xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                        xk = 0
                                        yk = 0
                                    else:
                                        xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast2(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                        xk = 0
                                        yk = 0
                                else:
                                    xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast2(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                    xk = 0
                                    yk = 0
                            else:
                                if yr+yk > 8:
                                    pass
                                else:
                                    xr,yr,needbattle,fightcount,mapreturn,mapreturnreal = wall(mat,xr,yr,xk,yk,k,needbattle,fightcount,mapreturn,mapreturnreal)
                                    xk = 0
                                    yk = 0
                        else:
                            xk = 0
                            yk = -1
                            if k == 15:
                                if yr+yk == 1:
                                    if mapy > 1:
                                        xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                        xk = 0
                                        yk = 0
                                    else:
                                        xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast2(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                        xk = 0
                                        yk = 0
                                else:
                                    xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast2(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                    xk = 0
                                    yk = 0
                            else:
                                if yr+yk < 0:
                                    pass
                                else:
                                    xr,yr,needbattle,fightcount,mapreturn,mapreturnreal = wall(mat,xr,yr,xk,yk,k,needbattle,fightcount,mapreturn,mapreturnreal)
                                    xk = 0
                                    yk = 0
                        

                    if event.key == K_w:
                        healcount = 0
                        if contralyesno%2 == 0:
                            xk = 0
                            yk = -1
                            if k == 15:
                                if yr+yk == 1:
                                    if mapy > 1:
                                        xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                        xk = 0
                                        yk = 0
                                    else:
                                        xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast2(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                        xk = 0
                                        yk = 0
                                else:
                                    xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast2(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                    xk = 0
                                    yk = 0
                            else:
                                if yr+yk < 0:
                                    pass
                                else:
                                    xr,yr,needbattle,fightcount,mapreturn,mapreturnreal = wall(mat,xr,yr,xk,yk,k,needbattle,fightcount,mapreturn,mapreturnreal)
                                    xk = 0
                                    yk = 0
                        else:
                            xk = 0
                            yk = 1
                            if k == 15:
                                if yr+yk == 7:
                                    if mapy < 28:
                                        xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                        xk = 0
                                        yk = 0
                                    else:
                                        xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast2(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                        xk = 0
                                        yk = 0
                                else:
                                    xr,yr,mapx,mapy,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno = walllast2(mat,xr,yr,xk,yk,mapx,mapy,k,needbattle,fightcount,mapreturn,mapreturnreal,contralyesno,inkyesno)
                                    xk = 0
                                    yk = 0
                            else:
                                if yr+yk > 8:
                                    pass
                                else:
                                    xr,yr,needbattle,fightcount,mapreturn,mapreturnreal = wall(mat,xr,yr,xk,yk,k,needbattle,fightcount,mapreturn,mapreturnreal)
                                    xk = 0
                                    yk = 0
                            
                        
                
                if needbattle%2 == 1:
                    if mycharacter.hpnd > 0:
                        if event.key == K_q:
                            useskill += 1
                        if event.key == K_g:
                            battleitemmenu += 1
                    else:
                        pass
                        
                if itemmenu%2 == 1 or battleitemmenu%2 == 1:
                    if event.key == K_w:
                        itemcolor -= 1
                    if event.key == K_s:
                        itemcolor += 1
                    if event.key == K_d:
                        if itemcolor%6 ==1:
                            buyitem(1,40,1200,mycharacter)
                        if itemcolor%6 ==2:
                            buyitem(1,200,2100,mycharacter)
                        if itemcolor%6 ==3:
                            buyitem(1,500,3200,mycharacter)
                        if itemcolor%6 ==4:
                            buyitem(2,30,100,mycharacter)
                        if itemcolor%6 ==5:
                            buyitem(2,80,300,mycharacter)
                        if itemcolor%6 ==0:
                            buyitem(2,130,500,mycharacter)
                            
                if abilitymenu%2 == 1:
                    if event.key == K_w:
                        abilitycolor -= 1
                    if event.key == K_s:
                        abilitycolor += 1
                    if event.key == K_d:
                        if mycharacter.remain > 0:
                            if abilitycolor%6 == 1:
                                mycharacter.remain -= 1
                                mycharacter.HPs += 1
                                numm1 = waterblue
                            elif abilitycolor%6 == 2:
                                mycharacter.remain -= 1
                                mycharacter.MPs += 1
                                numm2 = waterblue
                            elif abilitycolor%6 == 3:
                                mycharacter.remain -= 1
                                mycharacter.STRs += 1
                                numm3 = waterblue
                            elif abilitycolor%6 == 4:
                                mycharacter.remain -= 1
                                mycharacter.INTs += 1
                                numm4 = waterblue
                            elif abilitycolor%6 == 5:
                                mycharacter.remain -= 1
                                mycharacter.DEXs += 1
                                numm5 = waterblue
                            elif abilitycolor%6 == 0:
                                mycharacter.remain -= 1
                                mycharacter.LUKs += 1
                                numm6 = waterblue
                    if event.key == K_a:
                        if abilitycolor%6 == 1:
                            if mycharacter.HPs > pointstatus1:
                                mycharacter.remain += 1
                                mycharacter.HPs -= 1
                            if mycharacter.HPs == pointstatus1:
                                numm1 = 71,152,179
                        elif abilitycolor%6 == 2:
                            if mycharacter.MPs > pointstatus2:
                                mycharacter.remain += 1
                                mycharacter.MPs -= 1
                            if mycharacter.MPs == pointstatus2:
                                numm2 = 71,152,179
                        elif abilitycolor%6 == 3:
                            if mycharacter.STRs > pointstatus3:
                                mycharacter.remain += 1
                                mycharacter.STRs -= 1
                            if mycharacter.STRs == pointstatus3:
                                numm3 = 71,152,179
                        elif abilitycolor%6 == 4:
                            if mycharacter.INTs > pointstatus4:
                                mycharacter.remain += 1
                                mycharacter.INTs -= 1
                            if mycharacter.INTs == pointstatus4:
                                numm4 = 71,152,179
                        elif abilitycolor%6 == 5:
                            if mycharacter.DEXs > pointstatus5:
                                mycharacter.remain += 1
                                mycharacter.DEXs -= 1
                            if mycharacter.DEXs == pointstatus5:
                                numm5 = 71,152,179
                        elif abilitycolor%6 == 0:
                            if mycharacter.LUKs > pointstatus6:
                                mycharacter.remain += 1
                                mycharacter.LUKs -= 1
                            if mycharacter.LUKs == pointstatus6:
                                numm6 = 71,152,179
                    if event.key == K_v and mods & pygame.KMOD_LCTRL:
                        numm1 = 71,152,179
                        numm2 = 71,152,179
                        numm3 = 71,152,179
                        numm4 = 71,152,179
                        numm5 = 71,152,179
                        numm6 = 71,152,179
                        abilitycolor = 1
                        abilitymenu += 1
            if event.type == MOUSEMOTION:
                pos = pygame.mouse.get_pos()     
            if event.type ==  MOUSEBUTTONDOWN:
                pass
        
        if checkmenu%2 == 0 and needbattle%2 == 0:
            if mat[yr,xr] != 2 and mat[yr,xr] != 4:
                healcount += 1

        if needbattle%2 == 1:
            if battlelen < 1280:
                pygame.draw.rect(sc,rose,[0,0,battlelen,720])
                battlelen += 80
            else:
                pygame.draw.rect(sc,rose,[0,0,1280,720])
                
                if mycharacter.HPmonnd < 10:
                    monstatuslen1 = 311
                elif mycharacter.HPmonnd < 100:
                    monstatuslen1 = 288
                elif mycharacter.HPmonnd < 1000:
                    monstatuslen1 = 265
                else:
                    monstatuslen1 = 242
                    
                monsta = pygame.font.SysFont("stencil",40)
                monhp = monsta.render('/'+str(mycharacter.HPmon),1,numm)
                monhpnd = monsta.render(str(mycharacter.HPmonnd),1,numm)
                sc.blit(monhp,(340,85))
                sc.blit(monhpnd,(monstatuslen1,85))         
                
                if battleitemmenu%2 == 0:
                    battlecount += 1
                    
                    pygame.draw.circle(sc,battlecolor1,(120,259),60)
                    pygame.draw.circle(sc,rose,(120,259),52)
                    pygame.draw.circle(sc,battlecolor2,(120,429),60)
                    pygame.draw.circle(sc,rose,(120,429),52)
                    pygame.draw.circle(sc,battlecolor3,(120,599),60)
                    pygame.draw.circle(sc,rose,(120,599),52)
                    pygame.draw.circle(sc,battlecolor4,(335,259),60)
                    pygame.draw.circle(sc,rose,(335,259),52)
                    pygame.draw.circle(sc,battlecolor5,(335,429),60)
                    pygame.draw.circle(sc,rose,(335,429),52)
                    pygame.draw.circle(sc,battlecolor6,(335,599),60)
                    pygame.draw.circle(sc,rose,(335,599),52)
                    
                    bim = pygame.font.SysFont("stencil",100)
                    att = bim.render('A',1,battlecolor1)
                    sc.blit(att,(88,219))
                    ski = bim.render('S',1,battlecolor2)
                    sc.blit(ski,(92,389))
                    mis = bim.render('M',1,battlecolor3)
                    sc.blit(mis,(82,559))
                    attmon = bim.render('A',1,battlecolor4)
                    sc.blit(attmon,(303,219))
                    skimon = bim.render('S',1,battlecolor5)
                    sc.blit(skimon,(307,389))
                    mismon = bim.render('M',1,battlecolor6)
                    sc.blit(mismon,(297,559))
                    
                else:
                    store1 = pygame.font.SysFont("stencil",50)
                    store2 = store1.render('STORE',1,sblue)
                    sc.blit(store2,(150,192))
                    pygame.draw.line(sc,sblue,(150,240),(305,240),5)
                    pygame.draw.line(sc,sblue,(60,310),(395,310),5)

                    item1 = pygame.font.SysFont("stencil",40)
                    item2 = item1.render('ITEM',1,sblue)
                    sc.blit(item2,(90,267))
                    gold1 = pygame.font.SysFont("stencil",40)
                    gold2 = gold1.render('GOLD',1,sblue)
                    sc.blit(gold2,(275,267))

                    hps1 = pygame.font.SysFont("stencil",40)
                    hps2 = hps1.render('HP 1200',1,lightblue)
                    sc.blit(hps2,(60,322))
                    hpm1 = pygame.font.SysFont("stencil",40)
                    hpm2 = hpm1.render('HP 2100',1,lightblue)
                    sc.blit(hpm2,(60,372))
                    hpl1 = pygame.font.SysFont("stencil",40)
                    hpl2 = hpl1.render('HP 3200',1,lightblue)
                    sc.blit(hpl2,(60,422))
                    mps1 = pygame.font.SysFont("stencil",40)
                    mps2 = mps1.render('MP 100',1,lightblue)
                    sc.blit(mps2,(60,472))
                    mpm1 = pygame.font.SysFont("stencil",40)
                    mpm2 = mpm1.render('MP 300',1,lightblue)
                    sc.blit(mpm2,(60,522))
                    mpl1 = pygame.font.SysFont("stencil",40)
                    mpl2 = mpl1.render('MP 500',1,lightblue)
                    sc.blit(mpl2,(60,572))
                    buy1 = pygame.font.SysFont("stencil",40)
                    buy2 = buy1.render('BUY',1,lightblue)
                    sc.blit(buy2,(60,622))

                    if itemcolor%6 == 1:
                        ihps1 = pygame.font.SysFont("stencil",40)
                        ihps2 = ihps1.render('HP 1200',1,waterblue)
                        sc.blit(ihps2,(60,322))
                    elif itemcolor%6 == 2:
                        ihpm1 = pygame.font.SysFont("stencil",40)
                        ihpm2 = ihpm1.render('HP 2100',1,waterblue)
                        sc.blit(ihpm2,(60,372))
                    elif itemcolor%6 == 3:
                        ihpl1 = pygame.font.SysFont("stencil",40)
                        ihpl2 = ihpl1.render('HP 3200',1,waterblue)
                        sc.blit(ihpl2,(60,422))
                    elif itemcolor%6 == 4:
                        imps1 = pygame.font.SysFont("stencil",40)
                        imps2 = imps1.render('MP 100',1,waterblue)
                        sc.blit(imps2,(60,472))
                    elif itemcolor%6 == 5:
                        impm1 = pygame.font.SysFont("stencil",40)
                        impm2 = impm1.render('MP 300',1,waterblue)
                        sc.blit(impm2,(60,522))
                    elif itemcolor%6 == 0:
                        impl1 = pygame.font.SysFont("stencil",40)
                        impl2 = impl1.render('MP 500',1,waterblue)
                        sc.blit(impl2,(60,572))

                    yline = [360,410,460,510,560,610,660]
                    for i in yline:
                        pygame.draw.line(sc,shell,(60,i),(395,i),3)

                    bhps1 = pygame.font.SysFont("stencil",40)
                    bhps2 = bhps1.render('40',1,numm)
                    sc.blit(bhps2,(300,322))
                    bhpm1 = pygame.font.SysFont("stencil",40)
                    bhpm2 = bhpm1.render('200',1,numm)
                    sc.blit(bhpm2,(285,372))
                    bhpl1 = pygame.font.SysFont("stencil",40)
                    bhpl2 = bhpl1.render('500',1,numm)
                    sc.blit(bhpl2,(285,422))
                    bmps1 = pygame.font.SysFont("stencil",40)
                    bmps2 = bmps1.render('30',1,numm)
                    sc.blit(bmps2,(300,472))
                    bmpm1 = pygame.font.SysFont("stencil",40)
                    bmpm2 = bmpm1.render('80',1,numm)
                    sc.blit(bmpm2,(300,522)) 
                    bmpl1 = pygame.font.SysFont("stencil",40)
                    bmpl2 = bmpl1.render('130',1,numm)
                    sc.blit(bmpl2,(285,572))
                    bbuy1 = pygame.font.SysFont("stencil",40)
                    bbuy2 = bbuy1.render('D',1,numm)
                    sc.blit(bbuy2,(310,622))
                
                drawsquare([(475,367),(475,690),(765,690),(765,367)])
                monstatus1 = pygame.font.SysFont("stencil",50)
                monstatus2 = monstatus1.render('MONSTER',1,sblue)
                sc.blit(monstatus2,(505,397))
                pygame.draw.line(sc,sblue,(505,452),(735,452),5)

                yline = [510,560,610,660]
                for i in yline:
                    pygame.draw.line(sc,shell,(505,i),(735,i),3)
                
                monlv1 = pygame.font.SysFont("stencil",40)
                monlv2 = monlv1.render('LV',1,lightblue)
                sc.blit(monlv2,(505,472))
                monstr1 = pygame.font.SysFont("stencil",40)
                monstr2 = monstr1.render('STR',1,lightblue)
                sc.blit(monstr2,(505,522))
                mondex1 = pygame.font.SysFont("stencil",40)
                mondex2 = mondex1.render('DEX',1,lightblue)
                sc.blit(mondex2,(505,572))
                monmiss1 = pygame.font.SysFont("stencil",40)
                monmiss2 = monmiss1.render('MISS',1,lightblue)
                sc.blit(monmiss2,(505,622))
                
                if mycharacter.LVmon < 10:
                    monstatuslen2 = 670
                else:
                    monstatuslen2 = 658
                if mycharacter.STRmon < 10:
                    monstatuslen3 = 670
                elif mycharacter.STRmon < 100:
                    monstatuslen3 = 660
                else:
                    monstatuslen3 = 648
                if mycharacter.DEXmon < 10:
                    monstatuslen4 = 670
                else:
                    monstatuslen4 = 658
                if mycharacter.missmon < 10:
                    monstatuslen5 = 655
                else:
                    monstatuslen5 = 643
                
                smonlv1 = pygame.font.SysFont("stencil",40)
                smonlv2 = smonlv1.render(str(mycharacter.LVmon),1,numm)
                sc.blit(smonlv2,(monstatuslen2,472))
                smonstr1 = pygame.font.SysFont("stencil",40)
                smonstr2 = smonstr1.render(str(mycharacter.STRmon),1,numm)
                sc.blit(smonstr2,(monstatuslen3,522))
                smondex1 = pygame.font.SysFont("stencil",40)
                smondex2 = smondex1.render(str(mycharacter.DEXmon),1,numm)
                sc.blit(smondex2,(monstatuslen4,572))
                smonmiss1 = pygame.font.SysFont("stencil",40)
                smonmiss2 = smonmiss1.render(str(mycharacter.missmon)+'%',1,numm)
                sc.blit(smonmiss2,(monstatuslen5,622))                
                
                drawsquare([(815,167),(815,690),(1250,690),(1250,167)])
                status1 = pygame.font.SysFont("stencil",50)
                status2 = status1.render('STATUS',1,sblue)
                sc.blit(status2,(952,197))
                pygame.draw.line(sc,sblue,(850,252),(1220,252),5)

                yline = [310,360,410,460,510,560,610,660]
                for i in yline:
                    pygame.draw.line(sc,shell,(850,i),(1220,i),3)

                slv1 = pygame.font.SysFont("stencil",40)
                slv2 = slv1.render('LV',1,lightblue)
                sc.blit(slv2,(860,272))
                sexp1 = pygame.font.SysFont("stencil",40)
                sexp2 = sexp1.render('EXP',1,lightblue)
                sc.blit(sexp2,(850,322))
                sgold1 = pygame.font.SysFont("stencil",40)
                sgold2 = sgold1.render('GOLD',1,lightblue)
                sc.blit(sgold2,(850,372))
                shp1 = pygame.font.SysFont("stencil",40)
                shp2 = shp1.render('HP',1,lightblue)
                sc.blit(shp2,(860,422))
                smp1 = pygame.font.SysFont("stencil",40)
                smp2 = smp1.render('MP',1,lightblue)
                sc.blit(smp2,(860,472))
                if advenbutton == 3:
                    sintt1 = pygame.font.SysFont("stencil",40)
                    sintt2 = sintt1.render('INT',1,lightblue)
                    sc.blit(sintt2,(850,522))
                else:
                    sstr1 = pygame.font.SysFont("stencil",40)
                    sstr2 = sstr1.render('STR',1,lightblue)
                    sc.blit(sstr2,(850,522))
                sdex1 = pygame.font.SysFont("stencil",40)
                sdex2 = sdex1.render('DEX',1,lightblue)
                sc.blit(sdex2,(850,572))
                smiss1 = pygame.font.SysFont("stencil",40)
                smiss2 = smiss1.render('MISS',1,lightblue)
                sc.blit(smiss2,(850,622))

                mycharacter.status()
                if mycharacter.LV < 10:
                    statuslen1 = 1070
                else:
                    statuslen1 = 1058

                if mycharacter.goldnd < 10:
                    statuslen2 = 1070
                elif mycharacter.goldnd < 100:
                    statuslen2 = 1058
                elif mycharacter.goldnd < 1000:
                    statuslen2 = 1046
                else:
                    statuslen2 = 1034

                if mycharacter.STR < 10:
                    statuslen3 = 1070
                elif mycharacter.STR < 100:
                    statuslen3 = 1058
                else:
                    statuslen3 = 1046

                if mycharacter.miss < 0.1:
                    statuslen5 = 1045
                else:
                    statuslen5 = 1033

                if mycharacter.INT < 10:
                    statuslen4 = 1070
                elif mycharacter.INT < 100:
                    statuslen4 = 1058
                else:
                    statuslen4 = 1046

                if mycharacter.miss < 10:
                    statuslen5 = 1058
                else:
                    statuslen5 = 1046

                if mycharacter.expnd < 10:
                    statuslen6 = 1071
                elif mycharacter.expnd < 100:
                    statuslen6 = 1048
                elif mycharacter.expnd < 1000:
                    statuslen6 = 1025
                elif mycharacter.expnd < 10000:
                    statuslen6 = 1002
                else:
                    statuslen6 = 979

                if mycharacter.hpnd < 10:
                    statuslen7 = 1071
                elif mycharacter.hpnd < 100:
                    statuslen7 = 1048
                elif mycharacter.hpnd < 1000:
                    statuslen7 = 1025
                else:
                    statuslen7 = 1002

                if mycharacter.mpnd < 10:
                    statuslen8 = 1071
                elif mycharacter.mpnd < 100:
                    statuslen8 = 1048
                elif mycharacter.mpnd < 1000:
                    statuslen8 = 1025
                else:
                    statuslen8 = 1002
                    
                if mycharacter.DEXs < 10:
                    statuslen9 = 1070
                elif mycharacter.DEXs < 100:
                    statuslen9 = 1058

                statusnum = pygame.font.SysFont("stencil",40)
                nlv = statusnum.render(str(mycharacter.LV),1,numm)
                sc.blit(nlv,(statuslen1,272))
                nexpnd = statusnum.render(str(mycharacter.expnd),1,battlepluscolor)
                sc.blit(nexpnd,(statuslen6,322))
                nexp = statusnum.render('/'+str(mycharacter.exp),1,numm)
                sc.blit(nexp,(1100,322))
                ngold = statusnum.render(str(mycharacter.goldnd),1,battlepluscolor)
                sc.blit(ngold,(statuslen2,372))
                nhpnd = statusnum.render(str(mycharacter.hpnd),1,numm)
                sc.blit(nhpnd,(statuslen7,422))
                nhp = statusnum.render('/'+str(mycharacter.HP),1,numm)
                sc.blit(nhp,(1100,422))
                nmpnd = statusnum.render(str(mycharacter.mpnd),1,numm)
                sc.blit(nmpnd,(statuslen8,472))
                nmp = statusnum.render('/'+str(mycharacter.MP),1,numm)
                sc.blit(nmp,(1100,472))
                if advenbutton == 3:
                    nint = statusnum.render(str(mycharacter.INT),1,numm)
                    sc.blit(nint,(statuslen4,522))
                else:
                    nstr = statusnum.render(str(mycharacter.STR),1,numm)
                    sc.blit(nstr,(statuslen3,522))              
                ndex = statusnum.render(str(mycharacter.DEXs),1,numm)
                sc.blit(ndex,(statuslen9,572))
                nmiss = statusnum.render(str(mycharacter.miss)+'%',1,numm)
                sc.blit(nmiss,(statuslen5,622))
                
                if advenbutton == 1:
                    sc.blit(ppp13,(30,30))
                elif advenbutton == 2:
                    sc.blit(ppp14,(30,30))
                elif advenbutton == 3:
                    sc.blit(ppp15,(30,30))
                elif advenbutton == 4:
                    sc.blit(ppp16,(30,30))

                bloodlennd = mycharacter.hpnd/mycharacter.HP
                bloodlenmon = mycharacter.HPmonnd/mycharacter.HPmon
                pygame.draw.rect(sc,shell,[30,130,180,20])
                pygame.draw.rect(sc,blue,[30,130,int(180*bloodlennd),20])
                pygame.draw.rect(sc,shell,[245,130,180,20])
                pygame.draw.rect(sc,blue,[245,130,int(180*bloodlenmon),20])

                drawsquare([(30,167),(30,690),(425,690),(425,167)])
                
                if battlecount%24 == 0:
                    if mycharacter.HPmonnd > 0:
                        if fightcount%2 == 0:
                            missposibilitymon = random.randint(1,100)
                            if missposibilitymon <= mycharacter.missmon:
                                battlechangecolor3 += 1
                                fightcount += 1
                            else:
                                if useskill > 0:
                                    if mycharacter.mpnd >= 100:
                                        if advenbutton == 1:
                                            useskill = 0
                                            battlechangecolor2 += 1
                                            mycharacter.mpnd -= 100
                                            mycharacter.HPmonnd -= int(1.5*mycharacter.STR)
                                        elif advenbutton == 2:
                                            useskill = 0
                                            battlechangecolor2 += 1
                                            mycharacter.mpnd -= 100
                                            j = random.randint(1,2)
                                            if j == 1:
                                                mycharacter.HPmonnd -= mycharacter.STR
                                            else:
                                                mycharacter.HPmonnd -= (2*mycharacter.STR)
                                        else:
                                            battlechangecolor1 += 1
                                            if advenbutton == 3:
                                                mycharacter.HPmonnd -= mycharacter.INT
                                            else:
                                                mycharacter.HPmonnd -= mycharacter.STR
                                    else:
                                        battlechangecolor1 += 1
                                        if advenbutton == 3:
                                            mycharacter.HPmonnd -= mycharacter.INT
                                        else:
                                            mycharacter.HPmonnd -= mycharacter.STR
                                else:
                                    battlechangecolor1 += 1
                                    if advenbutton == 3:
                                        mycharacter.HPmonnd -= mycharacter.INT
                                    else:
                                        mycharacter.HPmonnd -= mycharacter.STR
                                fightcount += 1
                                if mycharacter.HPmonnd < 0:
                                    mycharacter.HPmonnd = 0
                        else:
                            missposibility = random.randint(1,100)
                            monskill = random.randint(1,100)
                            if missposibility <= mycharacter.miss:
                                battlechangecolor6 += 1
                                fightcount += 1
                            else:
                                if useskill > 0:
                                    if mycharacter.mpnd >= 100:
                                        if advenbutton == 4:
                                            battlechangecolor2 += 1
                                            battlechangecolor6 += 1
                                            useskill = 0
                                            mycharacter.mpnd -= 100
                                        elif advenbutton == 3:
                                            battlechangecolor2 += 1
                                            useskill = 0
                                            mycharacter.mpnd -= 100
                                            mycharacter.STRmon = int(0.5*mycharacter.STRmon)
                                            if monskill <= 30:
                                                battlechangecolor5 += 1
                                                mycharacter.hpnd -= 2*mycharacter.STRmon
                                            else:
                                                battlechangecolor4 += 1
                                                mycharacter.hpnd -= mycharacter.STRmon
                                        else:
                                            if monskill <= 30:
                                                battlechangecolor5 += 1
                                                mycharacter.hpnd -= 2*mycharacter.STRmon
                                            else:
                                                battlechangecolor4 += 1
                                                mycharacter.hpnd -= mycharacter.STRmon
                                    else:
                                        if monskill <= 30:
                                            battlechangecolor5 += 1
                                            mycharacter.hpnd -= 2*mycharacter.STRmon
                                        else:
                                            battlechangecolor4 += 1
                                            mycharacter.hpnd -= mycharacter.STRmon
                                else:
                                    if monskill <= 30:
                                        battlechangecolor5 += 1
                                        mycharacter.hpnd -= 2*mycharacter.STRmon
                                    else:
                                        battlechangecolor4 += 1
                                        mycharacter.hpnd -= mycharacter.STRmon
                                fightcount += 1
                                if mycharacter.hpnd < 0:
                                    mycharacter.hpnd = 0

                    elif mycharacter.HPmonnd <= 0:
                        battlewin += 1
                        if changecolor1 != 3:
                            battlepluscolor = 255,115,179
                            changecolor1 += 1
                        else:
                            changecolor1 = 0
                            needbattle += 1
                            battlepluscolor = 71,152,179
                            battlewin = 0
                            battlelen = 0
                            battlecount = 0    
                    else:
                        pass
                else:
                    pass
                
                if battlewin > 0:
                    if battlewin == 1:
                        
                        useskill = 0
                        goldnew = mycharacter.goldnd + mycharacter.goldmon
                        expnew = mycharacter.expnd + mycharacter.expmon
                        kexp = mycharacter.expmon%40
                        kkexp = int((mycharacter.expmon-kexp)/40)
                        mycharacter.expnd += kexp
                        battlewin += 1
                    else:
                        if mycharacter.goldnd != goldnew:
                            if mycharacter.goldmon <= 40:
                                mycharacter.goldnd += 1
                            elif mycharacter.goldmon <= 80:
                                if (goldnew - mycharacter.goldnd) < 2:
                                    mycharacter.goldnd = goldnew
                                else:
                                    mycharacter.goldnd += 2
                            elif mycharacter.goldmon <= 120:
                                if (goldnew - mycharacter.goldnd) < 3:
                                    mycharacter.goldnd = goldnew
                                else:
                                    mycharacter.goldnd += 3
                            elif mycharacter.goldmon <= 160:
                                if (goldnew - mycharacter.goldnd) < 4:
                                    mycharacter.goldnd = goldnew
                                else:
                                    mycharacter.goldnd += 4
                            elif mycharacter.goldmon <= 200:
                                if (goldnew - mycharacter.goldnd) < 5:
                                    mycharacter.goldnd = goldnew
                                else:
                                    mycharacter.goldnd += 5
                            elif mycharacter.goldmon <= 240:
                                if (goldnew - mycharacter.goldnd) < 5:
                                    mycharacter.goldnd = goldnew
                                else:
                                    mycharacter.goldnd += 6
                            else:
                                pass
                                    
                        if mycharacter.expnd != expnew:
                            mycharacter.expnd += kkexp
                        else:
                            pass
                        
                        if mycharacter.expnd >= mycharacter.exp:
                            mycharacter.expnd -= mycharacter.exp
                            expnew -= mycharacter.exp
                            mycharacter.LV += 1
                            mycharacter.remain += 3
                            mycharacter.hpnd = mycharacter.HP
                            mycharacter.mpnd = mycharacter.MP
                            expp =[2000,2400,2880,3460,4150,4980,5970,7160,8600,10310,12380,14860,17830,21400,23540,25900,28480,31330,34460,37910,41700,45870,50460,52480,54580,56760,59030,61390,63850]
                            mycharacter.exp = expp[mycharacter.LV-1]
                        else:
                            pass
                else:
                    pass
 
                if battlechangecolor1%2 == 1:
                    if changecolor1 != 12:
                        battlecolor1 = waterblue
                        changecolor1 += 1
                    else:
                        battlechangecolor1 += 1
                        battlecolor1 = lightblue
                        changecolor1 = 0
                if battlechangecolor2%2 == 1:
                    if changecolor2 != 12:
                        battlecolor2 = waterblue
                        changecolor2 += 1
                    else:
                        battlechangecolor2 += 1
                        battlecolor2 = lightblue
                        changecolor2 = 0
                if battlechangecolor3%2 == 1:
                    if changecolor3 != 12:
                        battlecolor3 = waterblue
                        changecolor3 += 1
                    else:
                        battlechangecolor3 += 1
                        battlecolor3 = lightblue
                        changecolor3 = 0
                if battlechangecolor4%2 == 1:
                    if changecolor4 != 12:
                        battlecolor4 = waterblue
                        changecolor4 += 1
                    else:
                        battlechangecolor4 += 1
                        battlecolor4 = lightblue
                        changecolor4 = 0
                if battlechangecolor5%2 == 1:
                    if changecolor5 != 12:
                        battlecolor5 = waterblue
                        changecolor5 += 1
                    else:
                        battlechangecolor5 += 1
                        battlecolor5 = lightblue
                        changecolor5 = 0
                if battlechangecolor6%2 == 1:
                    if changecolor6 != 12:
                        battlecolor6 = waterblue
                        changecolor6 += 1
                    else:
                        battlechangecolor6 += 1
                        battlecolor6 = lightblue
                        changecolor6 = 0
        
        if inkyesno%2 == 1 and needbattle%2 == 0 and checkmenu%2 == 0:
            sc.blit(pp28,(-70,-10))
            sc.blit(pp29,(870,200))
        
        if mycharacter.hpnd == 0:
            if len(moslist) != 0:
                mospos = random.choice(moslist)
                moslist.remove(mospos)
                if mospos%16 == 0:
                    mm = (mospos/16)-1
                    nn = 16
                else:
                    mm = int(mospos/16)
                    nn = mospos%16
                moscolor = random.randint(1,3)
                moslistreal.append((mm,nn,moscolor))
                for mostup in moslistreal:
                    cc1,cc2,cc3 = mostup
                    if cc3 == 1:
                        pygame.draw.rect(sc,gray1,[(cc2-1)*80,cc1*80,80,80])
                    elif cc3 == 2:
                        pygame.draw.rect(sc,gray2,[(cc2-1)*80,cc1*80,80,80])
                    else:
                        pygame.draw.rect(sc,gray3,[(cc2-1)*80,cc1*80,80,80])
            else:
                for mostup in moslistreal:
                    cc1,cc2,cc3 = mostup
                    if cc3 == 1:
                        pygame.draw.rect(sc,gray1,[(cc2-1)*80,cc1*80,80,80])
                    elif cc3 == 2:
                        pygame.draw.rect(sc,gray2,[(cc2-1)*80,cc1*80,80,80])
                    else:
                        pygame.draw.rect(sc,gray3,[(cc2-1)*80,cc1*80,80,80])
                        
                if faillen6 != 200:
                    failword = pygame.font.SysFont("harrington",250)
                    if faillen1 != 200:
                        faillen1 += 20
                        ff1 = failword.render('F',1,blue)
                        sc.blit(ff1,(220,faillen1))
                        ff2 = failword.render('F',1,waterblue)
                        sc.blit(ff2,(200,faillen1))
                    else:
                        sc.blit(ff1,(220,200))
                        sc.blit(ff2,(200,200))
                    if faillen2 != 200:
                        if faillen1 >= -20:
                            faillen2 += 20
                        aa1 = failword.render('A',1,blue)
                        sc.blit(aa1,(368,faillen2))
                        aa2 = failword.render('A',1,waterblue)
                        sc.blit(aa2,(348,faillen2))
                    else:
                        sc.blit(aa1,(368,200))
                        sc.blit(aa2,(348,200))
                    if faillen3 != 200:
                        if faillen2 >= -20:
                            faillen3 += 20
                        ii1 = failword.render('I',1,blue)
                        sc.blit(ii1,(555,faillen3))
                        ii2 = failword.render('I',1,waterblue)
                        sc.blit(ii2,(535,faillen3))
                    else:
                        sc.blit(ii1,(555,200))
                        sc.blit(ii2,(535,200))
                    if faillen4 != 200:
                        if faillen3 >= -20:
                            faillen4 += 20
                        ll1 = failword.render('L',1,blue)
                        sc.blit(ll1,(621,faillen4))
                        ll2 = failword.render('L',1,waterblue)
                        sc.blit(ll2,(601,faillen4))
                    else:
                        sc.blit(ll1,(621,200))
                        sc.blit(ll2,(601,200))
                    if faillen5 != 200:
                        if faillen4 >= -20:
                            faillen5 += 20
                        ee1 = failword.render('E',1,blue)
                        sc.blit(ee1,(765,faillen5))
                        ee2 = failword.render('E',1,waterblue)
                        sc.blit(ee2,(745,faillen5))
                    else:
                        sc.blit(ee1,(765,200))
                        sc.blit(ee2,(745,200))
                    if faillen6 != 200:
                        if faillen5 >= -20:
                            faillen6 += 20
                        ss1 = failword.render('D',1,blue)
                        sc.blit(ss1,(934,faillen6))
                        ss2 = failword.render('D',1,waterblue)
                        sc.blit(ss2,(914,faillen6))
                    else:
                        sc.blit(ss1,(934,200))
                        sc.blit(ss2,(914,200))
                else:
                    failword1 = failword.render('FAILED',1,blue)
                    failword2 = failword.render('FAILED',1,waterblue)
                    sc.blit(failword1,(220,200))
                    sc.blit(failword2,(200,200))
                    if deadtime < 70:
                        deadtime += 1
                    else:
                        yesnocolor1 = 220
                        yesnocolor2 = 240
                        yesnocolor3 = 240
                        surecolor1 = 220
                        surecolor2 = 240
                        surecolor3 = 240
                        choosecolor1 = 220
                        choosecolor2 = 240
                        choosecolor3 = 240

                        faillen1 = -300
                        faillen2 = -300
                        faillen3 = -300
                        faillen4 = -300
                        faillen5 = -300
                        faillen6 = -300

                        suretime = 0
                        yesnotime = 0

                        pa = (0,0,0)
                        pb = (0,0,0)
                        pc = (0,0,0)
                        pd = (0,0,0)
                        pe = (0,0,0)
                        pf = (0,0,0)
                        pg = (0,0,0)
                        ph = (0,0,0)
                        pi = (0,0,0)
                        pj = (0,0,0)
                        pk = (0,0,0)
                        pl = (0,0,0)

                        changecolor1,changecolor2,changecolor3,changecolor4 = (0,0,0,0)
                        
                        k = kk
                        xr = xrr
                        yr = yrr
                        mapx = mapxx
                        mapy = mapyy
                        charface = charfacee
                            
                        mycharacter.HPs = mycharacterold.HPs
                        mycharacter.MPs = mycharacterold.MPs
                        mycharacter.STRs = mycharacterold.STRs
                        mycharacter.INTs = mycharacterold.INTs
                        mycharacter.DEXs = mycharacterold.DEXs
                        mycharacter.LUKs = mycharacterold.LUKs
                        mycharacter.LV = mycharacterold.LV
                        mycharacter.key = mycharacterold.key
                        mycharacter.remain = mycharacterold.remain
                        mycharacter.exp = mycharacterold.exp
                        mycharacter.expnd = mycharacterold.expnd
                        mycharacter.hpnd = mycharacterold.hpnd
                        mycharacter.mpnd = mycharacterold.mpnd
                        mycharacter.goldnd = mycharacterold.goldnd

                        for i in mapreturn:
                            aaa,bbb,ccc = i
                            name = 'map'+str(bbb)+'.txt'
                            with open(name,'r+b') as f:
                                f.seek(ccc)
                                if int(aaa) == 3:
                                    f.write(b'3')
                                elif int(aaa) == 5:
                                    f.write(b'5')
                                elif int(aaa) == 6:
                                    f.write(b'6')
                                elif int(aaa) == 7:
                                    f.write(b'7')
                                else:
                                    f.write(b'0')
                                f.flush
                                f.seek(0)
                        
                        deadtime = 0
                        linelen = 200
                        picpos = 325
                        menupos1 = 320
                        menupos2 = 440
                        menupos3 = 560
                        color1 = 179,153,255
                        createnew = 0
                        choosemenu = 0
                        newgame = 0

                        moslist = []
                        moslistreal = []
                        for j in range(1,145):
                            moslist.append(i)

        if healcount >= 100:
            if mycharacter.hpnd < mycharacter.HP or mycharacter.mpnd < mycharacter.MP:
                if mycharacter.hpnd < mycharacter.HP:
                    if healcount%30 == 0:
                        if (mycharacter.HP - mycharacter.hpnd) < (0.1*mycharacter.HP):
                            mycharacter.hpnd = mycharacter.HP
                        else:
                            mycharacter.hpnd += (int(0.1*mycharacter.HP))
                    else:
                        pass
                else:
                    pass
                if mycharacter.mpnd < mycharacter.MP:
                    if healcount%30 == 0:
                        if (mycharacter.MP - mycharacter.mpnd) < (0.1*mycharacter.MP):
                            mycharacter.mpnd = mycharacter.MP
                        else:
                            mycharacter.mpnd += (int(0.1*mycharacter.MP))
                    else:
                        pass
                else:
                    pass
            else:
                healcount = 0
        
        #posss1 = pygame.font.SysFont("simhei",30)
        #posss2 = posss1.render(str(pos[0])+','+str(pos[1]),1,blue)
        #sc.blit(posss2,(1100,700))
        
        gamenum1 = pygame.font.SysFont("simhei",30)
        gamenum2 = gamenum1.render(str(k),1,rose)
        sc.blit(gamenum2,(10,10))

        pygame.display.update()

        clock.tick(25)
    
    if createnew == 0 and qu == 0:
        if c1 <= pos[0] <= c1+a1 and d1 <= pos[1] <= d1+b1:
            q1,w1,e1 = pa
            color1 = 140,230,0
            sc.blit(pp1,(407,325))
            sc.blit(pp1,(815,325))
            if q1 == 1:
                createnew = 1
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
                if isset('mycharacter'):
                    abilitymenu = 0
                    checkmenu = 0
                    newgame = 1
                else:
                    pass
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
            ph = pygame.mouse.get_pressed()
            pi = pygame.mouse.get_pressed()
            pj = pygame.mouse.get_pressed()
            pk = pygame.mouse.get_pressed()
            pl = pygame.mouse.get_pressed()
    
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
                    for i in mapreturnreal:
                        aaa,bbb,ccc = i
                        name = 'map'+str(bbb)+'.txt'
                        with open(name,'r+b') as f:
                            f.seek(ccc)
                            if int(aaa) == 3:
                                f.write(b'3')
                            elif int(aaa) == 5:
                                f.write(b'5')
                            elif int(aaa) == 6:
                                f.write(b'6')
                            elif int(aaa) == 7:
                                f.write(b'7')
                            elif int(aaa) == 9:
                                f.write(b'9')
                            else:
                                f.write(b'0')
                            f.flush
                            f.seek(0)
                    
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
            
            att1 = pygame.font.SysFont("simhei",60)
            atte1 = att1.render('QUIT',1,maincolor1)
            sc.blit(atte1,(390,550))
            att2 = pygame.font.SysFont("simhei",60)
            atte2 = att2.render('RETURN',1,maincolor2)
            sc.blit(atte2,(780,550))
    
    if createnew == 0 and qu == 0:
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
                            pl = pygame.font.SysFont("simhei",50)
                            pll = pl.render(str(rr),1,blue)
                            sc.blit(pll,(625,350))

                        if m == 5:
                            aa = 6
                            bb = 6

                        x += z
                        y += w

                        pf = pygame.font.SysFont("simhei",40)
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
                            pl = pygame.font.SysFont("simhei",50)
                            pll = pl.render(str(rr),1,blue)
                            sc.blit(pll,(625,350))

                        if m == 5:
                            aa = 6
                            bb = 6

                        x += z
                        y += w

                        pf = pygame.font.SysFont("simhei",40)
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
    
    #posss1 = pygame.font.SysFont("simhei",30)
    #posss2 = posss1.render(str(pos[0])+','+str(pos[1]),1,blue)
    #sc.blit(posss2,(1100,700))    
    
    #sc.blit(tree,(100,300))
    pygame.display.update()                 
            
    clock.tick(50)
pygame.quit()