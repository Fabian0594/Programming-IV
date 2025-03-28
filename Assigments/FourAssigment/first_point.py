# Base class
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def estimar_duracion_llantas(self, tipo_vehiculo, marca_llanta):
        duraciones = {
            "automovil": {"Michelin": 60000, "Pirelli": 50000, "Goodyear": 55000},
            "moto": {"Michelin": 40000, "Pirelli": 35000, "Goodyear": 37000},
            "camion": {"Michelin": 80000, "Pirelli": 75000, "Goodyear": 78000}
        }
        return duraciones.get(tipo_vehiculo, {}).get(marca_llanta, "Datos no disponibles")
    
    def recomendar_combustible(self, tipo_vehiculo):
        recomendaciones = {
            "automovil": "Gasolina o Diesel dependiendo del motor",
            "moto": "Gasolina",
            "camion": "Diesel"
        }
        return recomendaciones.get(tipo_vehiculo, "Tipo de vehículo desconocido")

# Derived class
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def tiempo_viaje(self, distancia, velocidad=None):
        if velocidad is None:
            velocidad = self.velocidad
        return distancia / velocidad if velocidad > 0 else "Velocidad no válida"
    
    def calcular_gasto_combustible(self, consumo_por_km, precio_combustible, distancia_mensual):
        consumo_total = distancia_mensual * consumo_por_km
        return consumo_total * precio_combustible
