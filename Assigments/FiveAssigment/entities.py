from datetime import datetime

class PersonalUniversitario:
    def __init__(self, name, age, department, start_date):
        self.name = name
        self.age = age
        self.department = department
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")

    def calcular_antiguedad(self):
        today = datetime.today()
        antiguedad = today.year - self.start_date.year - ((today.month, today.day) < (self.start_date.month, self.start_date.day))
        return antiguedad

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Department: {self.department}, Start Date: {self.start_date.date()}"

class Profesor(PersonalUniversitario):
    def __init__(self, name, age, department, start_date, tipo_profesor, horas_trabajadas):
        super().__init__(name, age, department, start_date)
        self.tipo_profesor = tipo_profesor
        self.horas_trabajadas = horas_trabajadas
        self.materias = []

    def calcular_sueldo(self):
        tarifa = 50 if self.tipo_profesor == "Titular" else 30
        return self.horas_trabajadas * tarifa

    def asignar_materias(self, materias):
        if len(materias) >= 3:
            self.materias = materias[:3]
        else:
            raise ValueError("Debe asignar al menos tres materias.")

    def mostrar_materias(self):
        return ", ".join(self.materias)

    def __str__(self):
        return super().__str__() + f", Tipo: {self.tipo_profesor}, Sueldo: {self.calcular_sueldo()}"

class Alumno(PersonalUniversitario):
    def __init__(self, name, age, department, start_date, matricula, carrera):
        super().__init__(name, age, department, start_date)
        self.matricula = matricula
        self.carrera = carrera

    def __str__(self):
        return super().__str__() + f", Matrícula: {self.matricula}, Carrera: {self.carrera}"

class ProfesorAyudante(Profesor, Alumno):
    def __init__(self, name, age, department, start_date, tipo_profesor, horas_trabajadas, matricula, carrera):
        Profesor.__init__(self, name, age, department, start_date, tipo_profesor, horas_trabajadas)
        Alumno.__init__(self, name, age, department, start_date, matricula, carrera)

    def __str__(self):
        return Profesor.__str__(self) + f", Matrícula: {self.matricula}, Carrera: {self.carrera}"