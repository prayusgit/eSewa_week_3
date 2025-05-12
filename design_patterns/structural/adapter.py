class CelciusThermometer:
    def get_temperature(self):
        return 25


class FahrenheitThermometer:
    def get_temperature(self):
        pass


class Adapter(FahrenheitThermometer):
    def __init__(self, celcius_thermometer: CelciusThermometer):
        self.celcius_thermometer = celcius_thermometer

    def get_temperature(self):
        c = self.celcius_thermometer.get_temperature()
        return (c * 9/5) + 32

celcius_thermo = CelciusThermometer()
adapter = Adapter(celcius_thermo)

print(adapter.get_temperature())
