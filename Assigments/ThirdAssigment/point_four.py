import math

class ScientificCalculator:
    def __init__(self):
        self.last_result = 0
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b if b != 0 else "Error: Division by zero"
    
    def power(self, base, exponent):
        return math.pow(base, exponent)
    
    def square_root(self, number):
        return math.sqrt(number) if number >= 0 else "Error: Square root of a negative number"
    
    def logarithm(self, number, base=10):
        return math.log(number, base) if number > 0 and base > 0 else "Error: Invalid logarithm parameters"
    
    def sine(self, angle):
        return math.sin(math.radians(angle))
    
    def cosine(self, angle):
        return math.cos(math.radians(angle))
    
    def tangent(self, angle):
        return "Error: Undefined tangent" if (angle % 180) == 90 else math.tan(math.radians(angle))
    
    def factorial(self, number):
        return math.factorial(number) if number >= 0 and isinstance(number, int) else "Error: Factorial only for non-negative integers"
    
    def absolute_value(self, number):
        return abs(number)


def get_two_numbers():
    """Utility function to get two numbers from user input."""
    while True:
        try:
            a, b = map(float, input("Enter two values separated by space: ").split())
            return a, b
        except ValueError:
            print("Invalid input. Please enter two numbers.")

def get_one_number():
    """Utility function to get one number from user input."""
    while True:
        try:
            return float(input("Enter a value: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

def menu():
    calculator = ScientificCalculator()

    operations = {
        1: ("Addition", calculator.add, get_two_numbers),
        2: ("Subtraction", calculator.subtract, get_two_numbers),
        3: ("Multiplication", calculator.multiply, get_two_numbers),
        4: ("Division", calculator.divide, get_two_numbers),
        5: ("Power", calculator.power, get_two_numbers),
        6: ("Square Root", calculator.square_root, get_one_number),
        7: ("Logarithm", calculator.logarithm, get_two_numbers),
        8: ("Sine", calculator.sine, get_one_number),
        9: ("Cosine", calculator.cosine, get_one_number),
        10: ("Tangent", calculator.tangent, get_one_number),
        11: ("Factorial", calculator.factorial, get_one_number),
        12: ("Absolute Value", calculator.absolute_value, get_one_number),
    }

    while True:
        print("\nWelcome! What operation do you want to perform?")
        for key, (name, _, _) in operations.items():
            print(f"{key}. {name}")
        
        try:
            option = int(input("Enter your option: "))
            if option in operations:
                name, func, input_func = operations[option]
                args = input_func()
                result = func(*args) if isinstance(args, tuple) else func(args)
                print(f"\n{name} Result: {result}")
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

        back_to = input("\nDo you want to go back to the main menu? (y/n): ").lower()
        if back_to != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    menu()
