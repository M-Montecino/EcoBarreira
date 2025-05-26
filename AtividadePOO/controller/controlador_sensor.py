from model.sensor import Sensor
from view.tela_sensor import TelaSensor

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.controlador_controladores import ControladorControladores


class ControladorSensor():
    def __init__(self, controlador_sistema: "ControladorControladores"):
        self.__sensores = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_sensor = TelaSensor()

    def cadastrar_sensor(self):
        dados_sensor = self.__tela_sensor.pega_dados_sensor()
        novo_sensor = Sensor(
            dados_sensor["codigo"],
            dados_sensor["tipo"],
            dados_sensor["ativo"]
        )

        for sensor in self.__sensores:
            if sensor.codigo == novo_sensor.codigo:
                self.__tela_sensor.mostra_mensagem(
                    "Atenção! Esse sensor já existe")
                return

        self.__sensores.append(novo_sensor)
        self.__tela_sensor.mostra_mensagem("Sensor criado com sucesso!")
        return

    def buscar_sensor_por_codigo(self, codigo: int):
        for sensor in self.__sensores:
            if sensor.codigo == codigo:
                return sensor
        return None

    def altera_sensor(self):
        self.listar_sensores()
        codigo = self.__tela_sensor.busca_sensor()
        sensor = self.buscar_sensor_por_codigo(codigo)

        if sensor:
            novos_dados = self.__tela_sensor.pega_dados_sensor()
            sensor.codigo = novos_dados["codigo"]
            sensor.tipo = novos_dados["tipo"]
            sensor.ativo = novos_dados["ativo"]
            self.__tela_sensor.mostra_mensagem("Sensor alterado com sucesso!")
        else:
            self.__tela_sensor.mostra_mensagem("Sensor não encontrado.")

    def excluir_sensor(self):
        self.listar_sensores()
        codigo = self.__tela_sensor.busca_sensor()
        sensor = self.buscar_sensor_por_codigo(codigo)

        if sensor:
            self.__sensores.remove(sensor)
            self.__tela_sensor.mostra_mensagem("Sensor removido com sucesso.")
        else:
            self.__tela_sensor.mostra_mensagem("Sensor não encontrado.")

    def listar_sensores(self):
        for sensor in self.__sensores:
            self.__tela_sensor.mostra_sensor({
                "codigo": sensor.codigo,
                "tipo": sensor.tipo,
                "ativo": sensor.ativo
            })

    def busca_e_mostra_sensor(self):
        print(">>>Busca e mostra sensor foi chamada<<<")
        codigo = self.__tela_sensor.busca_sensor()
        sensor = self.buscar_sensor_por_codigo(codigo)
        if sensor:
            self.__tela_sensor.mostra_sensor({
                "codigo": sensor.codigo,
                "tipo": sensor.tipo,
                "ativo": sensor.ativo
            })
        else:
            self.__tela_sensor.mostra_mensagem("Sensor não encontrado.")

    def retomar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_sensor,
            2: self.busca_e_mostra_sensor,
            3: self.altera_sensor,
            4: self.excluir_sensor,
            5: self.listar_sensores,
            0: self.retomar
        }

        while True:
            try:
                opcao_escolhida = self.__tela_sensor.tela_opcoes()
                funcao_escolhida = lista_opcoes.get(opcao_escolhida)
                if funcao_escolhida:
                    funcao_escolhida()
                else:
                    self.__tela_sensor.mostra_mensagem(
                        "Opção inválida. Tente novamente.")
            except Exception as e:
                self.__tela_sensor.mostra_mensagem(
                    f"Comando inesperado: {str(e)}")
