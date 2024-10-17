
from Animal import Animal
from abc import ABC

class PackPets(Animal, ABC):
    pass

class Horses(PackPets):
    pass

class Donkeys(PackPets):
    pass

class Camels(PackPets):
    pass


