from classes import Price, EXCHANGE_RATES
from classes import NegativePriceValueError, NoExchangeRatesError
import pytest


def test_create_price_standard():
    price = Price("zl", 125, 100, EXCHANGE_RATES)
    assert price.currency == "zl"
    assert price.value == 125
    assert price.base_value == 100
    assert price.exchange_rates == EXCHANGE_RATES


def test_create_price_invalid():
    with pytest.raises(ValueError):
        Price("", 125, 100, EXCHANGE_RATES)
    with pytest.raises(NoExchangeRatesError):
        Price("zl", 125, 100, [])
    with pytest.raises(NegativePriceValueError):
        Price("zl", -100, 125, EXCHANGE_RATES)
    with pytest.raises(NegativePriceValueError):
        Price("zl", 100, -125, EXCHANGE_RATES)


def test_price_multiply_by_const_int():
    price = Price("zl", 125, 100, EXCHANGE_RATES)
    assert price.value == 125
    price.multiply_by_const(5)
    assert price.value == 625


def test_price_multiply_by_const_float():
    price = Price("zl", 125, 100, EXCHANGE_RATES)
    assert price.value == 125
    price.multiply_by_const(5.5)
    assert price.value == 687


def test_price_multiply_by_const_negative():
    price = Price("zl", 125, 100, EXCHANGE_RATES)
    assert price.value == 125
    with pytest.raises(NegativePriceValueError):
        price.multiply_by_const(-1)


def test_price_str_standard():
    price = Price("zl", 125, 100, EXCHANGE_RATES)
    assert price.value == 125
    assert price.base_value == 100
    assert str(price) == "1.25 zl"
    price.multiply_by_const(4)
    assert str(price) == "5.00 zl"


def test_price_exchange_std():
    price = Price("zl", 2500, 100, EXCHANGE_RATES)
    price.exchange("usd")
    assert price.currency == "usd"
    assert price.value == 625
    assert price.base_value == 100


def test_price_exchange_bidirectional():
    price = Price("zl", 2500, 100, EXCHANGE_RATES)
    price.exchange("usd")
    assert price.currency == "usd"
    assert price.value == 625
    assert price.base_value == 100
    price.exchange("zl")
    assert price.currency == "zl"
    assert price.value == 2506
    assert price.base_value == 100


def test_price_add_same_currency():
    price1 = Price("zl", 25, 100, EXCHANGE_RATES)
    price2 = Price("zl", 25, 100, EXCHANGE_RATES)
    price3 = price1.add(price2, "zl")
    assert price3.currency == "zl"
    assert price3.value == 50
    assert price3.base_value == 100
    assert price3.exchange_rates == EXCHANGE_RATES


def test_price_add_different_currencies():
    price1 = Price("usd", 25, 100, EXCHANGE_RATES)
    price2 = Price("zl", 25, 100, EXCHANGE_RATES)
    price3 = price1.add(price2, "zl")
    assert price3.currency == "zl"
    assert price3.value == 124
    assert price3.base_value == 100
    assert price3.exchange_rates == EXCHANGE_RATES
