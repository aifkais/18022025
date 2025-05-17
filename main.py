
import os
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
  table1 += "Pokemonmeister der 1. Liga ist " + table[0][0] + " mit " + table[0][
      6] + "\n"
  table1 += "Glückwunsch an " + table[0][0] + "\n\n"
  table1 += "Vizemeister der 1.Liga ist " + table[1][0] + " mit " + table[1][
      6] + "\n"
  table1 += "Glückwunsch an " + table[1][0] + "\n\n"
  table1 += "2. Liga Pokemonmester ist " + table[10][0] + " mit " + table[10][
      6] + "\n"
  table1 += "Glückwunsch an " + table[10][0] + "\n\n"
  table1 += "2.Liga Pokemonvizemeister ist " + table[11][0] + " mit " + table[
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
  if (day >=7 and day<=10):
    day = day-1
    print(day)
  if (day >=17 and day<=20):
    day =day-1
  if(day >= 25):
    day = 24

  table1, spielergen1, pastresults11, pastresults12, pastresults13 = spieltag2(day + 1)

  rsp1 = []
  rsp21 = []
  rsp22 = []
  rsp23 = []
  rsp21 = rr2(table1[:10], day + 1)
  rsp22 = rr2(table1[10:-10], day + 1)
  rsp23 = rr2(table1[-10:], day + 1)
  compacttable = []
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
    compacttable.append(table)
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
    compacttable.append(table)
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
    compacttable.append(table)
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
    compacttable.append(table)
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
    compacttable.append(table)
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
    compacttable.append(table)
  

  diff = 0
  diff = convert_day_to_index(day)
  print(day)
  print(compacttable[day-diff])
  print(compacttable[day+1-diff])
  
  print(compacttable[day+18-diff])
  print(compacttable[day+19-diff])
  
  print(compacttable[day+36-diff])
  print(compacttable[day+37-diff])
  
  
  incday()
  #frontendInit()
  print("done")


def convert_day_to_index(day):
    day_to_index = {
    0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
    6: 1, 7: 2, 8: 3, 9: 3, 10: 4, 11: 4, 12: 4, 13: 4, 14: 4, 15: 4,
    16: 5, 17: 6, 18: 7, 19: 7, 20: 8, 21: 8, 22: 8, 23: 8, 24: 8, 25: 8,
    26: 9, 27: 10, 28: 11, 29: 11}
    if 0 <= day < len(day_to_index):
        return day_to_index[day]


def gameday2():

  day = 0
  day = int(getday())
  a1 = 12
  a2 = 4
  
  table1 = []

  pastresults11 = []
  pastresults12 = []
  pastresults13 = []
  
  table1, spielergen1, pastresults11, pastresults12, pastresults13 = spieltag2(day + 1)
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
    #print(table)
  enablePrint()

  print("doney")



#gameday2()
resetseason()
start_Game()
#change1("get ABRA move2 PSYCHIC")
#change1("scout ABRA give SEVIPER")
#change1("help")
#change1("show")

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
