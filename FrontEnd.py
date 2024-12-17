from Fight import getProfile
from Utility import asp, asp2


def showprofile(id, table):
  p1 = []
  #[(347156882374262795, 'Tony', 2, 'acetrainerf', 0, None, None)]
  p2 = []
  #[(216, 'acetrainerf', 'ELEKID SKIPLOOM UNOWN CHINCHOU', 0, 0, None, None, 5000000, None, None, 1366, 1)]
  p3 = []
  #[[('ELEKID', 'Elekid', 'Electric', '', '360', 45, 63, 37, 65, 55, 95, 255, 1, None, None, None, None, None...

  p1, p2, p3 = getProfile(id)
  table = "```\n"
  table += "Trainer " + p1[0][3] + " Wins:" + str(p2[0][3]) + " Losses:" + str(
      p2[0][4]) + "\n"
  table += "Transferwunsch: " + str(p1[0][5]) + " | ABGABEPKM: " + str(
      p1[0][6]) + "\n"
  table += "# Pokemon| Move1 Move2 Move3 Move4 Strategy\n"
  table += "1 " + p3[0][0][0] + " " + p3[0][0][18] + " " + p3[0][0][
      19] + " " + p3[0][0][20] + " " + p3[0][0][21] + " " + str(
          p3[0][0][12]) + "\n"
  table += "2 " + p3[1][0][0] + " " + p3[1][0][18] + " " + p3[1][0][
      19] + " " + p3[1][0][20] + " " + p3[1][0][21] + " " + str(
          p3[1][0][12]) + "\n"
  table += "3 " + p3[2][0][0] + " " + p3[2][0][18] + " " + p3[2][0][
      19] + " " + p3[2][0][20] + " " + p3[2][0][21] + " " + str(
          p3[2][0][12]) + "\n"
  table += "4 " + p3[3][0][0] + " " + p3[3][0][18] + " " + p3[3][0][
      19] + " " + p3[3][0][20] + " " + p3[3][0][21] + " " + str(
          p3[3][0][12]) + "\n"
  table += "```"  # Ende des Code-Blocks

  return table


def gethelp(table):
  table = "```\n"
  table += "Profil anzeigen:\n"
  table += "show\n\n"
  table += "Angriff ändern:\n"
  table += "get PIKACHU move1 THUNDER\n\n"
  table += "Position ändern:\n"
  table += "get PIKACHU position 2\n\n"
  table += "Pokemon scouten:\n"
  table += "scout ONIX give PIKACHU\n"

  table += "```"  # Ende des Code-Blocks
  return table
