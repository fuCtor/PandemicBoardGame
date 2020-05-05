import abc

from .game_script import GameScript

class GameLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load(self, location) -> GameScript:
        pass