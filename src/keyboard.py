from src.item import Item


class KeyBoardMixIn:
    __language = 'EN'

    def __str__(self) -> str:
        return self.__language

    @property
    def language(self) -> str:
        return self.__language

    def change_lang(self) -> object:
        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        else:
            self.__language = 'EN'
            return self


class KeyBoard(Item, KeyBoardMixIn):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.__language = 'EN'

