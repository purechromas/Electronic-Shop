import pytest

from exceptions import TooLongNameError
from src.item import Item


class TestItem:
    item = Item('iPhone 14 Pro Max', 100000, 50)

    def test_calculate_total_price(self):
        assert self.item.calculate_total_price() == 5000000

    def test_apply_discount(self):
        self.item.pay_rate = 0.8
        self.item.apply_discount()
        assert self.item.calculate_total_price() == 4000000.0

    def test_name_setter_getter(self):
        self.item.name = 'Iphone 13'
        assert self.item.name == 'Iphone 13'
        with pytest.raises(Exception):
            self.item.name = 'Iphone 13 Pro Max'

    def test_instantiate_from_csv(self):
        self.item.instantiate_from_csv('../items.csv')
        assert len(Item.all) == 5
        item1 = Item.all[0]
        assert item1.name == 'Смартфон'

    def test_string_to_number(self):
        assert Item.string_to_number('5') == 5
        assert Item.string_to_number('5.0') == 5
        assert Item.string_to_number('5.5') == 5

    def test_repr(self):
        item1 = Item("Смартфон", 10000, 20)
        assert repr(item1) == "Item('Смартфон', 10000, 20)"

    def test_str(self):
        item1 = Item("Смартфон", 10000, 20)
        assert str(item1) == 'Смартфон'

    def test_instantiate_from_csv_exceptions(self):
        assert self.item.instantiate_from_csv('asd.txt') == 'Отсутствует файл'

    def test_name_exception(self):
        with pytest.raises(TooLongNameError):
            self.item.name = 'СуперАппарат'
