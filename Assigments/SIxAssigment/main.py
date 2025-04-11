from objetos import crear_triangulo, crear_cuadrado, crear_rectangulo, crear_circulo

def menu_principal():
    print("\n===== CALCULADORA DE ÁREAS DE FIGURAS TRIGONOMÉTRICAS =====")
    print("1. Calcular área de un triángulo")
    print("2. Calcular área de un cuadrado")
    print("3. Calcular área de un rectángulo")
    print("4. Calcular área de un círculo")
    print("5. Salir")
    opcion = input("Seleccione una opción (1-5): ")
    return opcion

def obtener_valor_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Error: El valor debe ser positivo")
        except ValueError:
            print("Error: Debe ingresar un número válido")

def main():
    while True:
        opcion = menu_principal()
        
        if opcion == "1":
            # Triángulo
            base = obtener_valor_positivo("Ingrese la base del triángulo: ")
            altura = obtener_valor_positivo("Ingrese la altura del triángulo: ")
            triangulo = crear_triangulo(base, altura)
            print(f"\nÁrea del triángulo: {triangulo.calcular_area()}")
            print(triangulo.mostrar_info())
            
        elif opcion == "2":
            # Cuadrado
            lado = obtener_valor_positivo("Ingrese el lado del cuadrado: ")
            cuadrado = crear_cuadrado(lado)
            print(f"\nÁrea del cuadrado: {cuadrado.calcular_area()}")
            print(cuadrado.mostrar_info())
            
        elif opcion == "3":
            # Rectángulo
            base = obtener_valor_positivo("Ingrese la base del rectángulo: ")
            altura = obtener_valor_positivo("Ingrese la altura del rectángulo: ")
            rectangulo = crear_rectangulo(base, altura)
            print(f"\nÁrea del rectángulo: {rectangulo.calcular_area()}")
            print(rectangulo.mostrar_info())
            
        elif opcion == "4":
            # Círculo
            radio = obtener_valor_positivo("Ingrese el radio del círculo: ")
            circulo = crear_circulo(radio)
            print(f"\nÁrea del círculo: {circulo.calcular_area()}")
            print(circulo.mostrar_info())
            
        elif opcion == "5":
            print("¡Gracias por usar la calculadora de áreas!")
            break
            
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()