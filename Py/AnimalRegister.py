
from PackPets import *
from Pets import *
from typing import List, Any, Optional

class AnimalRegister:
    
    def __init__(self):
        self._reestr_list: List[Animal] = []

    def add(self, data: List[Any]) -> None:
        """Add a new animal to the register."""
        for animal in self._reestr_list:
            if animal.get_name() == data[0] and animal.get_type() == data[1]:
                print(f'\n{data[1].capitalize()} с таким именем уже существует\n')
                return
        
        animal_classes = {
            "верблюд": Camels,
            "кот": Cats,
            "лошадь": Horses,
            "хомяк": Hamsters,
            "собака": Dogs,
            "осел": Donkeys
        }
        
        animal_class = animal_classes.get(data[1])
        if animal_class:
            self._reestr_list.append(animal_class(data[0], data[1], data[2], data[3]))
        else:
            print(f'Неизвестный тип животного: {data[1]}')

    def __iter__(self):
        yield from self._reestr_list

    def __len__(self) -> int:
        return len(self._reestr_list)

    def get_reestr_list(self) -> List[Animal]:
        return self._reestr_list

    def __delitem__(self, data: List[str]) -> None:
        """Delete an animal from the register."""
        for i, animal in enumerate(self._reestr_list):
            if animal.get_name().lower() == data[0].lower() and animal.get_type() == data[1]:
                del self._reestr_list[i]
                print('Животное удалено из реестра')
                return
        print('Такого животного нет в реестре')