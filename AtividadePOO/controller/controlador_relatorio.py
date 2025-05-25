from model.relatorio import Relatorio
from view.tela_relatorio import TelaRelatorio
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.controlador_controladores import ControladorControladores


class ControladorRelatorio:
    def __init__(self, controlador_sistema: ControladorControladores):
        self.__controlador_sistema = controlador_sistema
        self.__tela_relatorio = TelaRelatorio()

    def relatorio_colaborador(self):
        cpf = self.__tela_relatorio.pega_cpf_colaborador()
        colaborador = self.__controlador_sistema.controlador_colaborador.buscar_colaborador_por_cpf(
            cpf)
        coletas = self.__controlador_sistema.controlador_coleta.lista_coletas

        if colaborador is None:
            self.__tela_relatorio.mostra_mensagem(
                "Colaborador não encontrado.")
            return

        total = self.__relatorio.relatorio_colaborador(colaborador, coletas)
        self.__tela_relatorio.mostra_mensagem(
            f"Total de lixo coletado pelo colaborador {colaborador.nome}: {total} kg")

    def relatorio_ecobarreira(self):
        codigo = self.__tela_relatorio.pega_codigo_ecobarreira()
        ecobarreira = self.__controlador_sistema.controlador_ecobarreira.buscar_ecobarreira_por_codigo(
            codigo)

        if ecobarreira is None:
            self.__tela_relatorio.mostra_mensagem(
                "Ecobarreira não encontrada.")
            return

        coletas = self.__controlador_sistema.controlador_coleta.lista_coletas
        coletas_da_barreira = [
            coleta for coleta in coletas if coleta.ecobarreira.codigo == codigo
        ]

        if not coletas_da_barreira:
            self.__tela_relatorio.mostra_mensagem(
                "Nenhuma coleta registrada para essa ecobarreira.")
            return

        for coleta in coletas_da_barreira:
            total_lixo = sum(lixo.quantidade for lixo in coleta.lixos)
            self.__tela_relatorio.mostra_mensagem({
                "Colaborador": coleta.colaborador.nome,
                "Código da Coleta": coleta.codigo,
                "Total de lixo (kg)": total_lixo,
                "Detalhes": [
                    {"Tipo": type(lixo).__name__,
                     "Quantidade": lixo.quantidade}
                    for lixo in coleta.lixos
                ]
            })

    def melhor_colaborador(self, lista_colaboradores, lista_coletas):
        melhor = None
        maior_lixo = -1

        for colaborador in lista_colaboradores:
            total = 0
            for coleta in lista_coletas:
                if coleta.colaborador == colaborador:
                    total += sum(lixo.quantidade for lixo in coleta.lixos)
            if total > maior_lixo:
                maior_lixo = total
                melhor = colaborador

        if melhor:
            return {
                "nome": melhor.nome,
                "cpf": melhor.cpf,
                "total_lixo": maior_lixo
            }
        return None

    def melhor_ecobarreira(self, lista_ecobarreiras, lista_coletas):
        melhor = None
        maior_lixo = -1

        for ecobarreira in lista_ecobarreiras:
            total = 0
            for coleta in lista_coletas:
                if coleta.ecobarreira == ecobarreira:
                    total += sum(lixo.quantidade for lixo in coleta.lixos)
            if total > maior_lixo:
                maior_lixo = total
                melhor = ecobarreira

        if melhor:
            return {
                "codigo": melhor.codigo,
                "cidade": melhor.cidade,
                "total_lixo": maior_lixo
            }
        return None

    def lixo_total(self):
        coletas = self.__controlador_sistema.controlador_coleta.lista_coletas
        total = self.__relatorio.lixo_total(coletas)
        self.__tela_relatorio.mostra_mensagem(
            f"Lixo total coletado: {total} kg")

    def retomar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.relatorio_colaborador,
            2: self.relatorio_ecobarreira,
            3: self.melhor_colaborador,
            4: self.melhor_ecobarreira,
            5: self.lixo_total,
            0: self.retomar
        }

        while True:
            try:
                opcao_escolhida = self.__tela_relatorio.tela_opcoes()
                funcao_escolhida = lista_opcoes.get(opcao_escolhida)
                if funcao_escolhida:
                    funcao_escolhida()
                else:
                    self.__tela_relatorio.mostra_mensagem(
                        "Opção inválida. Tente novamente")
            except Exception as e:
                self.__tela_relatorio.mostra_mensagem(
                    f"Comando inesperado: {str(e)}")
