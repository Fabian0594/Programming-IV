# utils.py
from datetime import datetime

def validar_anio(anio_str):
    """Valida que un año esté en formato correcto y dentro de un rango válido"""
    try:
        anio = int(anio_str)
        if 1000 <= anio <= datetime.now().year:
            return True, anio
        return False, f"El año debe estar entre 1000 y {datetime.now().year}"
    except ValueError:
        return False, "El año debe ser un número entero"

def validar_isbn(isbn):
    """Validación básica de ISBN (simplificada)"""
    if not isbn:
        return True, None  # ISBN opcional
    
    # Eliminar guiones para la validación
    isbn_limpio = isbn.replace("-", "").replace(" ", "")
    
    # Validar longitud (ISBN-10 o ISBN-13)
    if len(isbn_limpio) not in [10, 13]:
        return False, "El ISBN debe tener 10 o 13 dígitos"
    
    # Aquí se podría implementar la validación completa con dígitos de control
    # Por simplicidad, solo validamos que sean dígitos (con X permitida en ISBN-10)
    if len(isbn_limpio) == 10:
        if not (isbn_limpio[:-1].isdigit() and (isbn_limpio[-1].isdigit() or isbn_limpio[-1].upper() == 'X')):
            return False, "Formato de ISBN-10 inválido"
    else:  # ISBN-13
        if not isbn_limpio.isdigit():
            return False, "Formato de ISBN-13 inválido"
    
    return True, isbn_limpio

def formatear_fecha(formato="%Y-%m-%d %H:%M:%S"):
    """Devuelve la fecha actual formateada"""
    return datetime.now().strftime(formato)