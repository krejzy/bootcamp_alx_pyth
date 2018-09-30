"""
Zaimplementuj klase Vector dostarczającą funkcjonalność wektora swobodnego na dwuwymiarowej płaszczyźnie.
 Wektory powinny mieć możliwość dodawania, odejmoiwania, mnożenia (przez liczbę),
 porównywania (po długości) oraz powinny posiadać czytelną reprezentacje napisową.
"""
from math import sqrt


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        Vector(self.x + other.x, self.y + other.y)  # lub
        v_ret = Vector(new_x, new_y)
        return v_ret

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        Vector(self.x - other.x, self.y - other.y)  # lub
        v_ret = Vector(new_x, new_y)
        return v_ret

    def __mul__(self, other):
        new_x = self.x * other.x
        new_y = self.y * other.y
        Vector(self.x * other.x, self.y * other.y)  # lub
        v_ret = Vector(new_x, new_y)
        return v_ret

    @property
    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        return self.length == other.length

    def __ge__(self, other):
        return self.length >= other.length

    def __it__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length

    def __ne__(self, other):
        return self.length != other.length

    def __str__(self):
        return f' W({self.x}, {self.y}): {self.length}'


def test_sort():
    v1 = Vector(1, 2)
    v2 = Vector(0, 1)
    v3 = Vector(3, 2)
    v4 = Vector(0, 1)
    lista = [v1, v2, v3, v4]
    assert sorted(lista) == [v1, v2, v3, v4]
    assert sorted(lista) == [v1, v2, v3, v4]


def test_sub():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 - v2
    assert v3.x == 4
    assert v3.y == 6


def test_create():
    v1 = Vector(1, 2)
    assert v1.x == 1
    assert v1.y == 2


def test_add():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    assert v3.x == 4
    assert v3.y == 6


def test_len():
    v1 = Vector(3, 4)
    assert v1.length == 5.0


def test_equal():
    v1 = Vector(3, 4)
    v2 = Vector(3, 4)
    assert v1 == v2


def test_greater_or_equal():
    v1 = Vector(4, 4)
    v2 = Vector(3, 4)
    assert v1 > v2


def test_less_or_equal():
    v1 = Vector(4, 4)
    v2 = Vector(3, 4)
    assert v1 < v2

