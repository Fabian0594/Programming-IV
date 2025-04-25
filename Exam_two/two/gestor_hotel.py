# gestor_hotel.py
from habitacion import Habitacion, HabitacionSimple, HabitacionDoble, Suite, ServicioAdicional, EstadoHabitacion, HabitacionConServicios
from datetime import datetime, timedelta
import json

class Reserva:
    """Clase para representar una reserva"""
    
    def __init__(self, habitacion, huesped, fecha_entrada, fecha_salida):
        self._habitacion = habitacion
        self._huesped = huesped
        self._fecha_entrada = fecha_entrada
        self._fecha_salida = fecha_salida
        self._codigo = f"R{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self._fecha_reserva = datetime.now()
    
    @property
    def habitacion(self):
        return self._habitacion
    
    @property
    def huesped(self):
        return self._huesped
    
    @property
    def fecha_entrada(self):
        return self._fecha_entrada
    
    @property
    def fecha_salida(self):
        return self._fecha_salida
    
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def fecha_reserva(self):
        return self._fecha_reserva
    
    def calcular_precio_total(self):
        """Calcula el precio total de la reserva"""
        dias = (self._fecha_salida - self._fecha_entrada).days
        if dias <= 0:
            raise ValueError("La fecha de salida debe ser posterior a la de entrada")
        return self._habitacion.calcular_precio_total() * dias
    
    def __str__(self):
        return (f"Reserva {self._codigo}\n"
                f"Huésped: {self._huesped}\n"
                f"Habitación: {self._habitacion.numero}\n"
                f"Entrada: {self._fecha_entrada.strftime('%d/%m/%Y')}\n"
                f"Salida: {self._fecha_salida.strftime('%d/%m/%Y')}\n"
                f"Total: ${self.calcular_precio_total():.2f}")


