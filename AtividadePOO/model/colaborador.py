from endereco import Endereco


class Colaborador:
    def __init__(self, cpf: int, nome: str, cidade: str, cep: str, rua: str, complemento: str, estado: str):
        self.__cpf = cpf
        self.__nome = nome
        self.endereco = Endereco(cidade, cep, rua, complemento, estado)

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        if isinstance(cpf, str):
            self.__cpf = cpf

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
