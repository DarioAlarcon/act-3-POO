import re
from car import CompactCar, SUV

def validate_plate(plate):
    return re.match(r"^[A-Za-z]{3}\d{3}$", plate)

def validate_text(text):
    return re.match(r"^[A-Za-z\s]+$", text)

def validate_model(model):
    return re.match(r"^[A-Za-z0-9]+$", model)

def add_car_menu(parking):
    plate = input("Enter plate: ")
    if not validate_plate(plate):
        print("Invalid plate format.")
        return
    
    brand = input("Enter brand: ")
    if not validate_text(brand):
        print("Invalid brand format.")
        return
    
    model = input("Enter model: ")
    if not validate_model(model):
        print("Invalid model format.")
        return
    
    owner = input("Enter owner: ")
    if not validate_text(owner):
        print("Invalid owner format.")
        return
    
    hourly_rate = float(input("Enter hourly rate: "))
    car_type = input("Enter car type (compact or suv): ").lower()
    
    if car_type == "compact":
        car = CompactCar(plate, brand, model, owner, hourly_rate)
    elif car_type == "suv":
        car = SUV(plate, brand, model, owner, hourly_rate)
    else:
        print("Invalid car type.")
        return
    
    parking.add_car(car)
    print("Car added successfully.")
