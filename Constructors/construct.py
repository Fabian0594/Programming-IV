class Student:
    students_list = []
    
    def __init__(self, name, age, program):
        self.name = name
        self.age = age
        self.program = program
    
    def __str__(self):
        return f"name: {self.name}, age: {self.age}, program: {self.program}"

def fill_list():
    while True:
        name = input("Enter the name or press enter to exit: ")
        age = input("Enter the age or press enter to exit: ")
        program = input("Enter the program or press enter to exit: ")
        
        if name and age and program:
            student_obj = Student(name, age, program)
            Student.students_list.append(student_obj)
        else:
            break

def print_objects():
    for student in Student.students_list:
        print(student)
    
fill_list()
print_objects()
