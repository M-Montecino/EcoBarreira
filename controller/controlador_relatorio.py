from model.relatorio import Relatorio
from view.tela_relatorio import TelaRelatorio
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.controlador_controladores import ControladorControladores


class ControladorRelatorio:
    def __init__(self, controlador_sistema: "ControladorControladores"):
        self.__controlador_sistema = controlador_sistema
        self.__tela_relatorio = TelaRelatorio()
        self.__relatorio = Relatorio()

    def relatorio_colaborador(self):
        cpf = self.__tela_relatorio.pega_cpf_colaborador()
        colaborador = self.__controlador_sistema.controlador_colaborador.buscar_colaborador_por_cpf(
            cpf)
        coletas = self.__controlador_sistema.controlador_coleta.get_coletas()

        if not colaborador:
            self.__tela_relatorio.mostra_mensagem(
                "Colaborador não encontrado.")
            return

        total = self.__relatorio.relatorio_colaborador(colaborador, coletas)
        self.__tela_relatorio.mostra_mensagem(
            f"{colaborador.nome} coletou {total} kg de lixo.")

    def relatorio_ecobarreira(self):
        codigo = self.__tela_relatorio.pega_codigo_ecobarreira()
        ecobarreira = self.__controlador_sistema.controlador_ecobarreira.buscar_ecobarreira_por_codigo(
            codigo)

        if not ecobarreira:
            self.__tela_relatorio.mostra_mensagem(
                "Ecobarreira não encontrada.")
            return

        coletas = [
            coleta for coleta in self.__controlador_sistema.controlador_coleta.lista_coletas
            if coleta.ecobarreira.codigo == codigo
        ]

        if not coletas:
            self.__tela_relatorio.mostra_mensagem(
                "Nenhuma coleta registrada para essa ecobarreira.")
            return

        for coleta in coletas:
            total = sum(lixo.quantidade for lixo in coleta.lixos)
            detalhes = [
                {"Tipo": type(l).__name__, "Quantidade": l.quantidade} for l in coleta.lixos]
            self.__tela_relatorio.mostra_mensagem({
                "Colaborador": coleta.colaborador.nome,
                "Código da Coleta": coleta.codigo,
                "Total de lixo (kg)": total,
                "Detalhes": detalhes
            })

    def exibir_melhor_colaborador(self):
        colaboradores = self.__controlador_sistema.controlador_colaborador.get_colaboradores()
        coletas = self.__controlador_sistema.controlador_coleta.get_coletas()

        melhor = None
        maior_total = 0

        for colaborador in colaboradores:
            total = sum(
                sum(lixo.quantidade for lixo in coleta.lixos)
                for coleta in coletas if coleta.colaborador == colaborador
            )
            if total > maior_total:
                maior_total = total
                melhor = colaborador

        if melhor:
            self.__tela_relatorio.mostra_mensagem(
                f"Melhor colaborador: {melhor.nome} - {maior_total} kg coletados.")
        else:
            self.__tela_relatorio.mostra_mensagem(
                "Nenhum colaborador encontrado.")

    def exibir_melhor_ecobarreira(self):
        ecobarreiras = self.__controlador_sistema.controlador_ecobarreira.get_ecobarreiras()
        coletas = self.__controlador_sistema.controlador_coleta.get_coletas()

        melhor = None
        maior_total = 0

        for ecobarreira in ecobarreiras:
            total = sum(
                sum(lixo.quantidade for lixo in coleta.lixos)
                for coleta in coletas if coleta.ecobarreira == ecobarreira
            )
            if total > maior_total:
                maior_total = total
                melhor = ecobarreira

        if melhor:
            self.__tela_relatorio.mostra_mensagem(
                f"Melhor ecobarreira: {melhor.cidade} - {maior_total} kg coletados.")
        else:
            self.__tela_relatorio.mostra_mensagem(
                "Nenhuma ecobarreira encontrada.")

    def lixo_total(self):
        coletas = self.__controlador_sistema.controlador_coleta.get_coletas()
        total = self.__relatorio.lixo_total(coletas)
        self.__tela_relatorio.mostra_mensagem(
            f"Lixo total coletado: {total} kg.")

    def retomar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.relatorio_colaborador,
            2: self.relatorio_ecobarreira,
            3: self.exibir_melhor_colaborador,
            4: self.exibir_melhor_ecobarreira,
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
