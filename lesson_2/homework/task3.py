"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""


def get_month():
    while True:
        month = input('введите номер месяца (от 1 до 12) или пустую строку, чтобы отменить ввод: ')
        if month == '':
            return None
        if month.isnumeric():
            month = int(month)
            if 1 <= month <= 12:
                return month
        print('введите число в диапазоне от 1 до 12\n')


# через список
month_names = 'Январь Февраль Март Апрель Май Июнь Июль Август Сентябрь Октябрь Ноябрь Декабрь'.split()
season_names = 'Зима Весна Лето Осень'.split()

while (month := get_month()) is not None:
    print(f"{month}-й месяц - {month_names[month-1]} / {season_names[(month%12)//3]}\n")


# через словарь

season_names = {
    'Зима': {1, 2, 12},
    'Весна': {3, 4, 5},
    'Лето': {6, 7, 8},
    'Осень': {9, 10, 11}
}

while (month := get_month()) is not None:
    for season_name, months in season_names.items():
        if month in months:
            print(f"{month}-й месяц - {month_names[month-1]} / {season_name}\n")
            break
