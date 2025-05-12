# Base Component
class Coffee:
    def cost(self):
        return 5

# Base decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()


# Concrete Decorator
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.5


coffee = Coffee()

coffee_with_milk = MilkDecorator(coffee)
coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)

print(coffee_with_milk_and_sugar.cost())


def decorator_func(func):
    def wrapper_func(*args, **kwargs):
        print("Nice ")
        func(*args, **kwargs)
    return wrapper_func

@decorator_func
def print_hello(name):
    print("Hello "+name)

print_hello('hari')