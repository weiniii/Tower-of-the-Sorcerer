import pygame
from pygame.locals import *
import random
import time
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
    pygame.draw.rect(sc,skyblue,(0,0,1280,720))
    for m in range(0,9):
        for n in range(0,16):
            if mat[m,n] == 1:
                sc.blit(pp1,(80*n,80*m))
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
            else:
                pass
    
def wall(mat,xr,yr,xk,yk,k,needbattle,fightcount,mapreturn,mapreturnreal):
    if mat[yr+yk,xr+xk] == 0:
        xr += xk
        yr += yk
    elif mat[yr+yk,xr+xk] == 2:
        mycharacter.create(k)
        xr += xk
        yr += yk
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
    elif mat[yr+yk,xr+xk] == 3:
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

def drawsquare(point):
    mylist = []
    pygame.draw.lines(sc,sblue,1,point,8)
    for i in point:
        x,y = i
        mylist.append((x-3,y-3,8,8))
    for j in mylist:
        pygame.draw.rect(sc,sblue,j)

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

dd1 = pygame.image.load('block.png')
pp1 = pygame.transform.scale(dd1,(80,80))

dd2 = pygame.image.load('information1.png')
pp2 = pygame.transform.scale(dd2,(60,60))

dd3 = pygame.image.load('information2.png')
pp3 = pygame.transform.scale(dd3,(60,60))

dd21 = pygame.image.load('drink.png')
pp21 = pygame.transform.scale(dd21,(60,60))

dd22 = pygame.image.load('door.png')
pp22 = pygame.transform.scale(dd22,(80,80))

dd23 = pygame.image.load('key.png')
pp23 = pygame.transform.scale(dd23,(60,60))

dd24 = pygame.image.load('coin.png')
pp24 = pygame.transform.scale(dd24,(60,60))

pygame.init()
size = [1280,720]
sc = pygame.display.set_mode(size,FULLSCREEN)
clock = pygame.time.Clock()

rose = 255,228,225
white = 255,255,255 
blue = 0,0,200
sblue = 77,128,230
waterblue = 0,255,255
lightblue = 0,191,255
shell = 255,245,238
green = 255,100,255
rectt = 230,195,92
numm = 71,152,179
skyblue = 224,255,255

#判別地圖
k = 1

#主角位置
xr = 1
yr = 1

#球位置
ballx = random.randint(50,1230)
bally = random.randint(50,670)

#判斷能力點選單
abilitycolor = 1

#球顏色
firstcolor = random.randint(1,6)
rr,gg,bb = color(firstcolor)

#球初始方向
move = random.randint(1,4)

#球半徑
circlelength = 16

abilitymenu = 0
checkmenu = 0
pos = (0,0)

xk = 0
yk = 0

sc.fill(white)
pygame.display.update()

