from database import crear_tablas, obtener_maestros, obtener_estudiantes
from views import mostrar_menu, obtener_opcion, mostrar_maestros, mostrar_estudiantes
from controllers import agregar_maestro, agregar_estudiante

def main():
    crear_tablas()
    while True:
        mostrar_menu()
        opcion = obtener_opcion()
        if opcion == 1:
            nombre = input("Ingrese el nombre del maestro: ")
            materia = input("Ingrese la materia que enseña: ")
            agregar_maestro(nombre, materia)
            print("Maestro registrado exitosamente.")
        elif opcion == 2:
            nombre = input("Ingrese el nombre del estudiante: ")
            grado = input("Ingrese el grado del estudiante: ")
            agregar_estudiante(nombre, grado)
            print("Estudiante registrado exitosamente.")
        elif opcion == 3:
            maestros = obtener_maestros()
            mostrar_maestros(maestros)
        elif opcion == 4:
            estudiantes = obtener_estudiantes()
            mostrar_estudiantes(estudiantes)
        elif opcion == 5:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()