from entities import PersonalUniversitario, Profesor, Alumno, ProfesorAyudante

def crear_personal_universitario():
    name = input("Ingrese el nombre del personal universitario: ")
    age = int(input("Ingrese la edad: "))
    department = input("Ingrese el departamento: ")
    start_date = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    return PersonalUniversitario(name, age, department, start_date)

def crear_profesor():
    name = input("Ingrese el nombre del profesor: ")
    age = int(input("Ingrese la edad: "))
    department = input("Ingrese el departamento: ")
    start_date = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    tipo_profesor = input("Ingrese el tipo de profesor (Titular/Asociado): ")
    horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
    profesor = Profesor(name, age, department, start_date, tipo_profesor, horas_trabajadas)
    materias = input("Ingrese las materias separadas por comas (mínimo 3): ").split(",")
    try:
        profesor.asignar_materias(materias)
    except ValueError as e:
        print(f"Error: {e}")
    return profesor

def crear_alumno():
    name = input("Ingrese el nombre del alumno: ")
    age = int(input("Ingrese la edad: "))
    department = input("Ingrese el departamento: ")
    start_date = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    matricula = input("Ingrese la matrícula: ")
    carrera = input("Ingrese la carrera: ")
    return Alumno(name, age, department, start_date, matricula, carrera)

def crear_profesor_ayudante():
    name = input("Ingrese el nombre del profesor ayudante: ")
    age = int(input("Ingrese la edad: "))
    department = input("Ingrese el departamento: ")
    start_date = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    tipo_profesor = input("Ingrese el tipo de profesor (Titular/Asociado): ")
    horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
    matricula = input("Ingrese la matrícula: ")
    carrera = input("Ingrese la carrera: ")
    profesor_ayudante = ProfesorAyudante(name, age, department, start_date, tipo_profesor, horas_trabajadas, matricula, carrera)
    materias = input("Ingrese las materias separadas por comas (mínimo 3): ").split(",")
    try:
        profesor_ayudante.asignar_materias(materias)
    except ValueError as e:
        print(f"Error: {e}")
    return profesor_ayudante

def mostrar_entidad(entidad):
    print("\n=== Información de la Entidad ===")
    print(entidad)
    if isinstance(entidad, Profesor):
        print(f"Materias: {entidad.mostrar_materias()}")
    print(f"Antigüedad: {entidad.calcular_antiguedad()} años\n")

def guardar_entidades_en_txt(entidades, archivo="entidades.txt"):
    with open(archivo, "w") as file:
        for i, entidad in enumerate(entidades, start=1):
            file.write(f"=== Entidad #{i} ===\n")
            file.write(f"{entidad}\n")
            if isinstance(entidad, Profesor):
                file.write(f"Materias: {entidad.mostrar_materias()}\n")
            file.write(f"Antigüedad: {entidad.calcular_antiguedad()} años\n")
            file.write("\n")
    print(f"Información guardada exitosamente en {archivo}.")