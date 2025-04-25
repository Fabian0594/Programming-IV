# generador_base.py
import json

class GeneradorJSON:
    """Clase base para generación de archivos JSON"""
    
    def __init__(self, ruta_archivo=None):
        self._ruta_archivo = ruta_archivo
        self._datos = {}
    
    @property
    def ruta_archivo(self):
        return self._ruta_archivo
    
    @ruta_archivo.setter
    def ruta_archivo(self, ruta):
        if not isinstance(ruta, str):
            raise TypeError("La ruta debe ser una cadena de texto")
        self._ruta_archivo = ruta
    
    def generar_json(self):
        """Genera un archivo JSON con los datos actuales"""
        if not self._ruta_archivo:
            raise ValueError("No se ha especificado una ruta de archivo")
        
        try:
            with open(self._ruta_archivo, 'w', encoding='utf-8') as archivo_json:
                json.dump(self._datos, archivo_json, indent=4)
            print(f"Archivo JSON generado exitosamente en: {self._ruta_archivo}")
            return True
        except Exception as e:
            print(f"Error al generar el archivo JSON: {e}")
            return False
    
    def cargar_json(self, ruta=None):
        """Carga datos desde un archivo JSON existente"""
        ruta_a_usar = ruta if ruta else self._ruta_archivo
        
        if not ruta_a_usar:
            raise ValueError("No se ha especificado una ruta de archivo")
        
        try:
            with open(ruta_a_usar, 'r', encoding='utf-8') as archivo_json:
                self._datos = json.load(archivo_json)
            print(f"Datos cargados exitosamente desde: {ruta_a_usar}")
            return True
        except FileNotFoundError:
            print(f"El archivo {ruta_a_usar} no existe")
            return False
        except json.JSONDecodeError:
            print(f"El archivo {ruta_a_usar} no tiene un formato JSON válido")
            return False
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {e}")
            return False