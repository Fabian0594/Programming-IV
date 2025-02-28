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
    
    def __init__(self, name, ):
    


        
        
        
        
        
        
        
        
        
        