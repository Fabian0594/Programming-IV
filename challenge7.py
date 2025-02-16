#Ejercicio 7
#Realizar un programa que pida un caracter, y muestre las cadenas que contienen este caracter e imprima si dichas cadenas son par o impar 

def showStringsByCharacter():
    character = input("Enter a character: ")
    words = ["oso", "casa", "murcielago", "ventana", "programacion", "objetos", "listas", "metodos", "utp"]
    for word in words:
        if character in word:
            if len(word) % 2 == 0:
                print(f"{word} - even")
            else:
                print(f"{word} - odd")
            
showStringsByCharacter()