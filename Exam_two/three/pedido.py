"""
Define la clase para representar un pedido.
"""
from typing import List, Dict, Any
from datetime import datetime
from producto import Producto
from linea_pedido import LineaPedido

class Pedido:
    """Representa un pedido con múltiples líneas"""
    
    def __init__(self):
        self.lineas: List[LineaPedido] = []
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._confirmado = False
    
    def agregar_producto(self, producto: Producto, cantidad: int) -> None:
        """Agrega un producto al pedido"""
        if self._confirmado:
            raise ValueError("No se pueden agregar productos a un pedido confirmado")
        
        self.lineas.append(LineaPedido(producto, cantidad))
    
    def calcular_total(self) -> float:
        """Calcula el total del pedido"""
        return sum(linea.calcular_subtotal() for linea in self.lineas)
    
    def confirmar(self) -> None:
        """Confirma el pedido y actualiza el stock"""
        if self._confirmado:
            raise ValueError("El pedido ya ha sido confirmado")
        
        for linea in self.lineas:
            linea.confirmar()
        
        self._confirmado = True
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "fecha": self.fecha,
            "lineas": [linea.to_dict() for linea in self.lineas],
            "total": self.calcular_total(),
            "confirmado": self._confirmado
        }