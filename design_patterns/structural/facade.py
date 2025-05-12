# Subsystem classes
class Engine:
    def ignite(self):
        print("Fuel burning..")


class Wheel:
    def rotate(self):
        print("Wheel rotating..")


class Accelerator:
    def press(self):
        print('Accelerator pressed..')


# Facade
class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheel = Wheel()
        self.accelerator = Accelerator()

    def start(self):
        self.engine.ignite()
        self.accelerator.press()
        self.wheel.rotate()


# Client code
car = Car()
car.start()
