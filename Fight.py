import sys, os

from BattleTeam import BattleTeam
import sqlite3
from Game_Init import tupel_to_string
from Game_Init import tupel_to_string2
from Move import Move
from Stat import Stat
from PokeLib3 import moveList3
from PokeLib2 import moveList2
from PokeLib1 import moveList1
from PokeLib4 import moveList4
import random
import math

zuege = 0
totaldmg1 = 0
totaldmg2 = 0
cattack = False
cchange = False
confu = False
par = False
miss = False
death = False
r = 0

player1 = False
player2 = False
chosenmove1 = []
chosenmove2 = []
attackmove1 = []
attackmove2 = []
pokemon = []
team1moves = []
team2moves = []
moveset1 = []
moveset2 = []
#par slp gif brn frz ko cnf fln lch lov crs hyp
pokestat1 = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0,0
]
pokestat2 = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0 ,0
]
sun = 0  
rain = 0
sandstorm = 0
hail = 0
spikes1 = 0
spikes2 = 0
miss = [False, False]
lose1 = False
lose2 = False
flag1 = 0
flag2 = 0
slp1 = 0
slp2 = 0
hyp1 = 0
hyp2 = 0

primemove1 = []
primemove2 = []

pokeval1 = [0, 0, 0, 0, 0, 0, 0, 0]
pokeval2 = [0, 0, 0, 0, 0, 0, 0, 0]
#atk def spatk spdef init eva acc crt
attackmove = []
healthbar1 = []
healthbar2 = []
defeat = False
stats1 = []
stats2 = []
stattemplate = [
    "Type1", "Type2", "HP", "Attack", "Defense", "Sp.Attack", "Sp.Defense",
    "Speed", "Strat"
]
onelose = False


def onematch(turniername, trainer1, gen1, trainer2, gen2, allespieler):
  erg = 0
  blockPrint()
  getData(trainer1, gen1, trainer2, gen2)
  if trainer1 in allespieler and trainer2 in allespieler:
    clrtxt(allespieler)
    with open(trainer1 + ".txt", "w") as file:
      sys.stdout = file
      erg = fightmatch(trainer1, trainer2, turniername, gen1, gen2,
                       allespieler)
    sys.stdout = sys.__stdout__
    
  elif trainer1 in allespieler:
    clrtxt(allespieler)
    with open(trainer1 + ".txt", "w") as file:
      sys.stdout = file
      erg = fightmatch(trainer1, trainer2, turniername, gen1, gen2,
                       allespieler)
    sys.stdout = sys.__stdout__
  elif trainer2 in allespieler:
    clrtxt(allespieler)
    with open(trainer2 + ".txt", "w") as file:
      sys.stdout = file
      erg = fightmatch(trainer1, trainer2, turniername, gen1, gen2,
                       allespieler)
    sys.stdout = sys.__stdout__
  else:
    erg = fightmatch(trainer1, trainer2, turniername, gen1, gen2, allespieler)

  return erg


def getData(trainer1, gen1, trainer2, gen2):
  global defeat
  global stats1
  global stats2
  global team1moves
  global team2moves
  global primemove1
  global primemove2
  pokenames1 = []
  pokenames2 = []
  pokenames1 = kadertoArr(gen1, trainer1, pokenames1)
  pokenames2 = kadertoArr(gen2, trainer2, pokenames2)

  stats1 = makestats(pokenames1, gen1, stats1)
  stats2 = makestats(pokenames2, gen2, stats2)
  team1moves = makemoves(stats1, team1moves)
  team2moves = makemoves(stats2, team2moves)
  primemove1 = makemoves(stats1, primemove1)
  primemove2 = makemoves(stats2, primemove2)


