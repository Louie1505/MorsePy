from Morse import CharacterSpace, LetterSpace, WordSpace, Dot, Dash

class Parser:

    Alphabet = {
        "A": [Dot, Dash],
        "B": [Dash, Dot, Dot, Dot],
        "C": [Dash, Dot, Dash, Dot],
        "D": [Dash, Dot, Dot],
        "E": [Dot],
        "F": [Dot, Dot, Dash, Dot],
        "G": [Dash, Dash, Dot],
        "H": [Dot, Dot, Dot, Dot],
        "I": [Dot, Dot],
        "J": [Dot, Dash, Dash, Dash],
        "K": [Dash, Dot, Dash],
        "L": [Dot, Dash, Dot, Dot],
        "M": [Dash, Dash],
        "N": [Dash, Dot],
        "O": [Dash, Dash, Dash],
        "P": [Dot, Dash, Dash, Dot],
        "Q": [Dash, Dash, Dot, Dash],
        "R": [Dot, Dash, Dot],
        "S": [Dot, Dot, Dot],
        "T": [Dash],
        "U": [Dot, Dot, Dash],
        "V": [Dot, Dot, Dot, Dash],
        "W": [Dot, Dash, Dash],
        "X": [Dash, Dot, Dot, Dash],
        "Y": [Dash, Dot, Dash, Dash],
        "Z": [Dash, Dash, Dot, Dot],
        "1": [Dot, Dash, Dash, Dash, Dash],
        "2": [Dot, Dot, Dash, Dash, Dash],
        "3": [Dot, Dot, Dot, Dash, Dash],
        "4": [Dot, Dot, Dot, Dot, Dash],
        "5": [Dot, Dot, Dot, Dot, Dot],
        "6": [Dash, Dot, Dot, Dot, Dot],
        "7": [Dash, Dash, Dot, Dot, Dot],
        "8": [Dash, Dash, Dash, Dot, Dot],
        "9": [Dash, Dash, Dash, Dash, Dot],
        "0": [Dash, Dash, Dash, Dash, Dash],
    }

    def Parse(self, message: str):
        ret = []
        words = message.split()
        for word in words:
            for letter in word:
                if letter.upper() in self.Alphabet:
                    for char in self.Alphabet[letter.upper()]:
                        ret.append(char)           
                        ret.append(CharacterSpace)            
                    ret.append(LetterSpace)            
            ret.append(WordSpace)
        return ret[:-1]

