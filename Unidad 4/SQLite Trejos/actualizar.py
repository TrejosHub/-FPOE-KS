import sqlite3

def actualizar_estudiante():
    nombre = input("Ingresa el nombre del estudiante para actualizar: ")
    nueva_edad = int(input("Ingresa la nueva edad del estudiante: "))
    nueva_estatura = float(input("Ingresa la nueva estatura del estudiante: "))
    
    conn = sqlite3.connect('estudiantes.db')
    c = conn.cursor()
    c.execute("UPDATE estudiantes SET edad = ?, estatura = ? WHERE nombre = ?", (nueva_edad, nueva_estatura, nombre))
    print("Estudiante actualizado exitosamente")

    conn.commit()

    conn.close()

actualizar_estudiante()