class GestorHotel:
    """Clase principal para gestionar el hotel"""
    
    def __init__(self, nombre_hotel):
        self._nombre_hotel = nombre_hotel
        self._habitaciones = {}  # Diccionario con número de habitación como clave
        self._reservas = []
        self._servicios_disponibles = []
    
    @property
    def nombre_hotel(self):
        return self._nombre_hotel
    
    def agregar_habitacion(self, habitacion):
        """Agrega una nueva habitación al hotel"""
        if not isinstance(habitacion, Habitacion):
            raise TypeError("El objeto debe ser una instancia de Habitacion")
        
        if habitacion.numero in self._habitaciones:
            raise ValueError(f"Ya existe una habitación con el número {habitacion.numero}")
        
        self._habitaciones[habitacion.numero] = habitacion
        return True
    
    def definir_servicio_disponible(self, nombre, precio):
        """Define un nuevo servicio que estará disponible para agregar a habitaciones"""
        servicio = ServicioAdicional(nombre, precio)
        self._servicios_disponibles.append(servicio)
        return servicio
    
    def obtener_servicios_disponibles(self):
        """Devuelve la lista de servicios disponibles"""
        return self._servicios_disponibles.copy()
    
    def agregar_servicio_a_habitacion(self, numero_habitacion, nombre_servicio):
        """Agrega un servicio a una habitación"""
        if numero_habitacion not in self._habitaciones:
            raise ValueError(f"No existe una habitación con el número {numero_habitacion}")
        
        habitacion = self._habitaciones[numero_habitacion]
        
        # Verificar que la habitación pueda tener servicios
        if not isinstance(habitacion, HabitacionConServicios):
            raise TypeError(f"La habitación {numero_habitacion} no admite servicios adicionales")
        
        # Buscar el servicio por nombre
        servicio = None
        for s in self._servicios_disponibles:
            if s.nombre.lower() == nombre_servicio.lower():
                servicio = s
                break
        
        if not servicio:
            raise ValueError(f"No existe un servicio con el nombre '{nombre_servicio}'")
        
        return habitacion.agregar_servicio(servicio)
    
    def obtener_habitacion(self, numero_habitacion):
        """Obtiene una habitación por su número"""
        if numero_habitacion not in self._habitaciones:
            raise ValueError(f"No existe una habitación con el número {numero_habitacion}")
        return self._habitaciones[numero_habitacion]
    
    def listar_habitaciones_disponibles(self):
        """Lista todas las habitaciones disponibles"""
        disponibles = []
        for habitacion in self._habitaciones.values():
            if habitacion.estado == EstadoHabitacion.DISPONIBLE:
                disponibles.append(habitacion)
        return disponibles
    
    def reservar_habitacion(self, numero_habitacion, nombre_huesped, fecha_entrada, fecha_salida):
        """Crea una nueva reserva para una habitación"""
        if numero_habitacion not in self._habitaciones:
            raise ValueError(f"No existe una habitación con el número {numero_habitacion}")
        
        habitacion = self._habitaciones[numero_habitacion]
        
        if habitacion.estado == EstadoHabitacion.RESERVADO:
            raise ValueError(f"La habitación {numero_habitacion} ya está reservada")
        
        # Convertir fechas si son strings
        if isinstance(fecha_entrada, str):
            fecha_entrada = datetime.strptime(fecha_entrada, "%d/%m/%Y")
        if isinstance(fecha_salida, str):
            fecha_salida = datetime.strptime(fecha_salida, "%d/%m/%Y")
        
        # Validar fechas
        if fecha_entrada < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
            raise ValueError("La fecha de entrada no puede ser en el pasado")
        if fecha_salida <= fecha_entrada:
            raise ValueError("La fecha de salida debe ser posterior a la de entrada")
        
        # Crear la reserva
        reserva = Reserva(habitacion, nombre_huesped, fecha_entrada, fecha_salida)
        
        # Cambiar el estado de la habitación
        habitacion.reservar()
        
        # Agregar la reserva a la lista
        self._reservas.append(reserva)
        
        return reserva
    
    def cancelar_reserva(self, codigo_reserva):
        """Cancela una reserva existente"""
        for i, reserva in enumerate(self._reservas):
            if reserva.codigo == codigo_reserva:
                # Liberar la habitación
                reserva.habitacion.liberar()
                # Eliminar la reserva
                del self._reservas[i]
                return True
        
        raise ValueError(f"No existe una reserva con el código {codigo_reserva}")
    
    def buscar_reserva(self, codigo_reserva):
        """Busca una reserva por su código"""
        for reserva in self._reservas:
            if reserva.codigo == codigo_reserva:
                return reserva
        return None
    
    def listar_reservas(self):
        """Lista todas las reservas"""
        return self._reservas.copy()
    
    def inicializar_hotel_ejemplo(self):
        """Inicializa el hotel con habitaciones y servicios de ejemplo"""
        # Crear habitaciones de ejemplo
        self.agregar_habitacion(HabitacionSimple(101, 80.0))
        self.agregar_habitacion(HabitacionSimple(102, 80.0))
        self.agregar_habitacion(HabitacionDoble(201, 120.0))
        self.agregar_habitacion(HabitacionDoble(202, 120.0))
        self.agregar_habitacion(Suite(301, 200.0))
        self.agregar_habitacion(Suite(302, 250.0))
        
        # Crear servicios de ejemplo
        self.definir_servicio_disponible("Desayuno", 15.0)
        self.definir_servicio_disponible("Acceso al Spa", 30.0)
        self.definir_servicio_disponible("Minibar", 25.0)
        self.definir_servicio_disponible("Servicio a la habitación", 20.0)
        
        # Agregar servicios a algunas habitaciones
        self.agregar_servicio_a_habitacion(201, "Desayuno")
        self.agregar_servicio_a_habitacion(202, "Minibar")
        self.agregar_servicio_a_habitacion(301, "Desayuno")
        self.agregar_servicio_a_habitacion(301, "Acceso al Spa")
        self.agregar_servicio_a_habitacion(302, "Desayuno")
        self.agregar_servicio_a_habitacion(302, "Acceso al Spa")
        self.agregar_servicio_a_habitacion(302, "Minibar")
        self.agregar_servicio_a_habitacion(302, "Servicio a la habitación")
    
    def guardar_datos(self, archivo="datos_hotel.json"):
        """Guarda las habitaciones y reservas en un archivo JSON"""
        datos = {
            "habitaciones": [
                {
                    "numero": habitacion.numero,
                    "precio": habitacion.precio,
                    "estado": habitacion.estado.value,
                    "tipo": habitacion.__class__.__name__,
                    "servicios": [
                        {"nombre": servicio.nombre, "precio": servicio.precio}
                        for servicio in getattr(habitacion, "_servicios", [])
                    ] if isinstance(habitacion, HabitacionConServicios) else []
                }
                for habitacion in self._habitaciones.values()
            ],
            "reservas": [
                {
                    "codigo": reserva.codigo,
                    "habitacion": reserva.habitacion.numero,
                    "huesped": reserva.huesped,
                    "fecha_entrada": reserva.fecha_entrada.strftime("%d/%m/%Y"),
                    "fecha_salida": reserva.fecha_salida.strftime("%d/%m/%Y"),
                    "fecha_reserva": reserva.fecha_reserva.strftime("%d/%m/%Y %H:%M:%S")
                }
                for reserva in self._reservas
            ]
        }
        with open(archivo, "w") as f:
            json.dump(datos, f, indent=4)
        print(f"Datos guardados en {archivo}.")

    def cargar_datos(self, archivo="datos_hotel.json"):
        """Carga las habitaciones y reservas desde un archivo JSON"""
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
            
            # Cargar habitaciones
            self._habitaciones = {}
            for hab in datos["habitaciones"]:
                if hab["tipo"] == "HabitacionSimple":
                    habitacion = HabitacionSimple(hab["numero"], hab["precio"])
                elif hab["tipo"] == "HabitacionDoble":
                    habitacion = HabitacionDoble(hab["numero"], hab["precio"])
                elif hab["tipo"] == "Suite":
                    habitacion = Suite(hab["numero"], hab["precio"])
                else:
                    continue
                
                habitacion.estado = EstadoHabitacion(hab["estado"])
                for servicio in hab.get("servicios", []):
                    habitacion.agregar_servicio(ServicioAdicional(servicio["nombre"], servicio["precio"]))
                self._habitaciones[habitacion.numero] = habitacion
            
            # Cargar reservas
            self._reservas = []
            for res in datos["reservas"]:
                habitacion = self.obtener_habitacion(res["habitacion"])
                reserva = Reserva(
                    habitacion,
                    res["huesped"],
                    datetime.strptime(res["fecha_entrada"], "%d/%m/%Y"),
                    datetime.strptime(res["fecha_salida"], "%d/%m/%Y")
                )
                reserva._codigo = res["codigo"]  # Restaurar el código original
                reserva._fecha_reserva = datetime.strptime(res["fecha_reserva"], "%d/%m/%Y %H:%M:%S")
                self._reservas.append(reserva)
            
            print(f"Datos cargados desde {archivo}.")
        except FileNotFoundError:
            print(f"No se encontró el archivo {archivo}. Se iniciará con datos vacíos.")