import random as r

class Die:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        new_valeu: int = r.randint(1, 6)
        self._value = new_valeu
        return new_valeu