def fightmatch(trainer1, trainer2, turniername, gen1, gen2, asp):
  # Trainer Name 1 und 2 und Genzahl # asp = allespieler []

  global totaldmg1
  global totaldmg2
  global player1
  global player2
  p1first = False
  dmg1 = 0
  dmg2 = 0
  global chosenmove1  #List
  global chosenmove2  # List
  global healthbar1  # List of Integers <--
  global healthbar2
  global stats1  # List of Pokestats + Movenames  <--
  global stats2
  global team1moves  # List of Movesets <--?
  global team2moves
  global attackmove1  # List of Moves in Movesets
  global attackmove2
  global pokestat1  # List of Booleans like par, slp, gif, brn, frz, ko, cnf, fln, lov, crs <--
  global pokestat2
  global pokeval1  # List of Integers like atk, def, spatk, spdef, init, eva, acc, crt
  global pokeval2
  global lose1  # Sind alle HP = 0?
  global lose2
  global r  # Rundenzahl
  global flag1
  global flag2
  global primemove1
  global primemove2
  global hyp1
  global hyp2
  global slp1
  global slp2
  global spikes2
  global spikes1

  #print(turniername +" Battle!") #Liga1 Battle
  print(trainer1 + " gegen " + trainer2)  #tamer gegen lass

  print()
  print("Team " + trainer1 + ":")
  for i in range(4):
    print(stats1[i].pokename, end=" ")
  print()
  print()
  print("Team " + trainer2 + ":")
  for i in range(4):
    print(stats2[i].pokename, end=" ")
  print()
  print()
  for i in range(4):  # HP initialisieren
    healthbar1.append(initHP(stats1[i].hp)+31)
    healthbar2.append(initHP(stats2[i].hp)+31)
    
  a = False
  print(stats1[0].pokename + " mit " + str(healthbar1[0]) +
        " HP")  #Pikachu mit 100 HP
  print(stats2[0].pokename + " mit " + str(healthbar2[0]) + " HP\n")

  while lose1 != True or lose2 != True:  # Scheife solange es noch Pokemon gibt
    
    
    while healthbar1[0] > 0 or healthbar2[0] > 0:
      attackmove1,flag1 = getmove(team1moves, stats1, stats2, pokeval1, pokeval2,
                            flag1, healthbar1[0], pokestat2,
                            primemove1)  # players chose move according to AI
      #print(attackmove1)
      attackmove2,flag2 = getmove(team2moves, stats2, stats1, pokeval2, pokeval1,
                            flag2, healthbar2[0], pokestat1, primemove2)
      #print(attackmove2)
      p1first = choseprio(pokestat1[0], pokestat2[0], attackmove1[0][4],
                          attackmove2[0][4], stats1[0].speed, stats2[0].speed,
                          p1first)  # chose Prio
      if p1first:
        pokestat1 = clearafterdamage(pokestat1,stats1[0].pokename)
        print(stats1[0].pokename + " setzt " + attackmove1[0][0] +
              " ein")  # Nebulak setzt DreamEater ein
        dmg1 = fightstep1(stats1[0], stats2[0], pokestat1, pokeval1, pokeval2,
                          attackmove1, healthbar1, healthbar2, slp1, hyp1)
        dmg1 = math.floor(dmg1 * (100 - random.randint(0, 15)) / 100)
        print("verursacht " + str(dmg1) + " Schaden", end=" ")
        healthbar2[0] -= dmg1
        totaldmg1 += dmg1
        aftereffect(attackmove1, attackmove2, stats1, stats2, pokeval1,
                    pokeval2, pokestat1, pokestat2, healthbar1, healthbar2,
                    dmg1, 1)
        print("\n")

        if healthbar2[0] > 0:
          pokestat2 = clearafterdamage(pokestat2,stats2[0].pokename)
          print(stats2[0].pokename + " setzt " + attackmove2[0][0] +
                " ein")  # Traumato setzt Pfund ein
          dmg2 = fightstep1(stats2[0], stats1[0], pokestat2, pokeval2,
                            pokeval1, attackmove2, healthbar2, healthbar1,
                            slp2, hyp2)
          dmg2 = math.floor(dmg2 * (100 - random.randint(0, 15)) / 100)
          print("verursacht " + str(dmg2) + " Schaden", end=" ")
          healthbar1[0] -= dmg2
          totaldmg2 += dmg2
          aftereffect(attackmove2, attackmove1, stats2, stats1, pokeval2,
                      pokeval1, pokestat2, pokestat1, healthbar2, healthbar1,
                      dmg2, 2)
          print("\n")
        afterdamage(healthbar1[0], healthbar2[0], stats1, pokestat1)
        afterdamage(healthbar2[0], healthbar1[0], stats2, pokestat2)



        if healthbar1[0] <= 0:
          print(stats1[0].pokename + " ist KO!\n")  # Nebulak ist K.O!

        if healthbar2[0] <= 0:
          print(stats2[0].pokename + " ist KO!\n")  # Traumato ist K.O!
        break
      elif not p1first:
        pokestat2 = clearafterdamage(pokestat2,stats2[0].pokename)
        print(stats2[0].pokename + " setzt " + attackmove2[0][0] +
              " ein")  # Traumato setzt Pfund ein
        dmg2 = fightstep1(stats2[0], stats1[0], pokestat2, pokeval2, pokeval1,
                          attackmove2, healthbar2, healthbar1, slp2, hyp2)
        dmg2 = math.floor(dmg2* (100 - random.randint(0, 15)) / 100 )
        print("verursacht " + str(dmg2) + " Schaden", end=" ")
        healthbar1[0] -= dmg2
        totaldmg2 += dmg2
        aftereffect(attackmove2, attackmove1, stats2, stats1, pokeval2,
                    pokeval1, pokestat2, pokestat1, healthbar2, healthbar1,
                    dmg2, 2)
      
        
        print("\n")
        if healthbar1[0] > 0:
          pokestat1 = clearafterdamage(pokestat1,stats1[0].pokename)
          print(stats1[0].pokename + " setzt " + attackmove1[0][0] +
                " ein")  # Nebulak setzt DreamEater ein
          dmg1 = fightstep1(stats1[0], stats2[0], pokestat1, pokeval1,
                            pokeval2, attackmove1, healthbar1, healthbar2,
                            slp1, hyp1)
          dmg1 = math.floor(dmg1 * (100 - random.randint(0, 15)) / 100 )
          print("verursacht " + str(dmg1) + " Schaden", end=" ")
          healthbar2[0] -= dmg1
          totaldmg1 += dmg1
          aftereffect(attackmove1, attackmove2, stats1, stats2, pokeval1,
                      pokeval2, pokestat1, pokestat2, healthbar1, healthbar2,
                      dmg1, 1)
          print("\n")
        afterdamage(healthbar1[0], healthbar2[0], stats1, pokestat1)
        afterdamage(healthbar2[0], healthbar1[0], stats2, pokestat2)

        clearfln(pokestat1)
        clearfln(pokestat2)

        if healthbar2[0] <= 0:
          print(stats2[0].pokename + " ist KO!\n")  # Traumato ist K.O!

        if healthbar1[0] <= 0:
          print(stats1[0].pokename + " ist KO!\n")  # Nebulak ist K.O!
        break
    #afterdamage(healthbar1[0],healthbar2[0],stats1,pokestat1)
    #afterdamage(healthbar2[0],healthbar1[0],stats2,pokestat2)
    if healthbar1[0] <= 0:
      clearpokestat(pokestat1)
      clearpokeval(pokeval1)
      flag1 = 0
      lose1 = changequeue(healthbar1, stats1, team1moves, primemove1, lose1)
      if not lose1:
        print(stats1[0].pokename + " mit " + str(healthbar1[0]) +
              " HP")  #Pikachu mit 100 HP
        print(stats2[0].pokename + " mit " + str(healthbar2[0]) + " HP\n")
        #healthbar2,totaldmg2 = dospikes(spikes1,stats2,healthbar2,totaldmg2)
    if healthbar2[0] <= 0:

      clearpokestat(pokestat2)
      clearpokeval(pokeval2)
      flag2 = 0
      lose2 = changequeue(healthbar2, stats2, team2moves, primemove2, lose2)
      if not lose2:
        print(stats1[0].pokename + " mit " + str(healthbar1[0]) +
              " HP")  #Pikachu mit 100 HP
        print(stats2[0].pokename + " mit " + str(healthbar2[0]) + " HP\n")
        #afterdamage Hail, Posion
        #healthbar1,totaldmg1 = dospikes(spikes2,stats1,healthbar1,totaldmg1)

    if lose1 or lose2:
      break

  if lose1 and lose2:
    #ts = teamstärke
    ts1 = 0
    ts2 = 0
    ts1 = getcell("Trainer1Gen", "Stärke", "TrainerName", trainer1)
    ts2 = getcell("Trainer1Gen", "Stärke", "TrainerName", trainer2)
    print("remi")
    print(trainer1 + " hat eine Teamstärke von " + ts1)
    print(trainer2 + " hat eine Teamstärke von " + ts2)
    print("Total dmg von " + trainer1 + ": " + str(totaldmg1))
    print("Total dmg von " + trainer2 + ": " + str(totaldmg2))
    #getcell("Trainer"+str(gen)+"Gen","Lose","TrainerName",Spielerliste[i])
    if ts1 < ts2:

      print(trainer1 + " gewinnt aufgrund von Underdogvorangklausel!")

      print(trainer1 + " gewinnt gegen " + trainer2)
      enablePrint()
      resetall()
      return 1
    elif ts1 > ts2:
      print(trainer2 + " gewinnt aufgrund von Underdogvorangklausel")
      print(trainer1 + " gewinnt gegen " + trainer2)
      enablePrint()
      resetall()
      return 0
    elif ts1 == ts2:
      print(trainer1 + " und " + trainer2 + "Kaderstärke sind gleich")
      if totaldmg1 > totaldmg2:
        print(trainer1 + " Damage ist höher als " + trainer2)
        print(trainer1 + " gewinnt gegen " + trainer2)
        enablePrint()
        resetall()
        return 1
      elif totaldmg1 > totaldmg2:
        print(trainer2 + " Damage ist höher als " + trainer1)
        print(trainer2 + " gewinnt gegen " + trainer1)
        enablePrint()
        resetall()
        return 0
      else:
        print("Beide Teams haben gleich viele Damage")
        print("Zufall entscheidet...")
        zz = 0
        zz = random.randint(0, 1)
        if zz == 0:
          print(trainer2 + " gewinnt gegen " + trainer1)
        else:
          print(trainer1 + " gewinnt gegen " + trainer2)

        enablePrint()
        resetall()
        return zz
  if lose1:
    print(trainer1 + " hat keine Pokemon mehr..")

    print("Total dmg von " + trainer1 + ": " + str(totaldmg1))
    print("Total dmg von " + trainer2 + ": " + str(totaldmg2))
    print(trainer2 + " gewinnt gegen " +
          trainer1)  #def getcell(tabelle, x,y,ywert):
    enablePrint()
    wintodb2("Trainer" + str(1) + "Gen", "Win", 1, "TrainerName", trainer2)
    wintodb2("Trainer" + str(1) + "Gen", "Lose", 1, "TrainerName", trainer1)
    wintodb2("Trainer" + str(1) + "Gen", "Totaldamage", totaldmg1,
             "TrainerName", trainer1)
    wintodb2("Trainer" + str(1) + "Gen", "Totaldamage", totaldmg2,
             "TrainerName", trainer2)
    resetall()

    return 0
    #wintodb("Trainer"+str(gen1)+"Gen","Lose",getcell("Trainer"+str(gen1)+"Gen","Lose","TrainerName",trainer1)+1,"TrainerName",trainer1)
    #wintodb("Trainer"+str(gen2)+"Gen","Win",getcell("Trainer"+str(gen2)+"Gen","Win","TrainerName",trainer2)+1,"TrainerName",trainer2)
  if lose2:
    print(trainer2 + " hat keine Pokemon mehr..")

    print("Total dmg von " + trainer1 + ": " + str(totaldmg1))
    print("Total dmg von " + trainer2 + ": " + str(totaldmg2))

    print(trainer1 + " gewinnt gegen " + trainer2)
    enablePrint()
    wintodb2("Trainer" + str(1) + "Gen", "Win", 1, "TrainerName", trainer1)
    wintodb2("Trainer" + str(1) + "Gen", "Lose", 1, "TrainerName", trainer2)
    wintodb2("Trainer" + str(1) + "Gen", "Totaldamage", totaldmg1,
             "TrainerName", trainer1)
    wintodb2("Trainer" + str(1) + "Gen", "Totaldamage", totaldmg2,
             "TrainerName", trainer2)
    resetall()
    return 1
    #wintodb("Trainer"+str(gen1)+"Gen","Win",getcell("Trainer"+str(gen1)+"Gen","Win","TrainerName",trainer1)+1,"TrainerName",trainer1)
    #wintodb("Trainer"+str(gen2)+"Gen","Lose",getcell("Trainer"+str(gen2)+"Gen","Lose","TrainerName",trainer2)+1,"TrainerName",trainer2)
  resetall()

