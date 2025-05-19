from model.coleta import Coleta
from model.colaborador import Colaborador
from model.ecobarreira import EcoBarreira
from datetime import datetime


class ControladorColeta:
    def __init__(self):
        self.__coletas = []

    @property
    def coletas(self) -> list:
        return self.__coletas

    def cadastrar_coleta(self, id: int, data: datetime, ecobarreira: EcoBarreira, colaborador: Colaborador, lixos: list) -> Coleta:
        for coleta in self.__coletas:
            if coleta.id == id:
                return coleta
        if isinstance(id, int) and isinstance(data, datetime) and\
                isinstance(ecobarreira, EcoBarreira) and isinstance(colaborador, Colaborador) \
                and isinstance(lixos, list):
            nova_coleta = Coleta(id, data, ecobarreira, colaborador, lixos)
            self.__coletas.append(nova_coleta)
            return nova_coleta

    def buscar_coleta_por_id(self, id_coleta: int):
        for coleta in self.__coletas:
            if coleta.id == id_coleta:
                return coleta
        return None

    def altera_coleta(self, id_coleta=int,
                      nova_data: datetime = None,
                      nova_ecobarreira: EcoBarreira = None,
                      novo_colaborador: Colaborador = None,
                      novos_lixos: list = None
                      ):

        coleta = self.buscar_coleta_por_id(id_coleta)

        if coleta is None:
            return None

        if nova_data:
            if isinstance(nova_data, datetime):
                coleta.data = nova_data

        if nova_ecobarreira:
            if isinstance(nova_ecobarreira, EcoBarreira):
                coleta.ecobarreira = nova_ecobarreira

        if novo_colaborador:
            if isinstance(novo_colaborador, Colaborador):
                coleta.colaborador = novo_colaborador

        else:
            if isinstance(novos_lixos, list):
                coleta.lixos = novos_lixos

    def excluir_coleta(self, id_coleta: int):
        coleta = self.buscar_coleta_por_id(id_coleta)
        if coleta in self.__coletas:
            self.__coleta.remove(coleta)
            return coleta
        else:
            return None

    def listar_coletas(self):
        if not self.__coletas:
            return None
        else: 
            for coleta in self.__coletas:
                print(f" ID: {coleta.id}, Data: {coleta.data}, "
                f"Colaborador: {coleta.colaborador.nome}, "
                f"Barreira: {coleta.eco_barreira.nome}")
