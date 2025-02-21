from io import *

def insertData(data):
    archivo = open(r"FilesManipulating/archivo.txt", "w")
    archivo.write(data)
    archivo.close()
    
def readData():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    data = f"Name: {name} \nAge: {age}"
    insertData(data)
    
def showData():
    archivo = open(r"FilesManipulating/archivo.txt", "r")
    print (f"{archivo.read()}")
    
def removeData():
    data = ""
    insertData(data)
    
def menu():
    print("Select an option: \n")
    print("1.- Write data in the file \n")
    print("2.- list data \n")
    print("3.- remove data in the file \n")
    print("4.- leave \n")
    option = int(input())
    
    match option:
        case 1:
            readData()
        case 2:
            showData()
        case 3:
            removeData()
        case 4:
            print("Goodbye")
        case _:
            print("Invalid option")
            menu()
            
menu()
    
    
    