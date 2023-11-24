class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Имя: {self.fullname}, Возраст: {self.age}, Женат/замужем: {self.is_married}")


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def calculate_average_mark(self):
        return sum(self.marks.values()) / len(self.marks)


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, base_salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.base_salary = base_salary

    def calculate_salary(self):
        bonus_percentage = max(0, self.experience - 3) * 0.05
        return self.base_salary + (self.base_salary * bonus_percentage)


def create_students():
    student1 = Student("Студент1", 18, False, {"Математика": 90, "Наука": 85, "История": 92})
    student2 = Student("Студент2", 17, False, {"Математика": 88, "Наука": 80, "История": 95})
    student3 = Student("Студент3", 19, True, {"Математика": 78, "Наука": 92, "История": 87})
    return [student1, student2, student3]


students_list = create_students()

for student in students_list:
    student.introduce_myself()
    print("Оценки:", student.marks)
    print("Средняя оценка:", student.calculate_average_mark())
    print()

teacher = Teacher("Учитель", 35, True, 5, 50000)
teacher.introduce_myself()
print("Зарплата:", teacher.calculate_salary())