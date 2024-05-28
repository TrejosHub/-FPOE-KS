import sqlite3

def borrar_estudiante():
    nombre = input("Ingresa el nombre del estudiante que deseas borrar: ")
    
    conn = sqlite3.connect('estudiantes.db')
    c = conn.cursor()
    c.execute("DELETE FROM estudiantes WHERE nombre = ?", (nombre,))
    print("Estudiante borrado exitosamente")

    conn.commit()

    conn.close()

borrar_estudiante()