from datetime import datetime

# Definiciones de clases
class PersonalUniversitario:
    def __init__(self, name, age, department, start_date):
        self.name = name
        self.age = age
        self.department = department
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")

    # Método para calcular la antigüedad
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

    # Método para calcular el sueldo
    def calcular_sueldo(self):
        tarifa = 50 if self.tipo_profesor == "Titular" else 30
        return self.horas_trabajadas * tarifa

    # Método para asignar materias (minimo 3)
    def asignar_materias(self, materias):
        if len(materias) >= 3:
            self.materias = materias[:3]
        else:
            raise ValueError("Debe asignar al menos tres materias.")

    # Método para mostrar materias
    def mostrar_materias(self):
        return ", ".join(self.materias)

    def __str__(self):
        return super().__str__() + f", Tipo: {self.tipo_profesor}, Sueldo: {self.calcular_sueldo()}"

class Alumno(PersonalUniversitario):
    # Constructor de la clase Alumno que hereda de PersonalUniversitario
    def __init__(self, name, age, department, start_date, matricula, carrera):
        super().__init__(name, age, department, start_date)
        self.matricula = matricula
        self.carrera = carrera

    def __str__(self):
        return super().__str__() + f", Matrícula: {self.matricula}, Carrera: {self.carrera}"

class ProfesorAyudante(Profesor, Alumno):
    # Constructor de la clase ProfesorAyudante que hereda de Profesor y Alumno
    def __init__(self, name, age, department, start_date, tipo_profesor, horas_trabajadas, matricula, carrera):
        Profesor.__init__(self, name, age, department, start_date, tipo_profesor, horas_trabajadas)
        Alumno.__init__(self, name, age, department, start_date, matricula, carrera)

    def __str__(self):
        return Profesor.__str__(self) + f", Matrícula: {self.matricula}, Carrera: {self.carrera}"

class Producto:
    """Clase principal que representa un producto genérico del supermercado"""
    def __init__(self, nombre, marca, precio, codigo_barras, stock):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.codigo_barras = codigo_barras
        self.stock = stock
        self.en_promocion = False

    def aplicar_descuento(self, porcentaje):
        precio_original = self.precio
        self.precio = self.precio * (1 - porcentaje / 100)
        self.en_promocion = True
        return f"Descuento del {porcentaje}% aplicado a {self.nombre}. Precio anterior: ${precio_original:.2f}, Precio actual: ${self.precio:.2f}"

    def reponer_stock(self, cantidad):
        self.stock += cantidad
        return f"Stock de {self.nombre} actualizado. Stock actual: {self.stock} unidades"

    def info_producto(self):
        estado = "En promoción" if self.en_promocion else "Precio regular"
        return f"{self.nombre} - {self.marca} | Precio: ${self.precio:.2f} ({estado}) | Stock: {self.stock} unidades"


class Departamento:
    """Clase principal que representa características de un departamento del supermercado"""
    def __init__(self, area, ubicacion, responsable, temperatura_ambiente, horario_atencion):
        self.area = area
        self.ubicacion = ubicacion
        self.responsable = responsable
        self.temperatura_ambiente = temperatura_ambiente
        self.horario_atencion = horario_atencion
        self.ventas_diarias = 0

    def registrar_venta(self, monto):
        self.ventas_diarias += monto
        return f"Venta de ${monto:.2f} registrada en departamento de {self.area}"

    def cambiar_responsable(self, nuevo_responsable):
        antiguo = self.responsable
        self.responsable = nuevo_responsable
        return f"Responsable de {self.area} actualizado: {antiguo} → {nuevo_responsable}"

    def info_departamento(self):
        return f"Departamento: {self.area} | Ubicación: {self.ubicacion} | Responsable: {self.responsable} | Horario: {self.horario_atencion}"


class ProductoAlimenticio(Producto, Departamento):
    """Subclase que representa productos alimenticios"""
    def __init__(self, nombre, marca, precio, codigo_barras, stock, area, ubicacion, responsable, temperatura_ambiente, horario_atencion, fecha_caducidad):
        Producto.__init__(self, nombre, marca, precio, codigo_barras, stock)
        Departamento.__init__(self, area, ubicacion, responsable, temperatura_ambiente, horario_atencion)
        self.fecha_caducidad = fecha_caducidad
        self.tipo_conservacion = "Ambiente"

    def verificar_caducidad(self, fecha_actual):
        if fecha_actual > self.fecha_caducidad:
            return f"ALERTA: {self.nombre} ha caducado. Retirar del inventario."
        dias_restantes = (self.fecha_caducidad - fecha_actual).days
        if dias_restantes < 5:
            return f"ADVERTENCIA: {self.nombre} caducará en {dias_restantes} días."
        return f"{self.nombre} en buen estado. Caducidad en {dias_restantes} días."

    def __str__(self):
        return f"Alimento: {self.nombre} ({self.marca}) - Caducidad: {self.fecha_caducidad.strftime('%d/%m/%Y')}"


