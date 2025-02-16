#Ejercicio 1
#Sumar elementos enteros de una lista sin ordenarla

def addOnlyInt():
    total = 0
    list = [2, 8, "hola", "programacion", 10, "utp", 85, 82, 100, "mundo"]
    for i in list:
        if type(i) is int:
            total += i
        else:
            pass
    return total

print(addOnlyInt())


