class NegativePriceValueError(Exception):
    def __init__(self, value: int) -> None:
        super().__init__("Value cannot be negative")
        self.__value = value


class NoExchangeRatesError(Exception):
    def __init__(self) -> None:
        super().__init__("There cannot be no exchange rates")


EXCHANGE_RATES = {
    "zl": {"usd": (0.25, 100), "eur": (0.25, 100)},
    "usd": {"zl": (4.01, 100), "eur": (0.93, 100)},
    "eur": {"zl": (3.85, 100), "usd": (1.08, 100)},
}


class Price:
    """
    Price class. Contains attributes:

    :param currency: currency
    :type currency: str

    :param value: price represented in subbase units of a particular currency
    :type value: int

    :param base_value: subbase units count in a single base unit
    :type base_value: int

    :param exchange_rates: exchange rates for other currencies
    :type exchange_rates: dict[int]
    """

    def __init__(
        self, currency: str, value: int, base_value: int, exchange_rates: dict[int]
    ) -> None:
        if not currency:
            raise ValueError("Currency cannot be empty")
        else:
            self.__currency = currency
        if value < 0:
            raise NegativePriceValueError(value)
        else:
            self.__value = int(value)
        if base_value < 0:
            raise NegativePriceValueError(base_value)
        else:
            self.__base_value = int(base_value)
        if not exchange_rates:
            raise NoExchangeRatesError()
        self.__exchange_rates = exchange_rates

    @property
    def currency(self) -> str:
        return self.__currency

    @property
    def value(self) -> int:
        return self.__value

    @property
    def base_value(self) -> int:
        return self.__base_value

    @property
    def exchange_rates(self) -> dict[int]:
        return self.__exchange_rates

    def multiply_by_const(self, const: int | float) -> int:
        if const < 0:
            raise NegativePriceValueError(self.__value * const)
        else:
            self.__value = int(self.__value * const)

    def exchange(self, exchange_currency: str) -> None:
        exchange_rate, exchange_base_value = self.__exchange_rates[self.__currency][
            exchange_currency
        ]
        exchange_currency_base_value = exchange_base_value
        self.__value = int(self.__value * exchange_rate)
        self.__base_value = exchange_currency_base_value
        self.__currency = exchange_currency

    def add(self, price_to_add, final_currency):
        if price_to_add.currency != self.__currency:
            price_to_add.exchange(self.__currency)
        final_value = self.__value + price_to_add.__value
        final_price = Price(
            self.__currency, final_value, self.__base_value, self.__exchange_rates
        )
        if final_currency != self.__currency:
            final_price.exchange(final_currency)
        return final_price

    def sub(self, price_to_subtract, final_currency):
        if price_to_subtract.currency != self.__currency:
            price_to_subtract.exchange(self.__currency)
        final_value = self.__value - price_to_subtract.__value
        final_price = Price(
            self.__currency, final_value, self.__base_value, self.__exchange_rates
        )
        if final_currency != self.__currency:
            final_price.exchange(final_currency)
        return final_price

    def __str__(self) -> str:
        base_value = self.__value // self.__base_value
        subbase_value = self.__value % self.__base_value
        return f"{base_value}.{subbase_value:02} {self.__currency}"
