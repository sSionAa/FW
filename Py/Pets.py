
from Animal import Animal
from abc import ABC

class Pets(Animal, ABC):
    pass

class Cats(Pets):
    pass


class Dogs(Pets):
    pass
    

class Hamsters(Pets):
    pass