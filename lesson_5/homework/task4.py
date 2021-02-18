"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

with open('task4.txt', 'r', encoding='utf-8') as fp, \
        open('task4-out.txt', 'w', encoding='utf-8') as fpw:
    for line in fp:
        if (first_word := line.split()[0]) in dictionary:
            line = line.replace(first_word, dictionary[first_word])
        fpw.write(line)
