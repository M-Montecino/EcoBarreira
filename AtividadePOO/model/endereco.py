class Endereco:
    def __init__(self, cidade: str, cep: str, rua: str, complemento: str, estado: str):
        if isinstance(cidade, str):
            self.__cidade = cidade
        if isinstance(cep, str):
            self.__cep = cep
        if isinstance(rua, str):
            self.__rua = rua
        if isinstance(complemento, str):
            self.__complemento = complemento
        if isinstance(estado, str):
            self.__estado = estado

    @property
    def cidade(self) -> str:
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        if isinstance(cidade, str):
            self.__cidade = cidade

    @property
    def cep(self) -> str:
        return self.__cep

    @cep.setter
    def cep(self, cep: str):
        if isinstance(cep, str):
            self.__cep = cep

    @property
    def rua(self) -> str:
        return self.__rua

    @rua.setter
    def rua(self, rua: str):
        if isinstance(rua, str):
            self.__rua = rua

    @property
    def complemento(self) -> str:
        return self.__complemento

    @complemento.setter
    def complemento(self, complemento: str):
        if isinstance(complemento, str):
            self.__complemento = complemento

    @property
    def estado(self) -> str:
        return self.__estado

    @estado.setter
    def estado(self, estado: str):
        if isinstance(estado, str):
            self.__estado = estado
