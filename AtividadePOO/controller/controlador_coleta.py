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
        dados_coleta = self.__tela_coleta.pega_dados_coleta()

        if self.buscar_coleta_por_id(dados_coleta["id"]):
            self.__tela_coleta.mostra_mensagem("Essa coleta já existe.")
            return

        try:
            data = datetime.strptime(dados_coleta["data"], "%d/%m/%Y")
        except ValueError:
            self.__tela_coleta.mostra_mensagem(
                "Data inválida. Use o formato DD/MM/AAAA.")
            return

        colaborador = self.__controlador_sistema.controlador_colaborador.\
            buscar_colaborador_por_cpf(dados_coleta["cpf_colaborador"])
        if colaborador is None:
            self.__tela_coleta.mostra_mensagem("Colaborador não encontrado.")
            return

        ecobarreira = self.__controlador_sistema.controlador_ecobarreira.\
            buscar_ecobarreira_por_codigo(dados_coleta["codigo_ecobarreira"])
        if ecobarreira is None:
            self.__tela_coleta.mostra_mensagem("Ecobarreira não encontrada.")
            return

        nova_coleta = Coleta(
            dados_coleta["id"],
            data,
            ecobarreira,
            colaborador
        )

        self.__coletas.append(nova_coleta)
        self.__tela_coleta.mostra_mensagem("Coleta registrada com sucesso!")

    def buscar_coleta_por_id(self, id: int):
        for coleta in self.__coletas:
            if coleta.id == id:
                self.__tela_coleta.mostra_mensagem("Coleta encontrada!")
                return coleta
        self.__tela_coleta.mostra_mensagem("Coleta não encontrada!")
        return None

    def altera_coleta(self):
        self.listar_coleta()
        id_coleta = self.__tela_coleta.buscar_coleta()
        coleta = self.buscar_coleta_por_id(id_coleta)

        if coleta:
            dados_coleta = self.__tela_coleta.pega_dados_coleta()

            colaborador = self.buscar_colaborador_por_cpf(
                dados_coleta["cpf_colaborador"])
            if not colaborador:
                self.__tela_coleta.mostra_mensagem(
                    "Colaborador não encontrado.")
                return

            ecobarreira = self.buscar_ecobarreira_por_codigo(
                dados_coleta["codigo_ecobarreira"])
            if not ecobarreira:
                self.__tela_coleta.mostra_mensagem(
                    "Ecobarreira não encontrada.")
                return

            coleta.id = dados_coleta["id"]
            coleta.data = dados_coleta["data"]
            coleta.ecobarreira = ecobarreira
            self.__tela_coleta.mostra_mensagem("Coleta alterada com sucesso!")
        else:
            self.__tela_coleta.mostra_mensagem("Coleta não encontrada.")

    def excluir_coleta(self, id: int):
        self.listar_coleta()
        id = self.__tela_coleta.buscar_coleta()
        coleta = self.buscar_coleta_por_id(id)

        if coleta is not None:
            self.__coletas.remove(coleta)
            self.listar_coleta()
            self.__tela_coleta.mostra_mensagem("Coleta excluida com sucesso!")
        else:
            self.__tela_coleta.mostra_mensagem(
                "Atenção! essa coleta não existe")

    def listar_coleta(self):
        for coleta in self.__coletas:
            self.__tela_coleta.mostra_coleta({
                "ID": coleta.id,
                "Data": coleta.data,
                "Colaborador": coleta.colaborador.nome,
                "Barreira": coleta.eco_barreira.nome
            })

    def adicionar_lixo(self):
        dados_lixo = self.__tela_coleta.pega_dados_lixo()

        codigo_coleta = dados_lixo["codigo_coleta"]
        tipo = dados_lixo["tipo"]
        quantidade = dados_lixo["quantidade"]

        coleta = self.buscar_coleta_por_codigo(codigo_coleta)
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

        for idx, lixo in enumerate(coleta.lixos, start=1):
            self.__tela_coleta.mostra_mensagem(
                f"{idx}. Tipo: {type(lixo).__name__}, Quantidade: {lixo.quantidade}"
            )

    def excluir_lixo(self):
        codigo = self.__tela_coleta.pega_codigo_coleta()
        coleta = self.buscar_coleta_por_codigo(codigo)

        if coleta is None:
            self.__tela_coleta.mostra_mensagem("Coleta não encontrada!")
            return

        if not coleta.lixos:
            self.__tela_coleta.mostra_mensagem(
                "Nenhum lixo cadastrado nesta coleta.")
            return

        for i, lixo in enumerate(coleta.lixos):
            self.__tela_coleta.mostra_mensagem(
                f"{i}: Tipo: {type(lixo).__name__}, Quantidade: {lixo.quantidade}")

        indice = self.__tela_coleta.pega_indice_lixo()

        if 0 <= indice < len(coleta.lixos):
            removido = coleta.lixos.pop(indice)
            self.__tela_coleta.mostra_mensagem(
                f"{type(removido).__name__} removido com sucesso.")
        else:
            self.__tela_coleta.mostra_mensagem("Índice inválido.")

    def retomar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_coleta,
            2: self.buscar_coleta_por_id,
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
