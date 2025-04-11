import tkinter as tk
from tkinter import ttk, messagebox
from figuras import Triangulo, Cuadrado, Rectangulo, Circulo

class CalculadoraAreasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Áreas")
        self.root.geometry("500x300")
        
        # Crear pestañas para cada figura
        self.tab_control = ttk.Notebook(root)
        
        self.tab_triangulo = ttk.Frame(self.tab_control)
        self.tab_cuadrado = ttk.Frame(self.tab_control)
        self.tab_rectangulo = ttk.Frame(self.tab_control)
        self.tab_circulo = ttk.Frame(self.tab_control)
        
        self.tab_control.add(self.tab_triangulo, text="Triángulo")
        self.tab_control.add(self.tab_cuadrado, text="Cuadrado")
        self.tab_control.add(self.tab_rectangulo, text="Rectángulo")
        self.tab_control.add(self.tab_circulo, text="Círculo")
        
        self.tab_control.pack(expand=1, fill="both")
        
        # Configurar cada pestaña
        self.setup_triangulo_tab()
        self.setup_cuadrado_tab()
        self.setup_rectangulo_tab()
        self.setup_circulo_tab()
    
    def setup_triangulo_tab(self):
        # Etiquetas y campos de entrada para el triángulo
        ttk.Label(self.tab_triangulo, text="Base:").grid(column=0, row=0, padx=10, pady=10)
        self.base_triangulo = ttk.Entry(self.tab_triangulo)
        self.base_triangulo.grid(column=1, row=0, padx=10, pady=10)
        
        ttk.Label(self.tab_triangulo, text="Altura:").grid(column=0, row=1, padx=10, pady=10)
        self.altura_triangulo = ttk.Entry(self.tab_triangulo)
        self.altura_triangulo.grid(column=1, row=1, padx=10, pady=10)
        
        # Botón para calcular
        ttk.Button(self.tab_triangulo, text="Calcular Área", 
                  command=self.calcular_area_triangulo).grid(column=0, row=2, columnspan=2, padx=10, pady=20)
        
        # Etiqueta para mostrar el resultado
        self.resultado_triangulo = ttk.Label(self.tab_triangulo, text="")
        self.resultado_triangulo.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
    
    def setup_cuadrado_tab(self):
        # Etiquetas y campos de entrada para el cuadrado
        ttk.Label(self.tab_cuadrado, text="Lado:").grid(column=0, row=0, padx=10, pady=10)
        self.lado_cuadrado = ttk.Entry(self.tab_cuadrado)
        self.lado_cuadrado.grid(column=1, row=0, padx=10, pady=10)
        
        # Botón para calcular
        ttk.Button(self.tab_cuadrado, text="Calcular Área", 
                  command=self.calcular_area_cuadrado).grid(column=0, row=1, columnspan=2, padx=10, pady=20)
        
        # Etiqueta para mostrar el resultado
        self.resultado_cuadrado = ttk.Label(self.tab_cuadrado, text="")
        self.resultado_cuadrado.grid(column=0, row=2, columnspan=2, padx=10, pady=10)
    
    def setup_rectangulo_tab(self):
        # Etiquetas y campos de entrada para el rectángulo
        ttk.Label(self.tab_rectangulo, text="Base:").grid(column=0, row=0, padx=10, pady=10)
        self.base_rectangulo = ttk.Entry(self.tab_rectangulo)
        self.base_rectangulo.grid(column=1, row=0, padx=10, pady=10)
        
        ttk.Label(self.tab_rectangulo, text="Altura:").grid(column=0, row=1, padx=10, pady=10)
        self.altura_rectangulo = ttk.Entry(self.tab_rectangulo)
        self.altura_rectangulo.grid(column=1, row=1, padx=10, pady=10)
        
        # Botón para calcular
        ttk.Button(self.tab_rectangulo, text="Calcular Área", 
                  command=self.calcular_area_rectangulo).grid(column=0, row=2, columnspan=2, padx=10, pady=20)
        
        # Etiqueta para mostrar el resultado
        self.resultado_rectangulo = ttk.Label(self.tab_rectangulo, text="")
        self.resultado_rectangulo.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
    
    def setup_circulo_tab(self):
        # Etiquetas y campos de entrada para el círculo
        ttk.Label(self.tab_circulo, text="Radio:").grid(column=0, row=0, padx=10, pady=10)
        self.radio_circulo = ttk.Entry(self.tab_circulo)
        self.radio_circulo.grid(column=1, row=0, padx=10, pady=10)
        
        # Botón para calcular
        ttk.Button(self.tab_circulo, text="Calcular Área", 
                  command=self.calcular_area_circulo).grid(column=0, row=1, columnspan=2, padx=10, pady=20)
        
        # Etiqueta para mostrar el resultado
        self.resultado_circulo = ttk.Label(self.tab_circulo, text="")
        self.resultado_circulo.grid(column=0, row=2, columnspan=2, padx=10, pady=10)
    
    def obtener_valor_positivo(self, valor, campo):
        try:
            num = float(valor)
            if num <= 0:
                messagebox.showerror("Error", f"El {campo} debe ser un número positivo")
                return None
            return num
        except ValueError:
            messagebox.showerror("Error", f"El {campo} debe ser un número válido")
            return None
    
    def calcular_area_triangulo(self):
        base = self.obtener_valor_positivo(self.base_triangulo.get(), "base")
        altura = self.obtener_valor_positivo(self.altura_triangulo.get(), "altura")
        
        if base is not None and altura is not None:
            triangulo = Triangulo(base, altura)
            area = triangulo.calcular_area()
            self.resultado_triangulo.config(text=f"Área del triángulo: {area:.2f}")
    
    def calcular_area_cuadrado(self):
        lado = self.obtener_valor_positivo(self.lado_cuadrado.get(), "lado")
        
        if lado is not None:
            cuadrado = Cuadrado(lado)
            area = cuadrado.calcular_area()
            self.resultado_cuadrado.config(text=f"Área del cuadrado: {area:.2f}")
    
    def calcular_area_rectangulo(self):
        base = self.obtener_valor_positivo(self.base_rectangulo.get(), "base")
        altura = self.obtener_valor_positivo(self.altura_rectangulo.get(), "altura")
        
        if base is not None and altura is not None:
            rectangulo = Rectangulo(base, altura)
            area = rectangulo.calcular_area()
            self.resultado_rectangulo.config(text=f"Área del rectángulo: {area:.2f}")
    
    def calcular_area_circulo(self):
        radio = self.obtener_valor_positivo(self.radio_circulo.get(), "radio")
        
        if radio is not None:
            circulo = Circulo(radio)
            area = circulo.calcular_area()
            self.resultado_circulo.config(text=f"Área del círculo: {area:.2f}")

# Para ejecutar la aplicación:
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraAreasApp(root)
    root.mainloop()