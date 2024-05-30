import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

usuario_id = int(input("Ingrese el ID del usuario a actualizar: "))
nombre = input("Ingrese nuevo nombre: ")
correo = input("Ingrese nuevo correo: ")
edad = int(input("Ingrese nueva edad: "))

cursor.execute('''
    UPDATE usuarios
    SET nombre = ?, correo = ?, edad = ?
    WHERE id = ?
''', (nombre, correo, edad, usuario_id))

conn.commit()
conn.close()

print(f'El usuario con ID {usuario_id} ha sido actualizado exitosamente.')
