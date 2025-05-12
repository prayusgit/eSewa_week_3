# Implementation
class Color:
    def display(self):
        pass

# Refined Implementor
class RedColor(Color):
    def display(self):
        print('Red Color')

class BlueColor(Color):
    def display(self):
        print("Blue color")


# Abstraction
class Shape:
    def __init__(self, color: Color):
        self.color = color

    def draw(self):
        pass


# Refined Abstractor
class CircleShape(Shape):
    def draw(self):
        self.color.display()
        print("Circle")

class SquareShape(Shape):
    def draw(self):
        self.color.display()
        print("Square")


shape = SquareShape(BlueColor())
shape.draw()