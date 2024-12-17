
import os
import kivy
#from Fight import getData, linetoArr
from PokeLib5 import poke_mapping
from KaderTemplate import showTemplate
from Game_Init import gameinit
from Game_Init import initTrainer
from Game_Init import initPokemontoTrainer
from Utility import asp, asp2
from Spieltag import spieltag, rr2, spieltag2, aufabstieg, getsortettable,sortierfunktion
from FrontEnd import showprofile, gethelp
from Fight import getday, change, resetseason, incday, incday2,blockPrint, enablePrint,linetoArr,getalldb
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
# Definition der ersten Seite (MainScreen)


leagueTable=[]
days = []
days11 = []
days12 = []
days13 = []
player = []
pokestats11 = []
pokestats12 = []
pokestats13 = []
pokestats14 = []
pokestats21 = []
pokestats22 = []
pokestats23 = []
pokestats24 = []
pokestats =  []
pastresults = []

pastresults11 = []
pastresults12 = []
pastresults13 = []

tabelleni = 2
colori= 1

pokei = []
pokei0 = 0
pokei1 = 0
pokei2 = 0
pokei3 = 0
pokei4 = 0
pokei5 = 0
pokei6 = 0
pokei7 = 0
playerindex = 0
playername = 'breeder'
enemyplayer = ''
enemyplayerindex = 0
words = []
rsp21 = []
rsp22 = []
rsp23 = []
l1 = []
l2 = []
l3 = []
l = []
rsp =[]

def frontendInit():
  global l
  global l1
  global l2
  global l3
  global rsp
  global rsp21
  global rsp22
  global rsp23
  global tabelleni
  global colori
  global enemyplayerindex
  global enemyplayer
  global leagueTable
  global days 
  global days11
  global days12 
  global days13 
  global player 
  global pokestats11
  global pokestats12 
  global pokestats13 
  global pokestats14 
  global pokestats21
  global pokestats22 
  global pokestats23 
  global pokestats24 
  global pokestats
  global playeri
  global pokei0
  global pokei1
  global pokei2
  global pokei3
  global pokei4
  global pokei5
  global pokei6
  global pokei7
  global playername
  global words
  global pastresults
  global pastresults11
  global pastresults12 
  global pastresults13 
  leagueTable = getalldb("Trainer1Gen")
  

  days = getalldb("Spieltage")
  days11 = getalldb("SpieltagGen11")
  days12 = getalldb("SpieltagGen12")
  days13 = getalldb("SpieltagGen13")
  player = getalldb("Spieler")
  pastresults11 = getalldb("SpieltagGen11")
  pastresults12 = getalldb("SpieltagGen12")
  pastresults13 = getalldb("SpieltagGen13")
  pastresults =[pastresults11,pastresults12,pastresults13]
  print(pastresults11)
  print(pastresults12)
  print(pastresults13)

  leagueTable = sorted(leagueTable, key=lambda elem: (elem[11], -elem[3], elem[10] ,-elem[5]))
  print("ldksjflfk")
  print(leagueTable)
  for playeri in range(len(leagueTable)):
    if(leagueTable[playeri][1]==playername):
      tabelleni = leagueTable[playeri][11] -1
      break
  print(tabelleni)
  temp = []
  for i in range(len(leagueTable)):
    temp =leagueTable[i][2].split()
    words.append(temp[0])
    words.append(temp[1])
    words.append(temp[2])
    words.append(temp[3])
  print("Das sind Words")
  print(len(leagueTable))
  pokestats11 = linetoArr("PokeStats", "Species", words[playeri*4])
  pokestats12 = linetoArr("PokeStats", "Species", words[playeri*4+1])
  pokestats13 = linetoArr("PokeStats", "Species", words[playeri*4+2])
  pokestats14 = linetoArr("PokeStats", "Species", words[playeri*4+3])
  pokestats = [pokestats11,pokestats12, pokestats13,pokestats14]
  print(words[playeri*4])
  print(words[playeri*4+1])
  print(words[playeri*4+2])
  print(words[playeri*4+3])

  pokestats21 = linetoArr("PokeStats", "Species", "PIKACHU")
  pokestats22 = linetoArr("PokeStats", "Species", "PIKACHU")
  pokestats23 = linetoArr("PokeStats", "Species", "PIKACHU")
  pokestats24 = linetoArr("PokeStats", "Species", "PIKACHU")

  ####################################################
  day = 0
  day = int(getday())

  table1 = []

  pastresults11 = []
  pastresults12 = []
  pastresults13 = []
  table1, spielergen1, pastresults11, pastresults12, pastresults13 = spieltag2(day + 1)
  print(table1)
  print("")
  print(leagueTable)
  
  rsp21 = rr2(table1[:10], day + 1)
  rsp22 = rr2(table1[10:-10], day + 1)
  rsp23 = rr2(table1[-10:], day + 1)
  rsp = [rsp21,rsp22,rsp23]
  l = [l1,l2,l3]

   
def fpng(word):
    # Durchsuche das Mapping und finde den ersten Key mit dem gewünschten Wert
    key = next((k for k, v in poke_mapping.items() if v == word), None)
    return str(key) 





def change1(msg):
  change(msg,"347156882374262795")







def start_Game():
    day = int(getday())
    print("starte Spieltag: " + str(day+1))

    if day < 30:
      gameday()
    else:
      siegerehrung()
      aufabstieg()
      resetseason()


def siegerehrung():
  table = []
  table = getsortettable()
  table1 = ""
  table1 += "1. Pokemonmeister ist " + table[0][0] + " mit " + table[0][
      6] + "\n"
  table1 += "Glückwunsch an " + table[0][0] + "\n\n"
  table1 += "Zweiter Platz der 1.Liga ist " + table[1][0] + " mit " + table[1][
      6] + "\n"
  table1 += "Glückwunsch an " + table[1][0] + "\n\n"
  table1 += "2. Pokemonmeister ist " + table[10][0] + " mit " + table[10][
      6] + "\n"
  table1 += "Glückwunsch an " + table[10][0] + "\n\n"
  table1 += "Zweiter Platz der 2.Liga ist " + table[11][0] + " mit " + table[
      11][6] + "\n"
  table1 += "Glückwunsch an " + table[11][0] + "\n\n"

  table1 += table[10][0] + " und " + table[11][
      0] + " steigen in die Erste Liga auf\n\n"
  table1 += table[20][0] + " und " + table[21][
      0] + " steigen in die Zweite Liga auf\n\n"
  table1 += table[9][0] + " und " + table[8][
      0] + " steigen in die Zweite Liga ab\n\n"
  table1 += table[19][0] + " und " + table[18][
      0] + " steigen in die Dritte Liga ab\n\n"

  print(table1)

