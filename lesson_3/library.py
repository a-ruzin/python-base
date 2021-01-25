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
