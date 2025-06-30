from view.tela_controlador import TelaControlador
from controller.controlador_sensor import ControladorSensor
from controller.controlador_ecobarreira import ControladorEcoBarreira
from controller.controlador_colaborador import ControladorColaborador
from controller.controlador_coleta import ControladorColeta
from controller.controlador_relatorio import ControladorRelatorio


class ControladorControladores:
    def __init__(self):
        self.__controlador_sensor = ControladorSensor(self)
        self.__controlador_ecobarreira = ControladorEcoBarreira(self)
        self.__controlador_colaborador = ControladorColaborador(self)
        self.__controlador_coleta = ControladorColeta(self)
        self.__controlador_relatorio = ControladorRelatorio(self)
        self.__tela_controlador = TelaControlador()

    @property
    def controlador_sensor(self):
        return self.__controlador_sensor

    @property
    def controlador_ecobarreira(self):
        return self.__controlador_ecobarreira

    @property
    def controlador_colaborador(self):
        return self.__controlador_colaborador

    @property
    def controlador_coleta(self):
        return self.__controlador_coleta

    @property
    def controlador_relatorio(self):
        return self.controlador_relatorio

    @property
    def tela_controlador(self):
        return self.__tela_controlador

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_sensor(self):
        self.__controlador_sensor.abre_tela()

    def cadastra_ecobarreira(self):
        self.__controlador_ecobarreira.abre_tela()

    def cadastra_colaborador(self):
        self.__controlador_colaborador.abre_tela()

    def cadastra_coleta(self):
        self.__controlador_coleta.abre_tela()

    def cadastra_relatorio(self):
        self.__controlador_relatorio.abre_tela()

    def encerra_sistema(self):
        self.__tela_controlador.mostra_mensagem("Programa falhou com sucesso!")
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastra_colaborador,
            2: self.cadastra_ecobarreira,
            3: self.cadastra_coleta,
            4: self.cadastra_sensor,
            5: self.cadastra_relatorio,
            0: self.encerra_sistema
        }

        while True:
            try:
                opcao_escolhida = self.__tela_controlador.tela_opcoes()
                funcao_escolhida = lista_opcoes.get(opcao_escolhida)
                if funcao_escolhida:
                    funcao_escolhida()
                else:
                    self.__tela_controlador.mostra_mensagem(
                        "Opção inválida. Tente novamente.")
            except Exception as e:
                self.__tela_controlador.mostra_mensagem(
                    f"Comando inesperado: {str(e)}")
