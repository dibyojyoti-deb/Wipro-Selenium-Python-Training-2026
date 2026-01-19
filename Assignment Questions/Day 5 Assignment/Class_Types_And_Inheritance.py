class Vehicle:
    vehicle_count = 0   # class variable

    def __init__(self, name):
        self.name = name
        Vehicle.vehicle_count += 1

    def start(self):
        print(f"{self.name} is starting.")


# Single Inheritance
class Car(Vehicle):
    def drive(self):
        print(f"{self.name} is being driven.")


# Multilevel Inheritance
class ElectricCar(Car):
    def charge(self):
        print(f"{self.name} is charging.")


def main():
    print("=== Vehicle Inheritance Demo ===")

    v_name = input("Enter Vehicle name: ")
    vehicle = Vehicle(v_name)
    vehicle.start()

    print("\n--- Single Inheritance (Car) ---")
    c_name = input("Enter Car name: ")
    car = Car(c_name)
    car.start()
    car.drive()

    print("\n--- Multilevel Inheritance (ElectricCar) ---")
    e_name = input("Enter Electric Car name: ")
    ecar = ElectricCar(e_name)
    ecar.start()
    ecar.drive()
    ecar.charge()

    print(f"\nTotal Vehicles Created: {Vehicle.vehicle_count}")


if __name__ == "__main__":
    main()
