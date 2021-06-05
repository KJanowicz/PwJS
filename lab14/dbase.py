import sqlite3

if __name__ == "__main__":

    conn = sqlite3.connect('database.db')
    print("BD otwarta")
    
    conn.execute('CREATE TABLE praacownicy (imienazwisko TEXT, nrpracownika TEXT, adres TEXT)')
    print("Tabela utworzona")
    
    conn.close()
    print("BD zamknieta")
    
    conn = sqlite3.connect('database.db')
    print("BD otwarta")
    cur = conn.cursor()
    
    cur.execute("INSERT INTO praacownicy (imienazwisko, nrpracownika, adres) VALUES (?,?,?)",('Karol Janowicz','1','Elblag') )
    cur.execute("INSERT INTO praacownicy (imienazwisko, nrpracownika, adres) VALUES (?,?,?)",('Jan Kowalski','2','Olsztyn') )
    conn.commit()
    
    cur.execute('SELECT * FROM praacownicy ORDER BY nrpracownika')
    print(cur.fetchall())
    
    conn.close()
    print("BD zamknieta")