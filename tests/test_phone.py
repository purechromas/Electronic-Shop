import pytest

from src.phone import Phone
from src.item import Item


class TestPhone:
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)

    def test_phone(self):
        assert str(self.phone1) == 'iPhone 14'
        assert repr(self.phone1) == "Phone('iPhone 14', 120000, 5, 2)"
        assert self.phone1.number_of_sim == 2
        assert self.item1 + self.phone1 == 25
        assert self.phone1 + self.phone1 == 10
        with pytest.raises(ValueError):
            Phone("Iphone 14", 100000, 10, 0)
