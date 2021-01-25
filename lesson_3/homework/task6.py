"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое
слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word):
    if word:
        return word[0].upper() + word[1:]
    return word


def title_text(text):
    words = text.split()
    for index, word in enumerate(words):
        words[index] = int_func(word)
    result = ' '.join(words)
    return result


text = input('Введите текст: ')
titled_text = title_text(text)
print(f'Результат: {titled_text}')

# альтернативный способ
print(f'Результат: {text.title()}')
