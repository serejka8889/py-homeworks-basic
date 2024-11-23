class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []  # Завершенные курсы
        self.courses_in_progress = []  # Курсы в процессе изучения
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def average_grade(self):
        if not self.grades:
            return 0
        total = sum([sum(grades) for grades in self.grades.values()])
        count = sum([len(grades) for grades in self.grades.values()])
        return round(total / count, 1)

    def grade_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}"

    def average_grade(self):
        if not self.grades:
            return 0
        total = sum([sum(grades) for grades in self.grades.values()])
        count = sum([len(grades) for grades in self.grades.values()])
        return round(total / count, 1)

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()


class Reviewer(Mentor):
    def grade_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


# Функции для подсчета средней оценки
def average_student_grade(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return round(total / count, 1) if count != 0 else 0


def average_lecturer_grade(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return round(total / count, 1) if count != 0 else 0


# Создание 2-х экземпляров каждого класса
reviewer1 = Reviewer('Сергей', 'Иванов')
reviewer1.courses_attached = ['Python']

reviewer2 = Reviewer('Марина', 'Федорова')
reviewer2.courses_attached = ['Git']

lecturer1 = Lecturer('Иван', 'Ветров')
lecturer1.courses_attached = ['Python']

lecturer2 = Lecturer('Юлия', 'Драгунова')
lecturer2.courses_attached = ['Git']

student1 = Student('Андрей', 'Никифоров', 'м')
student1.courses_in_progress = ['Python']
student1.finished_courses = ['Введение в программирование']

student2 = Student('Лена', 'Иванова', 'ж')
student2.courses_in_progress = ['Git']
student2.finished_courses = ['Основы Python']

# Использование методов классов
reviewer1.grade_student(student1, 'Python', 9)
reviewer2.grade_student(student2, 'Git', 8)

student1.grade_lecture(lecturer1, 'Python', 10)
student2.grade_lecture(lecturer2, 'Git', 9)

# Вывод на экран
print('\nЭксперты, проверяющие домашние задания:')
print('---------')
print(reviewer1)
print('---------')
print(reviewer2)
print('\nЛекторы, читающие лекции:')
print('---------')
print(lecturer1)
print('---------')
print(lecturer2)
print('\nСтуденты:')
print('---------')
print(student1)
print('---------')
print(student2)

# Подсчет средних оценок
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print('\nОценки:')
print('---------')
print("Средняя оценка студентов по Python:", average_student_grade(students, 'Python'))
print('---------')
print("Средняя оценка студентов по Git:", average_student_grade(students, 'Git'))
print('---------')
print("Средняя оценка лекторов по Python:", average_lecturer_grade(lecturers, 'Python'))
print('---------')
print("Средняя оценка лекторов по Git:", average_lecturer_grade(lecturers, 'Git'))