from car import CompactCar, SUV
from parking_lot import ParkingLot

def main():
    parking = ParkingLot()

    while True:
        print("\nMenu:")
        print("1. Add Car")
        print("2. Remove Car")
        print("3. Display Cars")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            plate = input("Enter plate: ")
            brand = input("Enter brand: ")
            model = input("Enter model: ")
            owner = input("Enter owner: ")
            hourly_rate = float(input("Enter hourly rate: "))
            car_type = input("Enter car type (compact or suv): ").lower()
            
            if car_type == "compact":
                car = CompactCar(plate, brand, model, owner, hourly_rate)
            elif car_type == "suv":
                car = SUV(plate, brand, model, owner, hourly_rate)
            else:
                print("Invalid car type.")
                continue
            parking.add_car(car)
        elif choice == "2":
            plate = input("Enter plate of the car to remove: ")
            parking.remove_car(plate)
        elif choice == "3":
            parking.display_cars()
            parking.calculate_and_display_fees()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
