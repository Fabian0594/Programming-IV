class Student:
    age = 0
    name = ""
    program = ""
    
    def show_data(self):
        return f"Name: {self.name} \nAge: {self.age} \nProgram: {self.program}"
    
    def datos(self):
        pass
    
    def insert_data(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.program = input("Enter your program: ")
    
pepito = Student()
pepito.age = 20
pepito.name = "Pepito"
pepito.program = "Computer Science"
pepito.show_data()
print(pepito.show_data())

pepito.insert_data()
print(pepito.show_data())