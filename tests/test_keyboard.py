import pytest

from src.keyboard import KeyBoard


class TestKeyBoard:
    keyboard = KeyBoard('Dark Project KD87A', 9600, 5)

    def test_str_keyboard(self):
        assert str(self.keyboard) == 'Dark Project KD87A'

    def test_language_keyboard(self):
        assert self.keyboard.language == "EN"

    def test_change_language_keyboard(self):
        self.keyboard.change_lang()
        assert self.keyboard.language == 'RU'
        self.keyboard.change_lang()
        assert self.keyboard.language == 'EN'

    def test_no_setter(self):
        with pytest.raises(AttributeError):
            self.keyboard.language = 'BG'
