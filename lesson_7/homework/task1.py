"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join("".join(f'{value:5}' for value in columns) for columns in self.matrix)

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError('размеры матриц не совпадают')

        result_matrix_rows = []
        for row_index, row in enumerate(self.matrix):
            new_row = [value + other.matrix[row_index][col_index] for col_index, value in enumerate(row)]
            result_matrix_rows.append(new_row)

        return Matrix(result_matrix_rows)


m1 = Matrix([[1, 2], [3, 4]])
print('m1:')
print(m1)

m2 = Matrix([[9, 8], [7, 6]])
print('m2:')
print(m2)

print('m1+m2:')
print(m1+m2)
