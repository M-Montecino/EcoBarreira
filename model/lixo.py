from abc import ABC, abstractmethod


class Lixo(ABC):
    def __init__(self, quantidade: float):
        self._quantidade = quantidade

    @property
    def quantidade(self) -> float:
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade: float):
        if isinstance(quantidade, (int, float)):
            self._quantidade = quantidade

class Plastico(Lixo):
    def __init__(self, quantidade: float):
        super().__init__(quantidade)


class Vidro(Lixo):
    def __init__(self, quantidade: float):
        super().__init__(quantidade)


class Metal(Lixo):
    def __init__(self, quantidade: float):
        super().__init__(quantidade)


class Borracha(Lixo):
    def __init__(self, quantidade: float):
        super().__init__(quantidade)


class Organico(Lixo):
    def __init__(self, quantidade: float):
        super().__init__(quantidade)


class Outros(Lixo):
    def __init__(self, quantidade: float):
        super().__init__(quantidade)