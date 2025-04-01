from utilities import (
    crear_producto,
    crear_departamento,
    crear_producto_alimenticio,
    crear_producto_refrigerado,
    crear_producto_limpieza,
    crear_producto_electronico,
    crear_producto_ropa,
    mostrar_producto,
    guardar_productos_en_txt
)

def main():
    print("=== Sistema de Gestión de Supermercado ===")
    productos = []  # Lista para almacenar los productos creados

    while True:
        print("\nOpciones:")
        print("1. Crear Producto Genérico")
        print("2. Crear Producto Alimenticio")
        print("3. Crear Producto Refrigerado")
        print("4. Crear Producto de Limpieza")
        print("5. Crear Producto Electrónico")
        print("6. Crear Producto de Ropa")
        print("7. Mostrar Productos")
        print("8. Guardar Productos en Archivo")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto = crear_producto()
            productos.append(producto)
            print("Producto genérico creado exitosamente.")
        elif opcion == "2":
            producto_alimenticio = crear_producto_alimenticio()
            productos.append(producto_alimenticio)
            print("Producto alimenticio creado exitosamente.")
        elif opcion == "3":
            producto_refrigerado = crear_producto_refrigerado()
            productos.append(producto_refrigerado)
            print("Producto refrigerado creado exitosamente.")
        elif opcion == "4":
            producto_limpieza = crear_producto_limpieza()
            productos.append(producto_limpieza)
            print("Producto de limpieza creado exitosamente.")
        elif opcion == "5":
            producto_electronico = crear_producto_electronico()
            productos.append(producto_electronico)
            print("Producto electrónico creado exitosamente.")
        elif opcion == "6":
            producto_ropa = crear_producto_ropa()
            productos.append(producto_ropa)
            print("Producto de ropa creado exitosamente.")
        elif opcion == "7":
            if not productos:
                print("No hay productos creados.")
            else:
                print("\n=== Lista de Productos ===")
                for i, producto in enumerate(productos, start=1):
                    print(f"\nProducto #{i}:")
                    mostrar_producto(producto)
        elif opcion == "8":
            if not productos:
                print("No hay productos para guardar.")
            else:
                guardar_productos_en_txt(productos)
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()