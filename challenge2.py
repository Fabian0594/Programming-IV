#Ejercicio 2
#Unir todas las palabras de la lista en una sola cadena separada de espacios

def concatenateWords():
    actualWord = ""
    list = ["Hola", "mundo", "esto", "es", "python"]    
    for i in list:
        actualWord += i + " "
    return actualWord

#con .join() se puede hacer de una forma más sencilla

def concatenateWords2():
    list = ["Hola", "mundo", "esto", "es", "python"]
    return " ".join(list)

print(concatenateWords())
print(concatenateWords2())        
