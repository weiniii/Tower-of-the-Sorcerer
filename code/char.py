class character:
    
    #角色各能力初始值
    def __init__(self):
        self.name=''
        #能力點
        self.key=0
        self.remain=0
        self.HPs=0
        self.MPs=0
        self.STRs=0
        self.INTs=0
        self.DEXs=0
        self.LUKs=0
        #實際值
        self.LV=1
        self.HP=0
        self.MP=0
        self.STR=0
        self.miss=0
        #升級所需exp
        self.exp=0
        #現有exp
        self.expnd=0
        #現有hp、mp、gold
        self.hpnd=0
        self.mpnd=0
        self.goldnd=0
        #monster
        self.namemon=''
        self.LVmon=0
        self.expmon=0
        self.goldmon=0
        self.STRmon=0
        self.DEXmon=0
        self.HPmon=0
        self.HPmonnd=0
        self.missmon=0
    #create monster
    def create(self,k):
        self.namemon='monster'
        
        import random
        #self.LVmon=random.randrange(1,30)
        #s=self.LVmon-1
        if k <= 10:
            self.LVmon=random.randint(2*k-1,2*k)
        elif k == 11:
            self.LVmon=random.randint(21,23)
        elif k == 12:
            self.LVmon=random.randint(24,26)
        else:
            self.LVmon=random.randint(27,30)
            
        s=self.LVmon-1
        
        #怪物經驗值
        exps=[133,156,185,219,256,297,341,389,440,493,542,641,756,892,977,1061,1145,1237,1336,1443,1558,1683,1818,1874,1932,1989,2049,2111,2174,2239]
        self.expmon=exps[s]  
        
        #怪物黃金
        golda=[6,7,9,12,16,21,26,32,39,46,54,62,71,80,89,98,107,117,127,137,147,157,167,177,187,197,207,217,227,237]        
        goldb=[8,9,11,15,20,25,30,36,42,49,57,65,74,83,92,101,110,120,130,140,150,160,170,180,190,200,210,220,230,240]
        a=golda[s]
        b=goldb[s]
        self.goldmon=random.randint(a,b)

        #怪物HP
        HPa=[748,816,1014,1320,1568,1944,2242,2688,3036,3404,3700,3848,4144,4585,5040,5518,6204,6732,7488,8066,8284,8502,8720,8938,9156,9374,9812,10260,10718,11186]        
        HPb=[803,876,1079,1395,1648,2034,2337,2793,3146,3519,3825,3978,4284,4727,5190,5673,6369,6902,7668,8251,8474,8697,8920,9143,9366,9589,10032,10485,10948,11421]
        aa=HPa[s]
        bb=HPb[s]
        self.HPmon=random.randint(aa,bb)
        self.HPmonnd = self.HPmon
        
        dexs=[3,3,4,4,5,5,6,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,14,14,14,15,15,16,17,18]
        self.DEXmon=dexs[s]
        
        misss=[1,2,3,4,5,7,8,9,10,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,33,35]
        self.missmon=misss[s]

        #怪物STR
        STRa=[25,29,38,42,46,54,58,63,67,75,79,88,92,96,104,108,117,121,125,129,133,138,142,146,150,154,158,163,167,171]
        STRb=[30,35,45,50,55,65,70,75,80,90,95,105,110,115,125,130,140,145,150,155,160,165,170,175,180,185,190,195,200,205]
        aaa=STRa[s]
        bbb=STRb[s]
        self.STRmon=random.randint(aaa,bbb)  
                
    #目前能力值
    def status(self):    
        self.HP=100*self.HPs+100
        self.MP=(self.MPs-3)*30
        self.STR=10*self.STRs+40
        self.INT=10*self.INTs+40
        if self.LUKs<=40:
            self.miss=self.LUKs
        else:
            self.miss=40
        
    #PK-class
    def levelup(self):
      #level up
        if self.expnd>=self.exp:
            self.expnd-=self.exp
            self.LV+=1
            self.remain+=3
            self.hpnd=self.HP
            self.mpnd=self.MP
            #update exp of level up
            a=[2000,2400,2880,3460,4150,4980,5970,7160,8600,10310,12380,14860,17830,21400,23540,25900,28480,31330,34460,37910,41700,45870,50460,52480,54580,56760,59030,61390,63850]
            b=self.LV-1
            self.exp=a[b]
        else:
            pass 
        
    def desc(self):
        return "Name:{0} LV:{1} HP:{2} STR:{3} Gold:{4} exp:{5}\nName:{6} LV:{7} HP:{8} STR:{9} exp:{10}/{11} Gold:{12}".format(self.namemon,self.LVmon,self.HPmon,self.STRmon,self.goldmon,self.expmon,self.name,self.LV,self.hpnd,self.STR,self.expnd,self.exp,self.goldnd)
        
#戰士        
class warrior(character):   
    def __init__(self):
        self.name='warrior'
        self.key=0
        self.remain=0
        self.HPs=8
        self.MPs=4
        self.STRs=10
        self.INTs=2
        self.DEXs=4
        self.LUKs=2
        self.LV=1
        self.HP=900
        self.MP=0
        self.STR=120
        self.INT = 0
        self.miss=0
        self.exp=2000
        self.expnd=0
        self.hpnd=900
        self.mpnd=30
        self.goldnd=0
        
#法師        
class magician(character):    
    def __init__(self):
        self.name='magician'
        self.key=0
        self.remain=0
        self.HPs=6
        self.MPs=9
        self.STRs=2
        self.INTs=7
        self.DEXs=4
        self.LUKs=2
        self.LV=1
        self.HP=700
        self.MP=0
        self.STR=60
        self.INT = 0
        self.miss=0
        self.exp=2000
        self.expnd=0
        self.hpnd=700
        self.mpnd=180
        self.goldnd=0  
        
#忍者
class ninja(character):    
    def __init__(self):
        self.name='ninja'
        self.key=0
        self.remain=0
        self.HPs=6
        self.MPs=5
        self.STRs=7
        self.INTs=2
        self.DEXs=3
        self.LUKs=7
        self.LV=1
        self.HP=800
        self.MP=0
        self.STR=110
        self.INT = 0
        self.miss=0
        self.exp=2000
        self.expnd=0
        self.hpnd=700
        self.mpnd=60
        self.goldnd=0  
        
#射手        
class archer(character):    
    def __init__(self):
        self.name='archer'
        self.key=0
        self.remain=0
        self.HPs=7
        self.MPs=6
        self.STRs=7
        self.INTs=2
        self.DEXs=6
        self.LUKs=2
        self.LV=1
        self.HP=800
        self.MP=0
        self.STR=110
        self.INT = 0
        self.miss=0
        self.exp=2000
        self.expnd=0
        self.hpnd=800
        self.mpnd=90
        self.goldnd=0
    