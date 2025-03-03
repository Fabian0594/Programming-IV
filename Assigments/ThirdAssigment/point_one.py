import datetime

class plane:
    
    def __init__(self, capacity, speed, model, distance_travel):
        self.capacity = capacity
        self.speed = speed
        self.model = model
        self.distance_travel = distance_travel
    
    def travel_hours(self):
        travel_time = self.distance_travel / self.speed
        print(f"The travel hours are: {travel_time}")
        
    def get_cost(self):
        
        #Total Fuel Cost
        distance = self.distance_travel
        fuel_per_km = 3
        fuel_comsuption = fuel_per_km * distance
        fuel_cost = distance * fuel_comsuption
        
        #Mantein Cost
        passenger_mantein_cost = 10
        mantein_cost = passenger_mantein_cost * self.capacity
        
        #Ambiguity Cost
        actual_year = datetime.datetime.now().year
        efficiency_factor = 50
        ambiguity_cost = (actual_year - self.model) * efficiency_factor
        
        #Total Cost
        total_cost = fuel_cost + mantein_cost + ambiguity_cost
        
        print(f"The cost of your travel is: {total_cost}\n")
        
class smartphone:
    
    def __init__(self, capacity, ram, brand, year):
        self.capacity = capacity
        self.ram = ram
        self.brand = brand 
        self.year = year
    
    def get_info(self):
        print(f"Your smartphone is a {self.brand} {self.year}, with capacity of {self.capacity} GB and {self.ram} GB of ram\n")
        
    def expiration(self):
        actual_year = datetime.datetime.now().year
        diff_year = actual_year - self.year
        
        if diff_year > 5:
            print(f"Your smartphone is a little old, you must change it soon.\n")
        elif self.ram < 1 and self.capacity < 8:
            print(f"WTF, how do you use it? change that potato please.\n")
            
class subject:
    
    def __init__(self, name, code, credits, professor):
        self.name = name
        self.code = code
        self.credits = credits
        self.professor = professor
    
    def get_details(self):
        return f"Subject: {self.name}, Code: {self.code}, Credits: {self.credits}, Professor: {self.professor}"
    
    def is_passed(self, note):
        return note >= 60
    
        
class Army:
    
    def __init__(self, name, country, soldiers, budget):
        self.name = name
        self.country = country
        self.soldiers = soldiers
        self.budget = budget
    
    def get_info(self):
        return f"Army: {self.name}, Country: {self.country}, Soldiers: {self.soldiers}, Budget: {self.budget}"
    
    def is_large(self):
        return self.soldiers > 100000 

class Chair:
    
    def __init__(self, material, color, height, price):
        self.material = material
        self.color = color
        self.height = height
        self.price = price
    
    def get_info(self):
        return f"Chair: Material: {self.material}, Color: {self.color}, Height: {self.height} cm, Price: ${self.price}"
    
    def is_expensive(self):
        return self.price > 100

class Headphones:
    
    def __init__(self, brand, model, wireless, price):
        self.brand = brand
        self.model = model
        self.wireless = wireless
        self.price = price
    
    def get_info(self):
        return f"Headphones: Brand: {self.brand}, Model: {self.model}, Wireless: {self.wireless}, Price: ${self.price}"
    
    def is_wireless(self):
        return self.wireless

        
        
        
        
        
        