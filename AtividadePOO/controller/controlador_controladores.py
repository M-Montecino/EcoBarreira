from view.tela_controlador import TelaControlador
from controller.controlador_sensor import ControladorSensor


class ControladorControladores:
    def __init__(self):
        self.__controlador_sensor = ControladorSensor(self)
        self.__tela_controlador = TelaControlador()

    @property
    def controlador_sensor(self):
        return self.__controlador_sensor
    
    @property
    def tela_controlador(self):
        return self.__tela_controlador
    
    def inicializa_sistema(self):
        self.abre_tela()
    
    def cadastra_sensor(self):
        self.__controlador_sensor.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {4: self.cadastra_sensor, \
                        0: self.encerra_sistema}
    
        while True:
            opcao_escolhida = self.__tela_controlador.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()