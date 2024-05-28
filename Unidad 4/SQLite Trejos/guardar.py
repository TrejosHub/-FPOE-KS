import sqlite3

def guardar_estudiante():
    nombre = input("Ingresa el nombre del estudiante: ")
    edad = int(input("Ingresa la edad del estudiante: "))
    estatura = float(input("Ingresa la estatura del estudiante: "))
    
    conn = sqlite3.connect('estudiantes.db')
    c = conn.cursor()
    c.execute("INSERT INTO estudiantes VALUES (?, ?, ?)", (nombre, edad, estatura))
    print("Estudiante creado exitosamente")

    conn.commit()

    conn.close()

guardar_estudiante()