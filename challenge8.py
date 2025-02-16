#Ejercicio 8
#Realizar un programa que hagaconteo de todos los caracteres que no sean vocales en una lista de 10 cadenas

def count_consonants(lista):
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = 0
    for word in lista:
        for letter in word:
            if letter.lower() in consonants:
                count += 1
    return count

lista = ["Hola", "Mundo", "Python", "Programacion", "Cadena", "Lista", "Consonantes", "Vocales", "Conteo", "Caracteres"]
print(count_consonants(lista))