import math


class ComplexNumber:
    def __init__(self, re: int | float, im: int | float):
        self.__re = re
        self.__im = im

    @property
    def re(self):
        return self.__re

    @property
    def im(self):
        return self.__im

    def conjugate(self):
        return ComplexNumber(self.__re, -self.__im)

    def magnitude(self):
        return math.sqrt(self.__re**2 + self.__im**2)

    def __add__(self, num_to_add):
        re_sum = self.__re + num_to_add.re
        im_sum = self.__im + num_to_add.im
        return ComplexNumber(re_sum, im_sum)

    def __sub__(self, num_to_subtract):
        re_subtract = self.__re - num_to_subtract.re
        im_subtract = self.__im - num_to_subtract.im
        return ComplexNumber(re_subtract, im_subtract)

    def __mul__(self, num_to_multiply):
        re_multiply = (self.__re * num_to_multiply.re) - (
            self.__im * num_to_multiply.im
        )
        im_multiply = (self.__re * num_to_multiply.im) + (
            self.__im * num_to_multiply.re
        )
        return ComplexNumber(re_multiply, im_multiply)

    def __truediv__(self, num_to_divide_by):
        if num_to_divide_by.im == 0:
            return ComplexNumber(
                self.__re / num_to_divide_by.re, self.__im / num_to_divide_by.re
            )
        denominator_conjugate = ComplexNumber(
            num_to_divide_by.re, num_to_divide_by.im
        ).conjugate()
        numerator = self * denominator_conjugate
        denominator = num_to_divide_by * denominator_conjugate
        return ComplexNumber(
            numerator.re / denominator.re, numerator.im / denominator.re
        )

    def __str__(self):
        re = self.__re
        im = self.__im
        re_part_str = f"{re if re != 0 else ''}"
        im_part_sign_str = f"{'+' if (im > 0 and re != 0) else ''}{im}i"

        return f"{re_part_str}{im_part_sign_str if im != 0 else ''}"
