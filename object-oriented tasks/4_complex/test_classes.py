from classes import ComplexNumber


def test_create_complex_number_standard():
    num = ComplexNumber(1, 2)
    assert num.re == 1
    assert num.im == 2


def test_complex_number_conjugate_standard():
    num = ComplexNumber(1, 2)
    num_conjugate = num.conjugate()
    assert num_conjugate.re == 1
    assert num_conjugate.im == -2


def test_complex_number_mangnitude_standard():
    num = ComplexNumber(3, 4)
    assert num.magnitude() == 5


def test_complex_number_addition_standard():
    num1 = ComplexNumber(1, 2)
    num2 = ComplexNumber(3, 4)
    num_after_addition = num1 + num2
    assert num_after_addition.re == 4
    assert num_after_addition.im == 6


def test_complex_number_subtraction_standard():
    num1 = ComplexNumber(1, 2)
    num2 = ComplexNumber(3, 4)
    num_after_subtraction = num1 - num2
    assert num_after_subtraction.re == -2
    assert num_after_subtraction.im == -2


def test_complex_number_multiplication_standard():
    num1 = ComplexNumber(1, 2)
    num2 = ComplexNumber(3, 4)
    num_after_mult = num1 * num2
    assert num_after_mult.re == -5
    assert num_after_mult.im == 10


def test_complex_number_division_standard():
    num1 = ComplexNumber(1, 8)
    num2 = ComplexNumber(2, 3)
    num_after_division = num1 / num2
    assert num_after_division.re == 2
    assert num_after_division.im == 1


def test_complex_number_str_standard():
    num1 = ComplexNumber(1, 8)
    assert str(num1) == "1+8i"


def test_complex_number_str_im():
    num1 = ComplexNumber(0, 1)
    assert str(num1) == "1i"
    num2 = ComplexNumber(1, 1)
    assert str(num2) == "1+1i"


def test_complex_number_str_negative():
    num1 = ComplexNumber(-1, -1)
    assert str(num1) == "-1-1i"
    num2 = ComplexNumber(0, -1)
    assert str(num2) == "-1i"
