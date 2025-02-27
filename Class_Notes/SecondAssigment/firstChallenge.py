from io import *

#Realice un programa que reciba en una lista solo numeros enteros de dos cifras, luego de llenar la lista, recorra cada elemento sumando el digito uno con el digito dos, La lista puede ser de la longitud que el usuario ingrese.

def insertNumbers():
    length = int(input("Enter the length of the list: "))
    numbers = []
    for i in range(length):
        number = int(input("Enter a two digit number: "))
        while number < 10 or number > 99:
            print("The number must be two digits")
            number = int(input("Enter a two digit number: "))
        numbers.append(number)
    return numbers

def sumDigits(numbers):
    sumDigits = []
    for number in numbers:
        firstDigit = number // 10
        secondDigit = number % 10
        sumDigit = firstDigit + secondDigit
        sumDigits.append(sumDigit)
    return sumDigits

def putListInFile(numbers,sumDigits):
    file = open(r"SecondAssigment/FirstChallengeBD.txt", "w")
    file.write(f"List of numbers: {numbers} \nList of Sum Digits: {sumDigits} \n")
    file.close

numbers = insertNumbers()
sumsDigits = sumDigits(numbers)
putListInFile(numbers, sumsDigits)


    