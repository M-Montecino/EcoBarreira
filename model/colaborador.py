from model.endereco import Endereco


class Colaborador():
    def __init__(self, cpf: int, nome: str, cidade: str, cep: str, rua: str, complemento: str, estado: str):
        self.__cpf = cpf
        self.__nome = nome
        self.__endereco = Endereco(cidade, cep, rua, complemento, estado)

    @property
    def cpf(self) -> int:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: int):
        if isinstance(cpf, int):
            self.__cpf = cpf

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def cidade(self) -> str:
        return self.__endereco.cidade
    
    @cidade.setter
    def cidade(self, cidade:str):
        if isinstance(cidade, str):
            self.__endereco.cidade = cidade

    @property
    def cep(self) -> str:
        return self.__endereco.cep
    
    @cep.setter
    def cep(self, cep:str):
        if isinstance(cep, str):
            self.__endereco.cep = cep

    @property
    def rua(self) -> str:
        return self.__endereco.rua
    
    @rua.setter
    def rua(self, rua:str):
        if isinstance(rua, str):
            self.__endereco.rua = rua

    @property
    def complemento(self) -> str:
        return self.__endereco.complemento
    
    @complemento.setter
    def complemento(self, complemento: str):
        if isinstance(complemento, str):
            self.__endereco.complemento = complemento

    @property
    def estado(self) -> str:
        return self.__endereco.estado
    
    @estado.setter
    def estado(self, estado: str):
        if isinstance(estado, str):
            self.__endereco.estado = estado