class ProductoRefrigerado(ProductoAlimenticio):
    """Subclase que representa productos que necesitan refrigeración"""
    def __init__(self, nombre, marca, precio, codigo_barras, stock, area, ubicacion, responsable, temperatura_ambiente, horario_atencion, fecha_caducidad, temperatura_conservacion):
        super().__init__(nombre, marca, precio, codigo_barras, stock, area, ubicacion, responsable, temperatura_ambiente, horario_atencion, fecha_caducidad)
        self.temperatura_conservacion = temperatura_conservacion
        self.tipo_conservacion = "Refrigerado"

    def verificar_temperatura(self, temp_actual):
        if temp_actual > self.temperatura_conservacion + 2:
            return f"ALERTA: Temperatura demasiado alta para {self.nombre}. Actual: {temp_actual}°C, Recomendada: {self.temperatura_conservacion}°C"
        if temp_actual < self.temperatura_conservacion - 2:
            return f"ALERTA: Temperatura demasiado baja para {self.nombre}. Actual: {temp_actual}°C, Recomendada: {self.temperatura_conservacion}°C"
        return f"Temperatura adecuada para {self.nombre}: {temp_actual}°C"

    def __str__(self):
        return f"Refrigerado: {self.nombre} ({self.marca}) - Temp: {self.temperatura_conservacion}°C - Caducidad: {self.fecha_caducidad.strftime('%d/%m/%Y')}"


class ProductoLimpieza(Producto, Departamento):
    """Subclase que representa productos de limpieza"""
    def __init__(self, nombre, marca, precio, codigo_barras, stock, area, ubicacion, responsable, temperatura_ambiente, horario_atencion, tipo_superficie):
        Producto.__init__(self, nombre, marca, precio, codigo_barras, stock)
        Departamento.__init__(self, area, ubicacion, responsable, temperatura_ambiente, horario_atencion)
        self.tipo_superficie = tipo_superficie
        self.contiene_toxicos = False

    def advertencia_uso(self):
        if self.contiene_toxicos:
            return f"ADVERTENCIA: {self.nombre} contiene sustancias tóxicas. Usar guantes y mantener fuera del alcance de niños."
        return f"{self.nombre} es seguro para uso doméstico en superficies de {self.tipo_superficie}"

    def __str__(self):
        toxicos = "Contiene tóxicos" if self.contiene_toxicos else "No tóxico"
        return f"Limpieza: {self.nombre} ({self.marca}) - Para {self.tipo_superficie} - {toxicos}"


class ProductoElectronico(Producto, Departamento):
    """Subclase que representa productos electrónicos"""
    def __init__(self, nombre, marca, precio, codigo_barras, stock, area, ubicacion, responsable, temperatura_ambiente, horario_atencion, garantia_meses):
        Producto.__init__(self, nombre, marca, precio, codigo_barras, stock)
        Departamento.__init__(self, area, ubicacion, responsable, temperatura_ambiente, horario_atencion)
        self.garantia_meses = garantia_meses
        self.voltaje = "110-220V"

    def generar_garantia(self, nombre_cliente):
        fecha_actual = datetime.now()
        fecha_fin = fecha_actual.replace(month=fecha_actual.month + self.garantia_meses)
        return f"GARANTÍA para {nombre_cliente}: Producto {self.nombre} ({self.marca})\nInicio: {fecha_actual.strftime('%d/%m/%Y')}\nFin: {fecha_fin.strftime('%d/%m/%Y')}\nDuración: {self.garantia_meses} meses"

    def __str__(self):
        return f"Electrónico: {self.nombre} ({self.marca}) - Garantía: {self.garantia_meses} meses"


class ProductoRopa(Producto, Departamento):
    """Subclase que representa productos de ropa"""
    def __init__(self, nombre, marca, precio, codigo_barras, stock, area, ubicacion, responsable, temperatura_ambiente, horario_atencion, talla, material):
        Producto.__init__(self, nombre, marca, precio, codigo_barras, stock)
        Departamento.__init__(self, area, ubicacion, responsable, temperatura_ambiente, horario_atencion)
        self.talla = talla
        self.material = material
        self.temporada = "Todo el año"

    def verificar_disponibilidad_talla(self, talla_buscada):
        if talla_buscada == self.talla and self.stock > 0:
            return f"{self.nombre} disponible en talla {talla_buscada}. Stock: {self.stock} unidades."
        elif talla_buscada == self.talla and self.stock == 0:
            return f"{self.nombre} en talla {talla_buscada} agotado. Solicitar reposición."
        return f"{self.nombre} no disponible en talla {talla_buscada}. Solo disponible en talla {self.talla}."

    def __str__(self):
        return f"Ropa: {self.nombre} ({self.marca}) - Talla: {self.talla} - Material: {self.material}"

