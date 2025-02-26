 User:
    def insert_data(self):
        self.profession = input("Enter your profession: ")
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
    
    def return_data(self):
        return f"User(\nName: {self.name}\nProfession: {self.profession}\nAge: {self.age}\n )"
    
    def compare_by_name(self, other):
        return self.name == other.name
    
    def compare_by_profession(self, other):
        return self.profession == other.profession
    
    def compare_by_age(self, other):
        return self.age == other.age
    

def fill_the_list():
    users_list = []
    while True:
        user_temp = User()
        user_temp.insert_data()
        users_list.append(user_temp)
        if int(input("Enter 0 to exit or another number to continue adding users: \n")) == 0:
            return users_list


def count_occurrences_by_name(users, element):
    return sum(1 for user in users if user.name == element)


def count_occurrences_by_age(users, element):
    return sum(1 for user in users if user.age == element)


def count_occurrences_by_profession(users, element):
    return sum(1 for user in users if user.profession == element)


def is_even(number):
    return number % 2 == 0

def menu():
    global user_list  # Usar la lista global
    print("Welcome\nSelect your option:\n1. Create a list and enter data\n2. Count occurrences by Name\n3. Count occurrences by Age\n4. Count occurrences by Profession")
    option = int(input())
    
    if option == 1:
        user_list = fill_the_list()
    elif option == 2:
        name_to_find = input("Enter the name: ")
        occurrences_by_name = count_occurrences_by_name(user_list, name_to_find)
        print(occurrences_by_name)
        print(f"The times {name_to_find} appears is {'even' if is_even(occurrences_by_name) else 'odd'}\n")
    elif option == 3:
        age_to_find = int(input("Enter the age: "))
        occurrences_by_age = count_occurrences_by_age(user_list, age_to_find)
        print(occurrences_by_age)
        print(f"The times {age_to_find} appears is {'even' if is_even(occurrences_by_age) else 'odd'}\n")
    elif option == 4:
        profession_to_find = input("Enter the profession: ")
        occurrences_by_profession = count_occurrences_by_profession(user_list, profession_to_find)
        print(occurrences_by_profession)
        print(f"The times {profession_to_find} appears is {'even' if is_even(occurrences_by_profession) else 'odd'}\n")
    else:
        print("Invalid option. Exiting...")
        return
    
    option = input("Do you want to go back? (y/n): ")
    if option.lower() == 'y':
        menu()
    else:
        print("Goodbye!")
        
def main():
    user_list = []
    menu()

main()
