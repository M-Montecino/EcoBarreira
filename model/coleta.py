from datetime import datetime
from model.ecobarreira import EcoBarreira
from model.colaborador import Colaborador
from model.lixo import Lixo


class Coleta:
    def __init__(self, id: int, data: datetime, ecobarreira: EcoBarreira, colaborador: Colaborador):
        self.__id = id
        self.__data = data
        self.__ecobarreira = ecobarreira
        self.__colaborador = colaborador
        self.__lixos = []

    @property
    def data(self) -> datetime:
        return self.__data

    @data.setter
    def data(self, data: datetime):
        if isinstance(data, datetime):
            self.__data = data

    @property
    def ecobarreira(self) -> EcoBarreira:
        return self.__ecobarreira

    @ecobarreira.setter
    def ecobarreira(self, ecobarreira: EcoBarreira):
        if isinstance(ecobarreira, EcoBarreira):
            self.__ecobarreira = ecobarreira

    @property
    def colaborador(self) -> Colaborador:
        return self.__colaborador

    @colaborador.setter
    def colaborador(self, colaborador: Colaborador):
        if isinstance(colaborador, Colaborador):
            self.__colaborador = colaborador

# manipulacao de lixo

    @property
    def lixos(self) -> list:
        return self.__lixos

    def adicionar_lixo(self, lixo: Lixo):
        if lixo not in self.__lixos:
            self.__lixos.append(lixo)
            return lixo
        return None

    def remover_lixo(self, lixo: Lixo):
        if lixo in self.__lixos:
            self.__lixos.remove(lixo)
            return lixo
        return None
