"""1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix

    def __str__(self):
        matrix_text = ''
        for matrix_row in self.matrix:
            matrix_text += (' '.join(map(str, matrix_row))) + "\n"
        return matrix_text

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            new_matrix = []
            for row_num in range(len(self.matrix)):
                if len(self.matrix[row_num]) == len(other.matrix[row_num]):
                    new_row = []
                    for column_num in range(len(self.matrix[row_num])):
                        new_row.append(int(self.matrix[row_num][column_num]) + int(other.matrix[row_num][column_num]))
                    new_matrix.append(new_row)
                else:
                    raise Exception('Matrices cannot be summed if they have different sizes of row!')
        else:
            raise Exception('Matrices cannot be summed if they have different sizes of column!')
        return Matrix(new_matrix)


if __name__ == '__main__':
    matrix_example_01 = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
    matrix_example_02 = [[1100, 1200, 1300], [2100, 2200, 2300], [3100, 3200, 3300]]
    matrix_obj_01 = Matrix(matrix_example_01)
    matrix_obj_02 = Matrix(matrix_example_02)
    print(matrix_obj_01)
    print(matrix_obj_02)
    try:
        matrix_obj_03 = matrix_obj_01 + matrix_obj_02
        print(matrix_obj_03)
    except Exception as e:
        print(e)
