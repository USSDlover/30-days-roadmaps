class AnimalCantSpeakError(Exception):
    pass


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise AnimalCantSpeakError("Error: Should define the animal speak method first")
