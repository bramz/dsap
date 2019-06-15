"""
Write a class, Flower, that has three instance variables of type str, int, and float,
that respectively represent the name of the flower, its number of petals, and its price.
Your class must include a constructor method that initilaizes each variable to an
appropriate value, and your class should include methods for setting the value of each type, and retreiving
the value of each type.
"""

class Flower:
    def __init__(self):
        self.name = str('default')
        self.petals = int(0)
        self.price = float(0.0)

    def set_name(self, name):
        self.name = name

    def set_petals(self, petals):
        self.petals = petals

    def set_price(self, price):
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_petals(self) -> int:
        return self.petals

    def get_price(self) -> float:
        return self.price