def dospikes(spikes1,stats1,healthbar1,totaldmg1):
  print(spikes1)
  if spikes1 ==1:
    print("Stachler (1) verursacht "+stats1[0].pokename + " " + str(hd(healthbar1[0],8)) + " Schaden")
    totaldmg1 += hd(healthbar1[0],8)
    hpabfrage(stats1,healthbar1)
  elif spikes1 ==2:
    print("Stachler (2) fügt "+stats1[0].pokename + " " + str(hd(healthbar1[0],6)) + " Schaden")
    totaldmg1 += hd(healthbar1[0],6)
    hpabfrage(stats1,healthbar1)
  elif spikes1 >=3:
    print("Stachler (3) fügt "+stats1[0].pokename + " " + str(hd(healthbar1[0],4)) +" Schaden")
    totaldmg1 += hd(healthbar1[0],4)
    hpabfrage(stats1,healthbar1)
  return healthbar1,totaldmg1

def hpabfrage(stat1,healthbar1):
  print(stats1[0].pokename + " mit " + str(healthbar1[0]) +" HP")

def resetall():
  global zuege
  global chosenmove1  #List
  global chosenmove2  # List
  global healthbar1  # List of Integers <--
  global healthbar2
  global stats1  # List of Pokestats + Movenames  <--
  global stats2
  global team1moves  # List of Movesets <--?
  global team2moves
  global attackmove1  # List of Moves in Movesets
  global attackmove2
  global pokestat1  # List of Booleans like par, slp, gif, brn, frz, ko, cnf, fln, lov, crs <--
  global pokestat2
  global pokeval1  # List of Integers like atk, def, spatk, spdef, init, eva, acc, crt
  global pokeval2
  global lose1  # Sind alle HP = 0?
  global lose2
  global r  # Rundenzahl
  global flag1
  global flag2
  global primemove1
  global primemove2
  global hyp1
  global hyp2
  global slp1
  global slp2
  global totaldmg1
  global totaldmg2
  global spikes1
  global spikes2

  clear_list(chosenmove1)
  clear_list(chosenmove2)
  clear_list(healthbar1)
  clear_list(healthbar2)
  clear_list(stats1)
  clear_list(stats2)
  clear_list(team1moves)
  clear_list(team2moves)
  clear_list(attackmove1)
  clear_list(attackmove2)
  pokestat1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  pokestat2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  pokeval1 = [0, 0, 0, 0, 0, 0, 0, 0]
  pokeval2 = [0, 0, 0, 0, 0, 0, 0, 0]
  lose1 = False
  lose2 = False
  r = 0
  flag1 = 0
  flag2 = 0
  primemove1 = []
  primemove2 = []
  slp1 = 0
  slp2 = 0
  hyp1 = 0
  hyp2 = 0
  totaldmg1 = 0
  totaldmg2 = 0
  zuege = 0
  spikes1 = 0
  spikes2 = 0


def changequeue(list1, list2, list3, list4, loscon):
  e = 0
  while list1[0] <= 0:
    e = e + 1
    element = list1.pop(0)
    list1.append(element)
    element = list2.pop(0)
    list2.append(element)
    element = list3.pop(0)
    list3.append(element)
    element = list4.pop(0)
    list4.append(element)

    if e >= 4:
      loscon = True
      return loscon
  return loscon


#par slp gif brn frz ko cnf fln lch lov crs
def afterdamage(healthbar1, healthbar2, stats1, pokestat1):
  global zuege
  global hail
  global sandstorm
  zuege += 1
  if zuege > 50:
    print("Verzweifler fuegt " + stats1[0].pokename + " " +
          str(hd(stats1[0].hp , 8)) + " zu!")
    healthbar1 -= hd(stats1[0].hp , 8)
  if pokestat1[2] or pokestat1[3]:
    healthbar1 -=hd(stats1[0].hp , 8)
    if pokestat1[2]:
      print("Gift fuegt " + stats1[0].pokename + " " +
            str(hd(stats1[0].hp , 8)) + " zu!")
      healthbar1 -=hd(stats1[0].hp , 8)
    if pokestat1[3]:
      print("Verbrennung fuegt " + stats1[0].pokename + " " +
            str(hd(stats1[0].hp , 8)) + " zu!")
      healthbar1 -= hd(stats1[0].hp , 8)
  if pokestat1[8]:
    print(stats1[0].pokename + " stiehlt " + stats2[0].pokename+ " " +
          str(hd(stats1[0].hp , 8)) + " HP")
    healthbar1 -=hd(stats1[0].hp , 8)
    healthbar2 +=hd(stats1[0].hp , 8)
    if healthbar2 > stats2[0].hp * 2 + 110+31:
      healthbar2 = stats2[0].hp * 2 + 110 +31
  if pokestat1[10]:
    healthbar1 - math.floor(stats1[0].hp / 4)
    print("Fluch fuegt " + stats1[0].pokename +
          str(math.floor(stats1[0].hp / 8)) + " zu!")
  if hail >= 1 and stats1[0].type != "Ice":
    healthbar1 - math.floor(stats1[0].hp / 4)
    print("Hagel fuegt " + stats1[0].pokename +
          str(math.floor(stats1[0].hp / 16)) + " zu!")
  if sandstorm >= 1 and (stats1[0].type != ("Rock" or "Steel" or "Ground")):
    healthbar1 - math.floor(stats1[0].hp / 4)
    print("Sandsturm fuegt " + stats1[0].pokename +
          str(math.floor(stats1[0].hp / 8)) + " zu!")

#par slp gif brn frz ko cnf fln lch lov crs hyp
def clearafterdamage(pokestat1,pokename1):
  #slp
  if pokestat1[1] > 0 :
    pokestat1[1] -=1
    if pokestat1[1] == 0:
      print(pokename1 + " ist aufgewacht")
  #frz
  if pokestat1[4] > 0 :
    if random.random()< 0.2:
      pokestat1[4] =0
      if pokestat1[4] == 0:
        print(pokename1 + " ist aufgetaut")
  #cnf
  if pokestat1[6] >0:
    pokestat1[6] -=1
    if pokestat1[6] == 0:
      print(pokename1 + " ist nicht mehr verwirrt")

  #hyp
  if pokestat1[11] >0:
    pokestat1[11] -=1
  return pokestat1




