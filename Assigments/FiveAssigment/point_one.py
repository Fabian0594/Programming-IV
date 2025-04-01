from utilities import (
    crear_personal_universitario,
    crear_profesor,
    crear_alumno,
    crear_profesor_ayudante,
    mostrar_entidad,
    guardar_entidades_en_txt
)

def main():
    print("=== Sistema de Gestión Universitaria ===")
    entidades = []  # Lista para almacenar las entidades creadas

    while True:
        print("\nOpciones:")
        print("1. Crear Personal Universitario")
        print("2. Crear Profesor")
        print("3. Crear Alumno")
        print("4. Crear Profesor Ayudante")
        print("5. Mostrar todas las entidades")
        print("6. Guardar entidades en archivo")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            personal = crear_personal_universitario()
            entidades.append(personal)
            print("Personal Universitario creado exitosamente.")
        elif opcion == "2":
            profesor = crear_profesor()
            entidades.append(profesor)
            print("Profesor creado exitosamente.")
        elif opcion == "3":
            alumno = crear_alumno()
            entidades.append(alumno)
            print("Alumno creado exitosamente.")
        elif opcion == "4":
            profesor_ayudante = crear_profesor_ayudante()
            entidades.append(profesor_ayudante)
            print("Profesor Ayudante creado exitosamente.")
        elif opcion == "5":
            if not entidades:
                print("No hay entidades creadas.")
            else:
                print("\n=== Lista de Entidades ===")
                for i, entidad in enumerate(entidades, start=1):
                    print(f"\nEntidad #{i}:")
                    mostrar_entidad(entidad)
        elif opcion == "6":
            if not entidades:
                print("No hay entidades para guardar.")
            else:
                guardar_entidades_en_txt(entidades)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()