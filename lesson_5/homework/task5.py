"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
"""

import random

with open('task5.txt', 'w', encoding='utf-8') as fp:
    numbers = [random.randint(1, 100) for i in range(20)]
    print(' '.join(map(str, numbers)), file=fp)

with open('task5.txt', 'r', encoding='utf-8') as fp:
    numbers2 = map(int, fp.read().split())

result = sum(numbers2)
print('Сумма чисел:', result)
