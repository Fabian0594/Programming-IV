#Ejercicio 4
#Escribir un programa que pida la cantidad de la lista, los numeros para llenarla, despues imprima estos numeros y al lado el cuadrado de este numero y despues el cubo de este numero, asi con todos los numeros de la lista.

def showSquareAndCube():
    n = int(input("Enter the number of elements in the list: "))
    numbers = []
    for i in range(n):
        numbers.append(int(input("Enter a number: ")))
    for number in numbers:
        print(f"{number} - {number ** 2} - {number ** 3}")

showSquareAndCube()