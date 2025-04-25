"""
Proporciona funciones para la persistencia de datos.
"""
import json
from typing import List, Dict, Any
from producto import Producto
from electronico import Electronico
from ropa import Ropa
from alimento import Alimento

def guardar_productos(productos: List[Producto], archivo: str) -> None:
    """Guarda la lista de productos en un archivo JSON"""
    datos = [producto.to_dict() for producto in productos]
    with open(archivo, 'w') as f:
        json.dump(datos, f, indent=4)

def cargar_productos(archivo: str) -> List[Producto]:
    """Carga productos desde un archivo JSON"""
    try:
        with open(archivo, 'r') as f:
            datos = json.load(f)
        
        productos = []
        for item in datos:
            if item["tipo"] == "Electronico":
                productos.append(
                    Electronico(item["nombre"], item["precio"], item["cantidad"], item["periodo_garantia"])
                )
            elif item["tipo"] == "Ropa":
                productos.append(
                    Ropa(item["nombre"], item["precio"], item["cantidad"], item["tamano"])
                )
            elif item["tipo"] == "Alimento":
                productos.append(
                    Alimento(item["nombre"], item["precio"], item["cantidad"], item["fecha_caducidad"])
                )
        return productos
    except (FileNotFoundError, json.JSONDecodeError):
        return []