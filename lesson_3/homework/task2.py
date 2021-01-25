"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def print_person_info(first_name, last_name, year_of_birth, residence, email, phone):
    print(
        f"{first_name} {last_name}, {year_of_birth} года рождения\n"
        f"проживает: {residence}\n"
        f"email: {email}\n"
        f"phone: {phone}"
    )


questions = [
    ('first_name', 'Имя'),
    ('last_name', 'Фамилия'),
    ('year_of_birth', 'год рождения'),
    ('residence', 'город проживания'),
    ('email', 'email'),
    ('phone', 'Телефон'),
]

print('Заполните анкету пользователя:')
person_info = {}
for key, field in questions:
    person_info[key] = input(f'  {field}: ')

print_person_info(
    first_name=person_info['first_name'],
    last_name=person_info['last_name'],
    year_of_birth=person_info['year_of_birth'],
    residence=person_info['residence'],
    email=person_info['email'],
    phone=person_info['phone'],
)

# альтернативный способ

print_person_info(**person_info)
