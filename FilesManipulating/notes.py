from io import *

archivo = open(r"FilesManipulating/archivo.txt", "w")

archivo.write("Hola mundo\n")

archivo.close()

print(f"archivo.txt creado en {archivo.name}")

archivo = open(r"FilesManipulating/archivo.txt", "r")
print (f"{archivo.read()}")



