"""
Define la clase para productos de ropa.
"""
from typing import Dict, Any
from producto import Producto

class Ropa(Producto):
    """Subclase para productos de ropa"""
    
    def __init__(self, nombre: str, precio: float, cantidad: int, tamano: str):
        super().__init__(nombre, precio, cantidad)
        self._tamano = tamano
    
    @property
    def tamano(self) -> str:
        return self._tamano
    
    def to_dict(self) -> Dict[str, Any]:
        datos = super().to_dict()
        datos["tamano"] = self._tamano
        return datos
    
    def mostrar_detalles(self) -> str:
        return f"{super().mostrar_detalles()} - Tamaño: {self._tamano}"