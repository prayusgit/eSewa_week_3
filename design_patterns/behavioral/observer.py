from abc import ABC, abstractmethod


# Observer or Subscriber interface
class Observer(ABC):
    @abstractmethod
    def update(self, temp):
        pass


# Subject or Publisher interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


# Concrete Subject
class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = 0

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temp):
        self._temperature = temp
        self.notify()


# Concrete Observer
class PhoneDisplay(Observer):
    def update(self, temp):
        print(f"Phone Display: Temperature updated to {temp}")


class LEDDisplay(Observer):
    def update(self, temp):
        print(f'LED Display: Temperature updated to {temp}')


led = LEDDisplay()
phone = PhoneDisplay()

weather_station = WeatherStation()

weather_station.attach(led)
weather_station.attach(phone)

weather_station.set_temperature(20)
weather_station.set_temperature(15)

weather_station.detach(led)

weather_station.set_temperature(10)