done = False
while not done:
    
    sc.fill(white)
    keys = pygame.key.get_pressed()
    mods = pygame.key.get_mods()
    
    if k == 1:
        mat = getmat('map15.txt')
        drawmap(mat)
        xr,yr,k = switchmap(xr,yr,xk,yk,k,[0,0],[14,8])
    if k == 2:
        mat = getmat('map2.txt')
        drawmap(mat)
        xr,yr,k = switchmap(xr,yr,xk,yk,k,[14,0],[13,8])
        
    pygame.draw.rect(sc,green,(80*xr+20,80*yr+20,40,40))  
                
                
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
        
        ability1 = pygame.font.SysFont("Arial",50)
        ability2 = ability1.render('ABILITY',1,sblue)
        sc.blit(ability2,(80,80))
        ability3 = pygame.font.SysFont("Arial",50)
        ability4 = ability3.render('POINT',1,sblue)
        sc.blit(ability4,(100,140))
        
        pygame.draw.line(sc,sblue,(80,195),(270,195),5)
        
        yline = [258,315,372,429,486,543]
        for i in yline:
            pygame.draw.line(sc,shell,(80,i),(270,i),3)
        
        hp1 = pygame.font.SysFont("Arial",40)
        hp2 = hp1.render('HP',1,lightblue)
        sc.blit(hp2,(90,220))
        mp1 = pygame.font.SysFont("Arial",40)
        mp2 = mp1.render('MP',1,lightblue)
        sc.blit(mp2,(90,277))
        str1 = pygame.font.SysFont("Arial",40)
        str2 = str1.render('STR',1,lightblue)
        sc.blit(str2,(80,334))
        intt1 = pygame.font.SysFont("Arial",40)
        intt2 = intt1.render('INT',1,lightblue)
        sc.blit(intt2,(80,391))
        dex1 = pygame.font.SysFont("Arial",40)
        dex2 = dex1.render('DEX',1,lightblue)
        sc.blit(dex2,(80,448))
        luk1 = pygame.font.SysFont("Arial",40)
        luk2 = luk1.render('LUK',1,lightblue)
        sc.blit(luk2,(80,505))
        
        drawsquare([(880,50),(880,573),(1230,573),(1230,50)])
        status1 = pygame.font.SysFont("Arial",50)
        status2 = status1.render('STATUS',1,sblue)
        sc.blit(status2,(962,80))
        pygame.draw.line(sc,sblue,(915,135),(1200,135),5)
        
        yline = [193,243,293,343,393,443,493,543]
        for i in yline:
            pygame.draw.line(sc,shell,(915,i),(1200,i),3)
            
        slv1 = pygame.font.SysFont("Arial",40)
        slv2 = slv1.render('LV',1,lightblue)
        sc.blit(slv2,(925,155))
        sexp1 = pygame.font.SysFont("Arial",40)
        sexp2 = sexp1.render('EXP',1,lightblue)
        sc.blit(sexp2,(915,205))
        shp1 = pygame.font.SysFont("Arial",40)
        shp2 = shp1.render('HP',1,lightblue)
        sc.blit(shp2,(925,255))
        smp1 = pygame.font.SysFont("Arial",40)
        smp2 = smp1.render('MP',1,lightblue)
        sc.blit(smp2,(925,305))
        sstr1 = pygame.font.SysFont("Arial",40)
        sstr2 = sstr1.render('STR',1,lightblue)
        sc.blit(sstr2,(915,355))
        sintt1 = pygame.font.SysFont("Arial",40)
        sintt2 = sintt1.render('INT',1,lightblue)
        sc.blit(sintt2,(915,405))
        sdex1 = pygame.font.SysFont("Arial",40)
        sdex2 = sdex1.render('DEX',1,lightblue)
        sc.blit(sdex2,(915,455))
        sluk1 = pygame.font.SysFont("Arial",40)
        sluk2 = sluk1.render('LUK',1,lightblue)
        sc.blit(sluk2,(915,505))
        
        drawsquare([(350,50),(350,573),(745,573),(745,50)])
        contral1 = pygame.font.SysFont("Arial",50)
        contral2 = contral1.render('CONTRAL',1,sblue)
        sc.blit(contral2,(440,80))
        
        pygame.draw.line(sc,sblue,(380,135),(715,135),5)
        
        if abilitymenu%2 == 0:
            yline = [193,243,293,343,393,443,493,543]
            for i in yline:
                pygame.draw.line(sc,shell,(380,i),(715,i),3)

            up1 = pygame.font.SysFont("Arial",40)
            up2 = up1.render('UP',1,lightblue)
            sc.blit(up2,(385,155))
            down1 = pygame.font.SysFont("Arial",40)
            down2 = down1.render('DOWN',1,lightblue)
            sc.blit(down2,(380,205))
            right1 = pygame.font.SysFont("Arial",40)
            right2 = right1.render('RIGHT',1,lightblue)
            sc.blit(right2,(380,255))
            left1 = pygame.font.SysFont("Arial",40)
            left2 = left1.render('LEFT',1,lightblue)
            sc.blit(left2,(380,305))
            heal1 = pygame.font.SysFont("Arial",40)
            heal2 = heal1.render('HEAL',1,lightblue)
            sc.blit(heal2,(380,355))
            item1 = pygame.font.SysFont("Arial",40)
            item2 = item1.render('ITEM',1,lightblue)
            sc.blit(item2,(380,405))
            save1 = pygame.font.SysFont("Arial",40)
            save2 = save1.render('SAVE',1,lightblue)
            sc.blit(save2,(380,455))
            menu1 = pygame.font.SysFont("Arial",40)
            menu2 = menu1.render('MENU',1,lightblue)
            sc.blit(menu2,(380,505))

            cup1 = pygame.font.SysFont("Arial",40)
            cup2 = cup1.render('W',1,numm)
            sc.blit(cup2,(600,155))
            cdown1 = pygame.font.SysFont("Arial",40)
            cdown2 = cdown1.render('S',1,numm)
            sc.blit(cdown2,(605,205))
            cright1 = pygame.font.SysFont("Arial",40)
            cright2 = cright1.render('D',1,numm)
            sc.blit(cright2,(605,255))
            cleft1 = pygame.font.SysFont("Arial",40)
            cleft2 = cleft1.render('A',1,numm)
            sc.blit(cleft2,(605,305))
            cheal1 = pygame.font.SysFont("Arial",40)
            cheal2 = cheal1.render('Q',1,numm)
            sc.blit(cheal2,(605,355)) 
            citem1 = pygame.font.SysFont("Arial",40)
            citem2 = citem1.render('G',1,numm)
            sc.blit(citem2,(605,405))
            csave1 = pygame.font.SysFont("Arial",40)
            csave2 = csave1.render('ALT+B',1,numm)
            sc.blit(csave2,(555,455))
            cmenu1 = pygame.font.SysFont("Arial",40)
            cmenu2 = menu1.render('CTRL+Z',1,numm)
            sc.blit(cmenu2,(545,505))
            
            manage1 = pygame.font.SysFont("Arial",23)
            manage2 = manage1.render('Press [P] to Manage',1,blue)
            sc.blit(manage2,(58,590))
        
    if abilitymenu%2 == 1:
        if abilitycolor%6 == 1:
            ahp1 = pygame.font.SysFont("Arial",40)
            ahp2 = ahp1.render('HP',1,waterblue)
            sc.blit(ahp2,(90,220))
        elif abilitycolor%6 == 2:
            amp1 = pygame.font.SysFont("Arial",40)
            amp2 = amp1.render('MP',1,waterblue)
            sc.blit(amp2,(90,277))
        elif abilitycolor%6 == 3:
            astr1 = pygame.font.SysFont("Arial",40)
            astr2 = astr1.render('STR',1,waterblue)
            sc.blit(astr2,(80,334))
        elif abilitycolor%6 == 4:
            aintt1 = pygame.font.SysFont("Arial",40)
            aintt2 = aintt1.render('INT',1,waterblue)
            sc.blit(aintt2,(80,391))
        elif abilitycolor%6 == 5:
            adex1 = pygame.font.SysFont("Arial",40)
            adex2 = adex1.render('DEX',1,waterblue)
            sc.blit(adex2,(80,448))
        elif abilitycolor%6 == 0:
            aluk1 = pygame.font.SysFont("Arial",40)
            aluk2 = aluk1.render('LUK',1,waterblue)
            sc.blit(aluk2,(80,505))
            
        yline = [193,243,293,343,443,493,543]
        for i in yline:
            pygame.draw.line(sc,shell,(380,i),(715,i),3)

        up1 = pygame.font.SysFont("Arial",40)
        up2 = up1.render('UP',1,lightblue)
        sc.blit(up2,(385,155))
        down1 = pygame.font.SysFont("Arial",40)
        down2 = down1.render('DOWN',1,lightblue)
        sc.blit(down2,(380,205))
        right1 = pygame.font.SysFont("Arial",40)
        right2 = right1.render('PLUS',1,lightblue)
        sc.blit(right2,(380,255))
        left1 = pygame.font.SysFont("Arial",40)
        left2 = left1.render('MINUS',1,lightblue)
        sc.blit(left2,(380,305))
        heal1 = pygame.font.SysFont("Arial",40)
        heal2 = heal1.render('POINT',1,lightblue)
        sc.blit(heal2,(380,360))
        item1 = pygame.font.SysFont("Arial",40)
        item2 = item1.render('REMAIN',1,lightblue)
        sc.blit(item2,(380,405))
        save1 = pygame.font.SysFont("Arial",40)
        save2 = save1.render('SAVE',1,lightblue)
        sc.blit(save2,(380,455))
        menu1 = pygame.font.SysFont("Arial",40)
        menu2 = menu1.render('CANCEL',1,lightblue)
        sc.blit(menu2,(380,505))

        cup1 = pygame.font.SysFont("Arial",40)
        cup2 = cup1.render('W',1,numm)
        sc.blit(cup2,(600,155))
        cdown1 = pygame.font.SysFont("Arial",40)
        cdown2 = cdown1.render('S',1,numm)
        sc.blit(cdown2,(605,205))
        cright1 = pygame.font.SysFont("Arial",40)
        cright2 = cright1.render('D',1,numm)
        sc.blit(cright2,(605,255))
        cleft1 = pygame.font.SysFont("Arial",40)
        cleft2 = cleft1.render('A',1,numm)
        sc.blit(cleft2,(605,305))
        csave1 = pygame.font.SysFont("Arial",40)
        csave2 = csave1.render('CTRL+P',1,numm)
        sc.blit(csave2,(545,455))
        cmenu1 = pygame.font.SysFont("Arial",40)
        cmenu2 = menu1.render('P',1,numm)
        sc.blit(cmenu2,(605,505)) 
                    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if checkmenu%2 == 1:
                if abilitymenu%2 == 0:
                    if event.key == K_z and mods & pygame.KMOD_LCTRL:
                        done = True
                    if event.key == K_b and mods & pygame.KMOD_LALT:
                        pass
                    if event.key == K_g:
                        pass
                if event.key == K_p:
                    abilitycolor = 1
                    abilitymenu += 1
            if abilitymenu%2 == 0:
                if event.key == K_m:
                    checkmenu += 1
                    firstcolor = random.randint(1,6)
                    rr,gg,bb = color(firstcolor)
                    move = random.randint(1,4)
                    ballx = random.randint(50,1230)
                    bally = random.randint(50,670)
            if checkmenu%2 == 0:
                if event.key == K_d:
                    xk = 1
                    yk = 0
                    if xr+xk > 15:
                        pass
                    else:
                        xr,yr = wall(mat,xr,yr,xk,yk)
                        xk = 0
                        yk = 0

                if event.key == K_a:
                    xk = -1
                    yk = 0
                    if xr+xk < 0:
                        pass
                    else:
                        xr,yr = wall(mat,xr,yr,xk,yk)
                        xk = 0
                        yk = 0

                if event.key == K_s:
                    xk = 0
                    yk = 1
                    if yr+yk > 8:
                        pass
                    else:
                        xr,yr = wall(mat,xr,yr,xk,yk)
                        xk = 0
                        yk = 0

                if event.key == K_w:
                    xk = 0
                    yk = -1
                    if yr+yk < 0:
                        pass
                    else:
                        xr,yr = wall(mat,xr,yr,xk,yk)
                        xk = 0
                        yk = 0
            if abilitymenu%2 == 1:
                if event.key == K_w:
                    abilitycolor -= 1
                if event.key == K_s:
                    abilitycolor += 1
                if event.key == K_a:
                    pass
                if event.key == K_d:
                    pass
                if event.key == K_p and mods & pygame.KMOD_LCTRL:
                    pass
        if event.type == MOUSEMOTION:
                pos = pygame.mouse.get_pos()     
        if event.type ==  MOUSEBUTTONDOWN:
            pass

    posss1 = pygame.font.SysFont("Arial",30)
    posss2 = posss1.render(str(pos[0])+','+str(pos[1]),1,blue)
                
    gamenum1 = pygame.font.SysFont("Arial",30)
    gamenum2 = gamenum1.render(str(k),1,rose)
    sc.blit(gamenum2,(10,10))
                
    sc.blit(posss2,(1100,700)) 
    pygame.display.update()
            
    clock.tick(70)
pygame.quit()