class ParkingLot:
    def __init__(self):
        self.cars = []
    
    def calculate_and_display_fees(self):
        if not self.cars:
            print("No cars in the parking lot.")
        else:
            for car in self.cars:
                hours = float(input(f"Enter hours parked for {car.display()}: "))
                parking_fee = car.calculate_parking_fee(hours)
                print(f"Parking fee for {car.display()}: ${parking_fee:.2f}")

    def add_car(self, car):
        self.cars.append(car)
        print(f"Car with plate {car.plate} has entered the parking lot.")
    
    def remove_car(self, plate):
        for car in self.cars:
            if car.plate == plate:
                self.cars.remove(car)
                print(f"Car with plate {car.plate} has left the parking lot.")
                break
        else:
            print(f"Car with plate {plate} was not found in the parking lot.")
    
    def display_cars(self):
        if not self.cars:
            print("No cars in the parking lot.")
        else:
            print("Cars in the parking lot:")
            for car in self.cars:
                print(car.display())