def gameday():

  day = 0
  day = int(getday())
  print(day)
  a1 = 12
  a2 = 4
  f = 20
  f2 = 8
  f3 = 16
  table1 = []
  table2 = []
  table3 = []
  spielergen1 = []
  spielergen2 = []
  spielergen3 = []
  pkmgen1 = []
  pkmgen2 = []
  pkmgen3 = []
  pastresults11 = []
  pastresults12 = []
  pastresults13 = []
  pastresults21 = []
  pastresults22 = []
  pastresults31 = []
  pastresults32 = []
  pastresults33 = []
  table1, spielergen1, pastresults11, pastresults12, pastresults13 = spieltag(day + 1)
  print(table1)
  table1 = sorted(table1, key=sortierfunktion)


  if len(table1) != 0:
    table = "```\n"  # Anfang des Code-Blocks
    if day + 1 in [7, 8, 9, 10, 17, 18, 19, 20, 27, 28, 29, 30]:
      if day + 1 in [7, 17, 27]:
        table += "TRANSFERTAG: " + str(1) + " von 4\n"
      elif day + 1 in [8, 18, 28]:
        table += "TRANSFERTAG: " + str(2) + " von 4\n"
      elif day + 1 in [9, 19, 29]:
        table += "TRANSFERTAG: " + str(3) + " von 4\n"
      elif day + 1 in [10, 20, 20]:
        table += "TRANSFERTAG: " + str(4) + " von 4\n"

    table += asp(str("# "), 2) + asp("TrainerName", a1) + " " + asp("Win", a2) + " " + asp("Lose", a2) + " " + asp("StatSum", a2) + " Totaldmg " + "\n"  # Kopfzeile
    for i in range(10):
      table += asp(str(i + 1), 2) + " " + asp(table1[i][0], a1) + " " + asp(
          str(table1[i][1]), a2) + " " + asp(str(
              table1[i][2]), a2) + " " + asp(
                  str(table1[i][4]), a2 + 3) + " " + asp(
                      str(table1[i][3]),
                      a2 + 2) + "  " + table1[i][6] + "\n"  # Kopfzeile
    table += "```"  # Ende des Code-Blocks
    print(table)
    if len(table1) != 0:
      table = "```\n"  # Anfang des Code-Blocks
      table += asp(str("# "), 2) + asp("TrainerName", a1) + " " + asp(
          "Win", a2) + " " + asp("Lose", a2) + " " + asp(
              "StatSum", a2) + "\n"  # Kopfzeile
      for i in range(10):
        table += asp(
            str(i + 1), 2) + " " + asp(table1[i + 10][0], a1) + " " + asp(
                str(table1[i + 10][1]),
                a2) + " " + asp(str(table1[i + 10][2]), a2) + " " + asp(
                    str(table1[i + 10][4]), a2 + 3) + " " + asp(
                        str(table1[i + 10][3]),
                        a2 + 2) + "  " + table1[i + 10][6] + "\n"  # Kopfzeile
      table += "```"  # Ende des Code-Blocks
    print(table)
    if len(table1) != 0:
      table = "```\n"  # Anfang des Code-Blocks
      table += asp(str("# "), 2) + asp("TrainerName", a1) + " " + asp(
          "Win", a2) + " " + asp("Lose", a2) + " " + asp(
              "StatSum", a2) + "\n"  # Kopfzeile
      for i in range(10):
        table += asp(
            str(i + 1), 2) + " " + asp(table1[i + 20][0], a1) + " " + asp(
                str(table1[i + 20][1]),
                a2) + " " + asp(str(table1[i + 20][2]), a2) + " " + asp(
                    str(table1[i + 20][4]), a2 + 3) + " " + asp(
                        str(table1[i + 20][3]),
                        a2 + 2) + "  " + table1[i + 20][6] + "\n"  # Kopfzeile
      table += "```"  # Ende des Code-Blocks
    print(table)
  # postet Spieltagergebnisse sowie kommende Matches
  blockPrint()
  table1 = ""

  l = []
  r = []
  table1 = []
  table2 = []
  spielergen1 = []
  spielergen2 = []
  spielergen3 = []
  pkmgen1 = []
  pastresults11 = []
  pastresults12 = []
  pastresults13 = []
  table1, spielergen1, pastresults11, pastresults12, pastresults13 = spieltag2(day + 1)

  rsp1 = []
  rsp21 = []
  rsp22 = []
  rsp23 = []
  rsp21 = rr2(table1[:10], day + 1)
  rsp22 = rr2(table1[10:-10], day + 1)
  rsp23 = rr2(table1[-10:], day + 1)

  for i in range(9):
    table = "```\n"  # Anfang des Code-Blocks
    l.append([])
    table += "Spieltag " + str(i + 1) + "\n"

    for e in range(5):
      if pastresults11[i][e + 1] == 1:
        l[i].append("1|0 ")
      elif pastresults11[i][e + 1] == 0:
        l[i].append("0|1 ")
      else:
        l[i].append("?|? ")
      table += asp(rsp21[i][e][0][6], 40) + " " + asp(rsp21[i][e][0][0], 11) + l[i][e] + asp(rsp21[i][e][1][0], 11) + " " + asp(rsp21[i][e][1][6], 40) + "\n"
    table += "```"  # Ende des Code-Blocks
    print(table)
  for i in range(9):
    table = "```\n"  # Anfang des Code-Blocks
    l.append([])
    table += "Spieltag " + str(i + 10) + "\n"

    for e in range(5):
      if pastresults11[i + 9][e + 1] == 1:
        l[i + 9].append("1|0 ")
      elif pastresults11[i + 9][e + 1] == 0:
        l[i + 9].append("0|1 ")
      else:
        l[i + 9].append("?|? ")
      table += asp(rsp21[i][e][0][6], 40) + " " + asp(rsp21[i][e][0][0], 11) + l[i + 9][e] + asp(rsp21[i][e][1][0], 11) + " " + asp(rsp21[i][e][1][6], 40) + "\n"
    table += "```"  # Ende des Code-Blocks
    print(table)
  l = []
  for i in range(9):
    table = "```\n"  # Anfang des Code-Blocks
    l.append([])
    table += "Spieltag " + str(i + 1) + "\n"

    for e in range(5):
      if pastresults12[i][e + 1] == 1:
        l[i].append("1|0 ")
      elif pastresults12[i][e + 1] == 0:
        l[i].append("0|1 ")
      else:
        l[i].append("?|? ")
      table += asp(rsp22[i][e][0][6], 40) + " " + asp(rsp22[i][e][0][0], 11) + l[i][e] + asp(rsp22[i][e][1][0], 11) + " " + asp(rsp22[i][e][1][6], 40) + "\n"
    table += "```"  # Ende des Code-Blocks
    print(table)
  for i in range(9):
    table = "```\n"  # Anfang des Code-Blocks
    l.append([])
    table += "Spieltag " + str(i + 10) + "\n"

    for e in range(5):
      if pastresults12[i + 9][e + 1] == 1:
        l[i + 9].append("1|0 ")
      elif pastresults12[i + 9][e + 1] == 0:
        l[i + 9].append("0|1 ")
      else:
        l[i + 9].append("?|? ")
      table += asp(rsp22[i][e][0][6], 40) + " " + asp(rsp22[i][e][0][0], 11) + l[i + 9][e] + asp(rsp22[i][e][1][0], 11) + " " + asp(rsp22[i][e][1][6], 40) + "\n"
    table += "```"  # Ende des Code-Blocks
    print(table)
  l = []
  for i in range(9):
    table = "```\n"  # Anfang des Code-Blocks
    l.append([])
    table += "Spieltag " + str(i + 1) + "\n"

    for e in range(5):
      if pastresults13[i][e + 1] == 1:
        l[i].append("1|0 ")
      elif pastresults13[i][e + 1] == 0:
        l[i].append("0|1 ")
      else:
        l[i].append("?|? ")
      table += asp(rsp23[i][e][0][6], 40) + " " + asp(rsp23[i][e][0][0], 11) + l[i][e] + asp(rsp23[i][e][1][0], 11) + " " + asp(rsp23[i][e][1][6], 40) + "\n"
    table += "```"  # Ende des Code-Blocks
    print(table)
  for i in range(9):
    table = "```\n"  # Anfang des Code-Blocks
    l.append([])
    table += "Spieltag " + str(i + 10) + "\n"

    for e in range(5):
      if pastresults13[i + 9][e + 1] == 1:
        l[i + 9].append("1|0 ")
      elif pastresults13[i + 9][e + 1] == 0:
        l[i + 9].append("0|1 ")
      else:
        l[i + 9].append("?|? ")
      table += asp(rsp23[i][e][0][6], 40) + " " + asp(rsp23[i][e][0][0], 11) + l[i + 9][e] + asp(rsp23[i][e][1][0], 11) + " " + asp(rsp23[i][e][1][6], 40) + "\n"
    table += "```"  # Ende des Code-Blocks
    print(table)
  enablePrint()
  incday()
  print("done")

