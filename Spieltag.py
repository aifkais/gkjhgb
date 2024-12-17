from Fight import getData, linetoArr, fightmatch, boi, onematch, coltoArr5, coltoArr, getalldb, wintodb, delcell, coltoreset, wintodb2, getcell
from KaderTemplate import showTemplate
from Game_Init import gameinit
from Game_Init import initTrainer
from Game_Init import initPokemontoTrainer
import random

spieltagpla1 = [  #g1,g23,eu,cl,rl,tf
    [1, 2],
    [1],  #1
    [4],
    [1, 2],
    [1, 2],
    [3, 4],
    [1, 2],
    [1, 2],
    [6],
    [6],  #5
    [6],
    [6],
    [1],
    [4],
    [1, 2],
    [1, 2],
    [4],
    [1, 2],
    [1, 2],
    [3, 4],
    [1, 2],
    [1],  #10
    [6],
    [6],
    [6],
    [6],
    [4],
    [1, 2],
    [1, 2],
    [4],
    [1],
    [1, 2],
    [4],
    [1, 2],  #15
    [5],
    [3],
    [5],
    [4]  #17
]

spieltagplan1 = [  #g1,g23,eu,cl,rl,tf
    [1], [1], [1], [1], [1], [1], [6], [6], [6], [6], [1], [1], [1], [1], [1],
    [1], [6], [6], [6], [6], [1], [1], [1], [1], [1], [1], [6], [6], [6], [6],
    [7]
]

spieltagplan = [  #g1,g23,eu,cl,rl,tf
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [6],
    [6],
    [6],
    [6],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [6],
    [6],
    [6],
    [6],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [6],
    [6],
    [6],
    [6],
]

players = [
    "psychicm", "psychicf", "beauty", "rocker", "hiker", "twins", "supernerd",
    "engineer", "lass", "gamer"
]

players2 = ["1", "2", "3", "4", "5", "6", "7", "8"]


def softresetData():  #end
  print("Reset")


def giveIDs():  #end
  print()


def announceWinners():  #end
  print()

  #reset Data


def spieltag(tag):
  pkmgen1 = []
  spielergen1 = []
  spielergen2 = []
  spielergen3 = []
  spielerlist = []
  spieltage = []
  spieltage2 = []
  tableeintrag = []
  table1 = []
  table2 = []
  table3 = []
  result11 = []
  result12 = []
  result13 = []
  pastresults11 = []
  pastresults12 = []
  pastresults13 = []
  spieltage = getspielplan(tag)  #return [1,2,3,4,5,6]
  spieltage2 = getspielplan(tag - 1)
  spieltage2 = [x - y for x, y in zip(spieltage, spieltage2)]
  spieltage = [x * y for x, y in zip(spieltage, spieltage2)]
  spielergen1 = coltoArr5("Trainer1Gen", "Trainername",
                          spielergen1)  #liste aller Trainer aus Gen1
  pkmgen1 = coltoArr5("Trainer1Gen", "Pokemon", pkmgen1)
  pastresults11 = getalldb("SpieltagGen11")
  pastresults12 = getalldb("SpieltagGen12")
  pastresults13 = getalldb("SpieltagGen13")
  allespieler=[]
  allespieler = coltoArr("Spieler", "TrainerName", allespieler)

  if spieltage2[0] == 1:

    result11 = generate_round_robin(spielergen1[:-20], 1,
                                    tag,allespieler)  # Alle Win lose Results
    result12 = generate_round_robin(spielergen1[10:20], 1,
                                    tag,allespieler)  # Alle Win lose Results
    result13 = generate_round_robin(spielergen1[20:], 1, tag,allespieler)
    for i in range(5):
      wintodb("SpieltagGen11", "Field" + str(i + 1), result11[i], "ROWID",
              tag)
      wintodb("SpieltagGen12", "Field" + str(i + 1), result12[i], "ROWID",
              tag)

      wintodb("SpieltagGen13", "Field" + str(i + 1), result13[i], "ROWID",
              tag)

  #print(result11)
  #print(result12)
  #print(result13)
  table1 = getTable(1, spielergen1, table1)  #erstelle Tabellen einträge

  print("pkmgen1")  
  print(pkmgen1)
  print(len(table1))
  print(table1)

  for i in range(len(table1)):  # füge Pokemon hinzu
    table1[i].append(pkmgen1[i])

  table1 = sorted(table1, key=sortierfunktion)  # sortiere Tabelle nach gewinn

  #print(table1)
  #def getcell(tabelle, x, y, ywert):
  if spieltage2[5]:
    transferzahl = 0

    #def wintodb2(Tabelle, x, xwert, y, ywert):
    wintodb2("Spieltage", "Transfertag", str(1), "ROWID", str(1))
    transferzahl = getcell("Spieltage", "Transfertag", "ROWID", str(1))

    print("Transfertag")
    spieler = []
    spieler = getalldb("Spieler")
    #print()
    #print(table1)
    #print()
    #print(spieler)

    for i in range(len(table1)):
      for e in range(len(spieler)):
        if table1[i][0] == spieler[e][3]:
          if spieler[e][4] == 0:  #hat er schon Tranfer gemacht?
            if spieler[e][5] != None:  #Will er überhaupt nen Transfer machen?
              print(
                  spieler[e]
                  [1])  #def pokeaccess1(trainername, gen, pokemon1, pokemon2):
              pokeaccess2(spieler[e][1], spieler[e][5], spieler[e][6], table1)
    table1 = getsortettable()
    if transferzahl == 4:
      wintodb("Spieltage", "Transfertag", str(0), "ROWID", str(1))
      coltoreset("Spieler", "TransferZahl", 0)
    #darf der Spieler Transfers betätigen?
    #spieler (341326268765306890, 'Si', 1, 'crushgirl', 0, 'TYRANITAR', 'STANTLER')
    """
    for i in range(len(spieler)):
      if spieler[i][4] == 0:  #hat er schon Tranfer gemacht?
        if spieler[i][5] != None:  #Will er überhaupt nen Transfer machen?
          print(spieler[i]
                [1])  #def pokeaccess1(trainername, gen, pokemon1, pokemon2):
          pokeaccess2(spieler[i][1], spieler[i][5], spieler[i][6], table1)
      if tag == 12 or tag == 26:
        print("Check")
        #wintodb("Spieler", "TransferZahl", 0, "TrainerName", spieler[i][4])
        coltoreset("Spieler", "TransferZahl", 0)

    #ist das pokemon erreichbar?
    """
  return table1, spielergen1, pastresults11, pastresults12, pastresults13


