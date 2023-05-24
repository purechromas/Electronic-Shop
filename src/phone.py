from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        if number_of_sim <= 0:
            raise ValueError('Quantity of sim cards must be more then < 0')
        self.number_of_sim = number_of_sim

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
