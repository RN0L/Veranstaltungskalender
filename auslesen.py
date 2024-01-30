import sqlite3 

 
connection = sqlite3.connect('database.db') 
connection .row_factory = sqlite3.Row 

cur = connection.cursor() 
cur.execute("SELECT name, anzahl FROM einkaufsliste;") 

rows = cur.fetchall() 

connection.close() 

for row in rows:
    print(row[2])