def vtf(pokeval1):
  if pokeval1 == 0:
    return 1
  elif pokeval1 > 0:
    return 1 + pokeval1 * 0.5
  elif pokeval1 == -1:
    return 2 / 3
  elif pokeval1 == -2:
    return 2 / 4
  elif pokeval1 == -3:
    return 2 / 5
  elif pokeval1 == -4:
    return 2 / 6
  elif pokeval1 == -5:
    return 2 / 7
  elif pokeval1 == -6:
    return 2 / 8
  
  if pokeval1 >6:
    pokeval1 = 6
  elif pokeval1 <-6:
    pokeval1 = -6






#par slp gif brn frz ko cnf fln lch lov crs
def clearpokestat(pokestat1):
  for i in range(len(pokestat1)):
    pokestat1[i] = 0
  return pokestat1
  


#par slp gif brn frz ko cnf fln lch lov crs
def softclearpokestat(pokestat1):
  for i in range(5):
    pokestat1[i + 5] = False


def clearpokeval(pokeval1):
  for i in range(len(pokeval1)):
    pokeval1[i] = 0


def clearweather():
  global sun
  global hail
  global sandstorm
  global rain
  if sun == hail == sandstorm == rain == 0:
    return
  if sun > 0:
    sun -= 1
  if hail > 0:
    hail -= 1
  if sandstorm > 0:
    sandstorm -= 1
  if rain > 0:
    rain -= 1


def clearslp(slp1):
  if slp1 == 0:
    return slp1
  else:
    slp1 -= 1
    return slp1


def clearhyp(hyp1):
  if hyp1 == 0:
    return hyp1
  else:
    hyp1 -= 1
    return hyp1


def clear_list(my_list):
  my_list.clear()


def initHP(hp):
  return 2 * hp + 110


def truevalue(stat):
  return 2 * stat + 5


def fightstep1(stats1, stats2, pstatus1, pokeval1, pokeval2, attackmove1,
               healthbar1, healthbar2, slp1, hyp1):
  global miss
  global sun
  global hail
  global sandstorm
  global rain

  phy = [
      "Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug",
      "Ghost", "Steel"
  ]
  stab = 1
  effective = 1
  sundmg = 1
  sunnerf = 1
  rainnerf = 1
  raindmg = 1
  burndmg = 1
  miss = False
  #par slp gif brn frz ko cnf fln lch lov crs hyp
  if pstatus1[1]>0:  #Sleep,Flinch, Freeze, ko
    print(stats1.pokename + " liegt im Schlaf")
    return 0
  if pstatus1[7]>0:  #Sleep,Flinch, Freeze, ko
    print(stats1.pokename + " schreckt zurueck")
    return 0
  if pstatus1[4]>0:  #Sleep,Flinch, Freeze, ko
    print(stats1.pokename + " ist in Eis erstarrt")
    return 0
  if pstatus1[11]>0:  #Sleep,Flinch, Freeze, ko
    print(stats1.pokename + " muss sich aufladen")

    return 0
  """
  if pstatus1[11]:  #Sleep,Flinch, Freeze, ko
    return 0
  """
  if pstatus1[6] >0:  #Confuse 50% + selfdamage
    print(stats1.pokename + " ist verwirrt")
    if random.random() < 0.5:
      print(stats1.pokename + " fuegt sich selber " + str(tD(40, "Normal", stats1, stats2, pokeval1, pokeval2))+" zu")
      print(healthbar1[0])
      healthbar1[0] -= tD(40, "Normal", stats1, stats2, pokeval1, pokeval2)
      return 0
  if pstatus1[0]>0 and random.random() < 0.75:  #Paralyse 75% Trefferrate
    print(stats1.pokename + " ist paralysiert")
    return 0
  if pstatus1[9]>0 and random.random() < 0.5:  #love 50%
    print(stats1.pokename + " ist starr vor Liebe")
    return 0
  if attackmove1[0][3] != 0:
    if random.random() * 100 >= vtf(pokeval1[7]) * attackmove1[0][3]:  #Miss
      print("Der Angriff ging daneben")
      return 0

  effective = iseffective(attackmove1[0][1], stats2.type1,
                          stats2.type2)  #Wie effektiv?
  if effective == 0:
    print("Der Angriff hat keine Wirkung")
    return 0
  miss = True
  if pstatus1[3] and stats1.type1 in phy:  #burn reduces physical attacks
    burndmg = 0.75
  if attackmove1[0][1] in (stats1.type1, stats1.type2):  # stab does 1,5 damage

    stab = 1.50
  if sun != 0:
    if attackmove1[0][1] == "Fire":  #fireboost by sunshine
      sundmg = 1.5
    elif attackmove1[0][1] == "Water":  #Waternerf by sunshine
      sunnerf = 0.5
  if rain != 0:
    if attackmove1[0][1] == "Fire":  #Waterboost by rain
      raindmg = 1.5
    elif attackmove1[0][1] == "Water":  #Firenerf by rain
      rainnerf = 0.5
  if random.random() < 0.0625 * pokeval1[7]:  #Crit
    print("Volltreffer!")
    if effective >= 2:
      print("Der Angriff ist sehr Effektiv")
    return (tD2(attackmove1[0][2], attackmove1[0][1], stats1, stats2, pokeval1,
                pokeval2) * effective * stab * 2 * sundmg * raindmg)
  if effective >= 2:
    print("Der Angriff ist sehr Effektiv")
  return (tD(attackmove1[0][2], attackmove1[0][1], stats1, stats2, pokeval1,
             pokeval2) * effective * stab * burndmg * sundmg * raindmg *
          sunnerf * rainnerf)


#par slp gif brn frz ko cnf fln lch lov crs


def wintodb(Tabelle, x, xwert, y, ywert):
  conn = sqlite3.connect('PokeData.db')
  cursor = conn.cursor()

  cursor.execute("UPDATE " + Tabelle + " SET " + x + " = \"" + str(xwert) +
                 "\" WHERE " + y + "=\"" + str(ywert) + "\"")

  conn.commit()
  conn.close()


def wintodb2(Tabelle, x, xwert, y, ywert):
  conn = sqlite3.connect('PokeData.db')
  cursor = conn.cursor()

  cursor.execute("UPDATE " + Tabelle + " SET " + x + " = " + x + " + " +
                 str(xwert) + " WHERE " + y + "=\"" + str(ywert) + "\"")

  conn.commit()
  conn.close()


def delcell(Tabelle, x, y, ywert):
  conn = sqlite3.connect('PokeData.db')
  cursor = conn.cursor()
  print("UPDATE " + Tabelle + " SET " + x + " = NULL WHERE " + y + "=\"" +
        ywert + "\"")
  cursor.execute("UPDATE " + Tabelle + " SET " + x + " = NULL WHERE " + y +
                 "=\"" + ywert + "\"")

  conn.commit()
  conn.close()


def tD2(pw, type, stats1, stats2, pokeval1, pokeval2):
  phy = [
      "Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug",
      "Ghost", "Steel"
  ]
  spec = [
      "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark"
  ]
  zwei = 2
  pokeval12=[0,0]
  pokeval22 = [0,0]
  if pw == 0:
    zwei = 0
  if pokeval1[0] > 1:
    pokeval12[0] = pokeval1[0]
  if pokeval1[2] > 1:
    pokeval12[1] = pokeval1[2]
  if pokeval2[1] < 1:
    pokeval22[0] = pokeval2[1]
  if pokeval2[3] < 1:
    pokeval22[1] = pokeval2[3]

  

  if type in phy:
    return math.floor(math.floor(42 * stats1.attack * vtf(pokeval12[0]) / stats2.defense * vtf(pokeval22[0]) * pw) / 50) + zwei

  elif type in spec:
    return math.floor(math.floor(42 * stats1.spattack * vtf(pokeval12[1]) / stats2.spdefense * vtf(pokeval22[1]) * pw) / 50) + zwei

  return 0


