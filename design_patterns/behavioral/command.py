from abc import ABC, abstractmethod


# Abstract Receiver
class Receiver(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Concrete Receiver
class Light(Receiver):
    def turn_on(self):
        print("Light on..")

    def turn_off(self):
        print("Light off..")

class Fan(Receiver):
    def turn_on(self):
        print("Fan on..")

    def turn_off(self):
        print("Turn off..")

# Abstract Command
class Command(ABC):
    def __init__(self, receiver: Receiver):
        self._receiver = receiver

    @abstractmethod
    def execute(self):
        pass


# Concrete command
class LightOnCommand(Command):
    def execute(self):
        self._receiver.turn_on()

class LightOffCommand(Command):
    def execute(self):
        self._receiver.turn_off()

class FanOnCommand(Command):
    def execute(self):
        self._receiver.turn_on()

class FanOffCommand(Command):
    def execute(self):
        self._receiver.turn_off()


# Invoker
class RemoteControl:
    def __init__(self):
        self._command = None

    def set_command(self, command: Command):
        self._command = command

    def press_button(self):
        if self._command:
            self._command.execute()
        else:
            print("No command set.")


# Client code
light = Light()
fan = Fan()

light_on = LightOnCommand(light)
light_off = LightOffCommand(light)
fan_on = FanOnCommand(fan)
fan_off = FanOffCommand(fan)

remote = RemoteControl()

remote.set_command(light_on)
remote.press_button()

remote.set_command(light_off)
remote.press_button()

remote.set_command(fan_on)
remote.press_button()

remote.set_command(fan_off)
remote.press_button()
