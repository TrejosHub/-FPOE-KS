import sqlite3

def consultar_estudiantes():
    conn = sqlite3.connect('estudiantes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM estudiantes")
    estudiantes = c.fetchall()
    conn.close()
    return estudiantes

estudiantes = consultar_estudiantes()
for estudiante in estudiantes:
    print(estudiante)