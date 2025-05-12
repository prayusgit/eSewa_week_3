from abc import ABC, abstractmethod

# Product
class Computer:
    def __init__(self):
        self.cpu = None
        self.memory = None
        self.gpu = None

    def display_specs(self):
        print(f"The computer has CPU={self.cpu}, Memory={self.memory}, GPU={self.gpu}")


# Builder interface
class ComputerBuilder(ABC):
    @abstractmethod
    def set_cpu(self):
        pass

    @abstractmethod
    def set_memory(self):
        pass

    @abstractmethod
    def set_gpu(self):
        pass

    @abstractmethod
    def get_result(self):
        pass

# Concrete Builder
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self):
        self.computer.cpu = 'Intel'

    def set_memory(self):
        self.computer.memory = '16GB'

    def set_gpu(self):
        self.computer.gpu = '8GB'

    def get_result(self):
        return self.computer


# Director
class Director:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def initialize_computer(self):
        self.builder.set_cpu()
        self.builder.set_memory()
        self.builder.set_gpu()
        return self.builder.get_result()

builder = GamingComputerBuilder()
director = Director(builder)

computer = director.initialize_computer()
computer.display_specs()

