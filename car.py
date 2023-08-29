class Car:
    def __init__(self, plate, brand, model, owner, hourly_rate):
        self.plate = plate
        self.brand = brand
        self.model = model
        self.owner = owner
        self.hourly_rate = hourly_rate
    
    def display(self):
        return f"Plate: {self.plate} | Brand: {self.brand} | Model: {self.model} | Owner: {self.owner}"

class CompactCar(Car):
    def calculate_parking_fee(self, hours):
        return self.hourly_rate * hours

class SUV(Car):
    def calculate_parking_fee(self, hours):
        return self.hourly_rate * hours * 1.2