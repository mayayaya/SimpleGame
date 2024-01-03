# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:06:46 2023

@author: USER
"""

from MyRole import Warrior,Wizard,Assassin,Cleric,Bard
import random

if __name__=="__main__":
    player = list()
    com = list()

    for i in range(3):

        p = int(input("劍士(1)/法師(2)/刺客(3)/牧師(4)/吟遊詩人(5), 選擇："))
        name = input("輸入角色姓名：")

        if p == 1:
            player.append(Warrior(name))
        elif p == 2:
            player.append(Wizard(name))
        elif p == 3:
            player.append(Assassin(name))
        elif p == 4:
            player.append(Cleric(name))
        elif p == 5:
            player.append(Bard(name))

    # print(player)

    # 電腦

    name = ["紅茶", "綠茶", "烏龍茶", "金萱", "煎茶", "焙茶"]
    name = random.sample(name, 3)
    c_player = list(range(1, 6))
    c_player = random.sample(c_player, 3)

    for i in range(3):
        # random.choice(name) 從串列中隨機抓取一個項目值
        if c_player[i] == 1:
            com.append(Warrior(name[i]))
        elif c_player[i] == 2:
            com.append(Wizard(name[i]))
        elif c_player[i] == 3:
            com.append(Assassin(name[i]))
        elif c_player[i] == 4:
            com.append(Cleric(name[i]))
        elif c_player[i] == 5:
            com.append(Bard(name[i]))

    # print(com)
    # print(type(com[0]))
    # print(isinstance(com[0], Bard))

    playerDie=0
    comDie=0
    playerNo=0
    comNo=0
    Round=1
    print("-"*30)
    while len(player) > 0 and len(com) > 0 and Round<=200:
        print(f"第{Round}回合")
        n = random.randint(1,100)
        if n % 2 == 0: # player 攻
            No = playerNo % len(player)
            P = player[No]
            C = random.choice(com)
            print(f"玩家{P.getName()} 發起攻擊！")
            if isinstance(P, Warrior):
                if P.getEnergyBar() == 5:
                    blood = P.skill()
                    P.setEnergyBar(0)
                else:
                    blood = P.fight()
                    P.setEnergyBar(P.getEnergyBar()+1)
                C.setHp(C.getHp()-blood)
                if C.getHp() <= 0:
                    com.pop(com.index(C))
                    print(f"電腦{C.getName()} 陣亡")
                else:
                    print(f"電腦{C.getName()} 遭受攻擊 血量剩餘{C.getHp()}")
                    if isinstance(C, Cleric) and C.getHp()<5:
                        C.setHp(C.getHp()+10)
                        C.talent()
            elif isinstance(P, Wizard):
                if P.getEnergyBar() == 4:
                    blood = P.skill()
                    P.setEnergyBar(0)
                else:
                    blood = P.fight()
                    P.setEnergyBar(P.getEnergyBar()+1)
                for c in list(reversed(com)):
                    c.setHp(c.getHp()-blood)
                    if c.getHp() <= 0:
                        com.pop(com.index(c))
                        print(f"電腦{c.getName()} 陣亡")
                    else:
                        print(f"電腦{c.getName()} 遭受攻擊 血量剩餘{c.getHp()}")
                        if isinstance(c, Cleric) and c.getHp()<5:
                            c.setHp(c.getHp()+10)
                            c.talent()

            elif isinstance(P, Assassin):
                if P.getEnergyBar() == 6:
                    blood = P.skill()
                    P.setEnergyBar(0)
                else:
                    if P.getHp()<10:
                        P.talent()
                        blood = P.fight(1.5)
                        P.setEnergyBar(P.getEnergyBar()+1)
                    else:
                        blood = P.fight()
                        P.setEnergyBar(P.getEnergyBar()+1)
                C.setHp(C.getHp()-blood)
                if C.getHp() <= 0:
                    com.pop(com.index(C))
                    print(f"電腦{C.getName()} 陣亡")
                else:
                    print(f"電腦{C.getName()} 遭受攻擊 血量剩餘{C.getHp()}")
                    if isinstance(C, Cleric) and C.getHp()<5:
                        C.setHp(C.getHp()+10)
                        C.talent()

            elif isinstance(P, Cleric):
                if P.getEnergyBar() == 4:
                    blood = P.skill()
                    P.setEnergyBar(0)
                    for p in player:
                        p.setHp(p.getHp()+blood)
                        print(f"玩家{p.getName()} 血量回升{p.getHp()}")
                else:
                    blood = P.fight()
                    P.setEnergyBar(P.getEnergyBar()+1)
                    for c in list(reversed(com)):
                        c.setHp(c.getHp()-blood)
                        if c.getHp() <= 0:
                            com.pop(com.index(c))
                            print(f"電腦{c.getName()} 陣亡")
                        else:
                            print(f"電腦{c.getName()} 遭受攻擊 血量剩餘{c.getHp()}")
                            if isinstance(c, Cleric) and c.getHp()<5:
                                c.setHp(c.getHp()+10)
                                c.talent()

            else:
                if P.getEnergyBar() == 6:
                    blood = P.skill()
                    P.setEnergyBar(0)
                    p = random.choice(player)
                    p.setHp(p.getHp()+blood)
                    print(f"玩家{p.getName()} 血量回升{p.getHp()}")
                else:
                    blood = P.fight()
                    P.setEnergyBar(P.getEnergyBar()+1)
                    for c in list(reversed(com)):
                        c.setHp(c.getHp()-blood)
                        if c.getHp() <= 0:
                            com.pop(com.index(c))
                            print(f"電腦{c.getName()} 陣亡")
                        else:
                            print(f"電腦{c.getName()} 遭受攻擊 血量剩餘{c.getHp()}")
                            if isinstance(c, Cleric) and c.getHp()<5:
                                c.setHp(c.getHp()+10)
                                c.talent()

            playerNo = playerNo + 1

        else: # com 攻
            No = comNo % len(com)
            C = com[No]
            P = random.choice(player)
            print(f"電腦{C.getName()} 發起攻擊！")
            if isinstance(C, Warrior):
                if C.getEnergyBar() == 5:
                    blood = C.skill()
                    C.setEnergyBar(0)
                else:
                    blood = C.fight()
                    C.setEnergyBar(C.getEnergyBar()+1)
                P.setHp(P.getHp()-blood)
                if P.getHp() <= 0:
                    player.pop(player.index(P))
                    print(f"玩家{P.getName()} 陣亡")
                else:
                    print(f"玩家{P.getName()} 遭受攻擊 血量剩餘{P.getHp()}")
                    if isinstance(P, Cleric) and P.getHp()<5:
                        P.setHp(P.getHp()+10)
                        P.talent()
            elif isinstance(C, Wizard):
                if C.getEnergyBar() == 4:
                    blood = C.skill()
                    C.setEnergyBar(0)
                else:
                    blood = C.fight()
                    C.setEnergyBar(C.getEnergyBar()+1)
                for p in list(reversed(player)):
                    p.setHp(p.getHp()-blood)
                    if p.getHp() <= 0:
                        print(f"玩家{p.getName()} 陣亡")
                        player.pop(player.index(p))
                    else:
                        print(f"玩家{p.getName()} 遭受攻擊 血量剩餘{p.getHp()}")
                        if isinstance(p, Cleric) and p.getHp()<5:
                            p.setHp(p.getHp()+10)
                            p.talent()

            elif isinstance(C, Assassin):
                if C.getEnergyBar() == 6:
                    blood = C.skill()
                    C.setEnergyBar(0)
                else:
                    if C.getHp()<10:
                        C.talent()
                        blood = C.fight(1.5)
                        C.setEnergyBar(C.getEnergyBar()+1)
                    else:
                        blood = C.fight()
                        C.setEnergyBar(C.getEnergyBar()+1)
                P.setHp(P.getHp()-blood)
                if P.getHp() <= 0:
                    player.pop(player.index(P))
                    print(f"玩家{P.getName()} 陣亡")
                else:
                    print(f"玩家{P.getName()} 遭受攻擊 血量剩餘{P.getHp()}")
                    if isinstance(P, Cleric) and P.getHp()<5:
                        P.setHp(P.getHp()+10)
                        P.talent()

            elif isinstance(C, Cleric):
                if C.getEnergyBar() == 4:
                    blood = C.skill()
                    C.setEnergyBar(0)
                    for c in com:
                        c.setHp(c.getHp()+blood)
                        print(f"電腦{c.getName()} 血量回升{c.getHp()}")
                else:
                    blood = C.fight()
                    C.setEnergyBar(C.getEnergyBar()+1)
                    for p in list(reversed(player)):
                        p.setHp(p.getHp()-blood)
                        if p.getHp() <= 0:
                            player.pop(player.index(p))
                            print(f"玩家{p.getName()} 陣亡")
                        else:
                            print(f"玩家{p.getName()} 遭受攻擊 血量剩餘{p.getHp()}")
                            if isinstance(p, Cleric) and p.getHp()<5:
                                p.setHp(p.getHp()+10)
                                p.talent()

            else:
                if C.getEnergyBar() == 6:
                    blood = C.skill()
                    C.setEnergyBar(0)
                    c = random.choice(com)
                    c.setHp(c.getHp()+blood)
                    print(f"電腦{c.getName()} 血量回升{c.getHp()}")
                else:
                    blood = C.fight()
                    C.setEnergyBar(C.getEnergyBar()+1)
                    for p in list(reversed(player)):
                        p.setHp(p.getHp()-blood)
                        if p.getHp() <= 0:
                            player.pop(player.index(p))
                            print(f"玩家{p.getName()} 陣亡")
                        else:
                            print(f"玩家{p.getName()} 遭受攻擊 血量剩餘{p.getHp()}")
                            if isinstance(p, Cleric) and p.getHp()<5:
                                p.setHp(p.getHp()+10)
                                p.talent()

            comNo = comNo + 1


        print("-"*30)
        Round = Round+1

    if Round>200:
        print("平手！！！")
    elif len(player) == 0:
        print("電腦勝利")
    else:
        print("玩家勝利")





