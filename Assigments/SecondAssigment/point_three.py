class StringSorter:
    def __init__(self):
        self.strings = []
        self.file_path = r"/workspaces/Programming-IV/Assigments/SecondAssigment/point_three_DB.txt"

    def add_strings(self):
        print("Enter at least 15 strings:")
        while len(self.strings) < 15:
            string = input(f"Enter string {len(self.strings) + 1}: ")
            self.strings.append(string)
        
        while True:
            cont = input("Do you want to add more strings? (y/n): ").strip().lower()
            if cont == 'y':
                string = input("Enter additional string: ")
                self.strings.append(string)
            else:
                break
        
        self.save_strings_to_file()

    def sort_strings(self):
        even_strings = sorted([s for s in self.strings if len(s) % 2 == 0])
        odd_strings = sorted([s for s in self.strings if len(s) % 2 != 0])
        sorted_list = even_strings + odd_strings
        self.save_sorted_strings_to_file(sorted_list)
        self.display_sorted_strings(sorted_list)
        return sorted_list

    def save_strings_to_file(self):
        with open(self.file_path, "a") as f:
            f.write("Original Strings:\n")
            for s in self.strings:
                f.write(s + "\n")
            f.write("-" * 30 + "\n")

    def save_sorted_strings_to_file(self, sorted_list):
        with open(self.file_path, "a") as f:
            f.write("Sorted Strings:\n")
            for s in sorted_list:
                f.write(s + "\n")
            f.write("-" * 30 + "\n")

    def display_sorted_strings(self, sorted_list):
        print("\nSorted Strings:")
        for s in sorted_list:
            print(s)

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Add Strings")
            print("2. Sort Strings")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.add_strings()
            elif choice == "2":
                sorted_strings = self.sort_strings()
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    sorter = StringSorter()
    sorter.menu()