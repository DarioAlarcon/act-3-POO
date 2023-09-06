class Car:
    def __init__(self, plate, brand, model, owner, hourly_rate):
        self.plate = plate
        self.brand = brand
        self.model = model
        self.owner = owner
        self.hourly_rate = hourly_rate
    
    def calculate_parking_fee(self, hours):
        return self.hourly_rate * hours

    def display(self):
        return f"Plate: {self.plate} | Brand: {self.brand} | Model: {self.model} | Owner: {self.owner}"
    
class Taxi(Car):
    def __init__(self, plate, brand, model, owner, hourly_rate, codigo):
        super().__init__(plate, brand, model, owner, hourly_rate)
        self.codigo = codigo
    
    def calculate_parking_fee(self, hours):
        return self.hourly_rate * hours * 0.5

    def display(self):
        return f"Plate: {self.plate} | Brand: {self.brand} | Model: {self.model} | Owner: {self.owner} | Codigo: {self.codigo}"