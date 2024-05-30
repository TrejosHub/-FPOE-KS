import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

usuario_id = int(input("Ingrese el ID del usuario a eliminar: "))

cursor.execute('''
    DELETE FROM usuarios
    WHERE id = ?
''', (usuario_id,))

conn.commit()
conn.close()

print(f'El usuario con ID {usuario_id} ha sido eliminado exitosamente.')
