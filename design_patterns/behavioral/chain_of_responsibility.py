from abc import ABC, abstractmethod

# Abstract Handler
class SupportHandler(ABC):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        pass


# Concrete Handler
class PasswordHandler(SupportHandler):
    def handle(self, request):
        if 'password' in request:
            print("Level 1: Resetting your password..")
        elif self._next_handler:
            self._next_handler.handle(request)
        else:
            print("Level 1: No handler found for your issue.")


class NetworkHandler(SupportHandler):
    def handle(self, request):
        if 'network' in request:
            print("Level 2: Troubleshooting your network.")
        elif self._next_handler:
            self._next_handler.handle(request)
        else:
            print("Level 2: No handler found for your issue.")

class SoftwareHandler(SupportHandler):
    def handle(self, request):
        if 'software' in request:
            print("Level 3: Upgrading your software...")
        elif self._next_handler:
            self._next_handler.handle(request)
        else:
            print("Level 3: No handler found for your issue.")


# Client code
level_1 = SoftwareHandler()
level_2 = PasswordHandler()
level_3 = NetworkHandler()

level_1.set_next(level_2).set_next(level_3)

level_1.handle('network in not connecting')

