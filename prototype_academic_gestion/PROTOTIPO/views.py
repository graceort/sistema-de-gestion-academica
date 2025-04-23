def mostrar_menu():
    print("\n--- Menú de Gestión ---")
    print("1. Registrar Maestro")
    print("2. Registrar Estudiante")
    print("3. Mostrar Maestros")
    print("4. Mostrar Estudiantes")
    print("5. Salir")

def obtener_opcion():
    return int(input("Seleccione una opción: "))

def mostrar_maestros(maestros):
    print("\n--- Lista de Maestros ---")
    for maestro in maestros:
        print(f"ID: {maestro[0]}, Nombre: {maestro[1]}, Materia: {maestro[2]}")

def mostrar_estudiantes(estudiantes):
    print("\n--- Lista de Estudiantes ---")
    for estudiante in estudiantes:
        print(f"ID: {estudiante[0]}, Nombre: {estudiante[1]}, Grado: {estudiante[2]}")