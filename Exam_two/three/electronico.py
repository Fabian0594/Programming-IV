"""
Define la clase para productos electrónicos.
"""
from typing import Dict, Any
from producto import Producto

class Electronico(Producto):
    """Subclase para productos electrónicos"""
    
    def __init__(self, nombre: str, precio: float, cantidad: int, periodo_garantia: int):
        super().__init__(nombre, precio, cantidad)
        self._periodo_garantia = periodo_garantia  # en meses
    
    @property
    def periodo_garantia(self) -> int:
        return self._periodo_garantia
    
    def to_dict(self) -> Dict[str, Any]:
        datos = super().to_dict()
        datos["periodo_garantia"] = self._periodo_garantia
        return datos
    
    def mostrar_detalles(self) -> str:
        return f"{super().mostrar_detalles()} - Garantía: {self._periodo_garantia} meses"