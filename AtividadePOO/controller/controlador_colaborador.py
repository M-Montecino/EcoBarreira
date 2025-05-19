from model.colaborador import Colaborador
from model.endereco import Endereco
from model.estado import Estado

class ControladorColaborador:
    def __init__(self):
        self.__colaboradores = []

    @property
    def colaboradores(self) -> list:
        return self.__colaboradores
    
    def cadastrar_colaboradores(self, cpf: int, nome:str,
                                cidade: str, cep: str,
                                rua: str, complemento: str,
                                estado: Estado) -> Colaborador:
        for colaborador in self.__colaboradores:
            if colaborador.cpf == cpf:
                return colaborador
        if isinstance(nome, str) and isinstance(cpf, str) \
        and isinstance(cidade, str) and isinstance(cep, str) \
        and isinstance(rua, str) and isinstance(complemento, str) \
        and isinstance(estado, Estado):
            novo_colaborador = Colaborador(nome, cpf, cidade, cep, rua, complemento, estado)
            self.__colaboradores.append(novo_colaborador)
            return novo_colaborador

    def buscar_colaborador_por_cpf(self, cpf:str):
        for colaborador in self.__colaboradores:
            if colaborador.cpf == cpf:
                return colaborador
        return None
    
    def altera_colaborador(self, cpf: int,
                            novo_nome:str = None,
                            nova_cidade: str = None, 
                            novo_cep: str = None,
                            nova_rua: str = None, 
                            novo_complemento: str = None,
                            novo_estado: Estado = None):
        
        colaborador = self.buscar_colaborador_por_cpf(cpf)

        if colaborador is None:
            return None
        
        if novo_nome:
            if isinstance(novo_nome, str):
                colaborador.nome = novo_nome

        if nova_cidade:
            if isinstance(nova_cidade, str):
                colaborador.cidade = nova_cidade
        
        if novo_cep:
            if isinstance(novo_cep, str):
                colaborador.cep = novo_cep
        
        if nova_rua:
            if isinstance(nova_rua, str):
                colaborador.rua = nova_rua
        
        if novo_complemento:
            if isinstance(novo_complemento, str):
                colaborador.complemento = novo_complemento
        
        if novo_estado:
            if isinstance(novo_estado, Estado):
                colaborador.estado = novo_estado

    def excluir_colaborador(self, cpf:int):
        colaborador = self.buscar_colaborador_por_cpf(cpf)
        if colaborador in self.__colaboradores:
            self.__colaboradores.remove(colaborador)
            return colaborador
        else:
            return None

    def listar_colaboradores(self):
        if not self.__colaboradores:
            return None
        else:
            for colaborador in self.__colaboradores:
                print(f"CPF: {colaborador.cpf}, \
                        None: {colaborador.nome}, \
                        Cidade: {colaborador.cidade}, \
                        Cep: {colaborador.cep}, \
                        Rua: {colaborador.rua}, \
                        Complemento: {colaborador.complemento}, \
                        Estado: {colaborador.estado}, \
                        ")
