class Unit:
    #configurable - length of one 'unit' in seconds
    Length: int = 1

class Character:

    Units = []

    def __init__(self, cnt):
        self.units = [Unit()]
        for _ in range(1, cnt):
            self.units.append(Unit())

class Pause:

    Units = []

    def __init__(self, cnt):
        self.units = [Unit()]
        for _ in range(1, cnt):
            self.units.append(Unit())

# Intl. Morse Code:
    # A dot is one unit
    # A dash is three units
    # Space between dots/dashes within a letter is one unit
    # Space between letters is three units
    # Space between words is one unit
Dot = Character(1)
Dash = Character(3)
CharacterSpace = Pause(1)
LetterSpace = Pause(3)
WordSpace = Pause(7)