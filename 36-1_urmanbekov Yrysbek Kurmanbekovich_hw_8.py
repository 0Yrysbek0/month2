import sqlite3

conn = sqlite3.connect('school_database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )
''')

cursor.executemany('INSERT INTO countries (title) VALUES (?)', [('Kyrgyzstan',), ('Germany',), ('China',)])


cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries (id)
    )
''')


cursor.executemany('INSERT INTO cities (title, country_id) VALUES (?, ?)',
                   [('Bishkek', 1), ('Berlin', 2), ('Beijing', 3), ('Osh', 1), ('Paris', 2), ('Tokyo', 3), ('Moscow', 2)])


cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities (id)
    )
''')


cursor.executemany('INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)',
                   [('John', 'Doe', 1), ('Alice', 'Smith', 2), ('Bob', 'Johnson', 3),
                    ('Elena', 'Ivanova', 4), ('Michael', 'Miller', 5), ('Sophia', 'Lee', 6),
                    ('Daniel', 'Brown', 7), ('Olivia', 'Jones', 1), ('Liam', 'Wilson', 2),
                    ('Ava', 'Taylor', 3), ('Mia', 'Anderson', 4), ('Ethan', 'Moore', 5),
                    ('Emma', 'Hall', 6), ('Noah', 'Clark', 7), ('Isabella', 'White', 1)])


conn.commit()
conn.close()



import sqlite3

def display_students_by_city():
    # Подключение к базе данных
    conn = sqlite3.connect('school_database.db')
    cursor = conn.cursor()

    while True:
        print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
        cursor.execute('SELECT id, title FROM cities')
        cities = cursor.fetchall()

        for city in cities:
            print(f"{city[0]}. {city[1]}")


        city_id = input("Введите id города: ")

        if city_id == '0':
            break

        try:
            city_id = int(city_id)
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")
            continue


        cursor.execute('''
            SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
            FROM students
            JOIN cities ON students.city_id = cities.id
            JOIN countries ON cities.country_id = countries.id
            WHERE cities.id = ?
        ''', (city_id,))
        students = cursor.fetchall()

        if not students:
            print("В базе данных нет учеников из выбранного города.")
        else:
            for student in students:
                print(f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]}")


    conn.close()


display_students_by_city()