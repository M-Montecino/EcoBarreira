from abc import ABC, abstractmethod


class Lixo(ABC):

    @abstractmethod
    def __init__(self, quantidade: int):
        self.__quantidade = quantidade

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        if isinstance(quantidade, int):
            self.__quantidade = quantidade


class Plastico(Lixo):
    def __init__(self, quantidade: int):
        super().__init__(quantidade)


class Vidro(Lixo):
    def __init__(self, quantidade: int):
        super().__init__(quantidade)


class Metal(Lixo):
    def __init__(self, quantidade: int):
        super().__init__(quantidade)


class Borracha(Lixo):
    def __init__(self, quantidade: int):
        super().__init__(quantidade)


class Organico(Lixo):
    def __init__(self, quantidade: int):
        super().__init__(quantidade)


class Outros(Lixo):
    def __init__(self, quantidade: int):
        super().__init__(quantidade)
