"""
Write the function quadratic_equation with arguments a, b ,c that solution to quadratic equation without comlex solution.

Write unit tests for this function with QuadraticEquationTest class

Minimum 3 tests: discriminant < 0, discriminant > 0, discriminant = 0
"""

import pytest

import math


def quadratic_equation(a, b, c):

    d = b**2-4*a*c
    # x1 = (-b+math.sqrt(d))/(2*a)
    # x2 = (-b-math.sqrt(d))/(2*a)
    # print(d)
    return d


class TestClass:
    def test1(self):
        assert quadratic_equation(2, 1, -1) > 0

    def test2(self):
        assert quadratic_equation(1, -4, 4) == 0

    def test3(self):
        assert quadratic_equation(4, 1, 2) < 0

    def test4(self):
        assert quadratic_equation(0, 0, 0) == 0
