import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.executescript(open('tabla.sql', 'r').read())
conn.close()

print("La tabla 'usuarios' ha sido creada exitosamente.")
