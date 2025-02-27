import os

# Menú principal para elegir ejercicios
def main_menu():
    while True:
        print("\nSeleccione un ejercicio:")
        print("1. Sumar dígitos de números de dos cifras")
        print("2. Contar ocurrencias de un atributo en usuarios")
        print("3. Ordenar lista de cadenas")
        print("4. Diseñar entidades")
        print("5. Salir")
        opcion = input("Ingrese su opción: ")
        
        if opcion == "1":
            ejecutar_ejercicio_1()
        elif opcion == "2":
            ejecutar_ejercicio_2()
        elif opcion == "3":
            ejecutar_ejercicio_3()
        elif opcion == "4":
            ejecutar_ejercicio_4()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejercicio 1: Sumar dígitos de números de dos cifras y guardarlos en un archivo
class NumberProcessor:
    def __init__(self):
        self.numbers = []
        self.sums = []

    def insert_numbers(self):
        length = int(input("Ingrese la longitud de la lista: "))
        for _ in range(length):
            number = int(input("Ingrese un número de dos cifras: "))
            while number < 10 or number > 99:
                print("El número debe ser de dos cifras")
                number = int(input("Ingrese un número de dos cifras: "))
            self.numbers.append(number)

    def sum_digits(self):
        self.sums = [sum(map(int, str(num))) for num in self.numbers]

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(f"Lista de números: {self.numbers}\n")
            file.write(f"Lista de suma de dígitos: {self.sums}\n")

def ejecutar_ejercicio_1():
    number_processor = NumberProcessor()
    number_processor.insert_numbers()
    number_processor.sum_digits()
    number_processor.save_to_file("FirstChallengeBD.txt")
    print("Datos guardados en FirstChallengeBD.txt")

# Ejercicio 2: Contar ocurrencias de un atributo en una lista de objetos y determinar si es par o impar
class User:
    def __init__(self, name, profession, age):
        self.name = name
        self.profession = profession
        self.age = age

    def greet(self):
        return f"Hola, soy {self.name} y trabajo como {self.profession}."

    def __str__(self):
        return f"Usuario(Nombre: {self.name}, Profesión: {self.profession}, Edad: {self.age})"

class UserManager:
    def __init__(self):
        self.users = []

    def create_users(self):
        while True:
            name = input("Ingrese su nombre: ")
            profession = input("Ingrese su profesión: ")
            age = int(input("Ingrese su edad: "))
            self.users.append(User(name, profession, age))
            if input("Ingrese 0 para salir o cualquier otro número para continuar: ") == "0":
                break

    def count_occurrences(self, attribute, value):
        return sum(1 for user in self.users if getattr(user, attribute) == value)

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for user in self.users:
                file.write(str(user) + "\n")

def ejecutar_ejercicio_2():
    user_manager = UserManager()
    user_manager.create_users()
    attribute = input("Ingrese el atributo a buscar (name, profession, age): ")
    value = input("Ingrese el valor a buscar: ")
    if attribute == "age":
        value = int(value)
    occurrences = user_manager.count_occurrences(attribute, value)
    print(f"El valor {value} aparece {occurrences} veces y es {'par' if occurrences % 2 == 0 else 'impar'}")
    user_manager.save_to_file("secondChallengeBD.txt")
    print("Datos guardados en secondChallengeBD.txt")

# Ejercicio 3: Ordenar lista de cadenas por cantidad de caracteres (pares primero, luego impares)
class StringSorter:
    def __init__(self):
        self.strings = []
        self.sorted_strings = []

    def insert_strings(self):
        while len(self.strings) < 15:
            string = input("Ingrese una cadena: ")
            self.strings.append(string)

    def sort_strings(self):
        evens = [s for s in self.strings if len(s) % 2 == 0]
        odds = [s for s in self.strings if len(s) % 2 != 0]
        self.sorted_strings = evens + odds

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write("Lista ordenada de cadenas:\n")
            file.write("\n".join(self.sorted_strings))

def ejecutar_ejercicio_3():
    string_sorter = StringSorter()
    string_sorter.insert_strings()
    string_sorter.sort_strings()
    string_sorter.save_to_file("thirdChallengeBD.txt")
    print("Datos guardados en thirdChallengeBD.txt")

# Ejercicio 4: Diseñar entidades con atributos y métodos
class Entity:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    def describe(self):
        return f"{self.name} tiene las siguientes características: {', '.join(f'{k}: {v}' for k, v in self.attributes.items())}"

    def save_to_file(self, filename):
        with open(filename, "a") as file:
            file.write(self.describe() + "\n")

def ejecutar_ejercicio_4():
    entities = [
        Entity("Libro", {"Título": "1984", "Autor": "George Orwell", "Páginas": 328, "Idioma": "Español", "Editorial": "Debolsillo"}),
        Entity("Casa", {"Ubicación": "Ciudad", "Habitaciones": 3, "Baños": 2, "Color": "Blanco", "Tamaño": "120m²"}),
    ]
    with open("fourthChallengeBD.txt", "w") as file:
        file.write("Lista de entidades:\n")
    for entity in entities:
        entity.save_to_file("fourthChallengeBD.txt")
    print("Datos guardados en fourthChallengeBD.txt")

# Ejecutar menú
main_menu()
3
