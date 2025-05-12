
# Abstract product 1
class Button:
    def render(self):
        pass

# Abstract product 2
class CheckBox:
    def render(self):
        pass

# Concrete Product 1
class LightButton(Button):
    def render(self):
        print("Rendering light button")

# Concrete Product 2
class DarkButton(Button):
    def render(self):
        print("Rendering dark button")

# Concrete Product 3
class LightCheckBox(CheckBox):
    def render(self):
        print('Rendering light checkbox')

# Concrete Product 4
class DarkCheckBox(CheckBox):
    def render(self):
        print("Rendering dark checkbox")


# Abstract Factory
class UIFactory:
    def create_button(self) -> Button:
        pass

    def create_checkbox(self) -> CheckBox:
        pass

# Concrete Factory 1
class DarkUIFactory(UIFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> CheckBox:
        return DarkCheckBox()

# Concrete Factory 2
class LightUIFactory(UIFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> CheckBox:
        return LightCheckBox()

def process(factory: UIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.render()
    checkbox.render()


process(LightUIFactory())
process(DarkUIFactory())

