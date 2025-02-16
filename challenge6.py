#Ejercicio 6
#Realice un programa que pida un entero y despues imprima las cadenas con la longitud igual al entero ingresado

def showStringsByLength():
    n = int(input("Enter an integer: "))
    words = ["oso", "casa", "cara", "murcielago", "ventana", "programacion"]
    for word in words:
        if len(word) == n:
            print(word)

showStringsByLength()