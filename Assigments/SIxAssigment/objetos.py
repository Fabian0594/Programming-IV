from figuras import Triangulo, Cuadrado, Rectangulo, Circulo

def crear_triangulo(base, altura):
    triangulo = Triangulo(base, altura)
    return triangulo

def crear_cuadrado(lado):
    cuadrado = Cuadrado(lado)
    return cuadrado

def crear_rectangulo(base, altura):
    rectangulo = Rectangulo(base, altura)
    return rectangulo

def crear_circulo(radio):
    circulo = Circulo(radio)
    return circulo

def calcular_area_figura(figura):
    return figura.calcular_area()