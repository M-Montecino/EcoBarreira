class Sensor:
    def __init__(self, codigo: int, tipo: str, ativo: bool):
        self.__codigo = codigo
        self.__tipo = tipo
        self.__ativo = ativo

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            return self.__codigo

    @property
    def tipo(self) -> str:
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        if isinstance(tipo, str):
            self.__tipo = tipo

    @property
    def ativo(self) -> bool:
        return self.__ativo

    @ativo.setter
    def ativo(self, ativo: bool):
        if isinstance(ativo, bool):
            self.__ativo = ativo
