from model.ecobarreira import EcoBarreira
from model.endereco import Endereco
from model.estado import Estado
from model.sensor import Sensor


class ControladorEcoBarreira:
    def __init__(self):
        self.__ecobarreiras = []

    def cadastrar_ecobarreira(self, codigo: int, cidade: str,
                            cep: str, rua: str, 
                            complemento: str, estado: 
                            Estado, sensores: list) -> EcoBarreira:
        for ecobarreira in self.__ecobarreiras:
            if ecobarreira.codigo == codigo:
                return ecobarreira
        if isinstance(codigo, int) and isinstance(estado, Estado) \
        and isinstance(sensores, list):
            nova_ecobarreira = EcoBarreira(codigo, cidade, cep, rua, complemento, estado, sensores)
            self.__ecobarreiras.append(nova_ecobarreira)
            return nova_ecobarreira

    def buscar_ecobarreira_por_codigo(self, codigo:int):
        for ecobarreira in self.__ecobarreiras:
            if ecobarreira.codigo == codigo:
                return ecobarreira
        return None
    
    def altera_ecobarreira(self, codigo:int,
                           nova_cidade: str = None,
                           novo_cep: str = None,
                           nova_rua: str = None,
                           novo_complemento: str = None,
                           novo_estado: Estado = None,
                           novos_sensores: list = None
                           ):
        
        ecobarreira = self.buscar_ecobarreira_por_codigo(codigo)

        if ecobarreira is None:
            return None
        
        if nova_cidade:
            if isinstance(nova_cidade, str):
                ecobarreira.cidade = nova_cidade
        
        if novo_cep:
            if isinstance(novo_cep, str):
                ecobarreira.cep = novo_cep
        
        if nova_rua:
            if isinstance(nova_rua, str):
                ecobarreira.rua = nova_rua
        
        if novo_complemento:
            if isinstance(novo_complemento, str):
                ecobarreira.complemento = novo_complemento
        
        if novo_estado:
            if isinstance(novo_estado, Estado):
                ecobarreira.estado = novo_estado
        
        if novos_sensores:
            if isinstance(novos_sensores, list):
                ecobarreira.sensores = novos_sensores

    def excluir_ecobarreira(self, codigo:int):
        ecobarreira = self.buscar_ecobarreira_por_codigo(codigo)
        if ecobarreira in self.__ecobarreiras:
            self.__ecobarreiras.remove(ecobarreira)
            return ecobarreira
        else:
            return None
    
    def listar_ecobarreiras(self):
        if not self.__ecobarreiras:
            return None
        else:
            for ecobarreira in self.__ecobarreiras:
                print(f"Código: {ecobarreira.codigo}, \
                    Cidade: {ecobarreira.cidade}, \
                    Cep: {ecobarreira.cep}, \
                    Rua: {ecobarreira.rua}, \
                    Complemento: {ecobarreira.complemento}, \
                    Estado: {ecobarreira.estado}, \
                    Sensores: {ecobarreira.sensores}")