from abc import ABC, abstractmethod


# Mediator Interface
class ChatRoomMediator(ABC):
    @abstractmethod
    def show_messege(self, user, messege):
        pass


# Concrete Mediator
class ChatRoom(ChatRoomMediator):
    # Can contain fields that references all the components(colleague)
    def show_messege(self, user, messege): # Notification method
        print(f"{user.name} says: {messege}")


# Colleague
class User:
    def __init__(self, name, chatroom: ChatRoomMediator):
        self.name = name
        self.chatroom = chatroom

    def send(self, messege):
        self.chatroom.show_messege(self, messege)


# Usage
chatroom = ChatRoom()

bob = User('bob', chatroom)
hattori = User('hattori', chatroom)

bob.send('Hi hattori')
hattori.send('Hi bob')
