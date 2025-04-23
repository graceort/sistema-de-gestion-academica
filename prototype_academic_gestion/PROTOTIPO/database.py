import sqlite3

def conectar_db():
    conn = sqlite3.connect('plataforma.db')
    return conn

def crear_tablas():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS maestros (id INTEGER PRIMARY KEY, nombre TEXT, materia TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS estudiantes (id INTEGER PRIMARY KEY, nombre TEXT, grado TEXT)''')
    conn.commit()
    conn.close()

def obtener_maestros():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM maestros")
    maestros = cursor.fetchall()
    conn.close()
    return maestros

def obtener_estudiantes():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    estudiantes = cursor.fetchall()
    conn.close()
    return estudiantes