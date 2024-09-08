# Данные об оценках и учениках
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Сортируем имена учеников по алфавиту
sorted_students = sorted(students)

# Создаем словарь с именами учеников и их средними баллами
average_grades_dict = {}

for i, student in enumerate(sorted_students):
    # Вычисляем средний балл для каждого ученика
    average_grade = sum(grades[i]) / len(grades[i])
    # Добавляем в словарь
    average_grades_dict[student] = average_grade

# Выводим полученный словарь
print(average_grades_dict)
