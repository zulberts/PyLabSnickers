from classes import Item, Container
from classes import NegativeLoadError, NegativeWeightError, OverLoadError
import pytest


def test_create_item_standard():
    item = Item(10)
    assert item.weight == 10


def test_create_item_negative_weight():
    with pytest.raises(NegativeWeightError):
        Item(-10)


def test_item_set_weight():
    item = Item(10)
    assert item.weight == 10
    item.set_weight(15)
    assert item.weight == 15


def test_item_set_negative_weight():
    item = Item(10)
    assert item.weight == 10
    with pytest.raises(NegativeWeightError):
        Item(-10)


def test_create_container_standard():
    container = Container(0.5, 10)
    assert container.weight == 0.5
    assert container.load == 10


def test_create_container_negative_values():
    with pytest.raises(NegativeWeightError):
        Container(-1, 0)
    with pytest.raises(NegativeLoadError):
        Container(0.5, -10)


def test_container_insert_item_standard():
    item = Item(10)
    container = Container(0, 20)
    container.insert_item(item)
    assert container.load == 20
    assert container.weight == 10
    assert container.items == [item]


def test_container_insert_item_overload():
    item = Item(21)
    container = Container(0, 20)
    with pytest.raises(OverLoadError):
        container.insert_item(item)


def test_container_insert_container_standard():
    container_inner = Container(0, 20)
    container_outer = Container(0, 40)
    container_inner.insert_item(Item(10))
    container_inner.insert_item(Item(1))
    container_inner.insert_item(Item(5))
    assert container_inner.weight == 16
    container_outer.insert_item(container_inner)
    assert container_outer.items == [container_inner]
    assert container_outer.weight == 16


def test_container_insert_container_overload():
    container_inner = Container(0, 20)
    container_outer = Container(0, 10)
    container_inner.insert_item(Item(10))
    container_inner.insert_item(Item(1))
    container_inner.insert_item(Item(5))
    assert container_inner.weight == 16
    with pytest.raises(OverLoadError):
        container_outer.insert_item(container_inner)


def test_container_remove_item_standard():
    item1 = Item(5)
    item2 = Item(6)
    container = Container(0.5, 20)
    container.insert_item(item1)
    container.insert_item(item2)
    assert container.items == [item1, item2]
    assert container.weight == 11.5
    container.remove_item(item1)
    assert container.items == [item2]
    assert container.weight == 6.5


def test_container_remove_invalid_item():
    item1 = Item(5)
    item2 = Item(6)
    container = Container(0.5, 20)
    container.insert_item(item1)
    assert container.items == [item1]
    assert container.weight == 5.5
    with pytest.raises(ValueError):
        container.remove_item(item2)


def test_container_remove_container_standard():
    container_inner = Container(0, 20)
    container_outer = Container(0, 40)
    container_inner.insert_item(Item(10))
    container_inner.insert_item(Item(1))
    container_inner.insert_item(Item(5))
    assert container_inner.weight == 16
    container_outer.insert_item(container_inner)
    assert container_outer.weight == 16
    assert container_outer.items == [container_inner]
    container_outer.remove_item(container_inner)
    assert container_outer.items == []
    assert container_outer.weight == 0


def test_container_print_standard():
    item1 = Item(5)
    item2 = Item(6)
    container = Container(0.5, 20)
    container.insert_item(item1)
    container.insert_item(item2)
    assert container.items == [item1, item2]
    assert container.print() == "5 6"


def test_container_print_container_standard():
    container_inner = Container(0, 20)
    container_outer = Container(0, 40)
    container_inner.insert_item(Item(10))
    container_inner.insert_item(Item(1))
    container_inner.insert_item(Item(5))
    container_outer.insert_item(container_inner)
    assert container_outer.print() == "16"
    assert container_inner.print() == "10 1 5"


def test_container_print_as_str():
    item1 = Item(5)
    item2 = Item(6)
    container = Container(0.5, 20)
    container.insert_item(item1)
    container.insert_item(item2)
    assert container.items == [item1, item2]
    assert str(container) == container.print()


def test_container_print_container_as_str():
    container_inner = Container(0, 20)
    container_outer = Container(0, 40)
    container_inner.insert_item(Item(10))
    container_inner.insert_item(Item(1))
    container_inner.insert_item(Item(5))
    container_outer.insert_item(container_inner)
    assert container_outer.print() == str(container_outer)
    assert container_inner.print() == str(container_inner)