def spieltag2(tag):
  pkmgen1 = []
  spielergen1 = []
  spielergen2 = []
  spielergen3 = []
  spielerlist = []
  spieltage = []
  spieltage2 = []
  tableeintrag = []
  table1 = []
  table2 = []
  table3 = []
  result11 = []
  result12 = []
  result13 = []
  pastresults11 = []
  pastresults12 = []
  pastresults13 = []
  spieltage = getspielplan(tag)  #return [1,2,3,4,5,6]
  spieltage2 = getspielplan(tag - 1)
  spieltage2 = [x - y for x, y in zip(spieltage, spieltage2)]
  spieltage = [x * y for x, y in zip(spieltage, spieltage2)]

  spielergen1 = coltoArr5("Trainer1Gen", "Trainername",
                          spielergen1)  #liste aller Trainer aus Gen1
  pkmgen1 = coltoArr5("Trainer1Gen", "Pokemon", pkmgen1)
  pastresults11 = getalldb("SpieltagGen11")
  pastresults12 = getalldb("SpieltagGen12")
  pastresults13 = getalldb("SpieltagGen13")
  table1 = getTable(1, spielergen1, table1)  #erstelle Tabellen einträge
  for i in range(len(table1)):
    table1[i].append(pkmgen1[i])

    #wintodb("Spieler","TransferZahl",temp5, "TrainerName",spieler[i][4])

    #ist das pokemon erreichbar?

  return table1, spielergen1, pastresults11, pastresults12, pastresults13


