import pickle
from abc import ABC, abstractmethod


class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource='', chave: str = ""):
        self.__datasource = datasource
        self.__chave = chave
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

    def __get_chave(self, obj):
        return getattr(obj, self.__chave)

    def adiciona(self, obj):
        chave = self.__get_chave(obj)
        self.__cache[chave] = obj
        self.__dump()

    def altera(self, obj):
        chave = self.__get_chave(obj)
        if chave in self.__cache:
            self.__cache[chave] = obj
            self.__dump()

    def pega(self, chave):
        return self.__cache.get(chave, None)

    def remove(self, chave):
        if chave in self.__cache:
            del self.__cache[chave]
            self.__dump()

    def pega_todos(self):
        return list(self.__cache.values())