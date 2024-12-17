import random
import sqlite3
"""
#from Pokelib import Pokelib
from Spieler import Spieler
"""

startBudget11 = [620, 550, 470, 310, 240, 190, 170, 150, 120, 50]
startBudget12 = [110, 100, 50, 32, 25, 24, 20, 18, 16, 12, 7]
startBudget13 = [8, 8, 6, 5, 4, 4, 4, 3, 3, 2]
startBudget21 = [500, 150, 110, 100, 60, 40, 30, 20]
startBudget22 = [15, 14, 13, 9, 8, 6, 6, 5, 5]
startBudget31 = [480, 250, 230, 150, 110, 80, 50, 30, 20]
startBudget32 = [22, 19, 17, 15, 13, 9, 8, 7, 6]
startBudget33 = [6, 5, 4, 4, 3, 3, 2, 2, 2]
startBudget1 = [
    620, 550, 470, 310, 240, 190, 170, 150, 120, 50, 110, 100, 50, 32, 25, 24,
    20, 18, 16, 12, 7, 8, 8, 6, 5, 4, 4, 4, 3, 3
]
startBudget2 = [
    500, 150, 110, 100, 60, 40, 30, 20, 15, 14, 13, 9, 8, 6, 6, 5, 5, 4
]
startBudget3 = [
    480, 250, 230, 150, 110, 80, 50, 30, 20, 22, 19, 17, 15, 13, 9, 8, 7, 6, 6,
    5, 4, 4, 3, 3, 2, 2, 2
]
gen1TrainerName = [
    "acetrainerf", "acetrainerm", "aromalady", "beauty", "biker", "birdkeeper",
    "blackbelt", "bugcatcher", "burglar", "camper", "channeler", "coolcouple",
    "crushgirl", "crushkin", "engineer", "fisherman", "gamer", "gentleman",
    "hiker", "juggler", "lady", "lass", "painter", "picnicker", "pokemaniac",
    "pokemonbreeder", "pokemonrangerf", "pokemonrangerm", "psychicf",
    "psychicm", "rocker", "roughneck", "ruinmaniac", "sailor", "scientist",
    "sisandbro", "supernerd", "swimmerf", "swimmerm", "tamer",
    "teamrocketgruntf", "teamrocketgruntm", "tuberf", "tuberm", "twins",
    "youngcouple", "youngster"
]
gen2TrainerName = [
    "acetrainerf", "acetrainerm", "beauty", "biker", "birdkeeper", "blackbelt",
    "boarder", "boyandgirl", "bugcatcher", "burglar", "doubleteam",
    "firebreather", "gentleman", "juggler", "kimonogirl", "lady", "lass",
    "loveycouple", "medium", "pokemaniac", "rocketgruntf", "rocketgruntm",
    "sage", "schoolkid", "scientist", "skier", "supernerd", "swimmerf",
    "swimmerm", "twins", "youngster"
]
gen3TrainerName = [
    "acetrainerf", "acetrainerm", "aquagruntf", "aquagruntm", "aromalady",
    "battlegirl", "beauty", "birdkeeper", "blackbelt", "bugcatcher",
    "bugmaniac", "camper", "collector", "dragontamer", "expertf", "expertm",
    "fisherman", "gentleman", "guitarist", "hexmaniac", "hiker", "interviewer",
    "kindler", "lady", "lass", "magmagruntf", "magmagruntm", "ninjaboy",
    "oldcouple", "parasollady", "picnicker", "pokefanf", "pokefanm",
    "pokemaniac", "pokemonbreederf", "pokemonbreederm", "pokemonrangerf",
    "pokemonrangerm", "psychicf", "psychicm", "richboy", "ruinmaniac",
    "sailor", "schoolkidf", "schoolkidm", "sisandbro", "srandjr", "swimmerf",
    "swimmerm", "triathletecyclistf", "triathletecyclistm",
    "triathleterunnerf", "triathleterunnerm", "triathleteswimmerf",
    "triathleteswimmerm", "tuberf", "tuberm", "tucker", "twins", "youngcouple",
    "youngster"
]
gen1Liga1 = []
gen1Liga2 = []
gen1Liga3 = []
gen2Liga1 = []
gen2Liga2 = []
gen3Liga3 = []
gen3Liga1 = []
gen3Liga2 = []
poke_list = []
mio = 1000000


