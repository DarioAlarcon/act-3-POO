from car_manager import add_car_menu
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
            add_car_menu(parking)
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
