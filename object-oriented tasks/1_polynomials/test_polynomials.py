from classes import Polynomial
import pytest


def test_pars():
    para1 = Polynomial([(10, 1)])
    assert para1.pars == [(10, 1)]
    para2 = Polynomial([(10, 1), (9, 2)])
    assert para2.pars == ([(10, 1), (9, 2)])


def test_pars_negative():
    with pytest.raises(ValueError):
        Polynomial([(-1, 1)])
    with pytest.raises(ValueError):
        Polynomial([(1, 6), (1, 7)])
    with pytest.raises(ValueError):
        Polynomial([(7, 0)])


def test_set_pars_standard():
    para2 = Polynomial([(10, 2)])
    para2.set_pars([(10, 2), (9, 3), (6, 7)])
    assert para2.pars == [(10, 2), (9, 3), (6, 7)]


def test_power_not_float_int():
    with pytest.raises(ValueError):
        Polynomial([("5", 6)])


def test_factor_not_float_int():
    with pytest.raises(ValueError):
        Polynomial([(5, "6")])


def test_degree():
    para2 = Polynomial([(10, 2)])
    assert para2.degree() == 10


def test_pars_sort():
    para2 = Polynomial([(10, 2)])
    para2.set_pars([(9, 3), (6, 7), (10, 5)])
    assert para2.pars == [(10, 5), (9, 3), (6, 7)]


def test_value():
    para2 = Polynomial([(1, 3), (2, 7), (3, 5)])
    assert para2.value(1) == 15


def test_add():
    para1 = Polynomial([(1, 3), (2, 7), (3, 5)])
    para2 = Polynomial([(1, 3), (2, 7), (3, 6)])
    assert para1.__add__(para2) == [(1, 6), (2, 14), (3, 11)]


def test_substract():
    para1 = Polynomial([(1, 3), (2, 7), (3, 5)])
    para2 = Polynomial([(1, 4), (2, 8), (3, 6)])
    assert para1.__substract__(para2) == [(1, -1), (2, -1), (3, -1)]


def test_print():
    para1 = Polynomial([(1, 3), (2, 7), (3, 5)])
    assert para1.__str__() == "5*x^3+7*x^2+3*x"


def test_print_negative():
    para1 = Polynomial([(1, 3), (2, 7), (3, -5)])
    assert para1.__str__() == "-5*x^3+7*x^2+3*x"
