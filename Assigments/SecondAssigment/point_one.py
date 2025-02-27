class NumberProcessor:
    def __init__(self):
        self.numbers = []
        self.results = []

    def get_numbers(self):
        n = int(input("Enter the number of values: "))
        for _ in range(n):
            while True:
                num = input("Enter a two-digit integer: ")
                if num.isdigit() and 10 <= int(num) <= 99:
                    self.numbers.append(int(num))
                    break
                else:
                    print("Invalid number. It must be a two-digit integer.")

    def sum_digits(self):
        self.results = [int(str(num)[0]) + int(str(num)[1]) for num in self.numbers]

    def save_to_file(self):
        path = r"/workspaces/Programming-IV/Assigments/SecondAssigment/point_one_DB.txt"
        with open(path, "a") as f:
            f.write(f"Input: {self.numbers}\n")
            f.write(f"Output: {self.results}\n")
            f.write("-" * 30 + "\n")

    def run(self):
        self.get_numbers()
        self.sum_digits()
        print("Output:", self.results)
        self.save_to_file()


if __name__ == "__main__":
    processor = NumberProcessor()
    processor.run()
