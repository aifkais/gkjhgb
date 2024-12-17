import sqlite3

class Pokelib:

  def __init__(self):
    self.poke_list1 = []
    self.poke_list2 = []
    self.poke_list3 = []
    self.makePokeList()

  def makePokeList(self):
    conn = sqlite3.connect('database.db')

    # Cursor erstellen
    cursor = conn.cursor()

    # SQL-Anweisung ausführen
    cursor.execute('SELECT column_name FROM table_name')

    # Ergebnis abrufen
    results = cursor.fetchall()

    # Daten aus den Ergebniszeilen in das Array einfügen
    for result in results:
        self.poke_list1.append(result[0])
        

    # Verbindung schließen
    conn.close()