def gameday2():

  day = 0
  day = int(getday())
  print(day)
  a1 = 12
  a2 = 4
  
  table1 = []

  pastresults11 = []
  pastresults12 = []
  pastresults13 = []
  
  table1, spielergen1, pastresults11, pastresults12, pastresults13 = spieltag2(
      day + 1)
  print(table1)
  table1 = sorted(table1, key=sortierfunktion)


  if len(table1) != 0:
    table = "```\n"  # Anfang des Code-Blocks
    if day + 1 in [7, 8, 9, 10, 17, 18, 19, 20, 27, 28, 29, 30]:
      if day + 1 in [7, 17, 27]:
        table += "TRANSFERTAG: " + str(1) + " von 4\n"
      elif day + 1 in [8, 18, 28]:
        table += "TRANSFERTAG: " + str(2) + " von 4\n"
      elif day + 1 in [9, 19, 29]:
        table += "TRANSFERTAG: " + str(3) + " von 4\n"
      elif day + 1 in [10, 20, 20]:
        table += "TRANSFERTAG: " + str(4) + " von 4\n"

    table += asp(str("# "), 2) + asp("TrainerName", a1) + " " + asp(
        "Win", a2) + " " + asp("Lose", a2) + " " + asp(
            "StatSum", a2) + " Totaldmg " + "\n"  # Kopfzeile
    for i in range(10):
      table += asp(str(i + 1), 2) + " " + asp(table1[i][0], a1) + " " + asp(
          str(table1[i][1]), a2) + " " + asp(str(
              table1[i][2]), a2) + " " + asp(
                  str(table1[i][4]), a2 + 3) + " " + asp(
                      str(table1[i][3]),
                      a2 + 2) + "  " + table1[i][6] + "\n"  # Kopfzeile
    table += "```"  # Ende des Code-Blocks
    print(table)
    if len(table1) != 0:
      table = "```\n"  # Anfang des Code-Blocks
      table += asp(str("# "), 2) + asp("TrainerName", a1) + " " + asp(
          "Win", a2) + " " + asp("Lose", a2) + " " + asp(
              "StatSum", a2) + "\n"  # Kopfzeile
      for i in range(10):
        table += asp(
            str(i + 1), 2) + " " + asp(table1[i + 10][0], a1) + " " + asp(
                str(table1[i + 10][1]),
                a2) + " " + asp(str(table1[i + 10][2]), a2) + " " + asp(
                    str(table1[i + 10][4]), a2 + 3) + " " + asp(
                        str(table1[i + 10][3]),
                        a2 + 2) + "  " + table1[i + 10][6] + "\n"  # Kopfzeile
      table += "```"  # Ende des Code-Blocks
    print(table)
    if len(table1) != 0:
      table = "```\n"  # Anfang des Code-Blocks
      table += asp(str("# "), 2) + asp("TrainerName", a1) + " " + asp(
          "Win", a2) + " " + asp("Lose", a2) + " " + asp(
              "StatSum", a2) + "\n"  # Kopfzeile
      for i in range(10):
        table += asp(
            str(i + 1), 2) + " " + asp(table1[i + 20][0], a1) + " " + asp(
                str(table1[i + 20][1]),
                a2) + " " + asp(str(table1[i + 20][2]), a2) + " " + asp(
                    str(table1[i + 20][4]), a2 + 3) + " " + asp(
                        str(table1[i + 20][3]),
                        a2 + 2) + "  " + table1[i + 20][6] + "\n"  # Kopfzeile
      table += "```"  # Ende des Code-Blocks
    print(table)
  # postet Spieltagergebnisse sowie kommende Matches
  blockPrint()
  table1 = ""

  l = []
  r = []
  table1 = []
  table2 = []
  spielergen1 = []
  spielergen2 = []
  spielergen3 = []
  pkmgen1 = []
  pastresults11 = []
  pastresults12 = []
  pastresults13 = []
  table1, spielergen1, pastresults11, pastresults12, pastresults13 = spieltag2( day + 1)

  rsp1 = []
  rsp21 = []
  rsp22 = []
  rsp23 = []
  rsp21 = rr2(table1[:10], day + 1)
  rsp22 = rr2(table1[10:-10], day + 1)
  rsp23 = rr2(table1[-10:], day + 1)

  for i in range(9):
    table = "```\n"  # Anfang des Code-Blocks
    l.append([])
    table += "Spieltag " + str(i + 1) + "\n"

    for e in range(5):
      if pastresults11[i][e + 1] == 1:
        l[i].append("1|0 ")
      elif pastresults11[i][e + 1] == 0:
        l[i].append("0|1 ")
      else:
        l[i].append("?|? ")
      table += asp(rsp21[i][e][0][6], 40) + " " + asp(
          rsp21[i][e][0][0], 11) + l[i][e] + asp(
              rsp21[i][e][1][0], 11) + " " + asp(rsp21[i][e][1][6], 40) + "\n"
    table += "```"  # Ende des Code-Blocks
    print(table)
  for i in range(9):
    table = "```\n"  # Anfang des Code-Blocks
    l.append([])
    table += "Spieltag " + str(i + 10) + "\n"

    for e in range(5):
      if pastresults11[i + 9][e + 1] == 1:
        l[i + 9].append("1|0 ")
      elif pastresults11[i + 9][e + 1] == 0:
        l[i + 9].append("0|1 ")
      else:
        l[i + 9].append("?|? ")
      table += asp(rsp21[i][e][0][6], 40) + " " + asp(
          rsp21[i][e][0][0], 11) + l[i + 9][e] + asp(
              rsp21[i][e][1][0], 11) + " " + asp(rsp21[i][e][1][6], 40) + "\n"
    table += "```"  # Ende des Code-Blocks
    print(table)
  l = []
  for i in range(9):
    table = "```\n"  # Anfang des Code-Blocks
    l.append([])
    table += "Spieltag " + str(i + 1) + "\n"

    for e in range(5):
      if pastresults12[i][e + 1] == 1:
        l[i].append("1|0 ")
      elif pastresults12[i][e + 1] == 0:
        l[i].append("0|1 ")
      else:
        l[i].append("?|? ")
      table += asp(rsp22[i][e][0][6], 40) + " " + asp(
          rsp22[i][e][0][0], 11) + l[i][e] + asp(
              rsp22[i][e][1][0], 11) + " " + asp(rsp22[i][e][1][6], 40) + "\n"
    table += "```"  # Ende des Code-Blocks
    print(table)
  for i in range(9):
    table = "```\n"  # Anfang des Code-Blocks
    l.append([])
    table += "Spieltag " + str(i + 10) + "\n"

    for e in range(5):
      if pastresults12[i + 9][e + 1] == 1:
        l[i + 9].append("1|0 ")
      elif pastresults12[i + 9][e + 1] == 0:
        l[i + 9].append("0|1 ")
      else:
        l[i + 9].append("?|? ")
      table += asp(rsp22[i][e][0][6], 40) + " " + asp(
          rsp22[i][e][0][0], 11) + l[i + 9][e] + asp(
              rsp22[i][e][1][0], 11) + " " + asp(rsp22[i][e][1][6], 40) + "\n"
    table += "```"  # Ende des Code-Blocks
    print(table)
  l = []
  for i in range(9):
    table = "```\n"  # Anfang des Code-Blocks
    l.append([])
    table += "Spieltag " + str(i + 1) + "\n"

    for e in range(5):
      if pastresults13[i][e + 1] == 1:
        l[i].append("1|0 ")
      elif pastresults13[i][e + 1] == 0:
        l[i].append("0|1 ")
      else:
        l[i].append("?|? ")
      table += asp(rsp23[i][e][0][6], 40) + " " + asp(
          rsp23[i][e][0][0], 11) + l[i][e] + asp(
              rsp23[i][e][1][0], 11) + " " + asp(rsp23[i][e][1][6], 40) + "\n"
    table += "```"  # Ende des Code-Blocks
    print(table)
  for i in range(9):
    table = "```\n"  # Anfang des Code-Blocks
    l.append([])
    table += "Spieltag " + str(i + 10) + "\n"

    for e in range(5):
      if pastresults13[i + 9][e + 1] == 1:
        l[i + 9].append("1|0 ")
      elif pastresults13[i + 9][e + 1] == 0:
        l[i + 9].append("0|1 ")
      else:
        l[i + 9].append("?|? ")
      table += asp(rsp23[i][e][0][6], 40) + " " + asp(
          rsp23[i][e][0][0], 11) + l[i + 9][e] + asp(
              rsp23[i][e][1][0], 11) + " " + asp(rsp23[i][e][1][6], 40) + "\n"
    table += "```"  # Ende des Code-Blocks
    print(table)
  enablePrint()
  print("done")



