from Pets import *
from PackPets import *
from Menu import *
from datetime import datetime
from AnimalRegister import *

animals_registry = AnimalRegister()

# Предзаполнение животными
animal_data = [
    ('Дэни', 'собака', datetime(2019, 3, 11), ['Лежать', 'Сидеть']),
    ('Черныш', 'собака', datetime(2020, 1, 22), ['Лежать', 'Сидеть']),
    ('Бегемот', 'кошка', datetime(2021, 1, 13), ['Кушать', 'Ко мне']),
    ('Марс', 'кошка', datetime(2022, 7, 15), ['Гулять', 'Брысь']),
    ('Пухляш', 'хомяк', datetime(2021, 1, 21), ['Еда', 'Бу']),
    ('Стройняш', 'хомяк', datetime(2023, 1, 18), ['Бегать', 'Стоять']),
    ('Бэт', 'лошадь', datetime(2019, 1, 19), ['Но Но Но', 'Стой']),
    ('Сэм', 'лошадь', datetime(2022, 4, 28), ['Тпру', 'Можно']),
    ('Кафир', 'верблюд', datetime(2019, 3, 1), ['Лежать', 'Пошел']),
    ('Ра', 'верблюд', datetime(2021, 10, 14), ['Стой', 'Хоп']),
    ('Сфинкс', 'верблюд', datetime(2022, 9, 15), ['Тпру', 'Вниз']),
    ('Коля', 'осел', datetime(2023, 5, 24), ['Вперед', 'Стоять']),
]

for animal in animal_data:
    animals_registry.add(animal)

while True:
    try:
        choice = Menu.menu()
        if not isinstance(choice, int) or choice not in range(1, 7):
            raise ValueError("Неверный номер пункта меню. Пожалуйста, введите номер от 1 до 6.")
        match Menu.menu():
            case 1:
                animals_registry.add(Menu.for_one_menu())
                print("\nЖивотное добавлено в реестр\n")
            case 2:  # Показать реестр
                print(f"В регистре находятся:\n{'*' * 40}")
                if len(animals_registry) == 0:
                    print("В реестре еще нет животных. Добавьте животных в реестр.")
                else:
                    print(*animals_registry, sep='\n')
                print('*' * 40)
            case 3:  # Обучить животное
                Menu.to_teach_animal_to_commands(animals_registry)
            case 4:  # Удалить животное из регистра
                animal_to_delete = Menu.del_animal_from_register()
                try:
                    del animals_registry[animal_to_delete]
                    print(f"\nЖивотное '{animal_to_delete}' успешно удалено из реестра.\n")
                except KeyError:
                    print(f"\nЖивотное '{animal_to_delete}' не найдено в реестре.\n")
            case 5:  # Сохранить реестр в файл
                Menu.print_register_to_file(animals_registry)
            case 6:  # Выход из программы
                print("До свидания! Хорошего дня!")
                break
            case _:  # В случае ввода неверного значения
                # print("Для продолжения введите пункт меню от 1 до 6.")
                print("Неверный ввод. Пожалуйста, введите номер пункта меню от 1 до 6.")
                print("Вот доступные пункты меню:")
                print('*' * 40)
                Menu.menu()
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Произошла ошибка: {e}. Попробуйте еще раз.")