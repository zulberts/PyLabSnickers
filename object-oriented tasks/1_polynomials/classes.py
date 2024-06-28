class Polynomial:
    """
    Class Polynomial. Represents Polynomials.
    Contains attributes:

    :param pars: List of tuples containing polynomial's values
    :param type: List of tuples containing intigers or floats
    """

    def __init__(self, pars: list) -> None:
        """
        Creates an instance of pars.
        """
        dict_tuples = {}
        for power, factor in pars:
            if False if type(power) is int else True:
                raise ValueError("power cannot be float")
            if False if type(factor) is (int or float) else True:
                raise ValueError("factor must be float or intiger")
            if power not in dict_tuples:
                dict_tuples[power] = 1
            else:
                dict_tuples[power] += 1
            if power <= 0 or dict_tuples[power] > 1 or factor == 0:
                raise ValueError("Zmienne są źle dobrane")
            else:
                self.__pars = pars

    @property
    def pars(self) -> list[tuple]:
        return sorted(self.__pars, key=lambda x: x[0], reverse=True)

    def pars_sort(self) -> list[tuple]:
        return sorted(self.__pars, key=lambda x: x[0], reverse=True)

    def set_pars(self, pars: list) -> None:
        dict_tuples = {}
        for power, factor in pars:
            if False if type(power) is int else True:
                raise ValueError("power cannot be float")
            if False if type(factor) is (int or float) else True:
                raise ValueError("factor must be float or intiger")
            if power not in dict_tuples:
                dict_tuples[power] = 1
            else:
                dict_tuples[power] += 1
            if power <= 0 or dict_tuples[power] > 1 or factor == 0:
                raise ValueError("Zmienne są źle dobrane")
            else:
                self.__pars = pars

    def degree(self) -> int:
        """
        Returns degree of the Polynomial.
        """
        max = 0
        for power in self.__pars:
            if power[0] > max:
                max = power[0]
            else:
                max = max
        return max

    def value(self, x: float) -> float:
        output = 0
        for power, factor in self.__pars:
            output = output + factor * (x**power)
        return output

    def __add__(self, other) -> list:
        result = {}
        for power, factor in self.__pars:
            result[power] = factor
        for power, factor in other.__pars:
            if power in result:
                result[power] += factor
            else:
                result[power] = factor
        result_list = []
        for power in result:
            result_list.append((power, result[power]))
        return result_list

    def __substract__(self, other) -> list:
        result = {}
        for power, factor in self.__pars:
            result[power] = factor
        for power, factor in other.__pars:
            if power in result:
                result[power] -= factor
            else:
                result[power] = factor
        result_list = []
        for power in result:
            result_list.append((power, result[power]))
        return result_list

    def print(self):
        output = ""
        i = 0
        for power, factor in self.pars_sort():
            if power == 0:
                power_str = ""
            elif power == 1:
                power_str = "*x"
            else:
                power_str = f"*x^{power}"

            if factor > 0 and i > 0:
                factor_str = f"+{factor}" if power > 0 else f"{factor}"
            else:
                factor_str = f"{factor}"

            output += factor_str + power_str
            i += 1

        return output

    def __str__(self):
        return self.print()