def gameinit():
  random.shuffle(gen1TrainerName)
  random.shuffle(gen2TrainerName)
  random.shuffle(gen3TrainerName)

  werte = (0, "", 0, 0)
  izahl = 0
  sql_befehl = "INSERT INTO Trainer1Gen (TrainerID,TrainerName,Geld,Liga) VALUES (?,?,?,?)"
  initTrainer(werte, sql_befehl, izahl, gen1TrainerName, startBudget1, 1)
  sql_befehl = "INSERT INTO Trainer2Gen ('TrainerID','TrainerName','Geld','Liga') VALUES (?,?,?,?)"
  initTrainer(werte, sql_befehl, izahl, gen2TrainerName, startBudget2, 2)
  sql_befehl = "INSERT INTO Trainer3Gen ('TrainerID','TrainerName','Geld','Liga') VALUES (?,?,?,?)"
  initTrainer(werte, sql_befehl, izahl, gen3TrainerName, startBudget3, 3)


def initTrainer(werte, sql_befehl, izahl, genTrainerName, startBudget,
                genzahl):
  izahl = len(startBudget)

  conn = sqlite3.connect('PokeData.db')
  cursor = conn.cursor()
  f = 0
  try:
    for i in range(izahl):
      if i % izahl / 3 == 0:
        f += 1
      werte = (100 * genzahl + i + 1, genTrainerName[i], startBudget[i] * mio,
               f)
      cursor.execute(sql_befehl, (werte))
    conn.commit()
  except sqlite3.Error as e:
    conn.rollback()
    print("Fehler:", e)
  finally:
    conn.close()