#atk, def, spatk, spdef, init, eva, acc, crt
def tD(pw, type, stats1, stats2, pokeval1, pokeval2):
  phy = [
      "Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug",
      "Ghost", "Steel"
  ]
  spec = [
      "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark"
  ]
  zwei = 2
  if pw == 0:
    zwei = 0
  if type in phy:
    return math.floor(math.floor(42 * stats1.attack * vtf(pokeval1[0]) / stats2.defense * vtf(pokeval2[1]) * pw) / 50) + zwei
  elif type in spec:
    return math.floor(math.floor(42 * stats1.spattack * vtf(pokeval1[2]) / stats2.spdefense * vtf(pokeval2[3]) * pw) / 50) + zwei
  return 0


def hitormiss(pstatus1, eva2, acc1, pmove1):
  if pstatus1[0] and random.random() < 0.75:
    return
  if pstatus1[1] and pstatus1[5]:
    return


def choseprio(par1, par2, prio1, prio2, spd1, spd2, p1first):
  prio1 = int(prio1)
  prio2 = int(prio2)
  if prio1 > prio2:
    p1first = True
    return p1first
  if prio1 < prio2:
    p1first = False
    return p1first
  if par1<0:
    spd1 = math.floor(spd1 / 0.25)
  if par2<0:
    spd2 = math.floor(spd2 / 0.25)
  if spd1 > spd2:
    p1first = True
  elif spd1 < spd2:
    p1first = False
  else:
    p1first = random.choice([True, False])
  return p1first


def boi():
  for e in range(4):
    print(stats1[e].pokename)
    for i in range(4):
      print(team1moves[e][i][0] + "| ", end="")
    print()
  print()
  for e in range(4):
    print(stats2[e].pokename)
    for i in range(4):
      print(team2moves[e][i][0] + "| ", end="")


def iseffective(movetype, type1, type2):
  faktor = 1
  x = ""
  y = ""
  type = {
      "Normal": 0,
      "Fighting": 1,
      "Flying": 2,
      "Poison": 3,
      "Ground": 4,
      "Rock": 5,
      "Bug": 6,
      "Ghost": 7,
      "Steel": 8,
      "Fire": 9,
      "Water": 10,
      "Grass": 11,
      "Electric": 12,
      "Psychic": 13,
      "Ice": 14,
      "Dragon": 15,
      "Dark": 16,
      "": 17
  }
  matrix = [[1, 1, 1, 1, 1, 0.5, 1, 0, 0.5, 1, 1, 1, 1, 1, 1, 1, 1],
            [2, 1, 0.5, 0.5, 1, 2, 0.5, 0, 2, 1, 1, 1, 1, 0.5, 2, 1, 2],
            [1, 2, 1, 1, 1, 0.5, 2, 1, 0.5, 1, 1, 2, 0.5, 1, 1, 1, 1],
            [1, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 0, 1, 1, 2, 1, 1, 1, 1, 1],
            [1, 1, 0, 2, 1, 2, 0.5, 1, 2, 2, 1, 0.5, 2, 1, 1, 1, 1],
            [1, 0.5, 2, 1, 0.5, 1, 2, 1, 0.5, 2, 1, 1, 1, 1, 2, 1, 1],
            [1, 0.5, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 0.5, 1, 2, 1, 2, 1, 1, 2],
            [0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5],
            [1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 1, 2, 1, 1],
            [1, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5, 0.5, 2, 1, 1, 2, 0.5, 1],
            [1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 1, 0.5, 1],
            [1, 1, 0.5, 0.5, 2, 2, 0.5, 1, 0.5, 0.5, 2, 0.5, 1, 1, 1, 0.5, 1],
            [1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 0.5, 1],
            [1, 2, 1, 2, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 0],
            [1, 1, 2, 1, 2, 1, 1, 1, 0.5, 0.5, 0.5, 2, 1, 1, 0.5, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 1, 2, 1],
            [1, 0.5, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5]]
  x = type[movetype]
  y = type[type1]
  faktor *= matrix[x][y]

  if type2 != "":
    y = type[type2]
    faktor *= matrix[x][y]
  return faktor

def hd(hp,percent): #healthdamage
  dmg = 0
  hp= hp *2 +110+31
  dmg = math.floor(hp /percent)
  return dmg 

def getmove(teammoves, stats1, stats2, pokeval1, pokeval2, flag, healthbar,
            pokestat2,
            primemoves):  #Hier werden die Strategien-Algorythmen ausgeführt

  chosenmove = []
  chosenmove = teammoves

  dmg = []
  if stats1[
      0].strat == 1:  #Standartstrat AI sucht sich den Angriff mit der höchsten Dmg (verbesserungswürdig, weil Wetterfaktoren noch keine Rolle spielt)
    mostdamage(teammoves, stats1, stats2, pokeval1, pokeval2, chosenmove, flag,
               dmg)

  if stats1[
      0].strat == 2:  #Lässt Himeko-Chan mit ihrer jahrelanger Leidenschaft und fundiertem Fachwissen als PokeExpertin entscheiden! ->
    randarr(chosenmove[0])

  if stats1[
      0].strat == 3:  # oberster Angriff in Liste wird immer zuerst ausgeführt -> Annoyer, Booster, Evation, Spiker, Weather User
    if flag == 0:
      flag = flag + 1
      chosenmove = primemoves
    else:
      mostdamage(teammoves, stats1, stats2, pokeval1, pokeval2, chosenmove,
                 flag, dmg)
  if stats1[
      0].strat == 4:  # oberster Angriff in Liste wird immer 2mal zuerst ausgeführt -> Booster, Evation, Spiker
    if flag > 2:
      flag = flag + 1
      chosenmove = primemoves

    else:
      mostdamage(teammoves, stats1, stats2, pokeval1, pokeval2, chosenmove,
                 flag, dmg)
  if stats1[
      0].strat == 5:  # Wenn das Pokemon low ist, wird es stets den ersten Angriff wählen -> Boomer, Healer
    if healthbar[0] >= (stats1[0].hp * 2 + 110+31) / 50:
      chosenmove[0] = primemoves[0]

    else:
      mostdamage(teammoves, stats1, stats2, pokeval1, pokeval2, chosenmove,
                 flag, dmg)
      #par slp gif brn frz ko cnf fln lch lov crs

  # Wenn der Gegner noch keine Statusveränderungen hat, dann wird das pokemon seinen ersten Angriff machen    
  if stats1[0].strat == 6:
    if check_stats(pokestat2, 1):
      chosenmove[0] = primemoves[0]
    else:
      mostdamage(teammoves, stats1, stats2, pokeval1, pokeval2, chosenmove,flag, dmg)
  # Wenn der Gegner noch keine Statusveränderungen hat, dann wird das pokemon seinen ersten Angriff machen
  if stats1[0].strat == 7:
    if check_stats(pokestat2, 1):
      #Wenn er nur einen hat, wird der 2 angriff ausgewählt
      chosenmove[0] = primemoves[0]
      if check_stats(pokestat2, 2):
        chosenmove[0] = primemoves[0]

        chosenmove[0].insert(0, chosenmove[0].pop(1))
    else:
      mostdamage(teammoves, stats1, stats2, pokeval1, pokeval2, chosenmove,flag, dmg)
  return chosenmove[0] , flag

#par slp gif brn frz ko cnf fln lch lov crs hyp
def check_stats(lst, zahl):
  count_true = 0
  for item in lst:
    if item >0:
      count_true += 1
      if count_true >= zahl:
        return False
  return True


def randarr(liste):
  zz = random.randint(0, 3)
  liste.insert(0, liste.pop(zz))
  return liste


