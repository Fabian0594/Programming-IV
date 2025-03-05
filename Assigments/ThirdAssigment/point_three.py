import datetime

class Employee:
    
    def __init__(self):
        self.file_path = r"/workspaces/Programming-IV/Assigments/ThirdAssigment/employee_data.txt"
        self.salary_per_hour = 0
        self.working_hours_per_month = 0
        self.start_year = 0
        self.gender = ""
        self.age = 0
        
    def insert_data(self):
        try:
            self.salary_per_hour = float(input("Enter your salary per hour: "))
            self.working_hours_per_month = int(input("Enter your working hours: "))
            self.start_year = int(input("Enter the year you started working: "))
            self.gender = input("Enter your gender (male/female): ").strip().lower()
            self.age = int(input("Enter your age: "))
        except ValueError:
            print("Invalid input! Please enter numbers where required.")
            return
    
    def month_salary(self):
        return (self.salary_per_hour * self.working_hours_per_month) * 28 
    
    def seniority_time(self):
        current_year = datetime.datetime.now().year
        return current_year - self.start_year
    
    def time_to_retire(self):
        pension_age = 57 if self.gender == "female" else 62
        years_left = pension_age - self.age
        return max(years_left, 0)
    
    def calculate_deductions(self):
        salary = self.month_salary()
        pension_cost = salary * 0.04
        health_cost = salary * 0.04
        yearly_pension = pension_cost * 12
        return pension_cost, health_cost, yearly_pension
    
    def insert_data_to_file(self):
        pension_cost, health_cost, yearly_pension = self.calculate_deductions()
        years_left = self.time_to_retire()

        try:
            with open(self.file_path, "a") as f:
                f.write(f"Gender: {self.gender}\n")
                f.write(f"Salary per month: {self.month_salary():.2f}\n")
                f.write(f"Age: {self.age}\n")
                f.write(f"Years working: {self.seniority_time()}\n")
                f.write(f"Pension deduction per month: {pension_cost:.2f}\n")
                f.write(f"Health deduction per month: {health_cost:.2f}\n")
                f.write(f"Yearly pension contribution: {yearly_pension:.2f}\n")
                f.write(f"Years left for retirement: {years_left}\n")
                f.write("=" * 40 + "\n")
        except Exception as e:
            print(f"Error writing to file: {e}")
        
def main():
    employee = Employee()
    employee.insert_data()
    employee.insert_data_to_file()
    
if __name__ == "__main__":
    main()
