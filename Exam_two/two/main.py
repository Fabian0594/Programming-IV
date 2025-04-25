# main.py
from datetime import datetime, timedelta
from habitacion import HabitacionSimple, HabitacionDoble, Suite, EstadoHabitacion
from gestor_hotel import GestorHotel

def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("\n===== SISTEMA DE GESTIÓN DE HOTEL =====")
    print("1. Ver habitaciones disponibles")
    print("2. Reservar habitación")
    print("3. Cancelar reserva")
    print("4. Ver detalles de una reserva")
    print("5. Agregar servicio a una habitación")
    print("6. Ver todas las reservas")
    print("7. Salir")
    return input("Seleccione una opción: ")

def mostrar_habitaciones(habitaciones):
    """Muestra una lista de habitaciones"""
    if not habitaciones:
        print("No hay habitaciones disponibles.")
        return
    
    print("\n=== HABITACIONES ===")
    for habitacion in habitaciones:
        print(habitacion)

def main():
    """Función principal del programa"""
    # Crear el gestor del hotel
    hotel = GestorHotel("Hotel Paraíso")
    
    # Inicializar habitaciones y servicios de ejemplo
    hotel.inicializar_hotel_ejemplo()
    
    # Cargar datos desde el archivo JSON
    hotel.cargar_datos()
    
    print(f"¡Bienvenido al sistema de gestión del {hotel.nombre_hotel}!")
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":  # Ver habitaciones disponibles
            habitaciones = hotel.listar_habitaciones_disponibles()
            mostrar_habitaciones(habitaciones)
        
        elif opcion == "2":  # Reservar habitación
            try:
                # Mostrar habitaciones disponibles
                habitaciones = hotel.listar_habitaciones_disponibles()
                if not habitaciones:
                    print("No hay habitaciones disponibles para reservar.")
                    continue
                
                print("\n=== HABITACIONES DISPONIBLES ===")
                for habitacion in habitaciones:
                    print(habitacion)
                
                # Solicitar datos de la reserva
                numero = input("\nIngrese el número de la habitación a reservar: ")
                try:
                    numero = int(numero)
                except ValueError:
                    print("El número de habitación debe ser un número entero.")
                    continue
                
                nombre = input("Ingrese el nombre del huésped: ")
                if not nombre:
                    print("El nombre del huésped es obligatorio.")
                    continue
                
                # Obtener fechas
                try:
                    fecha_entrada_str = input("Fecha de entrada (DD/MM/YYYY): ")
                    fecha_entrada = datetime.strptime(fecha_entrada_str, "%d/%m/%Y")
                    
                    fecha_salida_str = input("Fecha de salida (DD/MM/YYYY): ")
                    fecha_salida = datetime.strptime(fecha_salida_str, "%d/%m/%Y")
                except ValueError:
                    print("Formato de fecha incorrecto. Use DD/MM/YYYY.")
                    continue
                
                # Realizar la reserva
                reserva = hotel.reservar_habitacion(numero, nombre, fecha_entrada, fecha_salida)
                
                print("\n¡Reserva realizada con éxito!")
                print(reserva)
            
            except ValueError as e:
                print(f"Error: {e}")
        
        elif opcion == "3":  # Cancelar reserva
            codigo = input("Ingrese el código de la reserva a cancelar: ")
            try:
                if hotel.cancelar_reserva(codigo):
                    print(f"Reserva {codigo} cancelada con éxito.")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif opcion == "4":  # Ver detalles de una reserva
            codigo = input("Ingrese el código de la reserva: ")
            reserva = hotel.buscar_reserva(codigo)
            if reserva:
                print("\n=== DETALLES DE LA RESERVA ===")
                print(reserva)
            else:
                print(f"No se encontró una reserva con el código {codigo}.")
        
        elif opcion == "5":  # Agregar servicio a una habitación
            try:
                # Mostrar habitaciones
                print("\n=== TODAS LAS HABITACIONES ===")
                for habitacion in hotel._habitaciones.values():
                    print(habitacion)
                
                numero = input("\nIngrese el número de la habitación: ")
                try:
                    numero = int(numero)
                except ValueError:
                    print("El número de habitación debe ser un número entero.")
                    continue
                
                # Verificar que la habitación exista y pueda tener servicios
                try:
                    habitacion = hotel.obtener_habitacion(numero)
                    if not hasattr(habitacion, "agregar_servicio"):
                        print(f"La habitación {numero} no admite servicios adicionales.")
                        continue
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
                
                # Mostrar servicios disponibles
                servicios = hotel.obtener_servicios_disponibles()
                print("\n=== SERVICIOS DISPONIBLES ===")
                for i, servicio in enumerate(servicios, 1):
                    print(f"{i}. {servicio}")
                
                servicio_nombre = input("\nIngrese el nombre del servicio a agregar: ")
                
                # Agregar el servicio
                hotel.agregar_servicio_a_habitacion(numero, servicio_nombre)
                print(f"Servicio '{servicio_nombre}' agregado a la habitación {numero}.")
                
                # Mostrar información actualizada
                habitacion = hotel.obtener_habitacion(numero)
                print(habitacion)
                print(f"Precio total con servicios: ${habitacion.calcular_precio_total():.2f}")
            
            except (ValueError, TypeError) as e:
                print(f"Error: {e}")
        
        elif opcion == "6":  # Ver todas las reservas
            reservas = hotel.listar_reservas()
            if not reservas:
                print("No hay reservas registradas.")
                continue
            
            print("\n=== TODAS LAS RESERVAS ===")
            for reserva in reservas:
                print("-" * 40)
                print(reserva)
        
        elif opcion == "7":  # Salir
            print("¡Gracias por usar el sistema de gestión del hotel!")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()