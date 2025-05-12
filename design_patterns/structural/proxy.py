# Virtual proxy
# Real class
class RealImage:
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print("Loading the image..")

    def diplay(self):
        print(f"Displaying: {self.filename}")


# Proxy class
class ProxyImage:
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None

    def display(self):
        if self._real_image is None:
            self._real_image = RealImage(self.filename)
        self._real_image.diplay()


image1 = ProxyImage('cat.img')
image1.display()
image1.display()

