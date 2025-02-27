#Ejercicio 3
"""Escribir un programa que almacene las asignaturas de un curso
en una lista, pida al usuario las 4 notas de cada materia y en
pantalla mostrar el promedio que ha sacado en cada materia y si
alguna materia queda por debajo de la nota 3 debe salir en
pantalla “asignatura perdida”, luego se deben calcular el
promedio general de todas las materias si el promedio está por
debajo de 3 debe imprimir “semestre perdido”, si esta entre 3 y 4
debe imprimir “buen trabajo”, si el promedio esta entre 4 y 5
debe imprimir “felicidades serás becado”."""

def getAverage():
    subjects = ["Maths", "English", "Science", "History"]
    grades = []
    for subject in subjects:
        print(f"Enter the grades for {subject}")
        for i in range(4):
            grade = float(input(f"Enter grade {i+1}: "))
            grades.append(grade)
        average = sum(grades)/len(grades)
        if average < 3:
            print(f"{subject} failed")
        print(f"Average for {subject}: {average}")
    generalAverage = sum(grades)/len(grades)
    if generalAverage < 3:
        print("Semester failed")
    elif generalAverage >= 3 and generalAverage < 4:
        print("Good job")
    elif generalAverage >= 4 and generalAverage <= 5:
        print("Congratulations, you will be granted a scholarship")
    else:
        print("Invalid average")
    return generalAverage

print(getAverage())