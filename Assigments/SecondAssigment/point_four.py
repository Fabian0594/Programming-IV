class Book:
    def __init__(self, title, author, genre, pages, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.year = year

    def get_summary(self):
        return f"{self.title} by {self.author}, {self.pages} pages, {self.genre} genre."

    def is_classic(self):
        return self.year < 1970


class House:
    def __init__(self, address, size, floors, rooms, price):
        self.address = address
        self.size = size
        self.floors = floors
        self.rooms = rooms
        self.price = price

    def get_info(self):
        return f"House at {self.address}, {self.size} sq ft, {self.floors} floors, {self.rooms} rooms."

    def is_expensive(self, threshold):
        return self.price > threshold


class Movie:
    def __init__(self, title, director, duration, genre, rating):
        self.title = title
        self.director = director
        self.duration = duration
        self.genre = genre
        self.rating = rating

    def get_details(self):
        return f"{self.title} directed by {self.director}, {self.duration} minutes, {self.genre} genre."

    def is_high_rated(self):
        return self.rating >= 8.0


class Warehouse:
    def __init__(self, location, capacity, manager, temperature_control, security_level):
        self.location = location
        self.capacity = capacity
        self.manager = manager
        self.temperature_control = temperature_control
        self.security_level = security_level

    def get_status(self):
        return f"Warehouse at {self.location} with {self.capacity} capacity, managed by {self.manager}."

    def is_secure(self):
        return self.security_level >= 7


class Lamp:
    def __init__(self, brand, type, color, brightness, power):
        self.brand = brand
        self.type = type
        self.color = color
        self.brightness = brightness
        self.power = power

    def turn_on(self):
        return "The lamp is now ON."

    def turn_off(self):
        return "The lamp is now OFF."


class Modem:
    def __init__(self, brand, model, speed, connection_type, ports):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.connection_type = connection_type
        self.ports = ports

    def connect(self):
        return "Modem is connecting to the internet..."

    def reset(self):
        return "Modem is resetting..."


class Router:
    def __init__(self, brand, model, speed, range, bands):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.range = range
        self.bands = bands

    def enable_wifi(self):
        return "WiFi is now enabled."

    def disable_wifi(self):
        return "WiFi is now disabled."


class Briefcase:
    def __init__(self, material, color, brand, lock_type, compartments):
        self.material = material
        self.color = color
        self.brand = brand
        self.lock_type = lock_type
        self.compartments = compartments

    def open(self):
        return "Briefcase is now open."

    def close(self):
        return "Briefcase is now closed."


class OncologyPatient:
    def __init__(self, name, age, diagnosis, stage, treatment):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.stage = stage
        self.treatment = treatment

    def get_info(self):
        return f"Patient {self.name}, {self.age} years old, diagnosed with {self.diagnosis} (Stage {self.stage})."

    def is_critical(self):
        return self.stage >= 3


class Cat:
    def __init__(self, name, breed, age, color, weight):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.weight = weight

    def meow(self):
        return "Meow!"

    def sleep(self):
        return "The cat is sleeping..."
