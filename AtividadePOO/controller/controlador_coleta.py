from model.coleta import Coleta
from view.tela_coleta import TelaColeta
from model.lixo import *
from datetime import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.controlador_controladores import ControladorControladores


class ControladorColeta:
    def __init__(self, controlador_sistema: "ControladorControladores"):
        self.__coletas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_coleta = TelaColeta()

    def cadastrar_coleta(self):
        dados = self.__tela_coleta.pega_dados_coleta()

        colaborador = self.__controlador_sistema.controlador_colaborador.buscar_colaborador_por_cpf(
            dados["cpf_colaborador"]
        )
        ecobarreira = self.__controlador_sistema.controlador_ecobarreira.buscar_ecobarreira_por_codigo(
            dados["codigo_ecobarreira"]
        )

        if not colaborador:
            self.__tela_coleta.mostra_mensagem("Colaborador não encontrado.")
            return
        if not ecobarreira:
            self.__tela_coleta.mostra_mensagem("Ecobarreira não encontrada.")
            return

        nova = Coleta(
            data=dados["data"],
            quantidade=dados["quantidade"],
            tipo=dados["tipo"],
            colaborador=colaborador,
            ecobarreira=ecobarreira
        )
        self.__coletas.append(nova)
        self.__tela_coleta.mostra_mensagem(
            "Nova coleta cadastrada com sucesso!")

    def buscar_coleta_por_id(self, id: int):
        for coleta in self.__coletas:
            if coleta.id == id:
                return coleta
        return None

    def altera_coleta(self):
        self.listar_coleta()
        id_coleta = self.__tela_coleta.busca_coleta()
        coleta = self.buscar_coleta_por_id(id_coleta)

        if coleta:
            dados_coleta = self.__tela_coleta.pega_dados_coleta()

            colaborador = self.__controlador_sistema.controlador_colaborador.buscar_colaborador_por_cpf(
                dados_coleta["cpf_colaborador"]
            )
            if not colaborador:
                self.__tela_coleta.mostra_mensagem(
                    "Colaborador não encontrado.")
                return

            ecobarreira = self.__controlador_sistema.controlador_ecobarreira.buscar_ecobarreira_por_codigo(
                dados_coleta["barreira"]
            )
            if not ecobarreira:
                self.__tela_coleta.mostra_mensagem(
                    "Ecobarreira não encontrada.")
                return

            coleta.data = dados_coleta["data"]
            coleta.quantidade = dados_coleta["quantidade"]
            coleta.tipo = dados_coleta["tipo"]
            coleta.colaborador = colaborador
            coleta.ecobarreira = ecobarreira
            self.__tela_coleta.mostra_mensagem("Coleta alterada com sucesso!")
        else:
            self.__tela_coleta.mostra_mensagem("Coleta não encontrada.")

    def excluir_coleta(self, id=None):
        self.listar_coleta()
        id = self.__tela_coleta.busca_coleta()
        coleta = self.buscar_coleta_por_id(id)

        if coleta:
            self.__coletas.remove(coleta)
            self.__tela_coleta.mostra_mensagem("Coleta excluída com sucesso!")
        else:
            self.__tela_coleta.mostra_mensagem("Coleta não encontrada.")

    def listar_coleta(self):
        for coleta in self.__coletas:
            self.__tela_coleta.mostra_coleta({
                "ID": coleta.id,
                "Data": coleta.data,
                "Colaborador": coleta.colaborador.nome,
                "Barreira": coleta.ecobarreira.nome
            })

    def buscar_e_mostrar_coleta(self):
        id = self.__tela_coleta.busca_coleta()
        coleta = self.buscar_coleta_por_id(id)
        if coleta:
            self.__tela_coleta.mostra_coleta({
                "ID": coleta.id,
                "Data": coleta.data,
                "Colaborador": coleta.colaborador.nome,
                "Barreira": coleta.ecobarreira.nome
            })
        else:
            self.__tela_coleta.mostra_mensagem("Coleta não encontrada.")

    def adicionar_lixo(self):
        dados_lixo = self.__tela_coleta.pega_dados_lixo()

        codigo_coleta = dados_lixo["codigo"]
        tipo = dados_lixo["tipo"]
        quantidade = dados_lixo["quantidade"]

        coleta = self.buscar_coleta_por_id(codigo_coleta)
        if coleta is None:
            self.__tela_coleta.mostra_mensagem("Coleta não encontrada!")
            return

        if tipo.lower() == ("plastico", "plástico"):
            lixo = Plastico(quantidade)

        elif tipo.lower() == "vidro":
            lixo = Vidro(quantidade)

        elif tipo.lower() == "metal":
            lixo = Metal(quantidade)

        elif tipo.lower() == "borracha":
            lixo = Borracha(quantidade)

        elif tipo.lower() == "organico":
            lixo = Organico(quantidade)

        elif tipo.lower() == "outros":
            lixo = Outros(quantidade)

        else:
            self.__tela_coleta.mostra_mensagem("Tipo não encontrado!")
            return

        coleta.lixos.append(lixo)
        self.__tela_coleta.mostra_mensagem("Lixo adicionado com sucesso!")

    def mostrar_lixos(self):
        codigo_coleta = self.__tela_coleta.busca_coleta()
        coleta = self.buscar_coleta_por_codigo(codigo_coleta)

        if coleta is None:
            self.__tela_coleta.mostra_mensagem("Coleta não encontrada!")
            return

        if not coleta.lixos:
            self.__tela_coleta.mostra_mensagem(
                "Nenhum lixo registrado nessa coleta.")
            return

        for i, lixo in enumerate(coleta.lixos, start=1):
            tipo = lixo.__class__.__name__
            self.__tela_coleta.mostra_mensagem(
                f"{i}) {tipo} - {lixo.quantidade} kg")

    def excluir_lixo(self):
        id = self.__tela_coleta.pega_codigo_coleta()
        coleta = self.buscar_coleta_por_id(id)

        if not coleta:
            self.__tela_coleta.mostra_mensagem("Coleta não encontrada!")
            return

        if not coleta.lixos:
            self.__tela_coleta.mostra_mensagem(
                "Nenhum lixo cadastrado nesta coleta.")
            return

        for i, lixo in enumerate(coleta.lixos, start=1):
            tipo = lixo.__class__.__name__
            self.__tela_coleta.mostra_mensagem(
                f"{i}) {tipo} - {lixo.quantidade} kg")

        indice = self.__tela_coleta.pega_indice_lixo()
        indice_real = indice - 1

        if 0 <= indice_real < len(coleta.lixos):
            removido = coleta.lixos.pop(indice_real)
            tipo_removido = removido.__class__.__name__
            self.__tela_coleta.mostra_mensagem(
                f"{tipo_removido} removido com sucesso.")
        else:
            self.__tela_coleta.mostra_mensagem(
                "Número inválido. Tente novamente.")

    def retomar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_coleta,
            2: self.buscar_e_mostrar_coleta,
            3: self.altera_coleta,
            4: self.excluir_coleta,
            5: self.listar_coleta,
            6: self.adicionar_lixo,
            7: self.excluir_lixo,
            8: self.mostrar_lixos,
            0: self.retomar
        }

        while True:
            try:
                opcao_escolhida = self.__tela_coleta.tela_opcoes()
                funcao_escolhida = lista_opcoes.get(opcao_escolhida)
                if funcao_escolhida:
                    funcao_escolhida()
                else:
                    self.__tela_coleta.mostra_mensagem(
                        "Opção inválida. Tente novamente")
            except Exception as e:
                self.__tela_coleta.mostra_mensagem(
                    f"Comando inesperado: {str(e)}")

    def get_coletas(self):
        return self.__coletas
