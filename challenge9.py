#Ejercicio 9
#Realizar un programa que inicialice una lista con 15 valores aleatorios y posteriormente muestre en pantalla cada elmento de la lista junto a su cuadrado y su cubo

import random

#Usemos la funcion de challenge4.py para mostrar el cuadrado y el cubo de los elementos de la lista
def showSquareAndCube():
    n = int(input("Enter the number of elements in the list: "))
    numbers = []
    for i in range(n):
        numbers.append(int(input("Enter a number: ")))
    for number in numbers:
        print(f"{number} - {number ** 2} - {number ** 3}")
#Haremos algunas modificaciones a esta funcion

def showSquareAndCube2(list):
    list = [random.randint(1, 10) for i in range(15)]
    for number in list:
        print(f"{number} - {number ** 2} - {number ** 3}")
    
showSquareAndCube2(list)