def pokeaccess1(trainername, gen, pokemon1, pokemon2):
  index = 0
  temptable = []
  temptable2 = []
  accessTrainer = []
  pokelist = []
  pokelist2 = []
  table1 = []
  table2 = []
  table3 = []
  mtable = [table1, table2, table3]
  spielergen1 = []
  spielergen2 = []
  spielergen3 = []
  mspielergen = [spielergen1, spielergen2, spielergen3]
  colarr = ["Trainer1Gen", "Trainer2Gen", "Trainer3Gen"]  #gen= 2
  for i in range(
      3):  #Spielerliste und Table initialisieren abhängig von der Genzahl
    if gen == i + 1:
      mspielergen[i] = coltoArr5(colarr[i], "Trainername", mspielergen[i])
      mtable[i] = getTable2(i + 1, mspielergen[i], mtable[i])
      index = mspielergen[i].index(trainername)
      if 1 / 3 * len(mtable[i]) >= index:  # Liga1

        temptable = mtable[i][:int(1 / 3 * len(mtable[i]))]
        temptable2 = mtable[i][int(1 / 3 * len(mtable[i])):]
      if 1 / 3 * len(mtable[i]) < index <= 2 / 3 * len(mtable[i]):  # Liga2
        print("Liga2")
        temptable = mtable[i][int(1 / 3 * len(mtable[i])):int(2 / 3 *
                                                              len(mtable[i]))]
        temptable2 = mtable[i][int(2 / 3 * len(mtable[i])):]
      if 2 / 3 * len(mtable[i]) <= index:  # Liga3
        print("Liga3")
        temptable = mtable[i][int(-1 / 3 * len(mtable[i])):]

  temptable = sorted(temptable, key=sortierfunktion)

  for idx, sublist in enumerate(temptable):
    if trainername in sublist:
      index = idx
      break
  temptable = temptable[index:]
  temptable3 = temptable + temptable2

  temp = ""
  for i in range(len(temptable3)):
    temp += temptable3[i][1] + " "
  temp2 = []
  temp2 = splitteam(temp, temp2)

  spielerpkm = []
  spielerpkm = getalldb("Spieler")

  forbidden = []
  for i in range(len(spielerpkm)):
    if spielerpkm[i][2] == gen:
      forbidden.append(spielerpkm[i][3])

  print(forbidden)
  allpkm = []
  #coltoArr("PokeStats" + str(gen), "Species", allpkm)
  coltoArr("PokeStats", "Species", allpkm)
  difference = list(set(allpkm) - set(temp2))
  temp2.extend(difference)
  print(temp2)
  index = 0

  for i in range(len(temp2)):
    if pokemon1 == temp2[i]:
      index = i // 4
      if index <= len(temptable3):
        if temptable3[index][0] in forbidden:
          print("Fehlgeschlagen, kein Zugriff auf Pkm von aktiven Spielern")
          return
        else:
          print("Erfolg / Switch mit Trainer" + temptable3[index][0])
          temp4 = []
          temp4 = splitteam(
              getcell("Trainer" + str(gen) + "Gen", "Pokemon", "Trainername",
                      temptable3[index][0]), temp4)
          temp5 = ""
          for i in range(len(temp4)):
            if pokemon1 == temp4[i]:
              temp4[i] = pokemon2
            temp5 += temp4[i] + " "
          #wintodb("Trainer"+str(gen)+"Gen","Pokemon",temp5, "Trainername",temptable3[index][0])
          delcell("Trainer" + str(gen) + "Gen", "Pokemon", "Trainername",
                  temptable3[index][0])

          temp4 = splitteam(
              getcell("Trainer" + str(gen) + "Gen", "Pokemon", "Trainername",
                      trainername), temp4)
          temp5 = ""
          for i in range(len(temp4)):
            if pokemon2 == temp4[i]:
              temp4[i] = pokemon1
            temp5 += temp4[i] + " "
          #wintodb("Trainer"+str(gen)+"Gen","Pokemon",temp5, "Trainername",trainername)
          #wintodb("Spieler","Pokemon",1, "Trainername",temptable3[index][0])
          delcell("Spieler", "TransferWunsch", "Trainername", trainername)
          delcell("Spieler", "PokeAbgang", "Trainername", trainername)
          return
      else:
        print("Erfolg")
        temp4 = []
        temp4 = splitteam(
            getcell("Trainer" + str(gen) + "Gen", "Pokemon", "Trainername",
                    temptable3[index][0]), temp4)
        temp5 = ""
        for i in range(len(temp4)):
          if pokemon1 == temp4[i]:
            temp4[i] = pokemon2
          temp5 += temp4[i] + " "
        #wintodb("Trainer"+str(gen)+"Gen","Pokemon",temp5, "Trainername",temptable3[index][0])
        #wintodb("Spieler","Pokemon",1, "Trainername",temptable3[index][0])
        delcell("Spieler", "TransferWunsch", "Trainername", trainername)
        delcell("Spieler", "PokeAbgang", "Trainername", trainername)
        return
  print("Fehlgeschlagen, kein Zugriff auf Pkm von höheren Platzierten")


