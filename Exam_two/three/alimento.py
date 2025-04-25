"""
Define la clase para productos alimenticios.
"""
from typing import Dict, Any
from producto import Producto

class Alimento(Producto):
    """Subclase para productos alimenticios"""
    
    def __init__(self, nombre: str, precio: float, cantidad: int, fecha_caducidad: str):
        super().__init__(nombre, precio, cantidad)
        self._fecha_caducidad = fecha_caducidad
    
    @property
    def fecha_caducidad(self) -> str:
        return self._fecha_caducidad
    
    def to_dict(self) -> Dict[str, Any]:
        datos = super().to_dict()
        datos["fecha_caducidad"] = self._fecha_caducidad
        return datos
    
    def mostrar_detalles(self) -> str:
        return f"{super().mostrar_detalles()} - Caduca: {self._fecha_caducidad}"