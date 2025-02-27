class User:
    def __init__(self, name, age, program):
        self.name = name
        self.age = age
        self.program = program

class UserCounter:
    def __init__(self):
        self.users = []
        self.file_path = r"/workspaces/Programming-IV/Assigments/SecondAssigment/point_two_DB.txt"

    def add_user(self):
        while True:
            name = input("Enter user name: ")
            age = int(input("Enter user age: "))
            program = input("Enter user program: ")
            user = User(name, age, program)
            self.users.append(user)
            self.save_user_to_file(user)
            cont = input("Do you want to add another user? (y/n): ").strip().lower()
            if cont != 'y':
                break

    def count_occurrences(self, attribute, value):
        count = sum(1 for user in self.users if getattr(user, attribute, None) == value)
        return count

    def check_even_odd(self, count):
        return "even" if count % 2 == 0 else "odd"

    def search_by_attribute(self, attribute):
        value = input(f"Enter the {attribute} to search for: ")
        if attribute == "age":
            value = int(value)
        count = self.count_occurrences(attribute, value)
        even_odd = self.check_even_odd(count)
        result_line = f"{attribute.capitalize()}: {value}, Count: {count}, Occurrences: {even_odd}"
        print(result_line)
        self.save_search_to_file(attribute, value, result_line)

    def save_user_to_file(self, user):
        with open(self.file_path, "a") as f:
            f.write(f"Added User -> Name: {user.name}, Age: {user.age}, Program: {user.program}\n")

    def save_search_to_file(self, attribute, value, result_line):
        with open(self.file_path, "a") as f:
            f.write(f"Search by: {attribute}, Value: {value}\n")
            f.write(result_line + "\n")
            f.write("-" * 30 + "\n")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Add User")
            print("2. Search by Name")
            print("3. Search by Age")
            print("4. Search by Program")
            print("5. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.add_user()
            elif choice == "2":
                self.search_by_attribute("name")
            elif choice == "3":
                self.search_by_attribute("age")
            elif choice == "4":
                self.search_by_attribute("program")
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    counter = UserCounter()
    counter.menu()
