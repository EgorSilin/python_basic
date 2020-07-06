"""7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNum:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)


if __name__ == '__main__':
    print(complex(1, 2) + complex(3, 4))
    print(ComplexNum(1, 2) + ComplexNum(3, 4))
    print(complex(1, 2) + complex(3, 4) == ComplexNum(1, 2) + ComplexNum(3, 4))

    print(complex(1, 2) * complex(3, 4))
    print(ComplexNum(1, 2) * ComplexNum(3, 4))
    print(complex(1, 2) * complex(3, 4) == ComplexNum(1, 2) * ComplexNum(3, 4))
