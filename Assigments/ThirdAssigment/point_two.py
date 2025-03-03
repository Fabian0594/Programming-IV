class rectangle:
    
    def __init__(self):
        self.height = 0
        self.width = 0
        
    def insert_data(self):
        self.height = int(input("Insert the heigth of the rectangle: \n"))
        self.width = int(input("Insert the width of the rectangle: \n"))
    
    def print_rectangle(self):
        for i in range(self.height):
            print(f"{"*" * self.width}")            

def main():
    rectangle_one = rectangle()
    rectangle_one.insert_data()
    rectangle_one.print_rectangle()
    
if __name__ == "__main__":
    main()