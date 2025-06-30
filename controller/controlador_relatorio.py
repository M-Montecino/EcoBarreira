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
        colaborador = self.__controlador_sistema.controlador_colaborador.buscar_colaborador_por_cpf(cpf)
        coletas = self.__controlador_sistema.controlador_coleta.get_coletas()

        if not colaborador:
            self.__tela_relatorio.mostra_mensagem("Colaborador não encontrado.")
            return

        dados = self.__relatorio.gerar_relatorio_colaborador(colaborador, coletas)
        msg = (
            f"Nome: {dados['nome']}\n"
            f"CPF: {dados['cpf']}\n"
            f"Total de coletas: {dados['total_coletas']}\n"
            f"Total de lixo coletado: {dados['total_lixo']} kg"
        )
        self.__tela_relatorio.mostra_mensagem(msg)

    def relatorio_ecobarreira(self):
        codigo = self.__tela_relatorio.pega_codigo_ecobarreira()
        ecobarreira = self.__controlador_sistema.controlador_ecobarreira.buscar_ecobarreira_por_codigo(codigo)
        coletas = self.__controlador_sistema.controlador_coleta.get_coletas()

        if not ecobarreira:
            self.__tela_relatorio.mostra_mensagem("Ecobarreira não encontrada.")
            return

        dados = self.__relatorio.gerar_relatorio_ecobarreira(ecobarreira, coletas)
        msg = (
            f"Cidade: {dados['cidade']}\n"
            f"Código: {dados['codigo']}\n"
            f"Total de coletas: {dados['total_coletas']}\n"
            f"Total de lixo coletado: {dados['total_lixo']} kg"
        )
        self.__tela_relatorio.mostra_mensagem(msg)

    def exibir_melhor_colaborador(self):
        colaboradores = self.__controlador_sistema.controlador_colaborador.get_colaboradores()
        coletas = self.__controlador_sistema.controlador_coleta.get_coletas()

        resultado = self.__relatorio.melhor_colaborador(colaboradores, coletas)

        if resultado:
            msg = (
                f"Melhor colaborador:\n"
                f"Nome: {resultado['nome']}\n"
                f"CPF: {resultado['cpf']}\n"
                f"Total de lixo: {resultado['total_lixo']} kg"
            )
        else:
            msg = "Nenhum colaborador encontrado."

        self.__tela_relatorio.mostra_mensagem(msg)

    def exibir_melhor_ecobarreira(self):
        ecobarreiras = self.__controlador_sistema.controlador_ecobarreira.get_ecobarreiras()
        coletas = self.__controlador_sistema.controlador_coleta.get_coletas()

        resultado = self.__relatorio.melhor_ecobarreira(ecobarreiras, coletas)

        if resultado:
            msg = (
                f"Melhor ecobarreira:\n"
                f"Cidade: {resultado['cidade']}\n"
                f"Código: {resultado['codigo']}\n"
                f"Total de lixo: {resultado['total_lixo']} kg"
            )
        else:
            msg = "Nenhuma ecobarreira encontrada."

        self.__tela_relatorio.mostra_mensagem(msg)

    def lixo_total(self):
        coletas = self.__controlador_sistema.controlador_coleta.get_coletas()
        total = self.__relatorio.lixo_total(coletas)
        self.__tela_relatorio.mostra_mensagem(f"Lixo total coletado: {total} kg.")

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
                    self.__tela_relatorio.mostra_mensagem("Opção inválida. Tente novamente.")
            except Exception as e:
                self.__tela_relatorio.mostra_mensagem(f"Comando inesperado: {str(e)}")
