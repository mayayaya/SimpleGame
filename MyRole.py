# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 21:36:11 2023

@author: USER
"""
import random

class Warrior: #戰士
    
    def __init__(self,name,hp=120,EnergyBar=0):
        self.__name = name
        self.__hp = hp
        self.__EnergyBar = EnergyBar
        
    def setHp(self,hp):
        if hp > 120:
            self.__hp = 120
        else:
            self.__hp = hp
        
    def setEnergyBar(self,EnergyBar):
        self.__EnergyBar = EnergyBar
        
    def getName(self):
        return self.__name
    
    def getHp(self):
        return self.__hp
    
    def getEnergyBar(self):
        return self.__EnergyBar
    
    
    def fight(self):
        boold = random.randint(6, 10)
        print(f"斬擊 單體傷害{boold}")
        return boold
        
    def skill(self):
        boold = random.randint(20, 25)
        print(f"水平四方斬 單體傷害{boold}")
        return boold
    
    def talent(self):
        print("護甲")
    
class Wizard: #法師
    
    def __init__(self,name,hp=80,EnergyBar=0):
        self.__name = name
        self.__hp = hp
        self.__EnergyBar = EnergyBar
        
    def setHp(self,hp):
        if hp > 80:
            self.__hp = 80
        else:
            self.__hp = hp
        
    def setEnergyBar(self,EnergyBar):
        self.__EnergyBar = EnergyBar
        
    def getName(self):
        return self.__name
    
    def getHp(self):
        return self.__hp
    
    def getEnergyBar(self):
        return self.__EnergyBar
    
    
    def fight(self):
        boold = random.randint(3, 5)
        print(f"火苗 群體傷害{boold}")
        return boold
        
    def skill(self):
        boold = random.randint(15, 20)
        print(f"火焰流星 群體傷害{boold}")
        return boold
    
    def talent(self):
        print("反彈")
     
class Assassin: #刺客
    
    def __init__(self,name,hp=100,EnergyBar=0):
        self.__name = name
        self.__hp = hp
        self.__EnergyBar = EnergyBar
        
    def setHp(self,hp):
        if hp > 100:
            self.__hp = 100
        else:
            self.__hp = hp
        
    def setEnergyBar(self,EnergyBar):
        self.__EnergyBar = EnergyBar
        
    def getName(self):
        return self.__name
    
    def getHp(self):
        return self.__hp
    
    def getEnergyBar(self):
        return self.__EnergyBar
    
    
    def fight(self, talent=1):
        boold = random.randint(4, 6)*talent
        print(f"突刺 單體傷害{boold}")
        return boold
        
    def skill(self):
        boold = random.randint(23, 27)
        print(f"暗影追擊 單體傷害{boold}")
        return boold
        
    def talent(self):
        print("生命值小於10 觸發 普攻增傷1.5倍")
      
class Cleric: #牧師
    
    def __init__(self,name,hp=140,EnergyBar=0):
        self.__name = name
        self.__hp = hp
        self.__EnergyBar = EnergyBar
        
    def setHp(self,hp):
        if hp > 140:
            self.__hp = 140
        else:
            self.__hp = hp
        
    def setEnergyBar(self,EnergyBar):
        self.__EnergyBar = EnergyBar
        
    def getName(self):
        return self.__name
    
    def getHp(self):
        return self.__hp
    
    def getEnergyBar(self):
        return self.__EnergyBar
    
    
    def fight(self):
        boold = random.randint(1, 3)
        print(f"杖擊 群傷{boold}")
        return boold
        
    def skill(self):
        boold = random.randint(8, 12)
        print(f"大天使的氣息 全體回血{boold}")
        return boold
        
    def talent(self):
        print(f"血量小於5 觸發 恩賜再臨 回升10血量至{self.getHp()}")
        
class Bard: #吟遊詩人
    
    def __init__(self,name,hp=90,EnergyBar=0):
        self.__name = name
        self.__hp = hp
        self.__EnergyBar = EnergyBar
        
    def setHp(self,hp):
        if hp > 90:
            self.__hp = 90
        else:
            self.__hp = hp
        
    def setEnergyBar(self,EnergyBar):
        self.__EnergyBar = EnergyBar
        
    def getName(self):
        return self.__name
    
    def getHp(self):
        return self.__hp
    
    def getEnergyBar(self):
        return self.__EnergyBar
    
    
    def fight(self):
        boold = random.randint(2, 4)
        print(f"雜響 群傷{boold}")
        return boold
        
    def skill(self):
        boold = random.randint(10, 15)
        print(f"古曲幽蘭靜 隨機回補一名血量{boold}")
        return boold
        
    def talent(self):
        print("第九樂章")
    
    
    
    