def mostdamage(teammoves, stats1, stats2, pokeval1, pokeval2, chosenmove, flag,
               dmg):
  for i in range(len(teammoves)):
    dmg.append(
        math.floor(
            iseffective(chosenmove[0][i][1], stats2[0].type1, stats2[0].type2)
            * tD(chosenmove[0][i][2], chosenmove[0][i][1], stats1[0],
                 stats2[0], pokeval1, pokeval2)))

  for i in range(4):
    chosenmove[0][i].append(dmg[i])
  chosenmove[0] = sorted(chosenmove[0],
                         key=lambda x: (x[-1], random.random()),
                         reverse=True)


def custom_sort(lst):
  last_element = lst[-1]
  return (last_element, random.random())


def tupel_to_integer(tupel):
  return int(''.join(str(e) for e in tupel))


def makemoves(stats, teammoves):

  for i in range(len(stats)):
    print(stats[i].pokename)
    print(stats[i].m1)
    print(stats[i].m2)
    print(stats[i].m3)
    print(stats[i].m4)

    teammoves.append([])
    if len(stats[i].m1) != 0:
      teammoves[i].append(Move("", "", 0, 0, 0, 0, 0, 0))
      teammoves[i][0] = movetoArr(stats[i].m1, teammoves[i])
    if len(stats1[i].m2) != 0:
      teammoves[i].append(Move("", "", 0, 0, 0, 0, 0, 0))
      teammoves[i][1] = movetoArr(stats[i].m2, teammoves[i])
    if len(stats1[i].m3) != 0:
      teammoves[i].append(Move("", "", 0, 0, 0, 0, 0, 0))
      teammoves[i][2] = movetoArr(stats[i].m3, teammoves[i])
    if len(stats1[i].m4) != 0:
      teammoves[i].append(Move("", "", 0, 0, 0, 0, 0, 0))
      teammoves[i][3] = movetoArr(stats[i].m4, teammoves[i])
  return teammoves


def makestats(pokenames, gen, statslist):
  tempstat = []
  tempmove = ["", "", "", ""]
  for i in range(len(pokenames)):
    statslist.append(
        Stat(pokenames[i], "", "", 0, 0, 0, 0, 0, 0, 0, "", "", "",
             ""))  #ich arbeite niewieder mit Konstruktoren. SOOO USELESS!!!
    tempstat = linetoArr(
        "PokeStats", "Species", pokenames[i])  #profile = linetoArr("Spieler", "NutzerID",str(id),profile)

    statslist[i].type1 = tempstat[0][2]
    statslist[i].type2 = tempstat[0][3]
    statslist[i].hp = tempstat[0][5]
    statslist[i].attack = sb(tempstat[0][6])+31
    statslist[i].defense = sb(tempstat[0][7])+31
    statslist[i].spattack = sb(tempstat[0][8])+31
    statslist[i].spdefense = sb(tempstat[0][9])+31
    statslist[i].speed = sb(tempstat[0][10])+31
    statslist[i].strat = tempstat[0][12]
    statslist[i].m1 = tempstat[0][18]
    statslist[i].m2 = tempstat[0][19]
    statslist[i].m3 = tempstat[0][20]
    statslist[i].m4 = tempstat[0][21]

  return statslist

def sb(wert): #statboost
  return 2*wert  +5

def stattoArr(genzahl, pokemon, statsList):
  tablename = "PokeStats" + str(genzahl)
  statsList = celltoArr3(tablename, pokemon, statsList)
  return statsList


def kadertoArr(genzahl, trainername, statsList):

  tablename = "Trainer" + str(genzahl) + "Gen"
  statsList = celltoArr2(tablename, trainername, statsList)
  return statsList


def movetoArr(moveName, moveList):
  moveList = linetoArr2("Moves", moveName, moveList)
  return moveList


def getalldb(tabelle):
  conn = sqlite3.connect('PokeData.db')
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM " + tabelle)
  result = cursor.fetchall()

  return result


def linetoArr(tabelle, x, trainerName):
  conn = sqlite3.connect('PokeData.db')
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM " + tabelle + " WHERE " + x + " =\"" +
                 trainerName + "\"")
  result = cursor.fetchall()
  conn.close()
  data_list = []
  for result1 in result:
    data_list.append(result1)
  return data_list


def linetoArr2(tabelle, trainerName, list):
  result2 = []
  conn = sqlite3.connect('PokeData.db')
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM " + tabelle + " WHERE Name =\"" + trainerName +
                 "\"")
  result = cursor.fetchall()
  ras = [tupel_to_string2(t) for t in result]
  parts = tupel_to_string(ras)
  parts = parts.split()
  for word in parts:
    if word.isdigit():
      result2.append(int(word))
    elif word == "" or word == "—" or word == "None":
      result2.append(0)
    else:
      result2.append(word)
  list = result2
  conn.close()
  return list


def celltoArr(tabelle, spalte, trainerID, list):
  conn = sqlite3.connect('PokeData.db')
  cursor = conn.cursor()

  cursor.execute(
      str("SELECT " + spalte + " FROM " + tabelle + " WHERE TrainerID =" +
          trainerID))
  result = cursor.fetchall()
  ras = [tupel_to_string(t) for t in result]
  for i in range(len(ras)):
    list[i] = ras[i]
  conn.close()
  return list


def celltoArr2(tabelle, trainerID, list):
  conn = sqlite3.connect('PokeData.db')
  cursor = conn.cursor()
  cursor.execute("SELECT Pokemon FROM " + tabelle + " Where TrainerName = \"" +
                 trainerID + "\"")
  result = cursor.fetchone()
  ras = tupel_to_string(result)
  list = ras.split()

  cursor.close()
  conn.close()
  return list


def celltoArr3(tabelle, species, list):
  global stattemplate
  conn = sqlite3.connect('PokeData.db')
  cursor = conn.cursor()
  for i in range(len(stattemplate)):
    cursor.execute("SELECT \"" + stattemplate[i] + "\" FROM " + tabelle +
                   " Where Species = \"" + species + "\"")
    result = cursor.fetchone()
    if i == 0 or i == 1:
      list[i] = tupel_to_string(result)
    else:
      list[i] = tupel_to_integer(result)
  cursor.close()
  conn.close()
  return list


def getcell(tabelle, x, y, ywert):
  #z.B getcell("Trainer"+str(gen)+"Gen","Lose","TrainerName",Spielerliste[i])
  conn = sqlite3.connect('PokeData.db')
  cursor = conn.cursor()
  cursor.execute("SELECT \"" + x + "\" FROM " + tabelle + " Where " + y +
                 " = \"" + ywert + "\"")
  result = cursor.fetchone()
  cursor.close()
  conn.close()
  return result[0]


def celltoArr4(tabelle, trainerID, list):
  conn = sqlite3.connect('PokeData.db')
  cursor = conn.cursor()
  cursor.execute("SELECT Pokemon FROM " + tabelle + " Where TrainerName = \"" +
                 trainerID + "\"")
  result = cursor.fetchone()
  ras = tupel_to_string(result)
  list = ras.split()

  cursor.close()
  conn.close()
  return list


def coltoArr(tabelle, spalte, list):
  conn = sqlite3.connect('PokeData.db')
  cursor = conn.cursor()
  cursor.execute("SELECT " + spalte + " FROM " + tabelle)
  result = cursor.fetchall()
  ras = [tupel_to_string(t) for t in result]
  for i in range(len(ras)):
    list.append(ras[i])
  conn.close()
  return list


#coltoArr("Trainer1Gen","Pokemon",testlist)


def coltoreset(tabelle, spalte, spaltenwert):
  conn = sqlite3.connect('PokeData.db')
  cursor = conn.cursor()

  cursor.execute("UPDATE " + tabelle + " SET " + spalte + " = " +
                 str(spaltenwert))
  conn.commit()
  conn.close()


