from models import Maestro, Estudiante
from database import conectar_db

def agregar_maestro(nombre, materia):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO maestros (nombre, materia) VALUES (?, ?)", (nombre, materia))
    conn.commit()
    conn.close()

def agregar_estudiante(nombre, grado):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO estudiantes (nombre, grado) VALUES (?, ?)", (nombre, grado))
    conn.commit()
    conn.close()