def pokeaccess2(trainername, pokemon1, pokemon2, table1):
  temptable = table1
  pokemon_list = []
  forbidden_list = []
  pokemon1index = 0
  pokemon2index = 0
  forbidden_list2 = []
  trainer_names = []
  trainer_names = coltoArr("Spieler", "TrainerName", trainer_names)

  for entry in table1:
    if entry[0] in trainer_names:
      pokemon_list2 = entry[-1].split()  # Trennen der Pokémon in der Liste
      forbidden_list2.extend(pokemon_list2)

  # Erstellt Liste aller Pokemon der gesamten Liga
  for entry in table1:
    pokemon_string = entry[-1]
    pokemon = pokemon_string.split()
    pokemon_list.extend(pokemon)

  #findet den Index wo sich Pokemon1 befindet
  for i, entry in enumerate(table1):
    if pokemon1 in entry[-1]:
      pokemon1index = i
      break
  #findet den Index wo sich Pokemon2 befindet
  for i, entry in enumerate(table1):
    if pokemon2 in entry[-1]:
      pokemon2index = i
      break

  # erstellt Liste Aller Pokemon die verboten sind
  for entry in table1[:pokemon2index + 1]:
    pokemon_string = entry[-1]
    pokemon = pokemon_string.split()
    forbidden_list.extend(pokemon)

  print(pokemon_list)
  print(forbidden_list)
  print(pokemon1index)
  print(pokemon2index)

  if pokemon1 in forbidden_list2:
    print("Fehlgeschlagen, kein Zugriff auf Pkm von aktiven Spielern")
    return
  if pokemon1 in forbidden_list:
    print("pokemon nicht erreichbar")

    return
  if pokemon1 in pokemon_list:

    for entry in temptable:  # tauscht das gewünschte Pokemon mit dem pkm2
      if pokemon1 in entry[-1]:
        entry[-1] = entry[-1].replace(pokemon1, pokemon2)
      elif pokemon2 in entry[-1]:
        entry[-1] = entry[-1].replace(pokemon2, pokemon1)
    #def wintodb(Tabelle, x, xwert, y, ywert):
    wintodb("Trainer1Gen", "Pokemon", temptable[pokemon1index][6],
            "Trainername", temptable[pokemon1index][0])
    wintodb("Trainer1Gen", "Pokemon", temptable[pokemon2index][6],
            "Trainername", temptable[pokemon2index][0])

    wintodb("Trainer1Gen", "Stärke", totalstats(temptable[pokemon1index][0]),
            "Trainername", temptable[pokemon1index][0])
    wintodb("Trainer1Gen", "Stärke", totalstats(temptable[pokemon2index][0]),
            "Trainername", temptable[pokemon2index][0])

    wintodb("Spieler", "TransferZahl", 1, "Trainername",
            temptable[pokemon2index][0])
    delcell("Spieler", "TransferWunschliste", "Name", trainername)
    delcell("Spieler", "PokeAbgänger", "Name", trainername)

  else:
    for entry in temptable:  # tauscht das gewünschte Pokemon mit dem pkm2
      if pokemon2 in entry[-1]:
        entry[-1] = entry[-1].replace(pokemon2, pokemon1)
    wintodb("Trainer1Gen", "Pokemon", temptable[pokemon2index][6],
            "Trainername", temptable[pokemon2index][0])
    wintodb("Trainer1Gen", "Stärke", totalstats(temptable[pokemon2index][0]),
            "Trainername", temptable[pokemon2index][0])
    
    wintodb("Spieler", "TransferZahl", 1, "Trainername",
            temptable[pokemon2index][0])
    delcell("Spieler", "TransferWunschliste", "Name", trainername)
    delcell("Spieler", "PokeAbgänger", "Name", trainername)


