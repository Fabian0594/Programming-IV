"""
Servicio principal para la gestión de productos y pedidos.
"""
from typing import List, Optional
from producto import Producto
from electronico import Electronico
from ropa import Ropa
from alimento import Alimento
from pedido import Pedido
from almacenamiento import cargar_productos, guardar_productos

class SistemaGestionPedidos:
    """Sistema principal para gestionar productos y pedidos"""
    
    def __init__(self, archivo_productos: str = "productos.json"):
        self.productos: List[Producto] = []
        self.pedidos: List[Pedido] = []
        self.archivo_productos = archivo_productos
        
        # Cargar productos o crear ejemplos si no existen
        self.productos = cargar_productos(archivo_productos)
        if not self.productos:
            self._crear_productos_ejemplo()
            self.guardar_productos()
    
    def _crear_productos_ejemplo(self) -> None:
        """Crea algunos productos de ejemplo"""
        self.productos = [
            Electronico("Smartphone XYZ", 499.99, 10, 12),
            Electronico("Laptop Pro", 1299.99, 5, 24),
            Ropa("Camiseta Algodón", 19.99, 50, "M"),
            Ropa("Pantalón Vaquero", 39.99, 30, "L"),
            Alimento("Chocolate Premium", 5.99, 100, "2025-12-31"),
            Alimento("Café Gourmet", 8.99, 40, "2025-06-30")
        ]
    
    def guardar_productos(self) -> None:
        """Guarda los productos en un archivo JSON"""
        guardar_productos(self.productos, self.archivo_productos)
    
    def mostrar_productos(self) -> List[str]:
        """Muestra todos los productos disponibles"""
        return [f"{i+1}. {producto.mostrar_detalles()}" for i, producto in enumerate(self.productos)]
    
    def buscar_producto(self, nombre: str) -> Optional[Producto]:
        """Busca un producto por su nombre"""
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
    
    def crear_pedido(self) -> Pedido:
        """Crea un nuevo pedido"""
        pedido = Pedido()
        self.pedidos.append(pedido)
        return pedido