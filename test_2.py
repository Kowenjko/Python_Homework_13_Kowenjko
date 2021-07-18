"""
Examples:
triangle = Triangle([3, 3, 3])
Use classes TriangleNotValidArgumentException and TriangleNotExistException
Create class TriangleTest with parametrized unittest for class Triangle
test data:
"""

import unittest
import math


class Triangle:
    def __init__(self, t):
        self.t = t

    def input_value(self):
        return self.t

    def perimetr(self):
        p = 0
        for i in self.t:
            p += i
        return p

    def square(self):
        p = self.perimetr()/2
        s = round(math.sqrt(p*(p-self.t[0])*(p-self.t[1])*(p-self.t[2])), 2)
        return s


valid_test_data = [[3, 4, 5], [10, 10, 10], [6, 7, 8], [7, 7, 7], [50, 50, 75], [
    37, 43, 22], [26, 25, 3], [30, 29, 5], [87, 55, 34], [120, 109, 13], [123, 122, 5]]
rezultat_test_data = [6.0, 43.3, 20.33, 21.22,
                      1240.2, 407.0, 36.0, 72.0, 396.0, 396.0, 300.0]

not_valid_arguments = [['3', 4, 5], ['a', 2, 3], [
    7, "str", 7], ['1', '1', '1'], ['a', 'str', 7]]


class TestClass(unittest.TestCase):
    # Перевіряємо чи розрахунки вірні

    def test1(self):
        triangle = Triangle([5, 3, 3])
        self.assertEqual(triangle.perimetr(), 11)
        self.assertEqual(triangle.square(), 4.15)
    # Перевіряємо чи тип даних коректний
    # ('3', 4, 5),
    # ('a', 2, 3),
    # (7, "str", 7),
    # ('1', '1', '1'),
    # ('a', 'str', 7)

    def test2(self):
        for i in not_valid_arguments:

            with self.assertRaises(TypeError):
                triangle = Triangle(i)
                triangle.perimetr()
                triangle.square()

    # Перевіряємо чи результат від'ємний або рівний 0

    def test3(self):
        triangle = Triangle([-3, -5, -3])
        self.assertLessEqual(triangle.perimetr(), 0)
    # Перевіряємо чи вхіні дані від'ємні або нулеві

    def test4(self):
        triangle = Triangle([-3, 0, -3])
        for i in triangle.input_value():
            self.assertLessEqual(i, 0)
    # Перевіряємо на правильність
    # ((3, 4, 5), 6.0),
    # ((10, 10, 10), 43.30),
    # ((6, 7, 8), 20.33),
    # ((7, 7, 7), 21.21),
    # ((50, 50, 75), 1240.19),
    # ((37, 43, 22), 406.99),
    # ((26, 25, 3), 36.0),
    # ((30, 29, 5), 72.0),
    # ((87, 55, 34), 396.0),
    # ((120, 109, 13), 396.0),
    # ((123, 122, 5), 300.0)

    def test5(self):
        for i in range(len(valid_test_data)):
            triangle = Triangle(valid_test_data[i])
            self.assertEqual(triangle.square(), rezultat_test_data[i])
    # Перевіряємо що довхина вхідних даних = 3

    def test6(self):
        triangle = Triangle([-5, -5, -3])
        self.assertLessEqual(len(triangle.input_value()), 3)


triangle = Triangle([-5, -5, -3])
print(triangle.perimetr())
print(triangle.square())
print(triangle.input_value())