def pokeaccess3(trainername, pokemon1, pokemon2, table1):
  temptable = table1
  pokemon_list = []
  forbidden_list = []
  pokemon1index = 0
  pokemon2index = 0
  forbidden_list2 = []
  trainer_names = []
  trainer_names = coltoArr("Spieler", "TrainerName", trainer_names)

  for entry in table1:
    if entry[0] in trainer_names:
      pokemon_list2 = entry[-1].split()  # Trennen der Pokémon in der Liste
      forbidden_list2.extend(pokemon_list2)

  # Erstellt Liste aller Pokemon der gesamten Liga
  for entry in table1:
    pokemon_string = entry[-1]
    pokemon = pokemon_string.split()
    pokemon_list.extend(pokemon)

  #findet den Index wo sich Pokemon1 befindet
  for i, entry in enumerate(table1):
    if pokemon1 in entry[-1]:
      pokemon1index = i
      break
  #findet den Index wo sich Pokemon2 befindet
  for i, entry in enumerate(table1):
    if pokemon2 in entry[-1]:
      pokemon2index = i
      break

  # erstellt Liste Aller Pokemon die verboten sind
  for entry in table1[:pokemon2index + 1]:
    pokemon_string = entry[-1]
    pokemon = pokemon_string.split()
    forbidden_list.extend(pokemon)

  print(pokemon_list)
  print(forbidden_list)
  print(pokemon1index)
  print(pokemon2index)

  if pokemon1 in forbidden_list2:
    print("Fehlgeschlagen, kein Zugriff auf Pkm von aktiven Spielern")
    return
  if pokemon1 in forbidden_list:
    print("pokemon nicht erreichbar")

    return
  if pokemon1 in pokemon_list:

    for entry in temptable:  # tauscht das gewünschte Pokemon mit dem pkm2
      if pokemon1 in entry[-1]:
        entry[-1] = entry[-1].replace(pokemon1, pokemon2)
      elif pokemon2 in entry[-1]:
        entry[-1] = entry[-1].replace(pokemon2, pokemon1)
    #def wintodb(Tabelle, x, xwert, y, ywert):
    wintodb("Trainer1Gen", "Pokemon", temptable[pokemon1index][6],
            "Trainername", temptable[pokemon1index][0])
    wintodb("Trainer1Gen", "Pokemon", temptable[pokemon2index][6],
            "Trainername", temptable[pokemon2index][0])

    wintodb("Trainer1Gen", "Stärke", totalstats(temptable[pokemon1index][0]),
            "Trainername", temptable[pokemon1index][0])
    wintodb("Trainer1Gen", "Stärke", totalstats(temptable[pokemon2index][0]),
            "Trainername", temptable[pokemon2index][0])

    wintodb("Spieler", "TransferZahl", 1, "Trainername",
            temptable[pokemon2index][0])
    delcell("Spieler", "TransferWunschliste", "Name", trainername)
    delcell("Spieler", "PokeAbgänger", "Name", trainername)

  else:
    for entry in temptable:  # tauscht das gewünschte Pokemon mit dem pkm2
      if pokemon2 in entry[-1]:
        entry[-1] = entry[-1].replace(pokemon2, pokemon1)
    wintodb("Trainer1Gen", "Pokemon", temptable[pokemon2index][6],
            "Trainername", temptable[pokemon2index][0])
    wintodb("Trainer1Gen", "Stärke", totalstats(temptable[pokemon2index][0]),
            "Trainername", temptable[pokemon2index][0])
    
    wintodb("Spieler", "TransferZahl", 1, "Trainername",
            temptable[pokemon2index][0])
    delcell("Spieler", "TransferWunschliste", "Name", trainername)
    delcell("Spieler", "PokeAbgänger", "Name", trainername)


"""


  return
"""


#z.B getcell("Trainer"+str(gen)+"Gen","Lose","TrainerName",Spielerliste[i])
def totalstats(trainername):
  newtotalstats = 0
  ps1 = 0
  ps2 = 0
  ps3 = 0
  ps4 = 0
  pokemonstring = ""
  pokeliste = []
  pokemonstring = getcell("Trainer1Gen", "Pokemon", "Trainername", trainername)
  pokeliste = pokemonstring.split(" ")
  ps1 = getcell("PokeStats", "Total", "Species", pokeliste[0])
  ps2 = getcell("PokeStats", "Total", "Species", pokeliste[1])
  ps3 = getcell("PokeStats", "Total", "Species", pokeliste[2])
  ps4 = getcell("PokeStats", "Total", "Species", pokeliste[3])
  newtotalstats = int(ps1) + int(ps2) + int(ps3) + int(ps4)
  return newtotalstats