def initPokemontoTrainer():
  conn = sqlite3.connect('PokeData.db')
  cursor = conn.cursor()

  try:
    cursor.execute("SELECT Species FROM PokeStats1 ORDER BY Total DESC")
    result = cursor.fetchall()
    ras = [tupel_to_string(t) for t in result]

    g = 0
    for i in range(30):
      g = g + 1
      i = i * 4
      v1 = ""
      v2 = ""
      v3 = ""
      v4 = ""

      v1 = ras[i]
      v2 = ras[i + 1]
      v3 = ras[i + 2]
      v4 = ras[i + 3]

      #arr = rm(result[i]) + rm(result[i + 1]) + rm(result[i + 2]) + rm(result[i + 3])
      sql_befehl = "UPDATE Trainer1Gen SET Pokemon = ? WHERE TrainerID =" + str(
          100 + g)
      name = [v1 + " " + v2 + " " + v3 + " " + v4]
      cursor.execute(sql_befehl, name)
    cursor.execute("SELECT Total FROM PokeStats1 ORDER BY Total DESC")
    result = cursor.fetchall()
    g = 0
    for i in range(30):
      g = g + 1
      i = i * 4
      ges = result[i] + result[i + 1] + result[i + 2] + result[i + 3]
      summe = [sum(int(x) for x in ges)]
      sql_befehl = "UPDATE Trainer1Gen SET Stärke = ? WHERE TrainerID =" + str(
          100 + g)
      cursor.execute(sql_befehl, summe)

  except sqlite3.Error as e:
    print("Fehler:", e)

  finally:
    conn.commit()
    # Verbindung zur Datenbank schließen
    conn.close()

  conn.close()
  conn = sqlite3.connect('PokeData.db')
  cursor = conn.cursor()
  try:
    cursor.execute("SELECT Species FROM PokeStats2 ORDER BY Total DESC")

    result = cursor.fetchall()
    ras = [tupel_to_string(t) for t in result]

    g = 0
    for i in range(18):
      g = g + 1
      i = i * 4
      v1 = ""
      v2 = ""
      v3 = ""
      v4 = ""

      v1 = ras[i]
      v2 = ras[i + 1]
      v3 = ras[i + 2]
      v4 = ras[i + 3]

      #arr = rm(result[i]) + rm(result[i + 1]) + rm(result[i + 2]) + rm(result[i + 3])
      sql_befehl = "UPDATE Trainer2Gen SET Pokemon = ? WHERE TrainerID =" + str(
          200 + g)
      name = [v1 + " " + v2 + " " + v3 + " " + v4]
      cursor.execute(sql_befehl, name)
    cursor.execute("SELECT Total FROM PokeStats2 ORDER BY Total DESC")
    result = cursor.fetchall()
    g = 0
    for i in range(18):
      g = g + 1
      i = i * 4
      ges = result[i] + result[i + 1] + result[i + 2] + result[i + 3]
      summe = [sum(int(x) for x in ges)]
      sql_befehl = "UPDATE Trainer2Gen SET Stärke = ? WHERE TrainerID =" + str(
          200 + g)
      cursor.execute(sql_befehl, summe)

  except sqlite3.Error as e:
    print("Fehler:", e)

  finally:
    conn.commit()
    # Verbindung zur Datenbank schließen
    conn.close()

  conn.close()
  conn = sqlite3.connect('PokeData.db')
  cursor = conn.cursor()
  try:
    cursor.execute("SELECT Species FROM PokeStats3 ORDER BY Total DESC")
    result = cursor.fetchall()
    ras = [tupel_to_string(t) for t in result]

    g = 0
    for i in range(27):
      g = g + 1
      i = i * 4
      v1 = ""
      v2 = ""
      v3 = ""
      v4 = ""

      v1 = ras[i]
      v2 = ras[i + 1]
      v3 = ras[i + 2]
      v4 = ras[i + 3]

      #arr = rm(result[i]) + rm(result[i + 1]) + rm(result[i + 2]) + rm(result[i + 3])
      sql_befehl = "UPDATE Trainer3Gen SET Pokemon = ? WHERE TrainerID =" + str(
          300 + g)
      name = [v1 + " " + v2 + " " + v3 + " " + v4]
      cursor.execute(sql_befehl, name)
    cursor.execute("SELECT Total FROM PokeStats3 ORDER BY Total DESC")
    result = cursor.fetchall()
    g = 0
    for i in range(27):
      g = g + 1

      i = i * 4
      ges = result[i] + result[i + 1] + result[i + 2] + result[i + 3]
      summe = [sum(int(x) for x in ges)]
      sql_befehl = "UPDATE Trainer3Gen SET Stärke = ? WHERE TrainerID =" + str(
          300 + g)
      cursor.execute(sql_befehl, summe)

  except sqlite3.Error as e:
    print("Fehler:", e)

  finally:
    conn.commit()
    # Verbindung zur Datenbank schließen
    conn.close()

  conn.close()


def rm(t):

  return str(t).replace("(", "").replace(")", "")


def rmc(s):
  return s[2:-3]


def tupel_to_string(tupel):
  
  return ''.join(str(e) for e in tupel)
  
def tupel_to_string2(tupel):
  return ' '.join(str(e) for e in tupel)

"""
def game_Init2():

  
  e = 0
  
  for i in range(10):
    gen1Liga1.append(Spieler(1,1100+i,gen1TrainerName[e+1], "", startBudget11[i]*mio,0,0, 0, 0))
    gen1Liga2.append(Spieler(1,1200+i,gen1TrainerName[e+1], "", startBudget12[i]*mio,0,0, 0, 0))
    gen1Liga3.append(Spieler(1,1300+i,gen1TrainerName[e+1], "", startBudget13[i]*mio,0,0, 0, 0))
  e = 0
  f = 0
  for i in range(9):
    gen2Liga1.append(Spieler(2,2100+i,gen2TrainerName[e+1], "", startBudget21[i]*mio,0,0, 0, 0))
    gen2Liga2.append(Spieler(2,2200+i,gen2TrainerName[e+1], "", startBudget22[i]*mio,0,0, 0, 0))
    gen3Liga1.append(Spieler(3,3100+i,gen3TrainerName[f+1], "", startBudget31[i]*mio,0,0, 0, 0))
    gen3Liga2.append(Spieler(3,3200+i,gen3TrainerName[f+1], "", startBudget32[i]*mio,0,0, 0, 0))
    gen3Liga3.append(Spieler(3,3300+i,gen3TrainerName[f+1], "", startBudget33[i]*mio,0,0, 0, 0))
    e =0
    f = 0

#Pokelib = Pokelib()
"""
