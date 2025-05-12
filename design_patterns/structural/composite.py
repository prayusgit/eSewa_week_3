from abc import ABC, abstractmethod

# Component
class Employee(ABC):
    @abstractmethod
    def show_details(self):
        pass

# Leaf
class Developer(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def show_details(self):
        print(f"{self.name} works as {self.position}")


# Composite
class Manager(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.subordinates = []

    def add(self, employee: Employee):
        self.subordinates.append(employee)

    def show_details(self):
        print(f"{self.name} works as {self.position}")
        for emp in self.subordinates:
            emp.show_details()

dev1 = Developer('Ram', 'Frontend')
dev2 = Developer('Hari', 'Backend')

mid_manager = Manager('Raju', 'IT Manager')
mid_manager.add(dev1)
mid_manager.add(dev2)

high_manager = Manager('Babu', 'Branch Manager')
high_manager.add(mid_manager)

mid_manager.show_details()