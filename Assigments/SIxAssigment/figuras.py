import math

class FiguraTrigonometrica:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def calcular_area(self):
        pass  # Método a implementar en las clases derivadas
    
    def mostrar_info(self):
        return f"Figura: {self.__nombre}, Área: {self.calcular_area()}"


class Triangulo(FiguraTrigonometrica):
    def __init__(self, base=0, altura=0):
        super().__init__("Triángulo")
        self.__base = 0
        self.__altura = 0
        self.set_base(base)
        self.set_altura(altura)
    
    def get_base(self):
        return self.__base
    
    def set_base(self, base):
        if base > 0:
            self.__base = base
        else:
            print("Error: La base debe ser un número positivo")
    
    def get_altura(self):
        return self.__altura
    
    def set_altura(self, altura):
        if altura > 0:
            self.__altura = altura
        else:
            print("Error: La altura debe ser un número positivo")
    
    def calcular_area(self):
        return (self.__base * self.__altura) / 2


class Cuadrado(FiguraTrigonometrica):
    def __init__(self, lado=0):
        super().__init__("Cuadrado")
        self.__lado = 0
        self.set_lado(lado)
    
    def get_lado(self):
        return self.__lado
    
    def set_lado(self, lado):
        if lado > 0:
            self.__lado = lado
        else:
            print("Error: El lado debe ser un número positivo")
    
    def calcular_area(self):
        return self.__lado ** 2


class Rectangulo(FiguraTrigonometrica):
    def __init__(self, base=0, altura=0):
        super().__init__("Rectángulo")
        self.__base = 0
        self.__altura = 0
        self.set_base(base)
        self.set_altura(altura)
    
    def get_base(self):
        return self.__base
    
    def set_base(self, base):
        if base > 0:
            self.__base = base
        else:
            print("Error: La base debe ser un número positivo")
    
    def get_altura(self):
        return self.__altura
    
    def set_altura(self, altura):
        if altura > 0:
            self.__altura = altura
        else:
            print("Error: La altura debe ser un número positivo")
    
    def calcular_area(self):
        return self.__base * self.__altura


class Circulo(FiguraTrigonometrica):
    def __init__(self, radio=0):
        super().__init__("Círculo")
        self.__radio = 0
        self.set_radio(radio)
    
    def get_radio(self):
        return self.__radio
    
    def set_radio(self, radio):
        if radio > 0:
            self.__radio = radio
        else:
            print("Error: El radio debe ser un número positivo")
    
    def calcular_area(self):
        return math.pi * (self.__radio ** 2)