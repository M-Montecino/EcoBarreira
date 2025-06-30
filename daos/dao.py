import pickle
from abc import ABC, abstractmethod


class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        with open(self.__datasource, 'wb') as f:
            pickle.dump(self.__cache, f)

    def __load(self):
        with open(self.__datasource, 'rb') as f:
            self.__cache = pickle.load(f)

    def adiciona(self, obj):
        self.__cache[obj.cpf] = obj
        self.__dump()

    def altera(self, obj):
        if obj.cpf in self.__cache:
            self.__cache[obj.cpf] = obj
            self.__dump()

    def pega(self, cpf):
        try:
            return self.__cache.get(cpf, None)
        except AttributeError:
            return None

    def remove(self, cpf):
        if cpf in self.__cache:
            del self.__cache[cpf]
            self.__dump()

    def pega_todos(self):
        return list(self.__cache.values())