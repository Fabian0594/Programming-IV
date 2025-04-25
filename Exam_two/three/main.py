"""
Punto de entrada principal del sistema de gestión de pedidos.
"""
from gestor_pedidos import SistemaGestionPedidos

def main():
    """Función principal que ejecuta el sistema interactivo"""
    # Inicializar el sistema
    sistema = SistemaGestionPedidos()
    
    while True:
        print("\n===== SISTEMA DE GESTIÓN DE PEDIDOS =====")
        print("1. Mostrar productos disponibles")
        print("2. Crear un pedido")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Mostrar productos disponibles
            print("\nProductos disponibles:")
            for producto in sistema.mostrar_productos():
                print(producto)
        
        elif opcion == "2":
            # Crear un pedido
            pedido = sistema.crear_pedido()
            
            while True:
                print("\n=== AGREGAR PRODUCTOS AL PEDIDO ===")
                nombre_producto = input("Ingrese el nombre del producto (o 'salir' para finalizar): ")
                if nombre_producto.lower() == "salir":
                    break
                
                producto = sistema.buscar_producto(nombre_producto)
                if not producto:
                    print("Producto no encontrado. Intente nuevamente.")
                    continue
                
                try:
                    cantidad = int(input(f"Ingrese la cantidad de '{producto.nombre}': "))
                    pedido.agregar_producto(producto, cantidad)
                    print(f"Producto '{producto.nombre}' agregado al pedido.")
                except ValueError as e:
                    print(f"Error: {e}")
            
            # Calcular total
            total = pedido.calcular_total()
            print(f"\nTotal del pedido: ${total:.2f}")
            
            # Confirmar pedido
            confirmar = input("¿Desea confirmar el pedido? (s/n): ").lower()
            if confirmar == "s":
                pedido.confirmar()
                print("Pedido confirmado.")
                sistema.guardar_productos()
            else:
                print("Pedido no confirmado.")
        
        elif opcion == "3":
            print("¡Gracias por usar el sistema de gestión de pedidos!")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()