"""
3. Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов. Определить, кто из сотрудников имеет
оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

SALARY_BORDER = 20000

total_salary = 0
total_employees = 0
with open('task3.txt', 'r', encoding='utf-8') as fp:
    for line in fp:
        name, salary = line.split()
        salary = float(salary)
        total_salary += salary
        total_employees += 1
        if salary >= SALARY_BORDER:
            print(f'{name}: {salary:.2f}')

if total_employees > 0:
    print(f'Средняя з.п.: {total_salary/total_employees:.2f}')
