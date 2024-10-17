from datetime import datetime
import csv

class Menu:
    ANIMAL_CLASS_TYPES = {
        'лошадь': 'Horses',
        'осел': 'Donkeys',
        'верблюд': 'Camels',
        'кот': 'Cats',
        'собака': 'Dogs',
        'хомяк': 'Hamsters'
    }

    ANIMAL_CLASS_TYPES_DECLENSION = {
        'лошадь': 'лошади',
        'осел': 'осла',
        'верблюд': 'верблюда',
        'кот': 'кота',
        'собака': 'собаки',
        'хомяк': 'хомяка'
    }

    @staticmethod
    def for_one_menu():
        """Collect data for a new animal."""
        while True:
            name = input("Введите имя животного => ").strip()
            if name.isalpha():
                break
            print("Неверный формат имени")

        animal_type = Menu.choose_animal_type()

        while True:
            try:
                data = input('Введите дату рождения в формате ДД.ММ.ГГГГ => ')
                birth_date = datetime.strptime(data, '%d.%m.%Y')
                break
            except ValueError:
                print('Введенная дата не является корректной, попробуйте еще раз')

        input_command = input("Перечислите команды, которые животное может выполнять (через запятую),\nили пропустите ввод, чтобы оставить поле пустым => ")
        commands = [cmd.strip() for cmd in input_command.split(',')] if input_command.strip() else []

        return name, animal_type, birth_date, commands

    @staticmethod
    def choose_animal_type():
        """Prompt user to select an animal type."""
        while True:
            try:
                choice = int(input(f"""
Выберите тип животного:
1. Лошадь
2. Осел
3. Верблюд
4. Кот
5. Собака
6. Хомяк
{'*' * 40}
Введите номер => """))
                if 1 <= choice <= 6:
                    return list(Menu.ANIMAL_CLASS_TYPES.keys())[choice - 1]
                else:
                    print("Выберите из предложенных вариантов")
            except ValueError:
                print("Введите корректный номер")

    @staticmethod
    def menu():
        """Display the main menu and get user choice."""
        print(f"\nВы работаете с реестром домашних животных.\nВыберите пункт меню:\n{'*' * 40}")
        print('''1. Добавить в реестр новое животное
2. Показать реестр
3. Обучить животное новой команде
4. Удалить животное из реестра
5. Сохранить реестр в файл
6. Выйти из реестра
''' + '*' * 40)

        while True:
            input_command = input("Пункт меню => ")
            if input_command.strip().isdigit() and 1 <= int(input_command) <= 6:
                return int(input_command)
            else:
                print("Неверный номер пункта меню. Пожалуйста, введите номер от 1 до 6.")

    @staticmethod
    def to_teach_animal_to_commands(register):
        """Teach an animal new commands."""
        name = input("Введите имя животного => ")
        animal_type = Menu.choose_animal_type()
        commands = [cmd.strip() for cmd in input("Введите команду или список команд через запятую => ").strip().split(',')]
        
        if not commands:
            print('Поле с командами не может быть пустым')
            return

        for animal in register.get_reestr_list():
            if animal.__class__.__name__ == Menu.ANIMAL_CLASS_TYPES[animal_type] and animal.get_name().lower() == name.strip().lower():
                for command in commands:
                    animal.set_commands(command)
                print("\nКоманды добавлены\n")
                return

        print(f'\n{Menu.ANIMAL_CLASS_TYPES_DECLENSION[animal_type].capitalize()} с таким именем не найдено. Проверьте имя или добавьте животное.')

    @staticmethod
    def del_animal_from_register():
        """Get the name and type of the animal to delete."""
        name = input("Введите имя животного => ")
        animal_type = Menu.choose_animal_type()
        return name, animal_type

    @staticmethod
    def print_register_to_file(animal_register):
        """Save the animal register to a CSV file."""
        try:
            with open("My_animal_register.csv", 'w', encoding='utf-8') as file:
                columns = ['Тип', 'Подтип', 'Имя животного', 'Дата рождения', 'Команды, которые умеет выполнять животное']
                writer = csv.writer(file)
                writer.writerow(columns)  # запись заголовков
                for animal in animal_register:  # запись строк
                    writer.writerow(animal.get_animal_list())
            print("Данные записаны в файл My_animal_register.csv")
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")
