class NegativeWeightError(Exception):
    """
    NegativeWeightError Exception.
    Raised when negative weight is passed as a parameter

    :param weight: passed weight value
    :type weight: float | int
    """

    def __init__(self, weight: float | int) -> None:
        super().__init__("Weight cannot be negative")
        self.__weight = weight


class NegativeLoadError(Exception):
    """
    NegativeLoadError Exception.
    Raised when negative load is passed as a parameter

    :param load: passed load value
    :type load: float | int
    """

    def __init__(self, load: float | int) -> None:
        super().__init__("Load cannot be negative")
        self.__load = load


class OverLoadError(Exception):
    """
    OverLoadError Exception.
    Raised when insertion of an item exceeded container's maximum load

    :param container_weight: container's current weight
    :type container_weight: float | int

    :param container_load: container's maximum load
    :type container_load: float | int

    :param item_weight: item's weight
    :type item_weight: float | int
    """

    def __init__(
        self, cweight: float | int, cload: float | int, iweight: float | int
    ) -> None:
        super().__init__("Overload")
        self.__container_weight = cweight
        self.__container_load = cload
        self.__item_weight = iweight


class Item:
    """
    Item Class. Contains attributes

    :param weight: item's weight in Kg
    :type weight: float | int
    """

    def __init__(self, weight: float | int) -> None:
        if weight < 0:
            raise NegativeWeightError(weight)
        else:
            self.__weight = weight

    @property
    def weight(self) -> float | int:
        return self.__weight

    def set_weight(self, weight: float | int) -> None:
        """
        Sets item's weight to a given value.
        Raises NegativeWeightError if the argument is negative
        """
        if weight < 0:
            raise NegativeWeightError(weight)
        else:
            self.__weight = weight


class Container(Item):
    """
    Container class. Contains attributes:

    :param weight: container's weight in Kg
    :type weight: float | int

    :param load: container's maximum load in Kg
    :type load: float | int

    :param items: container's items
    :type items: list[Item]

    """

    def __init__(self, weight: float | int, load: float | int) -> None:
        super().__init__(weight)
        if load < 0:
            raise NegativeLoadError(load)
        else:
            self.__load = load
        self.__items = []

    @property
    def load(self) -> float | int:
        return self.__load

    @property
    def items(self) -> list[Item]:
        return self.__items

    def insert_item(self, item: Item) -> None:
        """
        Inserts an item into the container.
        Raises OverLoadError if container's weight exceeds its maximum load
        after an item had been inserted
        """
        weight_after_insertion = self.weight + item.weight
        if weight_after_insertion > self.__load:
            raise OverLoadError(self.weight, self.__load, item.weight)
        else:
            self.__items.append(item)
            self.set_weight(weight_after_insertion)

    def remove_item(self, itemToRemove: Item) -> None:
        """
        Removes an item from the container
        """
        self.__items.remove(itemToRemove)
        self.set_weight(self.weight - itemToRemove.weight)

    def print(self) -> str:
        """
        Returns a list of container's contents in the following format:
        {item1.weight} {item2.weight} ... {itemN.weight}
        """
        joined_items = " ".join([str(item.weight) for item in self.__items])
        return f"{joined_items}"

    def __str__(self) -> str:
        return self.print()
