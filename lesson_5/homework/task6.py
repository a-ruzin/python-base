"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка
описывает учебный предмет и наличие лекционных, практических и лабораторных
занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь, содержащий
название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def extract_hours(activity):
    hours = ''
    for char in activity:
        if '0' <= char <= '9':
            hours += char
    return int(hours) if hours != '' else 0


courses = {}
with open('task6.txt', 'r', encoding='utf-8') as fp:
    for line in fp:
        course_name, activities = line.split(':', maxsplit=1)
        course_hours = 0
        for activity in activities.split():
            course_hours += extract_hours(activity)
        courses[course_name] = course_hours

for course_name, course_hours in courses.items():
    print(f'{course_name}: {course_hours}')


# Альтернативный способ
import re
hours_re = re.compile('^(\d+).*$')
def extract_hours2(activity):
    if match := hours_re.match(activity):
        return int(match.group(1))
    else:
        return 0
