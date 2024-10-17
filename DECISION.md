***

# РЕШЕНИЕ

1. Используя команду cat в терминале операционной системы Linux, создать
два файла Домашние животные ( заполнив файл собаками, кошками,
хомяками ) и Вьючные животными заполнив файл ( Лошадьми, верблюдами и
ослы ), а затем объединить их. Просмотреть содержимое созданного файла.
Переименовать файл, дав ему новое имя ( Друзья человека ).

    <details>
        <summary> Команды Bash (развернуть) </summary>

    ```bash
    cat > "Домашние животные"
    Собаки
    Кошки
    Хомяки

    'Ctrl+d'
    ```

    ```bash
    cat > "Вьючные животные"
    Лошади
    Верблюды
    Ослы

    'Ctrl+d'
    ```

    ```bash
    cat "Домашние животные" "Вьючные животные" > Animals
    cat Animals
    mv "Animals" "Друзья человека"
    ```

    </details>

    ![pictures for project](https://github.com/sSionAa/FW/blob/main/Pictures/1.png)

    ***

2. Создать директорию, переместить файл туда.

    <details>
        <summary> Команды Bash (развернуть) </summary>

    ```bash
    mkdir folder_test
    mv 'Друзья человека' folder_test/
    ls
    cd folder_test/
    ls
    ```

    </details>

    ![pictures for project](https://github.com/sSionAa/FW/blob/main/Pictures/2.png)

    ***

3. Подключить дополнительный репозиторий MySQL. Установить любой пакет из этого репозитория.

    <details>
        <summary> Команды Bash (развернуть) </summary>

    ```bash
    sudo apt-get update
    sudo apt update
    sudo apt install mysql-server
    sudo service mysql status
    ```

    </details>

    ![pictures for project](https://github.com/sSionAa/FW/blob/main/Pictures/3.1.png)

    ![pictures for project](https://github.com/sSionAa/FW/blob/main/Pictures/3.2.png)

    ***

4. Установить и удалить deb-пакет с помощью dpkg.
    
    <details>
        <summary> Команды Bash (развернуть) </summary>

    ```bash
    wget http://ftp.us.debian.org/debian/pool/main/s/sl/sl_5.02-1_amd64.deb
    sudo dpkg -i sl_5.02-1_amd64.deb
    sudo dpkg -r sl
    ```

    </details>

    ![pictures for project](https://github.com/sSionAa/FW/blob/main/Pictures/4.png)

    ***


5. Выложить историю команд в терминале ubuntu

    <details>
        <summary> Команды Bash (развернуть)</summary>

    ```bash
    
    1  clear
    2  sudo apt install gcc perl
    3  sudo apt install gcc make perl
    4  sudo apt update
    5  sudo apt upgrade
    6  sudo apt update
    7  sudo apt install mc
    8  mcdir test
    9  mkdir test
   10  cd test/
   11  clear
   12  cat > "Домашние животные"
   13  rm Домашние\ животные 
   14  ls
   15  clear
   16  cat > "Домашние животные"
   17  cat > "Вьючные животные"
   18  cat "Домашние животные" "Вьючные животные" > Animals
   19  cat Animals
   20  mv "Animals" "Друзья человека"
   21  ls
   22  clear
   23  mkdir folder_test
   24  mv 'Друзья человека' folder_test/
   25  ls
   26  cd folder_test/
   27  ls
   28  clear
   29  cd test/
   30  cd /
   31  cd ~
   32  cd test/
   33  clear
   34  sudo apt-get update
   35  sudo apt update
   36  sudo apt install mysql-server
   37  sudo service mysql status
   38  clear
   39  wget https://ftp.debian.org/debian/pool/main/s/spaced/spaced_1.2.0-201605+dfsg-1_amd64.deb
   40  sudo dpkg -i spaced_1.2.0-201605+dfsg-1_amd64.deb 
   41  sudo dpkg -r sl
   42  sudo dpkg -r spaced 
   43  clear
   44  history


    ```

    </details>

    ***


6. Нарисовать диаграмму, в которой есть класс родительский класс, домашние животные и вьючные животные, в составы которых в случае домашних животных войдут классы: собаки, кошки, хомяки, а в класс вьючные животные войдут: Лошади, верблюды и ослы.

    ![pictures for project](https://github.com/sSionAa/FW/blob/main/Pictures/6.jpg)

    ***

7. В подключенном MySQL репозитории создать базу данных “Друзья
человека”

    <details>
        <summary> Команды MySQL (развернуть) </summary>

    ```sql
    CREATE DATABASE Друзья_человека;
    ```

    </details>

    ![pictures for project](https://github.com/sSionAa/FW/blob/main/Pictures/7.png)

    ***

8. Создать таблицы с иерархией из диаграммы в БД

    <details>
        <summary> Команды MySQL (развернуть) </summary>

    ```sql
    CREATE TABLE Родительский_класс (
    id INT PRIMARY KEY AUTO_INCREMENT,
    тип VARCHAR(50)
    );


    CREATE TABLE Домашние_животные (
    id INT PRIMARY KEY,
    вид VARCHAR(50),
    FOREIGN KEY (id) REFERENCES Родительский_класс(id)
    );


    CREATE TABLE Собаки (
    id INT PRIMARY KEY,
    имя VARCHAR(50),
    команда VARCHAR(50),
    дата_рождения DATE,
    FOREIGN KEY (id) REFERENCES Домашние_животные(id)
    );


    CREATE TABLE Кошки (
    id INT PRIMARY KEY,
    имя VARCHAR(50),
    команда VARCHAR(50),
    дата_рождения DATE,
    FOREIGN KEY (id) REFERENCES Домашние_животные(id)
    );


    CREATE TABLE Хомяки (
    id INT PRIMARY KEY,
    имя VARCHAR(50),
    команда VARCHAR(50),
    дата_рождения DATE,
    FOREIGN KEY (id) REFERENCES Домашние_животные(id)
    );


    CREATE TABLE Вьючные_животные (
    id INT PRIMARY KEY,
    вид VARCHAR(50),
    FOREIGN KEY (id) REFERENCES Родительский_класс(id)
    );


    CREATE TABLE Лошади (
    id INT PRIMARY KEY,
    имя VARCHAR(50),
    команда VARCHAR(50),
    дата_рождения DATE,
    FOREIGN KEY (id) REFERENCES Вьючные_животные(id)
    );


    CREATE TABLE Верблюды (
    id INT PRIMARY KEY,
    имя VARCHAR(50),
    команда VARCHAR(50),
    дата_рождения DATE,
    FOREIGN KEY (id) REFERENCES Вьючные_животные(id)
    );


    CREATE TABLE Ослы (
    id INT PRIMARY KEY,
    имя VARCHAR(50),
    команда VARCHAR(50),
    дата_рождения DATE,
    FOREIGN KEY (id) REFERENCES Вьючные_животные(id)
    );

    show databases;
    show tables;
    ```

    </details>

    ![pictures for project](https://github.com/sSionAa/FW/blob/main/Pictures/8.png)

    ***

9. Заполнить низкоуровневые таблицы именами ( животных ), командами
которые они выполняют и датами рождения

    <details>
    <summary>SQL запросы (развернуть)</summary>

    ```sql
    INSERT INTO Собаки ( имя, команда, дата_рождения)
    VALUES ('Дэни', 'Лежать', '2019-03-11'),
           ('Черныш', 'Сидеть', '2020-01-22');
    
    INSERT INTO Кошки ( имя, команда, дата_рождения)
    VALUES ('Бегемот', 'Кушать', '2021-01-13'),
           ('Марс', 'Гулять', '2022-07-15');

    INSERT INTO Хомяки ( имя, команда, дата_рождения)
    VALUES ('Пухляш', 'Еда', '2021-01-21'),
           ('Стройняш', 'Бегать', '2023-01-18');

    INSERT INTO Лошади ( имя, команда, дата_рождения)
    VALUES ('Бэт', 'Но Но Но', '2019-01-20'),
           ('Сэм', 'Тпру', '2022-04-28');

    INSERT INTO Верблюды ( имя, команда, дата_рождения)
    VALUES ('Кафир', 'Лежать', '2019-03-01'),
           ('Ра', 'Хоп' '2021-10-14'),
           ('Сфинкс', 'Тпру' '2022-09-15');

    INSERT INTO Ослы ( имя, команда, дата_рождения)
    VALUES ('Коля', 'Вперед', '2023-05-24'),
           ('Толя', 'Стоять', '2024-01-08');
    ```

    </details>


    ***

10. Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой
питомник на зимовку. Объединить таблицы лошади, и ослы в одну таблицу.

    <details>
    <summary>SQL запросы (развернуть)</summary>

    ```sql
    TRUNCATE TABLE Верблюды;
    ```

    ```sql
    CREATE TABLE Копытные AS
    SELECT * FROM Лошади
    UNION
    SELECT * FROM Ослы;
    ```

    </details>


    ***

11. Создать новую таблицу “молодые животные” в которую попадут все
животные старше 1 года, но младше 3 лет и в отдельном столбце с точностью
до месяца подсчитать возраст животных в новой таблице

    <details>
        <summary>SQL запросы (развернуть)</summary>

    ```sql
    CREATE TABLE Копытные AS
    SELECT *, TIMESTAMPDIFF(MONTH, дата_рождения, CURDATE()) AS возраст_в_месяцах
    FROM (
        SELECT 'Собаки' AS тип_животного, имя, команда, дата_рождения FROM Собаки
        UNION ALL
        SELECT 'Кошки' AS тип_животного, имя, команда, дата_рождения FROM Кошки
        UNION ALL
        SELECT 'Хомяки' AS тип_животного, имя, команда, дата_рождения FROM Хомяки
        UNION ALL
        SELECT 'Лошади' AS тип_животного, имя, команда, дата_рождения FROM Лошади
        UNION ALL
        SELECT 'Ослы' AS тип_животного, имя, команда, дата_рождения FROM Ослы
    ) AS животные
    WHERE дата_рождения >= DATE_SUB(CURDATE(), INTERVAL 3 YEAR)
    AND дата_рождения <= DATE_SUB(CURDATE(), INTERVAL 1 YEAR);

    ```

    </details>


    ***

12. Объединить все таблицы в одну, при этом сохраняя поля, указывающие на
прошлую принадлежность к старым таблицам.

    <details>
        <summary>SQL запросы (развернуть)</summary>

    ```sql
    CREATE TABLE Полный_состав AS
    SELECT 'Собаки' AS тип_животного, имя, команда, дата_рождения FROM Собаки
    UNION ALL
    SELECT 'Кошки' AS тип_животного, имя, команда, дата_рождения FROM Кошки
    UNION ALL
    SELECT 'Хомяки' AS тип_животного, имя, команда, дата_рождения FROM Хомяки
    UNION ALL
    SELECT 'Лошади' AS тип_животного, имя, команда, дата_рождения FROM Лошади
    UNION ALL
    SELECT 'Ослы' AS тип_животного, имя, команда, дата_рождения FROM Ослы;

    ```

    </details>


    ***

13.14.15
    Создать класс с Инкапсуляцией методов и наследованием по диаграмме.
    Написать программу, имитирующую работу реестра домашних животных.


    **В программе должен быть реализован следующий функционал:**
    
        14.1 Завести новое животное

        14.2 определять животное в правильный класс

        14.3 увидеть список команд, которое выполняет животное

        14.4 обучить животное новым командам

        14.5 Реализовать навигацию по меню




    Создайте класс "Счетчик", у которого есть метод add(), увеличивающий̆
значение внутренней̆int переменной̆на 1 при нажатие “Завести новое
животное” Сделайте так, чтобы с объектом такого типа можно было работать в
блоке try-with-resources. Нужно бросить исключение, если работа с объектом
типа счетчик была не в ресурсном try и/или ресурс остался открыт. Значение
считать в ресурсе try, если при заведения животного заполнены все поля.

[**`Решение`**](https://github.com/sSionAa/FW/tree/main/Py)

    ***
*Подготовил студент Geek Brains* [**`Томайлы Владимир`**](https://github.com/sSionAa)
