from abc import ABC, abstractmethod

# State Interface
class State(ABC):
    @abstractmethod
    def play(self, player):
        pass

    @abstractmethod
    def pause(self, player):
        pass

    @abstractmethod
    def stop(self, player):
        pass


# Concrete State
class PlayingState(State):
    def play(self, player):
        print("Already playing.")

    def pause(self, player):
        print("Pausing playback.")
        player.set_state(PausedState())

    def stop(self, player):
        player.set_state(StoppedState())


class StoppedState(State):
    def play(self, player):
        print("Starting playback.")
        player.set_state(PlayingState())

    def pause(self, player):
        print("Nothing is playing to stop..")

    def stop(self, player):
        print("Already stopped.")


class PausedState(State):
    def play(self, player):
        print("Resuming playback.")
        player.set_state(PlayingState())

    def pause(self, player):
        print("Already paused.")

    def stop(self, player):
        print("Stopping the playback.")
        player.set_state(StoppedState())

# Context
class MusicPlayer:
    def __init__(self):
        self._state = StoppedState()

    def set_state(self, state: State):
        self._state = state

    def play(self):
        self._state.play(self)

    def pause(self):
        self._state.pause(self)

    def stop(self):
        self._state.stop(self)


# Usage
player = MusicPlayer()

player.stop()
player.play()

player.play()
player.pause()
player.stop()
player.pause()
player.play();