#gameday2()

#resetseason()
#start_Game()
#change1("get MISDREAVUS move3 RETURN")
#change1("scout GOREBYSS give CLEFABLE")

'''
def get_pokemon_image(name):
    # Finde die Nummer basierend auf dem Namen
    for number, pokemon_name in pokemon_mapping.items():
        if pokemon_name.lower() == name.lower():
            return f"{number}.png"  # oder der Pfad zum Bild
    return None  # Wenn das Pokémon nicht gefunden wird

def getalldb(tabelle):
    conn = sqlite3.connect('PokeData.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + tabelle)
    result = cursor.fetchall()

    # Überprüfe jede Zeile, ob sie nur NULL-Werte enthält
    cleaned_result = []
    for row in result:
        # Wenn alle Werte in der Zeile None sind, füge "?" ein
        if all(value is None for value in row):
            cleaned_result.append("?")
        else:
            cleaned_result.append(row)

    return cleaned_result
    
'''
class BlockingOverlay(Widget):
    # Ein unsichtbares Widget, das den gesamten Bildschirm abdeckt
    def on_touch_down(self, touch):
        return True  # Blockiere alle Touch-Ereignisse

    def on_touch_move(self, touch):
        return True  # Blockiere alle Touch-Ereignisse

    def on_touch_up(self, touch):
        return True  # Blockiere alle Touch-Ereignisse

