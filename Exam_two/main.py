# main.py
import os
from generador_libros import GeneradorLibros
from biblioteca_digital import BibliotecaDigital
from menu import (mostrar_menu_principal, menu_busqueda, menu_biblioteca_digital, 
                  mostrar_libro)
from utils import validar_anio, validar_isbn

def main():
    """Función principal que ejecuta el programa"""
    print("\n¡Bienvenido al Sistema de Gestión de Libros!")
    
    # Determinar el modo de ejecución
    print("\nSeleccione el modo de operación:")
    print("1. Generador de Libros")
    print("2. Biblioteca Digital")
    
    try:
        modo = int(input("\nSeleccione una opción (1-2): "))
        if modo not in [1, 2]:
            print("Opción no válida. Usando Generador de Libros por defecto.")
            modo = 1
    except ValueError:
        print("Opción no válida. Usando Generador de Libros por defecto.")
        modo = 1
    
    # Definir ruta del archivo
    ruta_archivo = input("\nIngrese la ruta del archivo JSON (o presione Enter para usar el predeterminado): ")
    if not ruta_archivo:
        if modo == 1:
            ruta_archivo = "libros.json"
        else:
            ruta_archivo = "biblioteca_digital.json"
    
    # Crear el objeto según el modo seleccionado
    if modo == 1:
        sistema = GeneradorLibros(ruta_archivo)
    else:
        nombre_biblioteca = input("Nombre de la biblioteca: ")
        ubicacion = input("Ubicación de la biblioteca: ")
        sistema = BibliotecaDigital(nombre_biblioteca, ubicacion, ruta_archivo)
    
    # Cargar datos existentes si el archivo existe
    if os.path.exists(ruta_archivo):
        sistema.cargar_json()
    
    # Bucle principal del programa
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == 1:  # Agregar libro
            sistema.agregar_libro_por_consola()
        
        elif opcion == 2:  # Buscar libros
            opcion_busqueda = menu_busqueda()
            
            if opcion_busqueda == 5:  # Volver al menú principal
                continue
            
            campos = ["titulo", "autor", "genero", "isbn"]
            campo = campos[opcion_busqueda - 1]
            
            valor = input(f"Ingrese el {campo} a buscar: ")
            resultados = sistema.buscar_libro(campo, valor)
            
            if resultados:
                print(f"\nSe encontraron {len(resultados)} libros:")
                for libro in resultados:
                    mostrar_libro(libro)
            else:
                print(f"No se encontraron libros con ese {campo}.")
        
        elif opcion == 3:  # Eliminar libro
            isbn = input("Ingrese el ISBN del libro a eliminar: ")
            if sistema.eliminar_libro(isbn):
                sistema.generar_json()
        
        elif opcion == 4:  # Mostrar todos los libros
            libros = sistema.obtener_todos_libros()
            if libros:
                print(f"\nTotal de libros: {len(libros)}")
                for libro in libros:
                    mostrar_libro(libro)
            else:
                print("No hay libros registrados.")
        
        elif opcion == 5:  # Opciones de biblioteca digital
            if isinstance(sistema, BibliotecaDigital):
                opcion_bd = menu_biblioteca_digital()
                
                if opcion_bd == 1:  # Agregar reseña
                    isbn = input("Ingrese el ISBN del libro: ")
                    resenia = input("Escriba su reseña: ")
                    while True:
                        try:
                            calificacion = int(input("Calificación (1-5): "))
                            if 1 <= calificacion <= 5:
                                break
                            print("La calificación debe estar entre 1 y 5.")
                        except ValueError:
                            print("Por favor, ingrese un número válido.")
                    
                    sistema.agregar_resenia(isbn, resenia, calificacion)
                
                elif opcion_bd == 2:  # Generar informe
                    informe = sistema.generar_informe()
                    if "error" not in informe:
                        print("\n===== INFORME DE LA BIBLIOTECA =====")
                        print(f"Total de libros: {informe['total_libros']}")
                        
                        print("\nDistribución por género:")
                        for genero, cantidad in informe['distribucion_generos'].items():
                            print(f"- {genero}: {cantidad} libros")
                        
                        print("\nDistribución por autor:")
                        for autor, cantidad in informe['distribucion_autores'].items():
                            print(f"- {autor}: {cantidad} libros")
                        
                        print("\nDistribución por año:")
                        for anio, cantidad in informe['distribucion_anios'].items():
                            print(f"- {anio}: {cantidad} libros")
                    else:
                        print(informe["error"])
            else:
                print("Esta opción solo está disponible en el modo Biblioteca Digital.")
        
        elif opcion == 6:  # Guardar y salir
            sistema.generar_json()
            print("\n¡Gracias por usar el Sistema de Gestión de Libros!")
            break

if __name__ == "__main__":
    main()