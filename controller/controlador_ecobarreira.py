from model.ecobarreira import EcoBarreira
from view.tela_ecobarreira import TelaEcoBarreira
from daos.ecobarreira_dao import EcobarreiraDAO

from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.controlador_controladores import ControladorControladores


class ControladorEcoBarreira:
    def __init__(self, controlador_sistema: "ControladorControladores"):
        self.__ecobarreira_dao = EcobarreiraDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_ecobarreira = TelaEcoBarreira()

    def cadastrar_ecobarreira(self):
        try:
            dados_ecobarreira = self.__tela_ecobarreira.pega_dados_ecobarreira()
            if dados_ecobarreira is None:
                return
            
            nova_ecobarreira = EcoBarreira(
                dados_ecobarreira["codigo"],
                dados_ecobarreira["cidade"],
                dados_ecobarreira["cep"],
                dados_ecobarreira["rua"],
                dados_ecobarreira["complemento"],
                dados_ecobarreira["estado"]
            )

            for ecobarreira in self.__ecobarreira_dao.pega_todos():
                if ecobarreira.codigo == nova_ecobarreira.codigo:
                    raise ElementoRepetidoException()

            self.__ecobarreira_dao.adiciona(nova_ecobarreira)
            self.__tela_ecobarreira.mostra_mensagem("Ecobarreira adicionada com sucesso!")

        except ElementoRepetidoException as e:
            self.__tela_ecobarreira.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_ecobarreira.mostra_mensagem(f"Erro inesperado: {str(e)}")

    def buscar_ecobarreira_por_codigo(self, codigo_input: int):
        try:
            codigo = int(codigo_input)
        except ValueError:
            self.__tela_ecobarreira.mostra_mensagem("Código inválido")
            return None
        
        ecobarreira = self.__ecobarreira_dao.pega(codigo)
        if ecobarreira is None:
            self.__tela_ecobarreira.mostra_mensagem("Ecobarreira não encontrada")
        return ecobarreira

    def altera_ecobarreira(self):
        try:
            codigo = self.__tela_ecobarreira.busca_ecobarreira()
            ecobarreira = self.buscar_ecobarreira_por_codigo(codigo)

            if ecobarreira is None:
                raise ElementoNaoExisteException()

            codigo_antigo = ecobarreira.codigo

            novos_dados = self.__tela_ecobarreira.pega_dados_ecobarreira()

            ecobarreira.codigo = novos_dados["codigo"]
            ecobarreira.cidade = novos_dados["cidade"]
            ecobarreira.cep = novos_dados["cep"]
            ecobarreira.rua = novos_dados["rua"]
            ecobarreira.complemento = novos_dados["complemento"]
            ecobarreira.estado = novos_dados["estado"]

            self.__ecobarreira_dao.remove(codigo_antigo)
            self.__ecobarreira_dao.adiciona(ecobarreira)

            self.__tela_ecobarreira.mostra_mensagem("Dados atualizados com sucesso!")

        except ElementoNaoExisteException as e:
            self.__tela_ecobarreira.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_ecobarreira.mostra_mensagem(f"Erro inesperado: {str(e)}")

    def excluir_ecobarreira(self):
        try:
            codigo = self.__tela_ecobarreira.busca_ecobarreira()
            ecobarreira = self.buscar_ecobarreira_por_codigo(codigo)
            
            if ecobarreira is None:
                raise ElementoNaoExisteException()
            
            self.__ecobarreira_dao.remove(codigo)
            self.__tela_ecobarreira.mostra_mensagem("Ecobarreira excluida com sucesso!")
            self.listar_ecobarreiras()

        except ElementoNaoExisteException as e:
            self.__tela_ecobarreira.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_ecobarreira.mostra_mensagem(f"Erro inesperado ao excluir ecobarreira: {str(e)}")  

    def listar_ecobarreiras(self):
        try:
            ecobarreias = self.__ecobarreira_dao.pega_todos()
            if not ecobarreias:
                self.__tela_ecobarreira.mostra_mensagem("Nenhuma ecobarreira cadastrada.")
                
            lista_dados = []
            for e in self.__ecobarreiras:
                lista_dados.append({
                    "codigo": e.codigo,
                    "cidade": e.cidade,
                    "cep": e.cep,
                    "rua": e.rua,
                    "complemento": e.complemento,
                    "estado": e.estado,
                    "sensores": [s.codigo for s in e.sensores]
                })

            self.__tela_ecobarreira.mostra_ecobarreira(lista_dados)

        except Exception as e:
            self.__tela_ecobarreira.mostra_mensagem(f"Erro ao listar ecobarreiras: {str(e)}")

    def buscar_e_mostrar_ecobarreira(self):
        try:
            codigo = self.__tela_ecobarreira.busca_ecobarreira()
            ecobarreira = self.buscar_ecobarreira_por_codigo(codigo)

            if ecobarreira is None:
                raise ElementoNaoExisteException()
            
            dados = ({
                "codigo": ecobarreira.codigo,
                "cidade": ecobarreira.cidade,
                "cep": ecobarreira.cep,
                "rua": ecobarreira.rua,
                "complemento": ecobarreira.complemento,
                "estado": ecobarreira.estado,
                "sensores": ecobarreira.sensores
            })

            self.__tela_ecobarreira.mostra_ecobarreira(dados)

        except ElementoNaoExisteException as e:
            self.__tela_ecobarreira.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_ecobarreira.mostra_mensagem(f"Erro ao buscar ecobarreira: {str(e)}")    

    def adicionar_sensor(self):
        self.listar_ecobarreiras()
        codigo = self.__tela_ecobarreira.busca_ecobarreira()
        ecobarreira = self.buscar_ecobarreira_por_codigo(codigo)

        if not ecobarreira:
            self.__tela_ecobarreira.mostra_mensagem(
                "Ecobarreira não encontrada!")
            return

        codigo_sensor = self.__tela_ecobarreira.pega_codigo_sensor()
        sensor = self.__controlador_sistema.controlador_sensor.buscar_sensor_por_codigo(
            codigo_sensor)

        if sensor is None:
            self.__tela_ecobarreira.mostra_mensagem(
                "Sensor não encontrado!")
            return

        if sensor in ecobarreira.sensores:
            self.__tela_ecobarreira.mostra_mensagem(
                "Sensor já foi adicionado!")
        else:
            ecobarreira.sensores.append(sensor)
            self.__tela_ecobarreira.mostra_mensagem(
                "Sensor adicionado à ecobarreira!")

    def excluir_sensor(self):
        self.listar_ecobarreiras()
        codigo = self.__tela_ecobarreira.busca_ecobarreira()
        ecobarreira = self.buscar_ecobarreira_por_codigo(codigo)

        if not ecobarreira:
            self.__tela_ecobarreira.mostra_mensagem(
                "Ecobarreira não encontrada!")
            return

        codigo_sensor = self.__tela_ecobarreira.pega_codigo_sensor()
        sensor = self.__controlador_sistema.controlador_sensor.buscar_sensor_por_codigo(
            codigo_sensor)

        if not sensor:
            self.__tela_ecobarreira.mostra_mensagem("Sensor não encontrado!")
        elif sensor not in ecobarreira.sensores:
            self.__tela_ecobarreira.mostra_mensagem(
                "Sensor não está na ecobarreira!")
        else:
            ecobarreira.sensores.remove(sensor)
            self.__tela_ecobarreira.mostra_mensagem(
                "Sensor removido com sucesso!")

    def checar_sensores(self):
        codigo = self.__tela_ecobarreira.busca_ecobarreira()
        ecobarreira = self.buscar_ecobarreira_por_codigo(codigo)

        if not ecobarreira:
            self.__tela_ecobarreira.mostra_mensagem(
                "Ecobarreira não encontrada!")
        elif not ecobarreira.sensores:
            self.__tela_ecobarreira.mostra_mensagem("Nenhum sensor associado.")
        else:
            lista = [s.codigo for s in ecobarreira.sensores]
            self.__tela_ecobarreira.mostra_mensagem(f"Sensores: {lista}")

    def retomar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_ecobarreira,
            2: self.buscar_e_mostrar_ecobarreira,
            3: self.altera_ecobarreira,
            4: self.excluir_ecobarreira,
            5: self.listar_ecobarreiras,
            6: self.adicionar_sensor,
            7: self.excluir_sensor,
            8: self.checar_sensores,
            0: self.retomar
        }

        while True:
            try:
                opcao_escolhida = self.__tela_ecobarreira.tela_opcoes()
                funcao_escolhida = lista_opcoes.get(opcao_escolhida)
                if funcao_escolhida:
                    funcao_escolhida()
                else:
                    self.__tela_ecobarreira.mostra_mensagem(
                        "Opção inválida. Tente novamente.")
            except Exception as e:
                self.__tela_ecobarreira.mostra_mensagem(
                    f"Comando inesperado: {str(e)}")