def pokeaccess(trainername, gen, pokemon1, pokemon2):
  index = 0
  temptable = []
  temptable2 = []
  accessTrainer = []
  pokelist = []
  pokelist2 = []
  table1 = []
  table2 = []
  table3 = []
  mtable = [table1, table2, table3]
  spielergen1 = []
  spielergen2 = []
  spielergen3 = []
  mspielergen = [spielergen1, spielergen2, spielergen3]
  colarr = ["Trainer1Gen", "Trainer2Gen", "Trainer3Gen"]  #gen= 2
  for i in range(
      3):  #Spielerliste und Table initialisieren abhängig von der Genzahl
    if gen == i + 1:
      mspielergen[i] = coltoArr5(colarr[i], "Trainername", mspielergen[i])
      mtable[i] = getTable2(i + 1, mspielergen[i], mtable[i])
      index = mspielergen[i].index(trainername)
      if 1 / 3 * len(mtable[i]) >= index:  # Liga1

        temptable = mtable[i][:int(1 / 3 * len(mtable[i]))]
        temptable2 = mtable[i][int(1 / 3 * len(mtable[i])):]
      if 1 / 3 * len(mtable[i]) < index <= 2 / 3 * len(mtable[i]):  # Liga2
        print("Liga2")
        temptable = mtable[i][int(1 / 3 * len(mtable[i])):int(2 / 3 *
                                                              len(mtable[i]))]
        temptable2 = mtable[i][int(2 / 3 * len(mtable[i])):]
      if 2 / 3 * len(mtable[i]) <= index:  # Liga3
        print("Liga3")
        temptable = mtable[i][int(-1 / 3 * len(mtable[i])):]
  temptable3 = temptable + temptable2
  temptable = sorted(temptable, key=sortierfunktion)
  for idx, sublist in enumerate(temptable):
    if trainername in sublist:
      index = idx
      break

  temptable = temptable[index + 1:]

  for i in range(len(temptable)):
    pokelist.append(temptable[i][1])
  for i in range(len(pokelist)):
    word_list = pokelist[i].split()
    for word in word_list:
      pokelist2.append(word)
  pokelist = []
  for i in range(len(temptable2)):
    pokelist.append(temptable2[i][1])
  for i in range(len(pokelist)):
    word_list = pokelist[i].split()
    for word in word_list:
      pokelist2.append(word)
  spielerpkm = []
  spielerpkm = getalldb("Spieler")

  forbidden = []
  for i in range(len(spielerpkm)):
    if spielerpkm[i][2] == gen:
      forbidden.append(spielerpkm[i][3])
  forbidden2 = []
  for i in range(len(forbidden)):
    for sublist in temptable3:
      if sublist[0] == forbidden[i]:
        forbidden2.extend(sublist[1].split())
  #print(pokelist2)
  #print(temptable3)

  for sublist in temptable:
    if pokemon1 in sublist[1]:
      temp3 = sublist[0]
      temp = sublist[1].split(" ")
      temp.remove(pokemon1)
      temp.append(pokemon2)
      temp2 = " ".join(temp)
      #wintodb("Trainer"+str(gen)+"Gen","Pokemon",temp2,"TrainerName",temp3)
  temp4 = []
  temp4 = linetoArr("Trainer" + str(gen) + "Gen", "TrainerName", trainername,
                    temp4)
  temp5 = temp4[0][2]
  temp5 = temp5.replace(pokemon1, pokemon2)
  #wintodb("Trainer"+str(gen)+"Gen","Pokemon",temp2,"TrainerName",trainername)
  if pokemon1 in (forbidden2):
    print(forbidden2)
    print("Fehlschlag")
    return False
  if pokemon1 in (pokelist2):
    print(pokelist2)
    print("Erfolg")
    return True


def sortierfunktion(elem):
  return (elem[5], -elem[1], elem[4], -elem[3])


#def getPlayerdb():


def getTable(gen, Spielerliste, tableeintrag):
  for i in range(len(Spielerliste)):
    trainername = getcell("Trainer" + str(gen) + "Gen", "TrainerName",
                          "TrainerName", Spielerliste[i])
    loses = getcell("Trainer" + str(gen) + "Gen", "Lose", "TrainerName",
                    Spielerliste[i])
    wins = getcell("Trainer" + str(gen) + "Gen", "Win", "TrainerName",
                   Spielerliste[i])
    staerke = getcell("Trainer" + str(gen) + "Gen", "Stärke", "TrainerName",
                      Spielerliste[i])
    totaldamage = getcell("Trainer" + str(gen) + "Gen", "Totaldamage",
                          "TrainerName", Spielerliste[i])
    liga = getcell("Trainer" + str(gen) + "Gen", "Liga", "TrainerName",
                   Spielerliste[i])
    tableeintrag.append([trainername, wins, loses, totaldamage, staerke, liga])
  return tableeintrag


