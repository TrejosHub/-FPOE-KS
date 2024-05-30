import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM usuarios')
filas = cursor.fetchall()

conn.close()

for usuario in filas:
    print(usuario)
