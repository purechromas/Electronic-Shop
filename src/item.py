import os
from csv import DictReader


class Item:
    """
    A class to represent a product in a store.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Creating an instance of the item class.

        :param name: Product name.
        :param price: Price per item.
        :param quantity: The quantity of the item in the store.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def calculate_total_price(self) -> float or int:
        """
        Calculates the total cost of a particular item in a store.

        :return: The total cost of the item.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Applies the set discount for a specific product.
        """
        self.price *= self.pay_rate

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise Exception("Can't addition this two objects")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception('TooLongNameError')
        else:
            self.__name = name

    @staticmethod
    def load_csv(filename) -> list:
        """
        Reading a csv-file and storing the data in list.
        """
        items = []
        try:
            filedir = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(f'{filedir}', filename), 'r', encoding='utf-8') as csv_file:
                csv_reader = DictReader(csv_file)

                for item in csv_reader:
                    items.append(item)
                return items

        except FileNotFoundError:
            print(f"File {filename} was not found")

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Making OOP-objects from specific data file.
        """
        try:
            cls.all = []
            data = cls.load_csv('items.csv')
            for line in data:
                cls(line['name'],
                    cls.string_to_number(line['price']),
                    cls.string_to_number(line['quantity']))
        except TypeError:
            print("There is no data for making object")

    @staticmethod
    def string_to_number(string: int or float) -> int or float:
        """
        Making string to int or float number and returning it.
        """
        if '.' in string:
            return float(string) // 1
        else:
            return int(string)
