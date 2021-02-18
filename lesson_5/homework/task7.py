"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней
прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить
ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

profitable_companies = {}
unprofitable_companies = {}
total_profit = 0
with open('task7.txt', 'r', encoding='utf-8') as fp:
    for line in fp:
        company_name, company_form, revenue, expenses = line.split()
        revenue = int(revenue)
        expenses = int(expenses)
        profit = revenue - expenses
        if profit >= 0:
            profitable_companies[company_name] = profit
            total_profit += profit
        else:
            unprofitable_companies[company_name] = profit

profitable_companies_count = len(profitable_companies)
result = [
    profitable_companies,
    {'average_profit': total_profit/profitable_companies_count if profitable_companies_count > 0 else None}
]
if len(unprofitable_companies) > 0:
    result.append(unprofitable_companies)

with open('task7.json', 'w', encoding='utf-8') as fp:
    json.dump(result, fp, indent=True, ensure_ascii=False)
