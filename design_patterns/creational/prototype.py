import copy


# Prototype
class Prototype:
    def clone(self):
        return copy.deepcopy(self)

# Concrete Prototype
class Car(Prototype):
    def __init__(self, name, features):
        self.name = name
        self.features = features

# Client
car = Car('Audi', ['AC', 'Music'])

cloned_car = car.clone()
cloned_car.features.append('Automatic')

print(cloned_car.name)