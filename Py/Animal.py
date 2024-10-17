
from abc import ABC
from datetime import datetime, timedelta
from typing import List, Optional, Union

class Animal(ABC):
    
    def __init__(self, name: str, type_animal: str, birth_date: datetime, commands: Optional[List[str]] = None):
        self._name = name
        self._type = type_animal
        self._birth_date = birth_date
        self._commands = commands if commands else []

    def __str__(self) -> str:
        age = self.calculate_age()
        return (f"Тип: {type(self).mro()[1].__name__}; "
                f"Подтип: {self._type}; "
                f"Кличка: {self._name}; "
                f"Возраст: {age}; "
                f"Знает команды: {', '.join(self._commands)}")

    def calculate_age(self) -> str:
        """Calculate the age of the animal in years and days."""
        today = datetime.now()
        age_days = (today - self._birth_date).days
        years = age_days // 365
        days = age_days % 365
        return f"{years} лет(года), {days} дней" if years else f"{days} дней"

    def get_name(self) -> str:
        return self._name

    def get_type(self) -> str:
        return self._type

    def get_commands(self) -> List[str]:
        return self._commands

    def add_command(self, command: str) -> None:
        """Add a command to the animal's command list."""
        if command not in self._commands:
            self._commands.append(command)

    def set_commands(self,value):
        if value not in self._commands:
            self._commands.append(value)

    def get_animal_list(self) -> List[Union[str, datetime, List[str]]]:
        return [type(self).mro()[1].__name__, self._type, self._name, self._birth_date, self._commands]