from model.coleta import Coleta
from view.tela_coleta import TelaColeta
from model.lixo import *
from datetime import datetime


class ControladorColeta:
    def __init__(self, controlador_sistema):
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
        self.listar_coletas()
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
            self.__tela_coleta.mostra_coleta({
                "ID": coleta.id,
                "Data": coleta.data,
                "Colaborador": coleta.colaborador.nome,
                "Barreira": coleta.eco_barreira.nome
            })

    def adicionar_lixo(self):
        self.listar_coletas()
        dados = self.__tela_coleta.pega_dados_lixo()
        quantidade = dados["quantidade"]
        pseudo_tipo = dados["tipo_lixo"].lower

        if pseudo_tipo == "plastico" or "plástico":

    def retomar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_coleta,
            2: self.buscar_coleta_por_id,
            3: self.altera_coleta,
            4: self.excluir_coleta,
            5: self.listar_coleta,
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
