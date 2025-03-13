import os

class Product:
    
    # Constructor para la clase Product con los atributos name, id, price y stock
    def __init__(self, name: str, id: int, price: float, stock: int):
        self.name = name
        self.id = id
        self.price = price
        self.stock = stock
    
    # Método para imprimir los atributos de la clase Product
    def __str__(self):
        return f"Product: {self.name}, ID: {self.id}, Price: {self.price}, Stock: {self.stock}"
    
    # Método para disminuir la cantidad de stock de un producto
    def decrease_stock(self, quantity: int):
        self.stock -= quantity
    
    # Método para aumentar la cantidad de stock de un producto    
    def increase_stock(self, quantity: int):
        self.stock += quantity
        
class Client:
    
    # Constructor para la clase Client con los atributos name, id y credit
    def __init__(self, name: str, id: int, credit: float):
        self.name = name
        self.id = id
        self.credit = credit
        
    # Método para imprimir los atributos de la clase Client
    def __str__(self):
        return f"Client: {self.name}, ID: {self.id}, Credit: {self.credit}"
    
    # Método para realizar una compra de un producto
    def make_purchase(self, product: Product, quantity: int):
        if product.stock >= quantity:
            product.decrease_stock(quantity)
            self.credit -= product.price * quantity
            return True
        else:
            return False
        
class Shop:
    
    # Constructor para la clase Shop con los atributos products y clients
    def __init__(self):
        self.products = []
        self.clients = []
        
    # Método para agregar un producto a la lista de productos
    def add_product(self, product: Product):
        self.products.append(product)
    
    # Método para agregar un cliente a la lista de clientes
    def add_client(self, client: Client):
        self.clients.append(client)
    
    # Método para realizar una compra de un producto por parte de un cliente
    def make_purchase(self, client_id: int, product_id: int, quantity: int):
        client = self.get_client(client_id)
        product = self.get_product(product_id)
        if client and product:
            return client.make_purchase(product, quantity)
        else:
            return False
        
    # Método para obtener un cliente a partir de su id    
    def get_client(self, client_id: int):
        for client in self.clients:
            if client.id == client_id:
                return client
        return None
    
    # Método para obtener un producto a partir de su id
    def get_product(self, product_id: int):
        for product in self.products:
            if product.id == product_id:
                return product
        return
    
    # Método para mostrar los productos disponibles
    def show_products(self):
        for product in self.products:
            print(product)
    
    # Método para mostrar los clientes registrados
    def show_clients(self):
        for client in self.clients:
            print(client)
            
    # Método para guardar los productos y clientes en un archivo
    def save_data(self, file_name: str):
        with open(file_name, "w") as file:
            for product in self.products:
                file.write(f"{product.name},{product.id},{product.price},{product.stock}\n")
            for client in self.clients:
                file.write(f"{client.name},{client.id},{client.credit}\n")
    
    # Método para cargar los productos y clientes desde un archivo
    def load_data(self, file_name: str):
        with open(file_name, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4:
                    product = Product(data[0], int(data[1]), float(data[2]), int(data[3]))
                    self.add_product(product)
                elif len(data) == 3:
                    client = Client(data[0], int(data[1]), float(data[2]))
                    self.add_client(client)
    
# Menu para el sistema
def menu():
    print("1. Add product")
    print("2. Add client")
    print("3. Make purchase")
    print("4. Show products")
    print("5. Show clients")
    print("6. Save data")
    print("7. Load data")
    print("8. Exit")
    option = int(input("Enter an option: "))
    return option

# Función principal para el sistema
def main():
    shop = Shop()
    option = 0
    while option != 8:
        option = menu()
        if option == 1:
            name = input("Enter the name of the product: ")
            id = int(input("Enter the id of the product: "))
            price = float(input("Enter the price of the product: "))
            stock = int(input("Enter the stock of the product: "))
            product = Product(name, id, price, stock)
            shop.add_product(product)
        elif option == 2:
            name = input("Enter the name of the client: ")
            id = int(input("Enter the id of the client: "))
            credit = float(input("Enter the credit of the client: "))
            client = Client(name, id, credit)
            shop.add_client(client)
        elif option == 3:
            client_id = int(input("Enter the id of the client: "))
            product_id = int(input("Enter the id of the product: "))
            quantity = int(input("Enter the quantity of the product: "))
            if shop.make_purchase(client_id, product_id, quantity):
                print("Purchase successful")
            else:
                print("Purchase failed")
        elif option == 4:
            shop.show_products()
        elif option == 5:
            shop.show_clients()
        elif option == 6:
            file_name = r"/workspaces/Programming-IV/Exam_one/products_clients_DB.txt"
            shop.save_data(file_name)
        elif option == 7:
            file_name = r"/workspaces/Programming-IV/Exam_one/products_clients_DB.txt"
            shop.load_data(file_name)
    print("Goodbye!")
    
if __name__ == "__main__":
    main()
    
    
        
        
    
        