"""
Сколько нужно энергии для обогрева города?

У пользователя надо спросить сколько домов (houses), и какая температура на улице (temperature).
При темпекратуре выше 15 градусов, отопление не требуется,
а при температуре ниже 15 градусов, на каждый градус меньше 15 нужно,
скажем, 2 Кв/час на домохозяйство в сутки.

e = 2 * (15 - temperature if temperature < 15 else 0) * houses
"""

def get_city_data():
    houses = int(input('количество домов:'))
    temperature = int(input('температура:'))
    return houses, temperature


def print_city_energy(city):
    # print(city)
    city += ' aksdjfkasjdkfj'
    print(city)
    houses, temperature = get_city_data()
    e = 2 * (15 - temperature if temperature < 15 else 0) * houses
    print(e)


def print_all_cities(all_cities):
    for city in all_cities:
        print('-', city)
        print_city_energy(city)
        print('+', city)
    all_cities.append('...')


cities = ['Новосибирск', 'Тюмень']
print(cities)
print_all_cities(cities)
print(cities)
