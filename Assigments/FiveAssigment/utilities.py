from entities import PersonalUniversitario, Profesor, Alumno, ProfesorAyudante
from entities import (
    Producto,
    Departamento,
    ProductoAlimenticio,
    ProductoRefrigerado,
    ProductoLimpieza,
    ProductoElectronico,
    ProductoRopa
)
from datetime import datetime

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

def crear_producto():
    nombre = input("Ingrese el nombre del producto: ")
    marca = input("Ingrese la marca: ")
    precio = float(input("Ingrese el precio: "))
    codigo_barras = input("Ingrese el código de barras: ")
    stock = int(input("Ingrese el stock: "))
    return Producto(nombre, marca, precio, codigo_barras, stock)

def crear_departamento():
    area = input("Ingrese el área del departamento: ")
    ubicacion = input("Ingrese la ubicación del departamento: ")
    responsable = input("Ingrese el responsable del departamento: ")
    temperatura_ambiente = float(input("Ingrese la temperatura ambiente (°C): "))
    horario_atencion = input("Ingrese el horario de atención: ")
    return Departamento(area, ubicacion, responsable, temperatura_ambiente, horario_atencion)

def crear_producto_alimenticio():
    producto = crear_producto()
    departamento = crear_departamento()
    fecha_caducidad = datetime.strptime(input("Ingrese la fecha de caducidad (YYYY-MM-DD): "), "%Y-%m-%d")
    return ProductoAlimenticio(
        producto.nombre, producto.marca, producto.precio, producto.codigo_barras, producto.stock,
        departamento.area, departamento.ubicacion, departamento.responsable, departamento.temperatura_ambiente,
        departamento.horario_atencion, fecha_caducidad
    )

def crear_producto_refrigerado():
    producto_alimenticio = crear_producto_alimenticio()
    temperatura_conservacion = float(input("Ingrese la temperatura de conservación (°C): "))
    return ProductoRefrigerado(
        producto_alimenticio.nombre, producto_alimenticio.marca, producto_alimenticio.precio,
        producto_alimenticio.codigo_barras, producto_alimenticio.stock, producto_alimenticio.area,
        producto_alimenticio.ubicacion, producto_alimenticio.responsable, producto_alimenticio.temperatura_ambiente,
        producto_alimenticio.horario_atencion, producto_alimenticio.fecha_caducidad, temperatura_conservacion
    )

def crear_producto_limpieza():
    producto = crear_producto()
    departamento = crear_departamento()
    tipo_superficie = input("Ingrese el tipo de superficie para el producto de limpieza: ")
    producto_limpieza = ProductoLimpieza(
        producto.nombre, producto.marca, producto.precio, producto.codigo_barras, producto.stock,
        departamento.area, departamento.ubicacion, departamento.responsable, departamento.temperatura_ambiente,
        departamento.horario_atencion, tipo_superficie
    )
    contiene_toxicos = input("¿El producto contiene tóxicos? (s/n): ").lower() == "s"
    producto_limpieza.contiene_toxicos = contiene_toxicos
    return producto_limpieza

def crear_producto_electronico():
    producto = crear_producto()
    departamento = crear_departamento()
    garantia_meses = int(input("Ingrese la garantía en meses: "))
    return ProductoElectronico(
        producto.nombre, producto.marca, producto.precio, producto.codigo_barras, producto.stock,
        departamento.area, departamento.ubicacion, departamento.responsable, departamento.temperatura_ambiente,
        departamento.horario_atencion, garantia_meses
    )

def crear_producto_ropa():
    producto = crear_producto()
    departamento = crear_departamento()
    talla = input("Ingrese la talla de la ropa: ")
    material = input("Ingrese el material de la ropa: ")
    return ProductoRopa(
        producto.nombre, producto.marca, producto.precio, producto.codigo_barras, producto.stock,
        departamento.area, departamento.ubicacion, departamento.responsable, departamento.temperatura_ambiente,
        departamento.horario_atencion, talla, material
    )

def mostrar_producto(producto):
    print("\n=== Información del Producto ===")
    print(producto)
    print(producto.info_producto())
    if isinstance(producto, Departamento):
        print(producto.info_departamento())
    if isinstance(producto, ProductoAlimenticio):
        fecha_actual = datetime.now()
        print(producto.verificar_caducidad(fecha_actual))
    if isinstance(producto, ProductoRefrigerado):
        temp_actual = float(input("Ingrese la temperatura actual (°C): "))
        print(producto.verificar_temperatura(temp_actual))
    if isinstance(producto, ProductoLimpieza):
        print(producto.advertencia_uso())
    if isinstance(producto, ProductoElectronico):
        nombre_cliente = input("Ingrese el nombre del cliente para la garantía: ")
        print(producto.generar_garantia(nombre_cliente))
    if isinstance(producto, ProductoRopa):
        talla_buscada = input("Ingrese la talla que desea verificar: ")
        print(producto.verificar_disponibilidad_talla(talla_buscada))

def guardar_productos_en_txt(productos, archivo="productos_supermercado.txt"):
    with open(archivo, "w", encoding="utf-8") as file:
        for i, producto in enumerate(productos, start=1):
            file.write(f"=== Producto #{i} ===\n")
            file.write(f"{producto}\n")
            file.write(f"{producto.info_producto()}\n")
            if isinstance(producto, Departamento):
                file.write(f"{producto.info_departamento()}\n")
            file.write("\n")
    print(f"Información guardada exitosamente en {archivo}.")