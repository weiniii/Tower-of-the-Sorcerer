import pygame
from pygame.locals import *
import time

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

dd13 = pygame.image.load('warrior.png')
pp13 = pygame.transform.scale(dd13,(150,150))

dd14 = pygame.image.load('archer.png')
pp14 = pygame.transform.scale(dd14,(150,150))

dd15 = pygame.image.load('magician.png')
pp15 = pygame.transform.scale(dd15,(150,150))

dd16 = pygame.image.load('ninja.png')
pp16 = pygame.transform.scale(dd16,(150,150))

dd17 = pygame.image.load('warrior2.png')
pp17 = pygame.transform.scale(dd17,(150,150))

dd18 = pygame.image.load('archer2.png')
pp18 = pygame.transform.scale(dd18,(150,150))

dd19 = pygame.image.load('magician2.png')
pp19 = pygame.transform.scale(dd19,(150,150))

dd20 = pygame.image.load('ninja2.png')
pp20 = pygame.transform.scale(dd20,(150,150))

#tree = pygame.image.load('tree.png')

bacc = 220,238,238
white = 255,255,255 
blue = 0,0,200
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

#判斷Quit按鍵
qu = 0

#判斷顏色
suretime = 0
yesnotime = 0
choosetime = 0

#判斷新遊戲
createnew = 0

#判斷選角選單
choosemenu = 0

#選角確認按鈕
advenbutton = 0

#選角選單橫線長度
linelen = 200

#關於欄伸縮的Y座標及Y長度
yp = 644
yl = 46

#判斷關於伸縮欄長度
yyqu = 0

#按下QUIT鍵後的位置
ypos1 = 560
ypos2 = 565

picpos = 325
menupos1 = 320
menupos2 = 440
menupos3 = 560

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
    
    mainmenu1 = pygame.font.SysFont("Arial",130)
    mainmenu2 = mainmenu1.render('Main Menu',1,maincolor)
    sc.blit(mainmenu2,(300,132))
    
    p1 = pygame.font.SysFont("Arial",95)
    p11 = p1.render('New Game',1,color1)
    sc.blit(p11,(467,menupos1))
    
    p2 = pygame.font.SysFont("Arial",95)
    p22 = p2.render('Continue',1,color2)
    sc.blit(p22,(490,menupos2))
    
    p3 = pygame.font.SysFont("Arial",95)
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
            areyousure1 = pygame.font.SysFont("Arial",85)
            areyousure2 = areyousure1.render('Are you sure ?',1,(surecolor1,surecolor2,surecolor3))
            sc.blit(areyousure2,(320,340))
            sureyes1 = pygame.font.SysFont("Arial",70)
            sureyes2 = sureyes1.render('Yes',1,(yesnocolor1,yesnocolor2,yesnocolor3))
            sc.blit(sureyes2,(410,500))
            sureno1 = pygame.font.SysFont("Arial",70)
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
                        csureyes1 = pygame.font.SysFont("Arial",70)
                        csureyes2 = csureyes1.render('Yes',1,(140,230,0))
                        sc.blit(csureyes2,(410,500))
                        if q6 == 1:
                            #按鈕動作
                            choosemenu = 1
                            pf = (0,0,0)
                        else:
                            pass
                    else:
                        pf = (0,0,0)
                        
                    if 803 <= pos[0] <= 890 and 504 <= pos[1] <= 550:
                        q7,w7,e7 = pg
                        csureno1 = pygame.font.SysFont("Arial",70)
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
        choose1 = pygame.font.SysFont("Arial",70)
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
                linelen += 5
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
                    ph = (0,0,0)
                    charcolor1 = 25,25,25
                    
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
                    pi = (0,0,0)
                    charcolor2 = 25,25,25
                    
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
                    pj = (0,0,0)
                    charcolor3 = 25,25,25
                    
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
                    pk = (0,0,0)
                    charcolor4 = 25,25,25
                
                warrior1 = pygame.font.SysFont("Arial",40)
                warrior2 = warrior1.render('warrior',1,charcolor1)
                sc.blit(warrior2,(180,470))
                archer1 = pygame.font.SysFont("Arial",40)
                archer2 = archer1.render('archer',1,charcolor2)
                sc.blit(archer2,(453,470))
                magician1 = pygame.font.SysFont("Arial",40)
                magician2 = magician1.render('magician',1,charcolor3)
                sc.blit(magician2,(681,470))
                ninja1 = pygame.font.SysFont("Arial",40)
                ninja2 = ninja1.render('ninja',1,charcolor4)
                sc.blit(ninja2,(964,470))
        
        if advenbutton != 0:
            adventure1 = pygame.font.SysFont("Arial",50)
            adventure2 = adventure1.render('adventure',1,maincolor)
            sc.blit(adventure2,(500,600))
            
            if 485 <= pos[0] <= 797 and 590 <= pos[1] <= 650:
                    q11,w11,e11 = pl
                    if q11 == 1:
                        #按鈕動作
                        pl = (0,0,0)
                else:
                    pl = (0,0,0)
            
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
                warrior2 = warrior1.render('warrior',1,(140,230,0))
                sc.blit(warrior2,(180,470))
            elif advenbutton == 2:
                sc.blit(pp18,(443,300))
                archer2 = archer1.render('archer',1,(140,230,0))
                sc.blit(archer2,(453,470))
            elif advenbutton == 3:
                sc.blit(pp19,(686,300))
                magician2 = magician1.render('magician',1,(140,230,0))
                sc.blit(magician2,(681,470))
            elif advenbutton == 4:
                sc.blit(pp20,(929,300))
                ninja2 = ninja1.render('ninja',1,(140,230,0))
                sc.blit(ninja2,(964,470))
            
    if createnew == 0 and qu == 0:
        if c1 <= pos[0] <= c1+a1 and d1 <= pos[1] <= d1+b1:
            q1,w1,e1 = pa
            color1 = 140,230,0
            sc.blit(pp1,(407,325))
            sc.blit(pp1,(815,325))
            if q1 == 1:
                #按鈕動作
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