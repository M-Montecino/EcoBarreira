from model.coleta import Coleta
from model.colaborador import Colaborador
from model.ecobarreira import EcoBarreira
from view.tela_coleta import TelaColeta
from datetime import datetime


class ControladorColeta:
    def __init__(self, controlador_sistema):
        self.__coletas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_coleta = TelaColeta()

    def cadastrar_coleta(self):
        dados_coleta = self.__tela_coleta.pega_dados_coleta()
        nova_coleta = Coleta(dados_coleta["id"],
                             dados_coleta["data"],
                             dados_coleta["ecobarreira"],
                             dados_coleta["colaborador"]
                             )
        for coleta in self.__coletas:
            if coleta.id == nova_coleta.id:
                self.__tela_coleta.mostra_mensagem(
                    "Atenção! Essa coleta já existe")
                return
        self.__coletas.append(nova_coleta)
        self.__tela_coleta.mostra_mensagem("Coleta criada com sucesso!")
        return

    def buscar_coleta_por_id(self, id: int):
        for coleta in self.__coletas:
            if coleta.id == id:
                self.__tela_coleta.mostra_mensagem("Coleta encontrada!")
                return coleta
        self.__tela_coleta.mostra_mensagem("Coleta não encontrada!")
        return None

    def altera_coleta(self):
        self.listar_coletas()
        id_coleta = self.__tela_coleta.buscar_coleta()
        coleta = self.buscar_coleta_por_id(id_coleta)

        if coleta is not None:
            novos_dados_coleta = self.__tela_coleta.pega_dados_coleta()
            coleta.id = novos_dados_coleta["id"]
            coleta.data = novos_dados_coleta["data"]
            coleta.ecobarreira = novos_dados_coleta["ecobarreira"]
            coleta.colaborador = novos_dados_coleta["colaborador"]
            self.listar_coletas()
            self.__tela_coleta.mostra_mensagem("Coleta alterada com sucesso!")
        else:
            self.__tela_coleta.mostra_mensagem(
                "Atenção! essa coleta não existe")

    def excluir_coleta(self, id: int):
        self.listar_coletas()
        id = self.__tela_coleta.buscar_coleta()
        coleta = self.buscar_coleta_por_id(id)

        if coleta is not None:
            self.__coletas.remove(coleta)
            self.listar_coletas()
            self.__tela_coleta.mostra_mensagem("Coleta excluida com sucesso!")
        else:
            self.__tela_coleta.mostra_mensagem(
                "Atenção! essa coleta não existe")

    def listar_coletas(self):
        for coleta in self.__coletas:
            self.__tela_coleta.mostra_coleta({"ID": coleta.id,
                                              "Data": coleta.data,
                                              "Colaborador": coleta.colaborador.nome,
                                              "Barreira": coleta.eco_barreira.nome
                                              })

    def retomar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_coleta, 2: self.buscar_coleta_por_id,
                        3: self.altera_coleta, 4: self.excluir_coleta,
                        5: self.listar_coletas}

    continua = True
    while continua:
        lista_opcoes[self.__tela_coleta.tela_opcoes()]()
