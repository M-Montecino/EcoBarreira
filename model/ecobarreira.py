from model.endereco import Endereco
from model.sensor import Sensor


class EcoBarreira():
    def __init__(self, codigo: int, cidade: str, cep: str, rua: str, complemento: str, estado: str):
        self.__codigo = codigo
        self.__endereco = Endereco(cidade, cep, rua, complemento, estado)
        self.__sensores = []

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

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

#manipulacao de sensores

    @property
    def sensores(self) -> list:
        return self.__sensores

    def adicionar_sensor(self, sensor: Sensor):
        if sensor not in self.__sensores:
            self.__sensores.append(sensor)
            return sensor
        return None

    def remover_sensor(self, sensor: Sensor):
        if sensor in self.__sensores:
            self.__sensores.remove(sensor)
            return sensor
        return None