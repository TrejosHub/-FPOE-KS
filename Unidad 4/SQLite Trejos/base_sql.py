#Para visuzlizar la tabla desde VSC instalar la extensaion 'SQLite Viewer' y dar click al archivo 'estudiantes.db'

import sqlite3

conn = sqlite3.connect('estudiantes.db')

c = conn.cursor()

'''c.execute("""CREATE TABLE estudiantes (
            nombre TEXT,
            edad INTEGER,
            estatura REAL
    )""")'''

c.execute("INSERT INTO estudiantes VALUES ('Kevin', 18, 1.6)")

todos_estudiantes = [
    ('Falcao', 38, 1.7),
    ('James', 32, 1.8),
    ('Editable', 1989, 6.8),
]

c.executemany("INSERT INTO estudiantes VALUES (?, ?, ?)", todos_estudiantes)

conn.commit()

conn.close()