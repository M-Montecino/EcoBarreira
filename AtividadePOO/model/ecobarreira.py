from model.endereco import Endereco
from model.sensor import Sensor


class EcoBarreira(Endereco):
    def __init__(self, codigo: int, cidade: str, cep: str, rua: str, complemento: str, estado: str):
        super().__init__(cidade, cep, rua, complemento, estado)
        self.__codigo = codigo
        self.endereco = Endereco(cidade, cep, rua, complemento, estado)
        self.__sensores = []

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def sensores(self) -> list:
        return self.__sensores

    @sensores.setter
    def sensores(self, sensores: list):
        if isinstance(sensores, list):
            self.__sensores = sensores
