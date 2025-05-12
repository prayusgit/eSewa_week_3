
# Memento
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


# Originator
class Editor:
    def __init__(self):
        self._text = "."

    def write(self, text):
        self._text += text

    def save(self):
        return Memento(self._text)

    def restore(self, memento: Memento):
        self._text = memento.get_state()

    def show(self):
        print(self._text)


# Caretaker
class History:
    def __init__(self, editor: Editor):
        self._mementos = []
        self._editor = editor

    def backup(self):
        self._mementos.append(self._editor.save())

    def undo(self):
        if self._mementos:
            self._editor.restore(self._mementos.pop())

    def show_history(self):
        for m in self._mementos:
            print(m.get_state())

# Usage
editor = Editor()
history = History(editor)

history.backup()

editor.write("Hello")
history.backup()  # backup after first write

editor.write(", world!")
history.backup()  # backup after second write

editor.show()     # Hello, world!

history.undo()
editor.show()     # Hello

history.undo()
editor.show()

history.undo()
editor.show()