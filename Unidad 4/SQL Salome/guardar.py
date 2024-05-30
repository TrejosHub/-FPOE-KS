import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

nombre = input("Ingrese nombre: ")
correo = input("Ingrese correo: ")
edad = int(input("Ingrese edad: "))

cursor.execute('''
    INSERT INTO usuarios (nombre, correo, edad)
    VALUES (?, ?, ?)
''', (nombre, correo, edad))

conn.commit()
conn.close()

print(f'El usuario {nombre} ha sido guardado exitosamente.')
