# Diseñar una clase para crear un objeto empleado con al menos 5
# atributos y los siguientes métodos:
# a. Calcular lo que se gana al mes teniendo en cuenta el
# número de horas que trabaja, el valor de cada hora.
# b. Calcular el tiempo de antigüedad y cuanto le falta para
# pensionarse teniendo en cuenta que las mujeres se
# pensionan antes que los hombres.
# c. Calcular cuánto paga por salud y pensión al mes el
# empleado teniendo en cuenta que es 4% de salud y 4% de
# pensión y al año cuanto abona en pensión.
# d. Se deben guardar todos los datos de los empleados en un
# archivo.

import datetime

class employer:
    
    def __init__(self):
        self.salary_per_hour = 0
        self.working_time = 0
        self.years_working = 0
        self.gender = ""
        self.age = ""
        
    def insert_data(self):
        self.salary_per_hour = int(input("Enter your salary per mounth: "))
        self.working_time = int(input("Enter your time at work, in hours: "))
        self.years_working = int(input("Enter yours years in your work: "))
        self.gender = input("Enter your gender male or female: ")
        self.age = int(input("Enter your age: "))
    
    def mounth_salary(self):
        mounth_salary = self.salary_per_hour * self.working_time
        return mounth_salary
    
    def seniority_time(self):
        actual_year = datetime.datetime.now().year
        seniority_time = actual_year - self.years_working
        return seniority_time
    
    def time_to_retire(self):
        if self.gender.lower() == "female":
            pension_age = 57
            time_to_retire = pension_age - self.age
            if time_to_retire < 0:
                print("You have complete the time to retire, begin to enjoy the rest of your live!!")
            else:
                print(f"You need complete {time_to_retire} years to retire")
        elif self.gender.lower() == "male":
            pension_age = 62
            time_to_retire = pension_age - self.age
            if time_to_retire < 0:
                print("You have complete the time to retire, begin to enjoy the rest of your live!!")
            else:
                print(f"You need complete {time_to_retire} years to retire")
                
    def pension_health_cost(self):
        mounth_salary = self.salary_per_hour * self.working_time
        pension_cost = mounth_salary * 0.04
        health_cost = mounth_salary * 0.04
        print(f"The value of the pension per mounth is: {pension_cost}, and health: {health_cost}")
        
def main():
    sample_employer = employer()
    sample_employer.insert_data()
    sample_employer.time_to_retire()
    
if __name__ == "__main__":
    main()
    
        
                
    
    