def coltoArr5(tabelle, spalte, list):
  conn = sqlite3.connect('PokeData.db')
  cursor = conn.cursor()
  cursor.execute("SELECT " + spalte + " FROM " + tabelle +
                 " ORDER BY TrainerID ASC")
  result = cursor.fetchall()
  ras = [tupel_to_string(t) for t in result]
  for i in range(len(ras)):
    list.append(ras[i])
  conn.close()
  return list

def clearfln(pokestat1):
    #fln
  if pokestat1[7] >0:
    pokestat1[7] =0
  

#par slp gif brn frz ko cnf fln lch lov crs
def aftereffect(attackmove1, attackmove2, stat1, stat2, pokeval1, pokeval2,
                pokestat1, pokestat2, healthbar1, healthbar2, dmg, zahl):
  global miss
  if miss == False:
    return
  if random.random() * 100 < attackmove1[0][5]:
    doeffect(attackmove1, attackmove2, stat1, stat2, pokeval1, pokeval2,
             pokestat1, pokestat2, healthbar1, healthbar2, dmg, zahl)



def doeffect(attackmove1, attackmove2, stat1, stat2, pokeval1, pokeval2,
             pokestat1, pokestat2, healthbar1, healthbar2, dmg, zahl):
  global sun
  global sandstorm
  global hail
  global rain
  global slp1
  global slp2
  global hyp1
  global hyp2
  global spikes1
  global spikes2
  valstring = ["Atk","Def","SpAtk","SpDef","Init","Eva","Acc","Crt"] 
  #par slp gif brn frz ko cnf fln lch lov crs hyp
  #par
  if attackmove1[0][6] ==1:
    print(stat2[0].pokename + " wurde paralysiert")
    pokestat2[0] = 1
    return
  #slp
  if attackmove1[0][6] ==2:
    pokestat2[1] =  random.randint(1,3 )+1
    print(stat2[0].pokename + " ist eingeschlafen")
    return
    #gif
  if attackmove1[0][6] ==3:
    print(stat2[0].pokename + " wurde vergiftet")
    pokestat2[2] = 1
    return
    #brn
  if attackmove1[0][6] ==4:
    print(stat2[0].pokename + " hat Feuer gefangen")
    pokestat2[3] = 1
    return
    #frz
  if attackmove1[0][6] ==5:
    print(stat2[0].pokename + " ist eingefroren")
    pokestat2[4] = 1
    return
    #cnf
  if attackmove1[0][6] ==6:
    print(stat2[0].pokename + " wurde verwirrt")    
    pokestat2[6] =  random.randint(2, 5)+1
    return
    #fln
  if attackmove1[0][6] ==7:
    pokestat2[7] = 1
    return
    #lch
  if attackmove1[0][6] ==8:
    print(stat2[0].pokename + " wurde bepflanzt")
    pokestat2[8] = 1
    return
    #lov
  if attackmove1[0][6] ==9:
    print(stat2[0].pokename + " hat sich in " +stat1[0].pokename+" verliebt" )   
    pokestat2[9] = 1
    return

  # FUCK HyperBeam
  if attackmove1[0][6] == 16: 
      pokestat1[11] = 2

  for i in range(7):  #atk def spatk spdef init eva acc crt Stats SELF
    if attackmove1[0][6] == i + 30:  # 30 - 70 Statuswerte
      pokeval1[i] += int(attackmove1[0][7])
      print("+ Eigene "+valstring[i] + " " + ads(attackmove1[0][7]), end="")
  for i in range(7):  #atk def spatk spdef init eva acc crt Stats ENEMY
    if attackmove1[0][6] == i + 50:
      pokeval2[i] += int(attackmove1[0][7])
      print("+ Gegner "+valstring[i] + " " + ads(attackmove1[0][7]), end="")
  if attackmove1[0][6] == 71:  #absorber
    print(stats1[0].pokename + " stiehlt " + stats2[0].pokename+ " " +
          str(math.floor(dmg / 2)) + " HP")
    healthbar1[0] += math.floor(dmg / 2)
    if healthbar1[0] > stats2[0].hp * 2 + 110:
      healthbar1[0] = stats2[0].hp * 2 + 110 +31
  if attackmove1[0][6] == 72:  # Fuchtler
    pokestat1[6] = True
  if attackmove1[0][6] == 73:  # Recoil
    healthbar1[0] -= math.floor(dmg / 3)
  if attackmove1[0][6] == 74:  # KO Attacken
    print("K.O-Angriff! " +stats2[0].pokename + " ist kampfunfaehig")
    healthbar2[0] = 0
  if attackmove1[0][6] == 76:  #sunday
    rain, sandstorm, hail = 0
    sun = 8
  if attackmove1[0][6] == 77:  #sunday
    rain, sandstorm, sun = 0
    hail = 8
  if attackmove1[0][6] == 78:  #sunday
    rain, sun, hail = 0
    sandstorm = 8
  if attackmove1[0][6] == 79:  #sunday
    sun, sandstorm, hail = 0
    rain = 8
  if attackmove1[0][6] == 80:  # true Damage
    print("verursacht " +str(attackmove1[0][7])+ " wahren Schaden" )
    healthbar2[0] -= attackmove1[0][7]
  if attackmove1[0][6] == 81:  # Flail
    if healthbar1[0] >= 68.75:
      healthbar2[0] - 20
    elif 35.42 <= healthbar1[0] < 68.75:
      healthbar2[0] - 40
    elif 20.83 <= healthbar1[0] < 35.42:
      healthbar2[0] - 80
    elif 10.42 <= healthbar1[0] < 20.83:
      healthbar2[0] - 100
    elif 4.17 <= healthbar1[0] < 10.42:
      healthbar2[0] - 150
    else:
      healthbar2[0] - 200
  if attackmove1[0][6] == 82:  # Swagger
    pokeval2[0] + 2
    if pokeval2[0] > 7:
      pokeval2[0] == 6
  if attackmove1[0][6] == 83:  # Flatter
    pokeval2[2] + 2
    if pokeval2[2] > 7:
      pokeval2[2] == 6
  if attackmove1[0][6] == 84:
    ps = math.floor((healthbar2[0] + healthbar1[0]) / 2)
    healthbar1[0] = ps
    if ps > stat1[0].hp * 2 + 110:
      healthbar1[0] = stat1[0].hp * 2 + 110
    healthbar2[0] = ps
    if ps > stat2[0].hp * 2 + 110:
      healthbar2[0] = stat2[0].hp * 2 + 110
  if attackmove1[0][6] == 85:  #Silberhauch
    for i in range(5):
      pokeval1[i] += 1
      if pokeval1[i] < 7:
        pokeval1[i] = 6
  if attackmove1[0][6] == 86:  # Erholung
    pokestat1[1] = True
    healthbar1[0] = stat2[0].hp * 2 + 110
  if attackmove1[0][6] == 87:  # Explosion Finale
    print("fuegt sich selbst " + str(hd(stats2[0].hp,attackmove1[0][7] )) + " zu" )
    healthbar1[0] -= hd(stats1[0].hp,attackmove1[0][7] )
  if attackmove1[0][6] == 88:
    if zahl == 1:
      spikes1 += 1
    else:
      spikes2 +=1
  


def ads(number):
    number = int(number)
    if number > 0:
        return "+" + str(number)
    elif number < 0:
        return "-" + str(abs(number))
    else:
        return str(number)

def blockPrint():
  sys.stdout = open(os.devnull, 'w')


def enablePrint():
  sys.stdout = sys.__stdout__


