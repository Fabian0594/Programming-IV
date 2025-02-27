from io import *

class User:
    def insert_data(self):
        self.profession = input("Enter your profession: ")
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))

    def return_data(self):
        return f"User(\nName: {self.name}\nProfession: {self.profession}\nAge: {self.age}\n)\n"


def fill_the_list():
    users_list = []
    while True:
        user_temp = User()
        user_temp.insert_data()
        users_list.append(user_temp)
        if input("Enter 0 to exit or another number to continue adding users: ") == "0":
            return users_list


def count_occurrences(users, attribute, value):
    return sum(1 for user in users if getattr(user, attribute) == value)


def is_even(number):
    return number % 2 == 0


def file_insert_data(data):
    path = r"SecondAssigment/secondChallengeBD.txt"

    with open(path, "w", encoding="utf-8") as file:
        for user in data:
            file.write(user.return_data())


def menu(user_list):
    if not user_list:
        print("No users found. Please create a list first.\n")
        user_list = fill_the_list()

    print("\nWelcome\nSelect your option:")
    print("1. Create a new list and enter data")
    print("2. Count occurrences by Name")
    print("3. Count occurrences by Age")
    print("4. Count occurrences by Profession")
    print("5. Show all users")
    print("6. Save data to file")
    print("7. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        user_list = fill_the_list()
    elif option in ["2", "3", "4"]:
        if not user_list:
            print("The list is empty. Please create a list first.\n")
            return menu(user_list)

        search_field = {"2": "name", "3": "age", "4": "profession"}[option]
        search_value = input(f"Enter the {search_field}: ")
        if option == "3":
            search_value = int(search_value)  # Convertir edad a entero

        occurrences = count_occurrences(user_list, search_field, search_value)
        print(f"\nOccurrences: {occurrences}")
        print(f"The times {search_value} appears is {'even' if is_even(occurrences) else 'odd'}\n")
    elif option == "5":
        print("\nUser List:")
        for user in user_list:
            print(user.return_data())
    elif option == "6":
        file_insert_data(user_list)
        print("Data saved successfully!")
    elif option == "7":
        print("Goodbye!")
        return
    else:
        print("Invalid option. Try again.\n")

    if input("Do you want to go back? (y/n): ").lower() == "y":
        menu(user_list)


def main():
    user_list = []
    menu(user_list)


main()
