import string
import os

class EncriptacionCesar:
    def __init__(self, key):
        self.key = key % 26  # Asegurar que la clave esté dentro del rango de 0-25
        self.original_alphabet = list(string.ascii_lowercase)
        self.shifted_alphabet = self.original_alphabet[-self.key:] + self.original_alphabet[:-self.key]
    
    def encriptar(self, texto):
        texto = texto.lower()
        encriptado = ''.join(
            self.shifted_alphabet[self.original_alphabet.index(c)] if c in self.original_alphabet else c
            for c in texto
        )
        return encriptado
    
    def desencriptar(self, texto):
        texto = texto.lower()
        desencriptado = ''.join(
            self.original_alphabet[self.shifted_alphabet.index(c)] if c in self.shifted_alphabet else c
            for c in texto
        )
        return desencriptado
    
    def guardar_en_archivo(self, texto, nombre_archivo):
        ruta = f"/workspaces/Programming-IV/Exam_one/{nombre_archivo}"
        with open(ruta, 'w', encoding='utf-8') as file:
            file.write(f"{self.key}\n{texto}")  # Guarda la clave en la primera línea
    
    def leer_desde_archivo(self, nombre_archivo):
        ruta = f"/workspaces/Programming-IV/Exam_one/{nombre_archivo}"
        if os.path.exists(ruta):
            with open(ruta, 'r', encoding='utf-8') as file:
                lineas = file.readlines()
                if len(lineas) < 2:
                    return None, None  # Archivo mal formado
                try:
                    key = int(lineas[0].strip())  # Primera línea: clave de cifrado
                    texto = "".join(lineas[1:]).strip()  # Resto del archivo: texto cifrado
                    return key, texto
                except ValueError:
                    return None, None  # Si la clave no es un número
        return None, None

def menu():
    while True:
        print("\nMenú de Cifrado César")
        print("1. Encriptar texto")
        print("2. Desencriptar texto")
        print("3. Guardar texto en archivo")
        print("4. Leer y desencriptar desde archivo")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            key = int(input("Ingrese la clave de cifrado: "))
            cesar = EncriptacionCesar(key)
            texto = input("Ingrese el texto a encriptar: ")
            encriptado = cesar.encriptar(texto)
            print("Texto Encriptado:", encriptado)

        elif opcion == "2":
            key = int(input("Ingrese la clave de cifrado: "))
            cesar = EncriptacionCesar(key)
            texto = input("Ingrese el texto a desencriptar: ")
            desencriptado = cesar.desencriptar(texto)
            print("Texto Desencriptado:", desencriptado)

        elif opcion == "3":
            key = int(input("Ingrese la clave de cifrado: "))
            cesar = EncriptacionCesar(key)
            texto = input("Ingrese el texto a encriptar y guardar: ")
            encriptado = cesar.encriptar(texto)
            archivo = input("Ingrese el nombre del archivo: ")
            cesar.guardar_en_archivo(encriptado, archivo)
            print("Texto encriptado y guardado con éxito.")

        elif opcion == "4":
            archivo = input("Ingrese el nombre del archivo a leer: ")
            key, contenido = EncriptacionCesar(0).leer_desde_archivo(archivo)
            if key is not None and contenido:
                cesar = EncriptacionCesar(key)
                desencriptado = cesar.desencriptar(contenido)
                print(f"Texto desencriptado con clave {key}: {desencriptado}")
            else:
                print("El archivo no existe o está mal formado.")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
