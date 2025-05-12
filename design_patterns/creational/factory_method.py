# Prodcut Interface
class Vehicle:
    def display(self):
        pass


# Concrete Product 1
class Car(Vehicle):
    def display(self):
        print("Four wheel.")


# Concrete Product 2
class Bike(Vehicle):
    def display(self):
        print("Two wheel.")


# Creator
class VehicleFactory:
    def create_vehicle(self) -> Vehicle:
        pass


# Concrete Creator 1
class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()


# Concrete Creator 2
class BikeFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Bike()


def process(factory: VehicleFactory):
    vehicle = factory.create_vehicle()
    vehicle.display()


process(CarFactory())
process(BikeFactory())


def test():
    yield 1
    yield 2

t = (x for x in range(1,3))
print(next(t))
print(next(t))
