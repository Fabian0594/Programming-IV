#Ejercicio 5
#Realice un programa que almacene palabras en una lista, y despues imprima que cadena es mayor y que cadena es menor

def showLargerAndShorterString():
    words = []
    option = "y"
    while option == "y":
        words.append(input("Enter a word: "))
        option = input("Do you want to enter another word? (y/n): ")
    larger = words[0]
    shorter = words[0]
    for word in words:
        if len(word) > len(larger):
            larger = word
        if len(word) < len(shorter):
            shorter = word
    print(f"The larger word is: {larger}")
    print(f"The shorter word is: {shorter}")
    
showLargerAndShorterString()