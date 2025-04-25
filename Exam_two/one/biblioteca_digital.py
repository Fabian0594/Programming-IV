# biblioteca_digital.py
from datetime import datetime
from generador_libros import GeneradorLibros

class BibliotecaDigital(GeneradorLibros):
    """Clase extendida para manejar una biblioteca digital con funcionalidades adicionales"""
    
    def __init__(self, nombre_biblioteca, ubicacion, ruta_archivo=None):
        super().__init__(ruta_archivo)
        self._datos = {
            "info_biblioteca": {
                "nombre": nombre_biblioteca,
                "ubicacion": ubicacion,
                "fecha_creacion": datetime.now().strftime("%Y-%m-%d")
            },
            "libros": []
        }
    
    def agregar_libro(self, titulo, autor, anio_publicacion, genero, isbn=None, editorial=None):
        libro = super().agregar_libro(titulo, autor, anio_publicacion, genero, isbn, editorial)
        self.generar_json()  # Guardar los cambios en el archivo JSON
        return libro
    
    def agregar_resenia(self, isbn, resenia, calificacion):
        """Agrega una reseña a un libro específico"""
        for libro in self._datos["libros"]:
            if libro.get("isbn") == isbn:
                if "resenias" not in libro:
                    libro["resenias"] = []
                
                libro["resenias"].append({
                    "texto": resenia,
                    "calificacion": calificacion,
                    "fecha": datetime.now().strftime("%Y-%m-%d")
                })
                
                # Actualizar calificación promedio
                calificaciones = [r["calificacion"] for r in libro["resenias"]]
                libro["calificacion_promedio"] = sum(calificaciones) / len(calificaciones)
                
                print(f"Reseña agregada al libro '{libro['titulo']}'")
                # Guardar los cambios en el archivo JSON
                self.generar_json()
                return True
        
        print(f"No se encontró ningún libro con ISBN {isbn}")
        return False
    
    def generar_informe(self):
        """Genera un informe estadístico de la biblioteca"""
        if not self._datos["libros"]:
            return {"error": "No hay libros en la biblioteca para generar un informe"}
        
        generos = {}
        autores = {}
        anios = {}
        
        for libro in self._datos["libros"]:
            # Contar por género
            genero = libro["genero"]
            generos[genero] = generos.get(genero, 0) + 1
            
            # Contar por autor
            autor = libro["autor"]
            autores[autor] = autores.get(autor, 0) + 1
            
            # Contar por año
            anio = libro["anio_publicacion"]
            anios[anio] = anios.get(anio, 0) + 1
        
        return {
            "total_libros": len(self._datos["libros"]),
            "distribucion_generos": generos,
            "distribucion_autores": autores,
            "distribucion_anios": anios,
            "fecha_informe": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }