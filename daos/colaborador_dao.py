from daos.dao import DAO
from model.colaborador import Colaborador


class ColaboradorDAO(DAO):
    def __init__(self):
        super().__init__('colaboradores.pkl', chave="cpf")

    def adiciona(self, colaborador: Colaborador):
        if colaborador is not None and \
           isinstance(colaborador, Colaborador) and \
           isinstance(colaborador.cpf, int):
            super().adiciona(colaborador)

    def altera(self, colaborador: Colaborador):
        if colaborador is not None and \
           isinstance(colaborador, Colaborador) and \
           isinstance(colaborador.cpf, int):
            super().altera(colaborador)

    def pega(self, cpf: int):
        if isinstance(cpf, int):
            return super().pega(cpf)

    def remove(self, cpf: int):
        if isinstance(cpf, int):
            super().remove(cpf)
    
    def pega_todos(self):
        return super().pega_todos()