def getTable2(gen, Spielerliste, tableeintrag):
  for i in range(len(Spielerliste)):
    name = getcell("Trainer" + str(gen) + "Gen", "TrainerName", "TrainerName",
                   Spielerliste[i])
    pokemon = getcell("Trainer" + str(gen) + "Gen", "Pokemon", "TrainerName",
                      Spielerliste[i])
    loses = getcell("Trainer" + str(gen) + "Gen", "Lose", "TrainerName",
                    Spielerliste[i])
    wins = getcell("Trainer" + str(gen) + "Gen", "Win", "TrainerName",
                   Spielerliste[i])
    staerke = getcell("Trainer" + str(gen) + "Gen", "Stärke", "TrainerName",
                      Spielerliste[i])
    tableeintrag.append([name, pokemon, wins, loses, staerke])
  return tableeintrag


def gettable(gen, liga, Spielerliste, tableeintrag):
  tableeintrag = []  #Wins, Loses,Stärke
  for i in range(10):
    loses = getcell("Trainer" + str(gen) + "Gen", "Lose", "TrainerName",
                    Spielerliste[i + 10 * liga - 1])
    wins = getcell("Trainer" + str(gen) + "Gen", "Win", "TrainerName",
                   Spielerliste[i + 10 * liga - 1])
    staerke = getcell("Trainer" + str(gen) + "Gen", "Stärke", "TrainerName",
                      Spielerliste[i + 10 * liga - 1])
    tableeintrag.append(loses, wins, staerke)
  return tableeintrag


def getsortettable():
  pkmgen1 = []
  spielergen1 = []
  table1 = []
  spielergen1 = coltoArr5("Trainer1Gen", "Trainername",
                          spielergen1)  #liste aller Trainer aus Gen1
  pkmgen1 = coltoArr5("Trainer1Gen", "Pokemon", pkmgen1)

  table1 = getTable(1, spielergen1, table1)  #erstelle Tabellen einträge
  for i in range(len(table1)):  # füge Pokemon hinzu
    table1[i].append(pkmgen1[i])

  table1 = sorted(table1, key=sortierfunktion)  # sortiere Tabelle nach gewinn
  return table1


