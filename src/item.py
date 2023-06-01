from csv import DictReader
from exceptions import InstantiateCSVError, TooLongNameError


class Item:
    """A class to represent a product in a store."""
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
        """Applies the set discount for a specific product."""
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
            raise TooLongNameError('TooLongNameError')
        else:
            self.__name = name

    @staticmethod
    def read_csv_file(path: str) -> list:
        """Reading a csv-file and storing the data in list."""

        items = []
        with open(path, encoding='utf-8') as f:
            files = DictReader(f)
            for file in files:
                if len(file) < 3:
                    raise InstantiateCSVError
                items.append(file)
        return items

    @classmethod
    def instantiate_from_csv(cls, path):
        """Making OOP-objects from specific data file."""
        try:
            cls.all = []
            data = cls.read_csv_file(path)
            for line in data:
                cls(line['name'],
                    cls.string_to_number(line['price']),
                    cls.string_to_number(line['quantity']))
        except FileNotFoundError:
            print('Отсутствует файл')
            return 'Отсутствует файл'
        except InstantiateCSVError:
            print('Файл поврежден')
            return 'Файл поврежден'

    @staticmethod
    def string_to_number(string: int or float) -> int or float:
        """Making string to int or float number and returning it."""
        if '.' in string:
            return float(string) // 1
        else:
            return int(string)
