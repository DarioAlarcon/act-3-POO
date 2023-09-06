import re
from car import Taxi, Car

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
    car_type = input("Is it a taxi? (yes/no): ").lower()
    
    if car_type == "yes":
        code = input("Enter a 5-digit code: ")
        if not re.match(r"^\d{5}$", code):
            print("Invalid code format. Please enter 5 digits.")
            return
        car = Taxi(plate, brand, model, owner, hourly_rate, code)
    elif car_type == "no":
        car = Car(plate, brand, model, owner, hourly_rate)
    else:
        print("Invalid input for taxi type.")
        return
    
    parking.add_car(car)
    print("Car added successfully.")