class BaseScreen(Screen):
    frontendInit()
    overlay = BlockingOverlay()

        
    def confirm_page_change(self):
        # Layout für das Popup
        popup_layout = BoxLayout(orientation='vertical')
        label = Label(text='Kampf beginnen?')
        button_layout = BoxLayout(orientation='horizontal')

        # Bestätigungs- und Abbruch-Buttons
        confirm_button = Button(text='Ja')
        cancel_button = Button(text='Nein')

        button_layout.add_widget(confirm_button)
        button_layout.add_widget(cancel_button)

        popup_layout.add_widget(label)
        popup_layout.add_widget(button_layout)

        # Erstelle das Popup und speichere es als Instanzvariable
        self.popup = Popup(title='Bestätigung', content=popup_layout, size_hint=(0.7, 0.4))

        # Button-Funktionalität
        confirm_button.bind(on_press=self.fight)  # Richtiges Binden der Methode
        cancel_button.bind(on_press=self.popup.dismiss)

        # Zeige das Popup an
        self.popup.open()

    def fight(self, instance):
        # Logik, um das Spiel zu starten
        self.add_widget(self.overlay)
        print(player)
        self.remove_widget(self.overlay)
        # Schließe das Popup
        self.popup.dismiss()
        
    def confirm_reset(self, next_screen_name):
        # Layout für das Popup
        popup_layout = BoxLayout(orientation='vertical')
        label = Label(text='Game reseten?')
        button_layout = BoxLayout(orientation='horizontal')

        # Bestätigungs- und Abbruch-Buttons
        confirm_button = Button(text='Ja')
        cancel_button = Button(text='Nein')

        button_layout.add_widget(confirm_button)
        button_layout.add_widget(cancel_button)

        popup_layout.add_widget(label)
        popup_layout.add_widget(button_layout)

        # Erstelle das Popup
        popup = Popup(title='Bestätigung', content=popup_layout, size_hint=(0.7, 0.4))

        # Button-Funktionalität:
        confirm_button.bind(on_press=self.resetall(next_screen_name))
        cancel_button.bind(on_press=popup.dismiss)

        # Zeige das Popup an
        popup.open()
    def resetall(self,next_screen_name):
        self.add_widget(self.overlay)
        #resetGame

        self.reload_table_content()
        self.reload_plan()
        self.manager.current = next_screen_name
        self.remove_widget(self.overlay)

    def help_popup(self, next_screen_name):
        # Layout für das Popup
        popup_layout = BoxLayout(orientation='vertical')
        label1 = Label(text='Angriff ändern')
        label2 = Label(text='get PIKACHU move1 THUNDER')
        label3 = Label(text='')
        
        label4 = Label(text='Position ändern:')
        label5 = Label(text='get PIKACHU position 2')
        label6 = Label(text='')

        label7 = Label(text='Pokemon scounten:')
        label8 = Label(text='scout ONIX give PIKACHU')

        button_layout = BoxLayout(orientation='horizontal')

        # Bestätigungs- und Abbruch-Buttons
        cancel_button = Button(text='Danke!')

        button_layout.add_widget(cancel_button)

        popup_layout.add_widget(label1)
        
        popup_layout.add_widget(label2)
        
        popup_layout.add_widget(label3)
        
        popup_layout.add_widget(label4)
        
        popup_layout.add_widget(label5)
        
        popup_layout.add_widget(label6)

        
        popup_layout.add_widget(label7)
        
        popup_layout.add_widget(label8)

        popup_layout.add_widget(button_layout)

        # Erstelle das Popup
        popup = Popup(title='Help', content=popup_layout, size_hint=(0.7, 0.4))

        # Button-Funktionalität:
        cancel_button.bind(on_press=popup.dismiss)

        # Zeige das Popup an
        popup.open()
    # Funktion zum Wechseln der Seite
    def close_pop(popup):
        popup.dismiss()
    def change_page(self, popup, next_screen_name):
        # Schließe das Popup und wechsle zur nächsten Seite
        popup.dismiss()
        self.manager.current = next_screen_name
    def reload_table_content(self):
        # Lösche das bestehende `table_layout`-Widget aus `ScrollView`
        if self.scroll_view.children:
            self.scroll_view.clear_widgets()
        # Neues `table_layout` erstellen und konfigurieren
        self.table_layout = GridLayout(cols=1, padding=10, spacing=10, size_hint_y=None)
        self.table_layout.bind(minimum_height=self.table_layout.setter('height'))

        # Beispiel-Daten zur Tabelle hinzufügen
        for e in range(10):
            i = e + tabelleni * 10
            entry_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=80)
            
            # Erste Zeile
            row1 = GridLayout(cols=6, spacing=5, size_hint_y=None, height=40)
            row1.add_widget(Label(text=str(i % 10+1), size_hint_y=None, height=40))
            row1.add_widget(Label(text=leagueTable[i][1], size_hint_y=None, height=40))
            row1.add_widget(Label(text=str(leagueTable[i][3]), size_hint_y=None, height=40))
            row1.add_widget(Label(text=str(leagueTable[i][4]), size_hint_y=None, height=40))
            row1.add_widget(Label(text=str(leagueTable[i][10]), size_hint_y=None, height=40))
            row1.add_widget(Label(text=str(leagueTable[i][5]), size_hint_y=None, height=40))
            
            # Zweite Zeile
            row2 = GridLayout(cols=4, spacing=5, size_hint_y=None, height=40)
            row2.add_widget(Image(source="Pokepics\\" + fpng(words[i * 4]) + ".png"))
            row2.add_widget(Image(source="Pokepics\\" + fpng(words[i * 4 + 1]) + ".png"))
            row2.add_widget(Image(source="Pokepics\\" + fpng(words[i * 4 + 2]) + ".png"))
            row2.add_widget(Image(source="Pokepics\\" + fpng(words[i * 4 + 3]) + ".png"))

            # Füge Zeilen zu entry_layout hinzu
            entry_layout.add_widget(row1)
            entry_layout.add_widget(row2)
            
            # Füge das entry_layout zur Tabelle hinzu
            self.table_layout.add_widget(entry_layout)

        # Füge `table_layout` dem ScrollView hinzu
        self.scroll_view.add_widget(self.table_layout)
    def reload_plan(self):
        # Lösche das bestehende `table_layout`-Widget aus `ScrollView`
        self.add_widget(self.overlay)
        if self.scroll_view.children:
            self.scroll_view.clear_widgets()
        # Neues `table_layout` erstellen und konfigurieren
        self.table_layout = GridLayout(cols=1, padding=10, spacing=10, size_hint_y=None)
        self.table_layout.bind(minimum_height=self.table_layout.setter('height'))

        f=0
        for i in range (18):

          self.table_layout.add_widget(Label(text="Spieltag "+f"{i+1}", size_hint_y=None, height=40))

          for e in range(5):  # Beispielsweise 100 Zeilen
            # Eintrag-Layout als vertikales Layout für Zeilen 1 und 2
            
            if pastresults[tabelleni][i][e + 1] == 1:
              l[tabelleni].append("1|0")
            elif pastresults[tabelleni][i][e + 1] == 0:
              l[tabelleni].append("0|1")
            else:
              l[tabelleni].append("?|?")

            entry_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=80)
            
            # Erste Zeile mit 5 Spalten
            row1 = GridLayout(cols=3, spacing=5, size_hint_y=None, height=40)
            row1.add_widget(Label(text=rsp[tabelleni][i%9][e][0][0], size_hint_y=None, height=40))
            row1.add_widget(Label(text=l[tabelleni][f], size_hint_y=None, height=40))
            #row1.add_widget(Label(text="l[tabelleni][f]", size_hint_y=None, height=40))
            row1.add_widget(Label(text=rsp[tabelleni][i%9][e][1][0], size_hint_y=None, height=40))
            f= f+1
            tempwords=[]
            
            temp =rsp[tabelleni][i%9][e][0][6].split()
            tempwords.append(temp[0])
            tempwords.append(temp[1])
            tempwords.append(temp[2])
            tempwords.append(temp[3])
            temp =rsp[tabelleni][i%9][e][1][6].split()
            tempwords.append(temp[0])
            tempwords.append(temp[1])
            tempwords.append(temp[2])
            tempwords.append(temp[3])
              
            
            # Zweite Zeile mit 8 Spalten
            row2 = GridLayout(cols=8, spacing=5, size_hint_y=None, height=40)
            row2.add_widget(Image(source="Pokepics/" + fpng(tempwords[0]) + ".png", size_hint_y=None, height=40))
            row2.add_widget(Image(source="Pokepics/" + fpng(tempwords[1]) + ".png", size_hint_y=None, height=40))
            row2.add_widget(Image(source="Pokepics/" + fpng(tempwords[2]) + ".png", size_hint_y=None, height=40))
            row2.add_widget(Image(source="Pokepics/" + fpng(tempwords[3]) + ".png", size_hint_y=None, height=40))       
            row2.add_widget(Image(source="Pokepics/" + fpng(tempwords[4]) + ".png", size_hint_y=None, height=40))
            row2.add_widget(Image(source="Pokepics/" + fpng(tempwords[5]) + ".png", size_hint_y=None, height=40))
            row2.add_widget(Image(source="Pokepics/" + fpng(tempwords[6]) + ".png", size_hint_y=None, height=40))
            row2.add_widget(Image(source="Pokepics/" + fpng(tempwords[7]) + ".png", size_hint_y=None, height=40))
            

            #image_widget = Image(source="Pokepics/" + fpng(words[playeri * 4 + i]) + ".png", size_hint_y=None, height=40)
            #entry_layout11.add_widget(image_widget)
            # Füge die Zeilen zum Eintrag-Layout hinzu
            entry_layout.add_widget(row1)
            entry_layout.add_widget(row2)

            # Füge den Eintrag dem Haupt-Table-Layout hinzu
            self.table_layout.add_widget(entry_layout)

        # Füge `table_layout` dem ScrollView hinzu
        self.scroll_view.add_widget(self.table_layout)

        self.remove_widget(self.overlay)        
