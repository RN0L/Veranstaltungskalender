import sqlite3 
 
connection = sqlite3.connect('database.db') 
cur = connection.cursor() 
 
cur.execute("INSERT INTO einkaufsliste (name, anzahl) VALUES ('Bananen', '6');") 
 
connection.commit() 
connection.close() 