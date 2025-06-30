from model.sensor import Sensor
from daos.sensor_dao import SensorDAO
from view.tela_sensor import TelaSensor

from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.controlador_controladores import ControladorControladores


class ControladorSensor():
    def __init__(self, controlador_sistema: "ControladorControladores"):
        self.__sensore_dao = SensorDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_sensor = TelaSensor()

    def cadastrar_sensor(self):
        try:
            dados_sensor = self.__tela_sensor.pega_dados_sensor()
            if dados_sensor is None:
                return

            novo_sensor = Sensor(
                dados_sensor["codigo"],
                dados_sensor["tipo"],
                dados_sensor["ativo"]
            )

            for sensor in self.__sensore_dao.pega_todos():
                if sensor.codigo == novo_sensor.codigo:
                    raise ElementoRepetidoException()

            self.__sensore_dao.adiciona(novo_sensor)
            self.__tela_sensor.mostra_mensagem("Sensor adicionado com sucesso!")

        except ElementoRepetidoException as e:
            self.__tela_sensor.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_sensor.mostra_mensagem(f"Erro inesperado: {str(e)}")

    def buscar_sensor_por_codigo(self, codigo_input: int):
        try:
            codigo = int(codigo_input)
        except ValueError:
            self.__tela_sensor.mostra_mensagem("Código inválido")
            return None

        sensor = self.__sensore_dao.pega(codigo)
        if sensor is None:
            self.__tela_sensor.mostra_mensagem("Sensor não encontrado")
        return sensor

    def altera_sensor(self):
        try:
            codigo_input = self.__tela_sensor.busca_sensor()
            sensor = self.buscar_sensor_por_codigo(codigo_input)

            if sensor is None:
                raise ElementoNaoExisteException()

            codigo_antigo = sensor.codigo

            novos_dados = self.__tela_sensor.pega_dados_sensor()

            sensor.codigo = novos_dados["codigo"]
            sensor.tipo = novos_dados["tipo"]
            sensor.ativo = novos_dados["ativo"]

            self.__sensore_dao.remove(codigo_antigo)
            self.__sensore_dao.adiciona(sensor)

            self.__tela_sensor.mostra_mensagem("Sensor alterado com sucesso!")

        except ElementoNaoExisteException as e:
            self.__tela_sensor.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_sensor.mostra_mensagem(f"Erro inesperado: {str(e)}")

    def excluir_sensor(self):
        try:
            codigo_input = self.__tela_sensor.busca_sensor()
            codigo = int(codigo_input)
            sensor = self.buscar_sensor_por_codigo(codigo)

            if sensor is None:
                raise ElementoNaoExisteException()
            
            self.__sensore_dao.remove(codigo)
            self.__tela_sensor.mostra_mensagem("Sensor excluído com sucesso!")

        except ElementoNaoExisteException as e:
            self.__tela_sensor.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_sensor.mostra_mensagem(f"Erro inesperado: {str(e)}")

    def listar_sensores(self):
        try:
            sensores = self.__sensore_dao.pega_todos()
            if not sensores:
                self.__tela_sensor.mostra_mensagem("Nenhum sensor cadastrado.")
                return
            
            lista_dados = []
            for sensor in sensores:
                lista_dados.append({
                    "codigo": sensor.codigo,
                    "tipo": sensor.tipo,
                    "ativo": sensor.ativo
                })

            self.__tela_sensor.mostra_sensores(lista_dados)
        
        except Exception as e:
            self.__tela_sensor.mostra_mensagem(f"Erro ao listar colaboradores: {str(e)}")

    def busca_e_mostra_sensor(self):
        try:
            codigo = self.__tela_sensor.busca_sensor()
            sensor = self.buscar_sensor_por_codigo(codigo)

            if sensor is None:
                raise ElementoNaoExisteException()

            dados = {
                "codigo": sensor.codigo,
                "tipo": sensor.tipo,
                "ativo": "Sim" if sensor.ativo else "Não"
            }

            self.__tela_sensor.mostra_sensor(dados)

        except ElementoNaoExisteException as e:
            self.__tela_sensor.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_sensor.mostra_mensagem(f"Erro ao buscar sensor: {str(e)}")

    def get_sensores(self):
        return self.__sensore_dao.pega_todos()

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
