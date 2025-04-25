# menu.py
from utils import validar_anio, validar_isbn

def mostrar_menu_principal():
    """Muestra el menú principal de opciones"""
    print("\n===== SISTEMA DE GESTIÓN DE LIBROS =====")
    print("1. Agregar libro")
    print("2. Buscar libros")
    print("3. Eliminar libro")
    print("4. Mostrar todos los libros")
    print("5. Opciones de biblioteca digital")
    print("6. Guardar y salir")
    
    try:
        opcion = int(input("\nSeleccione una opción (1-6): "))
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("Opción no válida. Intente nuevamente.")
            return mostrar_menu_principal()
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return mostrar_menu_principal()

def menu_busqueda():
    """Muestra el menú de opciones de búsqueda"""
    print("\n===== BUSCAR LIBROS POR =====")
    print("1. Título")
    print("2. Autor")
    print("3. Género")
    print("4. ISBN")
    print("5. Volver al menú principal")
    
    try:
        opcion = int(input("\nSeleccione una opción (1-5): "))
        if 1 <= opcion <= 5:
            return opcion
        else:
            print("Opción no válida. Intente nuevamente.")
            return menu_busqueda()
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return menu_busqueda()

def menu_biblioteca_digital():
    """Muestra el menú de opciones de biblioteca digital"""
    print("\n===== BIBLIOTECA DIGITAL =====")
    print("1. Agregar reseña a un libro")
    print("2. Generar informe de la biblioteca")
    print("3. Volver al menú principal")
    
    try:
        opcion = int(input("\nSeleccione una opción (1-3): "))
        if 1 <= opcion <= 3:
            return opcion
        else:
            print("Opción no válida. Intente nuevamente.")
            return menu_biblioteca_digital()
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return menu_biblioteca_digital()

def mostrar_libro(libro):
    """Muestra la información de un libro en formato legible"""
    print(f"\n{'='*50}")
    print(f"Título: {libro['titulo']}")
    print(f"Autor: {libro['autor']}")
    print(f"Año de publicación: {libro['anio_publicacion']}")
    print(f"Género: {libro['genero']}")
    
    if "isbn" in libro:
        print(f"ISBN: {libro['isbn']}")
    if "editorial" in libro:
        print(f"Editorial: {libro['editorial']}")
    
    # Mostrar reseñas si existen
    if "resenias" in libro and libro["resenias"]:
        print("\nReseñas:")
        for i, resenia in enumerate(libro["resenias"], 1):
            print(f"  {i}. Calificación: {resenia['calificacion']}/5 - {resenia['fecha']}")
            print(f"     \"{resenia['texto']}\"")
    
    if "calificacion_promedio" in libro:
        print(f"\nCalificación promedio: {libro['calificacion_promedio']:.1f}/5")
    
    print(f"{'='*50}")