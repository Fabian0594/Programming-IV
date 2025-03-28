# Base class
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"{self.__class__.__name__}(Color: {self.color}, Ruedas: {self.ruedas})"

# Subclasses
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{super().__str__()}, Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc"

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()}, Tipo: {self.tipo}"

class Camioneta(Vehiculo):
    def __init__(self, color, ruedas, carga):
        super().__init__(color, ruedas)
        self.carga = carga

    def __str__(self):
        return f"{super().__str__()}, Carga: {self.carga} kg"

class Motocicleta(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{super().__str__()}, Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc"

# Function to catalog vehicles
def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        filtered = [v for v in vehiculos if v.ruedas == ruedas]
        print(f"Se han encontrado {len(filtered)} vehículos con {ruedas} ruedas:")
        for vehiculo in filtered:
            print(vehiculo)
    else:
        for vehiculo in vehiculos:
            print(vehiculo)

# Example usage
vehiculos = [
    Coche("Rojo", 4, 120, 1500),
    Bicicleta("Azul", 2, "Deportiva"),
    Camioneta("Blanco", 4, 800),
    Motocicleta("Negro", 2, 100, 250)
]

catalogar(vehiculos)
catalogar(vehiculos, 4)