class MainScreen(BaseScreen):
    def __init__(self, **kwargs):



        super(MainScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical')
        # Erstelle das Hauptlayout
        mainmainwindow = BoxLayout(orientation='vertical')
        mainwindow1 = BoxLayout(orientation='vertical')
        mainwindow2 = BoxLayout(orientation='vertical')
        
        
        window1 = BoxLayout(orientation='horizontal')
        
        

           
        info11 = Label(text='Day:'+str(days[0]))
        info12 = Label(text='Liga:'+str(leagueTable[playeri][11]))
        info14 = Label(text="Pow:"+str(leagueTable[playeri][10]))
        print("playeri")
        print(playeri)
        print(playeri%10)
        
        info13 = Label(text='Place:'+str((playeri%10)+1))
        info15 = Label(text = 'W:'+str(leagueTable[playeri][3]))
        info16 = Label(text = 'L:'+str(leagueTable[playeri][4]))

        window2 = BoxLayout(orientation='horizontal')

        window21 = BoxLayout(orientation='vertical')
        window22 = BoxLayout(orientation='vertical')
        window23 = BoxLayout(orientation='vertical')
        window24 = BoxLayout(orientation='vertical')
        window25 = BoxLayout(orientation='vertical')
        window26 = BoxLayout(orientation='vertical')
        
        window27 = BoxLayout(orientation='vertical')
        window28 = BoxLayout(orientation='vertical')
        window29 = BoxLayout(orientation='vertical')
        print(playeri)
        info211 = Label(text =str( pokestats11[0][12]))
        info212 = Image(source="Pokepics\\"+fpng(words[playeri*4])+".png")

        window21.add_widget(info211)
        window21.add_widget(info212)

        info213 = Label(text = str( pokestats12[0][12]))
        info214 =  Image(source="Pokepics\\"+fpng(words[playeri*4+1])+".png")

        window22.add_widget(info213)
        window22.add_widget(info214)

        info215 = Label(text = str( pokestats13[0][12]))
        info216 =  Image(source="Pokepics\\"+fpng(words[playeri*4+2])+".png")

        window23.add_widget(info215)
        window23.add_widget(info216)
        info217 = Label(text = str( pokestats14[0][12]))
        info218 = Image(source="Pokepics\\"+fpng(words[playeri*4+3])+".png")

        window24.add_widget(info217)
        window24.add_widget(info218)

        info219 = Label(text = "VS")

        window25.add_widget(info219)

        info2111 = Label(text = "1")
        info2112 = Label(text = "O")

        window26.add_widget(info2111)
        window26.add_widget(info2112)

        info2113= Label(text = "1")
        info2114= Label(text = "O")

        window27.add_widget(info2113)
        window27.add_widget(info2114)

        info2115= Label(text = "1")
        info2116= Label(text = "O")
        window28.add_widget(info2115)
        window28.add_widget(info2116)

        info2117 = Label(text = "1")
        info2118 = Label(text = "O")
        
        window29.add_widget(info2117)
        window29.add_widget(info2118)

        window3 = BoxLayout(orientation='horizontal')

        info31 = Label(text = playername.title())
        info32 = Label(text = "Turner")

        

        window4 = BoxLayout(orientation='horizontal')
        window5 = BoxLayout(orientation='horizontal')
        window6 = BoxLayout(orientation='horizontal')
        window7 = BoxLayout(orientation='horizontal')
        window8 = BoxLayout(orientation = 'horizontal')

        window9 = BoxLayout(orientation = 'horizontal')
        info41 = Button(text = "FIGHT")
        info41.bind(on_press=lambda x: self.confirm_page_change())
        info51 = Button(text = "Show Table")
        info81 = Button(text = "Show Plan")
        
        info61 = Button(text = "Show Team")
        info71 = Button(text = "Settings")
        info51.bind(on_press=self.go_to_page_3)  
        info61.bind(on_press=self.go_to_page_4)  
        info71.bind(on_press=self.go_to_page_5)
        info81.bind(on_press=self.go_to_page_6)

        window1.add_widget(info11)
        window1.add_widget(info12)
        window9.add_widget(info13)
        window1.add_widget(info14)
        window9.add_widget(info15)
        window9.add_widget(info16)

        window2.add_widget(window21)
        window2.add_widget(window22)
        window2.add_widget(window23)
        window2.add_widget(window24)
        window2.add_widget(window25)
        window2.add_widget(window26)
        window2.add_widget(window27)
        window2.add_widget(window28)
        window2.add_widget(window29)
        
        window3.add_widget(info31)
        window3.add_widget(info32)

        window4.add_widget(info41)
        window5.add_widget(info51)
        window6.add_widget(info61)
        window7.add_widget(info71)
        window8.add_widget(info81)

        mainwindow1.add_widget(window1)
        mainwindow1.add_widget(window9)
        mainwindow1.add_widget(window2)
        mainwindow1.add_widget(window3)
        mainwindow2.add_widget(window4)
        mainwindow2.add_widget(window5)
        mainwindow2.add_widget(window8)
        mainwindow2.add_widget(window6)
        mainwindow2.add_widget(window7)
        mainmainwindow.add_widget(mainwindow1)
        mainmainwindow.add_widget(mainwindow2)

        layout.add_widget(mainmainwindow)
        self.add_widget(layout)


    # Funktion zum Wechseln zu Seite 2
    def go_to_page_2(self, instance):
        self.manager.current = 'second'
    def go_to_page_3(self, instance):
        self.manager.current = 'third11'
    def go_to_page_4(self, instance):
        self.manager.current = 'forth'    
    def go_to_page_5(self, instance):
        self.manager.current = 'fifth1'  
    def go_to_page_6(self, instance):
        self.manager.current = 'third12' 


# Definition der zweiten Seite
class SecondScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', size_hint=(1, 1))
        rootlayout1 = BoxLayout(orientation='vertical')
        rootlayout11 = BoxLayout(orientation='horizontal')
        rootlayout12 = BoxLayout(orientation='vertical',size_hint=(1, 0.3))
        rootlayout121 = BoxLayout(orientation='vertical')
        rootlayout122 = BoxLayout(orientation='vertical')
        
        
        rootlayout2 = BoxLayout(orientation='vertical')
        
        rootlayout1.add_widget(rootlayout11)
        rootlayout1.add_widget(rootlayout12)
        rootlayout11.add_widget(rootlayout121)
        rootlayout11.add_widget(rootlayout122)


        label1111=Label(text = 'Status',size_hint=(1, 0.2))
        label1112=Label(text = 'PokemonBild')

        rootlayout121.add_widget(label1111)
        rootlayout121.add_widget(label1112)
        
  	    
        label1121=Label(text = 'Status',size_hint=(1, 0.2))
        label1122=Label(text = 'PokemonBild')

        
        rootlayout122.add_widget(label1122)
        rootlayout122.add_widget(label1121)

        
        label1221=Label(text = 'Pokemon Kampf Geschehen')

        rootlayout12.add_widget(label1221)
        
        button = Button(text='Menu', size_hint=(None, None), size=(40,40), pos_hint={'right': 1, 'top': 1})
        button.bind(on_press=self.go_to_page_1)

        layout.add_widget(button)
        layout.add_widget(rootlayout1)
        
        layout.add_widget(rootlayout2)

        self.add_widget(layout)

    # Funktion zum Wechseln zu Seite 1
    def go_to_page_1(self, instance):
        self.manager.current = 'main'


# Definition der zweiten Seite
class ThirdScreen1(BaseScreen):
    def __init__(self, **kwargs):
        super(ThirdScreen1, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', size_hint=(1, 1))

        label1 = Label(text = 'sf')

        button1 = Button(text='Zeitplan')
        button1.bind(on_press=self.go_to_page_1)
        button2 = Button(text='Tabelle')
        button2.bind(on_press=self.go_to_page_2)
        
        layout.add_widget(label1)        
        layout.add_widget(button1)
        layout.add_widget(button2)

        self.add_widget(layout)

    # Funktion zum Wechseln zu Seite 1
    def go_to_page_1(self, instance):
        self.manager.current = 'third11'
    def go_to_page_2(self, instance):
        self.manager.current = 'third12'    


class ThirdScreen11(BaseScreen):
    def __init__(self, **kwargs):
        super(ThirdScreen11, self).__init__(**kwargs)
        
        # Haupt-Layout der Seite
        self.main_layout = BoxLayout(orientation='vertical')
        
        # Kopfzeile mit Buttons
        header_layout = BoxLayout(size_hint_y=None, height=50)
        
        # Buttons für Menü, Vorwärts und Zurück
        button1 = Button(text="Menu", size_hint_x=0.6, on_press=self.go_to_page_1)
        button2 = Button(text="<", size_hint_x=0.4, on_press=self.reload_content2)
        button3 = Button(text=">", size_hint_x=0.4, on_press=self.reload_content1)
        header_layout.add_widget(button2)
        header_layout.add_widget(Label(text="Table " + str(int(tabelleni + 1)), size_hint_x=0.8))
        header_layout.add_widget(button3)
        header_layout.add_widget(button1)
        
        # Überschriftenzeile für Tabelle
        row3 = GridLayout(cols=6, spacing=5, size_hint_y=None, height=90)
        row3.add_widget(Label(text="#", size_hint_y=None))
        row3.add_widget(Label(text="Trainer", size_hint_y=None))
        row3.add_widget(Label(text="W", size_hint_y=None))
        row3.add_widget(Label(text="L", size_hint_y=None))
        row3.add_widget(Label(text="Pow", size_hint_y=None))
        row3.add_widget(Label(text="Dmg", size_hint_y=None))
        
        self.main_layout.add_widget(header_layout)
        self.main_layout.add_widget(row3)
        
        # ScrollView erstellen
        self.scroll_view = ScrollView(size_hint=(1, 1))
        self.main_layout.add_widget(self.scroll_view)

        # Haupt-Layout der Seite dem Screen hinzufügen
        self.add_widget(self.main_layout)
        
        # Tabelle laden
        self.reload_table_content()



    def go_to_page_1(self, instance):
        self.manager.current = 'main'


    def reload_content2(self, instance):
        global tabelleni
        # Aktualisiere den Index und den Tabelleninhalt
        tabelleni = (tabelleni - 1) % 3
        self.reload_table_content()
    def reload_content1(self, instance):
        global tabelleni
        # Aktualisiere den Index und den Tabelleninhalt
        tabelleni = (tabelleni + 1) % 3
        self.reload_table_content()


class ThirdScreen12(BaseScreen):
    def __init__(self, **kwargs):
        super(ThirdScreen12, self).__init__(**kwargs)
        main_layout = BoxLayout(orientation='vertical')
        
        # Horizontales Layout für den Button oben rechts
        header_layout = BoxLayout(size_hint_y=None, height=50)

        
        button1 = Button(text="Menu", size_hint_x=0.4,on_press=self.go_to_page_1)
        button2 = Button(text="<",  size_hint_x=0.2,on_press=self.reload_content2)
        button3 = Button(text=">",  size_hint_x=0.2, on_press=self.reload_content2)
        header_layout.add_widget(button2)
        header_layout.add_widget(Label(text="Spielplan", size_hint_x=0.8))  # Ein Titel in der Mitte
        header_layout.add_widget(button3)
        header_layout.add_widget(button1)

        main_layout.add_widget(header_layout)
        # ScrollView und die Tabelle erstellen
        self.scroll_view = ScrollView(size_hint=(1, 1))

        table_layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None)
        table_layout.bind(minimum_height=table_layout.setter('height'))

        
        # Fügen Sie Daten zur Tabelle hinzu (hier nur Beispielwerte)
        #print(rsp21)
        #print(len(rsp21))
        f=0
        for i in range (18):

          table_layout.add_widget(Label(text="Spieltag "+f"{i+1}", size_hint_y=None, height=40))

          for e in range(5):  # Beispielsweise 100 Zeilen
            # Eintrag-Layout als vertikales Layout für Zeilen 1 und 2
            
            if pastresults[tabelleni][i][e + 1] == 1:
              l[tabelleni].append("1|0")
            elif pastresults[tabelleni][i][e + 1] == 0:
              l[tabelleni].append("0|1")
            else:
              l[tabelleni].append("?|?")

            entry_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=80)
            
            # Erste Zeile mit 5 Spalten
            row1 = GridLayout(cols=3, spacing=5, size_hint_y=None, height=40)
            row1.add_widget(Label(text=rsp[tabelleni][i%9][e][0][0], size_hint_y=None, height=40))
            row1.add_widget(Label(text=l[tabelleni][f], size_hint_y=None, height=40))
            #row1.add_widget(Label(text="l[tabelleni][f]", size_hint_y=None, height=40))
            row1.add_widget(Label(text=rsp[tabelleni][i%9][e][1][0], size_hint_y=None, height=40))
            f= f+1
            tempwords=[]
            
            temp =rsp[tabelleni][i%9][e][0][6].split()
            tempwords.append(temp[0])
            tempwords.append(temp[1])
            tempwords.append(temp[2])
            tempwords.append(temp[3])
            temp =rsp[tabelleni][i%9][e][1][6].split()
            tempwords.append(temp[0])
            tempwords.append(temp[1])
            tempwords.append(temp[2])
            tempwords.append(temp[3])
              
            
            # Zweite Zeile mit 8 Spalten
            row2 = GridLayout(cols=8, spacing=5, size_hint_y=None, height=40)
            row2.add_widget(Image(source="Pokepics/" + fpng(tempwords[0]) + ".png", size_hint_y=None, height=40))
            row2.add_widget(Image(source="Pokepics/" + fpng(tempwords[1]) + ".png", size_hint_y=None, height=40))
            row2.add_widget(Image(source="Pokepics/" + fpng(tempwords[2]) + ".png", size_hint_y=None, height=40))
            row2.add_widget(Image(source="Pokepics/" + fpng(tempwords[3]) + ".png", size_hint_y=None, height=40))       
            row2.add_widget(Image(source="Pokepics/" + fpng(tempwords[4]) + ".png", size_hint_y=None, height=40))
            row2.add_widget(Image(source="Pokepics/" + fpng(tempwords[5]) + ".png", size_hint_y=None, height=40))
            row2.add_widget(Image(source="Pokepics/" + fpng(tempwords[6]) + ".png", size_hint_y=None, height=40))
            row2.add_widget(Image(source="Pokepics/" + fpng(tempwords[7]) + ".png", size_hint_y=None, height=40))
            

            #image_widget = Image(source="Pokepics/" + fpng(words[playeri * 4 + i]) + ".png", size_hint_y=None, height=40)
            #entry_layout11.add_widget(image_widget)
            # Füge die Zeilen zum Eintrag-Layout hinzu
            entry_layout.add_widget(row1)
            entry_layout.add_widget(row2)

            # Füge den Eintrag dem Haupt-Table-Layout hinzu
            table_layout.add_widget(entry_layout)

        # Füge das Table-Layout zum ScrollView hinzu
        self.scroll_view.add_widget(table_layout)
        main_layout.add_widget(self.scroll_view)

        self.add_widget(main_layout)
    def go_to_page_1(self, instance):
        self.manager.current = 'main'     

    def reload_content1(self, instance):
        global tabelleni
        # Aktualisiere den Index und den Tabelleninhalt
        tabelleni = (tabelleni + 1) % 3
        self.reload_plan()
    def reload_content2(self, instance):
        global tabelleni
        # Aktualisiere den Index und den Tabelleninhalt
        tabelleni = (tabelleni - 1) % 3
        self.reload_plan()



class ForthScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(ForthScreen, self).__init__(**kwargs)
        main_layout = BoxLayout(orientation='vertical')
        
        # Horizontales Layout für den Button oben rechts
        header_layout = GridLayout(cols=4, spacing=5, size_hint_y=None, height=80)
        input_barlayout = BoxLayout(size_hint_y=None, height=50)
        text_input = TextInput(text='', size_hint_y=None, height=50)
        button2 = Button(text="Help", size_hint_x=0.2, on_press=self.help_popup)
        button3 = Button(text="input", size_hint_x=0.2, on_press=self.go_to_page_1)
        input_barlayout.add_widget(button2)
        input_barlayout.add_widget(text_input)
        input_barlayout.add_widget(button3)
        
        button1 = Button(text="Menu", size_hint_x=0.4, on_press=self.go_to_page_1)

        header_layout.add_widget(Label(text=playername.title(), size_hint_x=0.8))
        header_layout.add_widget(Label(text='D:'+str(days[0]), size_hint_x=0.8))
        header_layout.add_widget(Label(text='Lg:'+str(leagueTable[playeri][11]), size_hint_x=0.8))
        header_layout.add_widget(button1)
        header_layout.add_widget(Label(text="#"+str((playeri%10)+1), size_hint_x=0.8))
        
        header_layout.add_widget(Label(text="Pow:"+str(leagueTable[playeri][10]), size_hint_x=0.8))
        header_layout.add_widget(Label(text="W:"+str(leagueTable[playeri][3]), size_hint_x=0.8))
        header_layout.add_widget(Label(text="L:"+str(leagueTable[playeri][4]), size_hint_x=0.8))
        header_layout2 = BoxLayout(orientation='horizontal',size_hint_y=None, height=40)
        header_layout2.add_widget(Label(text="Abg: "+str(player[0][5])))
        header_layout2.add_widget(Label(text="Wun: "+str(player[0][6])))



        main_layout.add_widget(header_layout)
        main_layout.add_widget(header_layout2)        
        main_layout.add_widget(input_barlayout)

        # ScrollView und die Tabelle erstellen
        scroll_view = ScrollView(size_hint=(1, 1))

        # GridLayout für die Tabelle (cols=1 für eine Spalte, da jede Zeile eine Box mit 2 Reihen ist)
        table_layout = GridLayout(cols=1, padding=70, spacing=70, size_hint_y=None)
        table_layout.bind(minimum_height=table_layout.setter('height'))

        for i in range(4):  # Beispielsweise 4 Zeilen für Tests
            # Erhöhte Höhe für `entry_layout`, um Überschneidungen zu verhindern
            entry_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=100, spacing=10)

            # Gesamt-Layout für die beiden vertikalen Spalten
            # `entry_layout11` bekommt keinen Abstand auf der linken Seite
            entry_layout11 = BoxLayout(orientation='vertical', size_hint_x=0.2, height=100, padding=(0, 0))
            entry_layout12 = BoxLayout(orientation='vertical', size_hint_x=0.2, height=100, padding=(0, 0))
            entry_layout13 = BoxLayout(orientation='vertical', size_hint_x=0.9, height=100, padding=(0, 0))
            # Erstelle die obere Zeile mit Image, Attack1 und Attack2
            image_widget = Image(source="Pokepics/" + fpng(words[playeri * 4 + i]) + ".png", size_hint_y=None, height=40)
            entry_layout11.add_widget(image_widget)

            label1 = Label(text=str(pokestats[i][0][12]), size_hint_y=None, height=40)
            entry_layout11.add_widget(label1)

            # Weitere Labels für entry_layout12
            label2 = Label(text=pokestats[i][0][18], size_hint_y=None, height=40)
            entry_layout12.add_widget(label2)

            label3 = Label(text=pokestats[i][0][19], size_hint_y=None, height=40)
            entry_layout12.add_widget(label3)

            # Zweite Zeile für weitere Informationen
            label4 = Label(text=pokestats[i][0][0], size_hint_y=None, height=40)
            entry_layout11.add_widget(label4)

            label5 = Label(text=pokestats[i][0][20], size_hint_y=None, height=40)
            entry_layout12.add_widget(label5)

            label6 = Label(text=pokestats[i][0][21], size_hint_y=None, height=40)
            entry_layout12.add_widget(label6)

            # Füge die beiden vertikalen Layouts zur horizontalen BoxLayout hinzu
            entry_layout.add_widget(entry_layout11)
            entry_layout.add_widget(entry_layout13)
            entry_layout.add_widget(entry_layout12)

            # Füge den Eintrag dem Haupt-Table-Layout hinzu
            table_layout.add_widget(entry_layout)


        # Tabelle zum ScrollView hinzufügen

        scroll_view.add_widget(table_layout)
        main_layout.add_widget(scroll_view)

        self.add_widget(main_layout)

    def go_to_page_1(self, instance):
        self.manager.current = 'main'


class FifthScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(FifthScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        # Erstelle das Hauptlayout
        mainmainwindow = BoxLayout(orientation='vertical')
        mainwindow1 = BoxLayout(orientation='vertical')
        
        
        window1 = BoxLayout(orientation='horizontal')
        
        
        
        
        info11 = Label(text='Settings')

        
        


        

        window4 = BoxLayout(orientation='horizontal')
        window7 = BoxLayout(orientation='horizontal')
        window8 = BoxLayout(orientation='horizontal')

        info41 = Button(text = "Reset Game")
        info71 = Button(text = "Back")
        info81 = Button(text = "Exit Game")
        
        info41.bind(on_press=lambda x: self.confirm_reset('main'))
        info71.bind(on_press=self.go_to_page_1)
          

        window1.add_widget(info11)
        

        window4.add_widget(info41)
        window7.add_widget(info71)
        window8.add_widget(info81)

        mainwindow1.add_widget(window1)
        mainwindow1.add_widget(window4)
        mainwindow1.add_widget(window7)
        mainwindow1.add_widget(window8)

        mainmainwindow.add_widget(mainwindow1)

        layout.add_widget(mainmainwindow)
        self.add_widget(layout)


    # Funktion zum Wechseln zu Seite 2
    def go_to_page_1(self, instance):
        self.manager.current = 'main'


class TestApp(App):
    def build(self):
        # Erstelle einen ScreenManager
        sm = ScreenManager()

        # Füge die zwei Seiten (Screens) zum ScreenManager hinzu
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen1(name='third1'))
        sm.add_widget(ThirdScreen11(name='third11'))
        sm.add_widget(ThirdScreen12(name='third12'))
        sm.add_widget(ForthScreen(name='forth'))
        sm.add_widget(FifthScreen(name='fifth1'))
        sm.add_widget(FifthScreen(name='fifth11'))        
        
        #sm.add_widget(SecondScreen(name='third12'))

        return sm




if __name__ == '__main__':
    TestApp().run()



