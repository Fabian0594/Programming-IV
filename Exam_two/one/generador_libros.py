# generador_libros.py
from datetime import datetime
from generador_base import GeneradorJSON

class GeneradorLibros(GeneradorJSON):
    """Clase especializada en la generación de JSON de libros"""
    
    def __init__(self, ruta_archivo=None):
        super().__init__(ruta_archivo)
        self._datos = {"libros": []}
    
    def agregar_libro(self, titulo, autor, anio_publicacion, genero, isbn=None, editorial=None):
        """Agrega un nuevo libro a la colección"""
        libro = {
            "titulo": titulo,
            "autor": autor,
            "anio_publicacion": anio_publicacion,
            "genero": genero,
            "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Agregamos campos opcionales si se proporcionan
        if isbn:
            libro["isbn"] = isbn
        if editorial:
            libro["editorial"] = editorial
            
        self._datos["libros"].append(libro)
        print(f"Libro '{titulo}' agregado correctamente")
        return libro
    
    def buscar_libro(self, campo, valor):
        """Busca libros según un campo y valor específicos"""
        resultados = []
        for libro in self._datos["libros"]:
            if campo in libro and libro[campo] == valor:
                resultados.append(libro)
        return resultados
    
    def eliminar_libro(self, isbn):
        """Elimina un libro por su ISBN"""
        libros_filtrados = [libro for libro in self._datos["libros"] if libro.get("isbn") != isbn]
        
        if len(libros_filtrados) < len(self._datos["libros"]):
            self._datos["libros"] = libros_filtrados
            print(f"Libro con ISBN {isbn} eliminado correctamente")
            return True
        else:
            print(f"No se encontró ningún libro con ISBN {isbn}")
            return False
    
    def obtener_todos_libros(self):
        """Retorna todos los libros en la colección"""
        return self._datos["libros"]
    
    def agregar_libro_por_consola(self):
        """Permite agregar un libro solicitando los datos por consola y actualiza el archivo JSON"""
        print("\n=== Agregar nuevo libro ===")
        titulo = input("Título: ")
        autor = input("Autor: ")
        
        while True:
            try:
                anio = int(input("Año de publicación: "))
                if 1000 <= anio <= datetime.now().year:
                    break
                print(f"El año debe estar entre 1000 y {datetime.now().year}")
            except ValueError:
                print("Por favor, ingrese un número válido")
        
        genero = input("Género: ")
        isbn = input("ISBN (opcional, presione Enter para omitir): ") or None
        editorial = input("Editorial (opcional, presione Enter para omitir): ") or None
        
        libro = self.agregar_libro(titulo, autor, anio, genero, isbn, editorial)
        
        # Guardar los cambios en el archivo JSON
        self.generar_json()
        
        return libro