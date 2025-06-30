from daos.dao import DAO
from model.coleta import Coleta

class ColetaDAO(DAO):
    def __init__(self):
        super().__init__('coletas.pkl')
    
    def adiciona(self, coleta: Coleta):
        if coleta is not None and \
        isinstance(coleta, Coleta) and \
        isinstance(coleta.id, int):
            super().adiciona(coleta)
    
    def altera(self, coleta: Coleta):
        if coleta is not None and \
        isinstance(coleta, Coleta) and \
        isinstance(coleta.id, int): 
            super().altera(coleta)

    def pega(self, id: int):
        if isinstance(id, int):
            return super().pega(id)

    def remove(self, id: int):
        if isinstance(id, int):
            super().remove(id)

    def pega_todos(self):
        return super().pega_todos()
    
    def adicionar_lixo(self, coleta: Coleta, lixo):
        return coleta.adicionar_lixo(lixo)
    
    def remover_lixo(self, coleta: Coleta, lixo):
        return coleta.remover_lixo(lixo)