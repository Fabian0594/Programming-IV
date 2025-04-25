"""
Define la clase para representar una línea de pedido.
"""
from typing import Dict, Any
from producto import Producto

class LineaPedido:
    """Representa una línea en un pedido"""
    
    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad
        
        # Verificar si hay suficiente stock
        if not producto.hay_stock(cantidad):
            raise ValueError(f"No hay suficiente stock de {producto.nombre}")
    
    def calcular_subtotal(self) -> float:
        """Calcula el subtotal de esta línea"""
        subtotal = self.producto.precio * self.cantidad
        
        # Aplicar descuento si corresponde (más de 5 unidades)
        if self.cantidad > 5:
            subtotal *= 0.9  # 10% de descuento
        
        return subtotal
    
    def confirmar(self) -> None:
        """Confirma la línea y actualiza el stock"""
        self.producto.actualizar_stock(self.cantidad)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "producto": self.producto.nombre,
            "cantidad": self.cantidad,
            "precio_unitario": self.producto.precio,
            "subtotal": self.calcular_subtotal()
        }