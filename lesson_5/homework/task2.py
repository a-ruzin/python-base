"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

lines = 0
with open('task2.py', 'r', encoding='utf-8') as fp:
    for line in fp:
        lines += 1
        words = len(line.split())
        print(words)

print(f'lines: {lines}')
