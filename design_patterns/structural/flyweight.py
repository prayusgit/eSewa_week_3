# Flyweight
class Character:
    def __init__(self, char, font):
        self.char = char
        self.font = font

    def display_character(self, context):
        print(f"Displaying {self.char} at position {context.position} with {context.color}")


# Flyweight factory
class CharacterFactory:
    def __init__(self):
        self._characters = {}

    def get_character(self, char, font):
        key = (char, font)
        if key not in self._characters:
            self._characters[key] = Character(char, font)
        return self._characters[key]


# Context class
class CharacterContext:
    def __init__(self, position, color):
        self.position = position
        self.color = color


text = 'HELLO'
positions = [(1,0), (2,0), (3,0), (4,0), (5, 0)]
colors = ['Red', 'Blue', 'Green', 'Black', 'Grey']

factory = CharacterFactory()

for i, ch in enumerate(text):
    char = factory.get_character(ch, 'Arial')
    context = CharacterContext(positions[i], colors[i])
    char.display_character(context)
