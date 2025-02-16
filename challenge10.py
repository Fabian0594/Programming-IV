#Ejercicio 10
#Realizar un programa para A) borrar los elementos repetidos de una lista B) borrar cadenas que no contengan vocales C) ordenar la lista en orden alfabetico respecto al primer elemento de la lista

list = ["casa", "programacion", "utp", "universidad", "utp", "casa", "casa", "thj", "vbh", "456", "987"]

def removeDuplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

def removeNoVowels(list):
    vowels = "aeiou"
    new_list = []
    for i in list:
        for j in i:
            if j.lower() in vowels:
                new_list.append(i)
                break
    return new_list

def sortList(list):
    new_list = []
    for i in list:
        if list[0] == i:
            new_list.insert(0, i)
        else:
            new_list.append(i)
    return new_list

print(removeDuplicates(list))
print(removeNoVowels(list))
print(sortList(list))

    


