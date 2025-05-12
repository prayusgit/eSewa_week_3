from abc import ABC, abstractmethod

# Visitor interface
class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle: 'Circle'):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle: 'Rectangle'):
        pass


# Element Interface
class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


# Concrete element
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor: Visitor):
        visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def accept(self, visitor: Visitor):
        visitor.visit_rectangle(self)


# Concrete Visitor
class AreaCalculator(Visitor):
    def visit_circle(self, circle: 'Circle'):
        area =  3.141 * circle.radius**2
        print(f"Circle area: {area}")

    def visit_rectangle(self, rectangle: 'Rectangle'):
        area = rectangle.length * rectangle.breadth
        print(f"Rectangle area: {area}")


class PerimeterCalculator(Visitor):
    def visit_circle(self, circle: Circle):
        perimeter = 2 * 3.141 * circle.radius
        print(f"Circle perimeter: {perimeter}")

    def visit_rectangle(self, rectangle: 'Rectangle'):
        perimeter = 2 * (rectangle.length + rectangle.breadth)
        print(f"Rectangle perimeter: {perimeter}")


# Usage
shapes = [
    Circle(5),
    Rectangle(4, 5)
]

area_visitor = AreaCalculator()
perimeter_visitor = PerimeterCalculator()

for shape in shapes:
    shape.accept(area_visitor)

for shape in shapes:
    shape.accept(perimeter_visitor)