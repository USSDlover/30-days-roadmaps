from Bird import Bird
from Animal import AnimalCantSpeakError


dog = Bird('Chessin')

try:
    print(dog.name)
    print(dog.speak())
except AnimalCantSpeakError as error:
    print(error)
