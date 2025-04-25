"""
Define la clase base abstracta para todos los productos.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any

class Producto(ABC):
    """Clase base abstracta para todos los productos"""
    
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def precio(self) -> float:
        return self._precio
    
    @property
    def cantidad(self) -> int:
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, nueva_cantidad: int) -> None:
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            raise ValueError("La cantidad no puede ser negativa")
    
    def hay_stock(self, cantidad_solicitada: int) -> bool:
        """Verifica si hay suficiente stock para la cantidad solicitada"""
        return self._cantidad >= cantidad_solicitada
    
    def actualizar_stock(self, cantidad_vendida: int) -> None:
        """Reduce el stock después de una venta"""
        if self.hay_stock(cantidad_vendida):
            self.cantidad -= cantidad_vendida
        else:
            raise ValueError(f"No hay suficiente stock de {self._nombre}")
    
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Convierte el producto a un diccionario para guardar en JSON"""
        return {
            "tipo": self.__class__.__name__,
            "nombre": self._nombre,
            "precio": self._precio,
            "cantidad": self._cantidad
        }
    
    @abstractmethod
    def mostrar_detalles(self) -> str:
        """Muestra los detalles del producto"""
        return f"{self._nombre} - Precio: ${self._precio:.2f} - Stock: {self._cantidad}"