def aufabstieg():
  pkmgen1 = []
  spielergen1 = []
  table1 = []
  spielergen1 = coltoArr5("Trainer1Gen", "Trainername",
                          spielergen1)  #liste aller Trainer aus Gen1
  pkmgen1 = coltoArr5("Trainer1Gen", "Pokemon", pkmgen1)

  table1 = getTable(1, spielergen1, table1)  #erstelle Tabellen einträge
  for i in range(len(table1)):  # füge Pokemon hinzu
    table1[i].append(pkmgen1[i])

  table1 = sorted(table1, key=sortierfunktion)  # sortiere Tabelle nach gewinn
  id1 = ""
  id2 = ""
  id3 = ""
  id4 = ""
  id5 = ""
  id6 = ""
  id7 = ""
  id8 = ""
  #get TrainerID
  #z.B getcell("Trainer"+str(gen)+"Gen","Lose","TrainerName",Spielerliste[i])
  id1 = getcell("Trainer1Gen", "TrainerID", "TrainerName", table1[8][0])
  id2 = getcell("Trainer1Gen", "TrainerID", "TrainerName", table1[9][0])
  id3 = getcell("Trainer1Gen", "TrainerID", "TrainerName", table1[10][0])
  id4 = getcell("Trainer1Gen", "TrainerID", "TrainerName", table1[11][0])
  id5 = getcell("Trainer1Gen", "TrainerID", "TrainerName", table1[18][0])
  id6 = getcell("Trainer1Gen", "TrainerID", "TrainerName", table1[19][0])
  id7 = getcell("Trainer1Gen", "TrainerID", "TrainerName", table1[20][0])
  id8 = getcell("Trainer1Gen", "TrainerID", "TrainerName", table1[21][0])

  wintodb("Trainer1Gen", "TrainerName", table1[10][0], "TrainerID", id1)
  wintodb("Trainer1Gen", "Pokemon", table1[10][6], "TrainerID", id1)
  wintodb("Trainer1Gen", "Stärke", table1[10][4], "TrainerID", id1)
    
  wintodb("Trainer1Gen", "TrainerName", table1[11][0], "TrainerID", id2)
  wintodb("Trainer1Gen", "Pokemon", table1[11][6], "TrainerID", id2)
  wintodb("Trainer1Gen", "Stärke", table1[11][6], "TrainerID", id2)

  wintodb("Trainer1Gen", "TrainerName", table1[8][0], "TrainerID", id3)
  wintodb("Trainer1Gen", "Pokemon", table1[8][6], "TrainerID", id3)
  wintodb("Trainer1Gen", "Stärke", table1[8][6], "TrainerID", id3)
    
  wintodb("Trainer1Gen", "TrainerName", table1[9][0], "TrainerID", id4)
  wintodb("Trainer1Gen", "Pokemon", table1[9][6], "TrainerID", id4)
  wintodb("Trainer1Gen", "Stärke", table1[9][6], "TrainerID", id4)
    
  wintodb("Trainer1Gen", "TrainerName", table1[20][0], "TrainerID", id5)
  wintodb("Trainer1Gen", "Pokemon", table1[20][6], "TrainerID", id5)
  wintodb("Trainer1Gen", "Stärke", table1[20][6], "TrainerID", id5)
    
  wintodb("Trainer1Gen", "TrainerName", table1[21][0], "TrainerID", id6)
  wintodb("Trainer1Gen", "Pokemon", table1[21][6], "TrainerID", id6)
  wintodb("Trainer1Gen", "Stärke", table1[21][6], "TrainerID", id6)
    
  wintodb("Trainer1Gen", "TrainerName", table1[18][0], "TrainerID", id7)
  wintodb("Trainer1Gen", "Pokemon", table1[18][6], "TrainerID", id7)
  wintodb("Trainer1Gen", "Stärke", table1[18][6], "TrainerID", id7)
    
  wintodb("Trainer1Gen", "TrainerName", table1[19][0], "TrainerID", id8)
  wintodb("Trainer1Gen", "Pokemon", table1[19][6], "TrainerID", id8)
  wintodb("Trainer1Gen", "Stärke", table1[19][6], "TrainerID", id8)
  """
  for i, index in enumerate([9, 10, 11, 12, 19, 20, 21, 22]):
    row_index = 10 + i if i < 4 else 18 + i
    wintodb("Trainer1Gen", "TrainerName", table1[index][0], "ROWID", str(row_index))
    wintodb("Trainer1Gen", "Pokemon", table1[index][1], "ROWID", str(row_index))
  """
  #def wintodb(Tabelle, x, xwert, y, ywert):


def changeID(spieler1, spieler2):
  print("")


def generate_round_robin(players, gen, spieltag,allespieler):
  if len(players) % 2 != 0:
    players.append("Bye")
  num_rounds = len(players) - 1
  erg = []
  round_matchups = []
  for round_num in range(spieltag - 1):
    players = [players[0]] + [players[-1]] + players[1:-1]
  for i in range(len(players) // 2):
    erg.append(onematch("Liga 2", players[i], gen, players[-i - 1], gen,allespieler))
    round_matchups.append((players[i], players[-i - 1]))
  #matchups.append(round_matchups)
  return erg


# Beispiel für 10 Spieler


def printrobin():
  round_robin = generate_round_robin(players)

  # Ausgabe der Paarungen für jede Runde
  for i, round_matchups in enumerate(round_robin):
    print("Runde", i + 1)
    for matchup in round_matchups:
      print(matchup[0], "vs", matchup[1])
    print()


#onematch("fickifici","birdkeeper",3,"psychicm",1)


def season():
  spieltagnr = 0
  spieltag(spieltagnr)


def spieltag1(spieltag):
  if spieltag == 0:
    allfight()


def allfight():
  print()
  onematch()


def getspielplan(spieltag):
  spieltagzähler = [0, 0, 0, 0, 0, 0]
  for i in range(spieltag):
    for e in range(len(spieltagplan[i])):
      spieltagzähler[spieltagplan[i][e] - 1] += 1
  return spieltagzähler


def splitteam(team, list1):
  list1 = team.split()
  return list1


def rr2(players, rundentag):
  rundentag -= 1
  if len(players) % 2 != 0:
    players.append("Bye")
  num_rounds = len(players) - 1
  matchups = []
  for round_num in range(num_rounds):
    round_matchups = []
    for i in range(len(players) // 2):
      round_matchups.append((players[i], players[-i - 1]))
    matchups.append(round_matchups)
    players = [players[0]] + [players[-1]] + players[1:-1]
  return matchups




