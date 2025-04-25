# habitacion.py
from enum import Enum

class EstadoHabitacion(Enum):
    """Enumeración para los posibles estados de una habitación"""
    DISPONIBLE = "disponible"
    RESERVADO = "reservado"


class Habitacion:
    """Clase base para las habitaciones del hotel"""
    
    def __init__(self, numero, precio):
        self._numero = numero
        self._precio = precio
        self._estado = EstadoHabitacion.DISPONIBLE
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        self._precio = nuevo_precio
    
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, nuevo_estado):
        if not isinstance(nuevo_estado, EstadoHabitacion):
            raise TypeError("El estado debe ser un valor de EstadoHabitacion")
        self._estado = nuevo_estado
    
    def reservar(self):
        """Cambia el estado de la habitación a reservado"""
        if self._estado == EstadoHabitacion.RESERVADO:
            raise ValueError(f"La habitación {self._numero} ya está reservada")
        self._estado = EstadoHabitacion.RESERVADO
        return True
    
    def liberar(self):
        """Cambia el estado de la habitación a disponible"""
        if self._estado == EstadoHabitacion.DISPONIBLE:
            raise ValueError(f"La habitación {self._numero} ya está disponible")
        self._estado = EstadoHabitacion.DISPONIBLE
        return True
    
    def calcular_precio_total(self):
        """Calcula el precio total de la habitación"""
        return self._precio
    
    def __str__(self):
        return f"Habitación {self._numero} - ${self._precio:.2f} - {self._estado.value}"


class HabitacionSimple(Habitacion):
    """Clase para habitaciones simples"""
    
    def __init__(self, numero, precio):
        super().__init__(numero, precio)
        self._tipo = "Simple"
    
    @property
    def tipo(self):
        return self._tipo
    
    def __str__(self):
        return f"Habitación Simple {self._numero} - ${self._precio:.2f} - {self._estado.value}"


class ServicioAdicional:
    """Clase para representar servicios adicionales"""
    
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def precio(self):
        return self._precio
    
    def __str__(self):
        return f"{self._nombre} - ${self._precio:.2f}"


class HabitacionConServicios(Habitacion):
    """Clase base para habitaciones que pueden tener servicios adicionales"""
    
    def __init__(self, numero, precio):
        super().__init__(numero, precio)
        self._servicios = []
    
    def agregar_servicio(self, servicio):
        """Agrega un servicio adicional a la habitación"""
        if not isinstance(servicio, ServicioAdicional):
            raise TypeError("El servicio debe ser de tipo ServicioAdicional")
        self._servicios.append(servicio)
        return True
    
    def quitar_servicio(self, nombre_servicio):
        """Quita un servicio adicional de la habitación por su nombre"""
        for i, servicio in enumerate(self._servicios):
            if servicio.nombre.lower() == nombre_servicio.lower():
                del self._servicios[i]
                return True
        return False
    
    def listar_servicios(self):
        """Devuelve una lista de servicios adicionales"""
        return self._servicios.copy()
    
    def calcular_precio_total(self):
        """Calcula el precio total incluyendo servicios adicionales"""
        precio_base = super().calcular_precio_total()
        precio_servicios = sum(servicio.precio for servicio in self._servicios)
        return precio_base + precio_servicios


class HabitacionDoble(HabitacionConServicios):
    """Clase para habitaciones dobles"""
    
    def __init__(self, numero, precio):
        super().__init__(numero, precio)
        self._tipo = "Doble"
    
    @property
    def tipo(self):
        return self._tipo
    
    def __str__(self):
        servicios = ", ".join(servicio.nombre for servicio in self._servicios) if self._servicios else "ninguno"
        return f"Habitación Doble {self._numero} - ${self._precio:.2f} - {self._estado.value} - Servicios: {servicios}"


class Suite(HabitacionConServicios):
    """Clase para suites"""
    
    def __init__(self, numero, precio):
        super().__init__(numero, precio)
        self._tipo = "Suite"
    
    @property
    def tipo(self):
        return self._tipo
    
    def calcular_precio_total(self):
        """Calcula el precio total con un descuento especial del 5% para suites"""
        precio_total = super().calcular_precio_total()
        # 5% de descuento en el total para las suites
        return precio_total * 0.95
    
    def __str__(self):
        servicios = ", ".join(servicio.nombre for servicio in self._servicios) if self._servicios else "ninguno"
        return f"Suite {self._numero} - ${self._precio:.2f} - {self._estado.value} - Servicios: {servicios}"