def getProfile(id):
  profile = [
  ]  #[(347156882374262795, 'Tony', 2, 'acetrainerf', 0, None, None)]
  profile2 = [
  ]  #[(216, 'acetrainerf', 'ELEKID SKIPLOOM UNOWN CHINCHOU', 0, 0, None, None, 5000000, None, None, 1366, 1)]
  profile3 = [
  ]  #[[('ELEKID', 'Elekid', 'Electric', '', '360', 45, 63, 37, 65, 55, 95, 255, 1, None, None, None, None, None...
  fourpokemon = []
  profile = linetoArr("Spieler", "NutzerID", str(id))
  profile2 = linetoArr("Trainer" + str(profile[0][2]) + "Gen", "Trainername",
                       profile[0][3])
  fourpokemon = profile2[0][2].split()
  for i in range(len(fourpokemon)):
    profile3.append(linetoArr("PokeStats", "SPECIES", fourpokemon[i]))
  #print(profile)
  #print(profile2)
  #print(profile3)
  return profile, profile2, profile3


def makestats2():
  tempmove = []
  j = -1
  temp = []
  coltoArr("PokeStats", "Species", temp)
  #temp2 = []
  for i in range(len(temp)):
    f = 0
    j = j + 1
    for key, value in moveList3:
      f += 1
      if key == temp[i]:
        #print(temp[i])
        #print(i)
        #print(j)
        #print(f)
        temp2 = moveList3[f - 1][1][-4:]
        wintodb("PokeStats", "Move1", temp2[0], "Species", temp[i])
        wintodb("PokeStats", "Move2", temp2[1], "Species", temp[i])
        wintodb("PokeStats", "Move3", temp2[2], "Species", temp[i])
        wintodb("PokeStats", "Move4", temp2[3], "Species", temp[i])
        #print(moveList3[f-1][1][-4:]) #def wintodb(Tabelle,x,xwert, y,ywert):


def change(befehl, id):
  p1 = []  #[(347156882374262795, 'Tony', 2, 'acetrainerf', 0, None, None)]
  p2 = [
  ]  #[(216, 'acetrainerf', 'ELEKID SKIPLOOM UNOWN CHINCHOU', 0, 0, None, None, 5000000, None, None, 1366, 1)]
  p3 = [
  ]  #[[('ELEKID', 'Elekid', 'Electric', '', '360', 45, 63, 37, 65, 55, 95, 255, 1, None, None, None, None, None...
  p1, p2, p3 = getProfile(id)
  ba = []  #befehlarray
  ba = befehl.split()
  kader = [p3[0][0][0], p3[1][0][0], p3[2][0][0], p3[3][0][0]]
  for i in range(4):
    if ba[0] == "get" and ba[2] == "move" + str(
        i + 1):  # syntax eingehalten? get ABRA move1 MEGA_DRAIN
      if ba[1] in kader or ba[1] == p3[3][0][0]:  #ist das pokemon im Kader?
        if islearnable2(ba[1], ba[3]):
          wintodb("PokeStats", "Move" + str(i + 1), ba[3], "Species", ba[1])
      else:
        print("Fehler")

    if ba[0] == "get" and ba[2] == "position" and ba[3] == str(
        i + 1):  #get gyarados position 1

      if ba[1] in kader:  #ist das pokemon im Kader?
        changepos(
            ba[1], i + 1, p1[0][2], p1[0][3], p2[0][2]
        )  #changepos("ABRA",0,1,"crushgirl","SLOWPOKE SQUIRTLE ABRA DODUO")
        pass
      else:
        print("Fehler")

  if ba[0] == "get" and ba[
      2] == "strat":  # syntax eingehalten? get ABRA strat 2
    if ba[1] in kader:  #ist das pokemon im Kader?
      wintodb("PokeStats", "Strat", ba[3], "Species", ba[1])
    else:
      print("Fehler")
    pass

  if ba[0] == "scout" and ba[
      2] == "give":  # syntax eingehalten? scout ABRA give PIKACHU
    if ba[3] in kader and ba[1] != ba[3] and ba[
        1] not in kader:  #ist das pokemon im Kader?
      for i in range(len(moveList3)):
        if ba[1] == moveList3[i][0]:
          wintodb("Spieler", "TransferWunschliste", ba[1], "NutzerID",
                  p1[0][0])
          wintodb("Spieler", "PokeAbgänger", ba[3], "NutzerID", p1[0][0])
          print("erfolgS")

          break

    else:
      print("Fehler")
    pass


def changepos(pkm, pos, gen, trainer, kader):
  temp = []
  temp = kader.split()
  if pkm in temp:
    temp.remove(pkm)
    temp.insert(pos - 1, pkm)
  temp2 = " ".join(temp)
  #print()
  #print(temp2)
  wintodb("Trainer" + str(gen) + "Gen", "Pokemon", str(temp2), "TrainerName",
          trainer)


#def wintodb(Tabelle,x,xwert, y,ywert):

#wintodb("SpieltagGen1l1","Field1","1","ROWID",str(2))

#onematch("Liga 1","birdkeeper",3,"psychicm",1)
#def coltoArr(tabelle, spalte,  list):


#getProfile(347156882374262795)
#change("hai hao",347156882374262795)
#wintodb("SpieltagGen1l1","Field1","1","ROWID",str(2))
#wintodb("Spieler","PokeAbgänger","s","ROWID",str(2))
def islearnable(pkm, move):
  for i in range(len(moveList3)):
    if pkm in moveList3[i]:
      if move in moveList3[i][1]:
        return True
      else:
        print("false")


def islearnable2(pkm, move):

  for i in range(len(moveList3)):
    if pkm in moveList3[i]:
      if move in moveList3[i][1]:
        return True
  for i in range(len(moveList2)):
    if pkm in moveList2[i]:
      if move in moveList2[i][1]:
        return True

  for i in range(len(moveList1)):
    if pkm in moveList1[i]:
      if move in moveList1[i][1]:
        return True

  for i in range(len(moveList4)):
    if pkm in moveList4[i]:
      
      if move in moveList4[i]:
        return True
      else:
        return False


def addtxt2(satz, asp):
  global player1
  global player2
  if player1 in asp:
    file_path = str(player1) + ".txt"
    with open(file_path,
              "a") as file:  # Verwende "a" (append) statt "w" (write)
      file.write(satz + "\n")
  if player2 in asp:
    file_path = str(player2) + ".txt"
    with open(file_path,
              "a") as file:  # Verwende "a" (append) statt "w" (write)
      file.write(satz + "\n")


def clrtxt(asp):
  global player1
  global player2
  if player1 in asp:
    file_path = str(player1) + ".txt"
    with open(file_path, "w") as file:
      file.truncate()
  if player2 in asp:
    file_path = str(player2) + ".txt"
    with open(file_path, "w") as file:
      file.truncate()


def copy_file(source_file, destination_file):
  try:
    with open(source_file, 'r') as source:
      with open(destination_file, 'w') as destination:
        # Lese den Inhalt der Quelldatei
        content = source.read()
        # Schreibe den Inhalt in die Zieldatei
        destination.write(content)
  except FileNotFoundError:
    pass
  except IOError:
    pass




def getday(
):  #getcell("Trainer"+str(gen)+"Gen","Lose","TrainerName",Spielerliste[i])
  z1 = getcell("Spieltage", "Tag", "ROWID", str(1))
  return z1


def incday():
  wintodb2("Spieltage", "Tag", str(1), "ROWID", str(1))


def incday2():
  wintodb2("Spieltage", "Transfertag", str(1), "ROWID", str(1))


#def coltoArr(tabelle, spalte, list):
def resetseason():
  coltoreset("Trainer1Gen", "Win", 0)
  coltoreset("Trainer1Gen", "Lose", 0)
  coltoreset("Trainer1Gen", "Totaldamage", 0)
  coltoreset("Spieler", "TransferZahl", 0)
  coltoreset("Spieltage", "Tag", 0)
  for i in range(5):
    coltoreset("SpieltagGen11", "Field" + str(i + 1), "NULL")
    coltoreset("SpieltagGen12", "Field" + str(i + 1), "NULL")
    coltoreset("SpieltagGen13", "Field" + str(i + 1), "NULL")

