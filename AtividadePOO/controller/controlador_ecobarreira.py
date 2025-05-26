from model.ecobarreira import EcoBarreira
from view.tela_ecobarreira import TelaEcoBarreira
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.controlador_controladores import ControladorControladores


class ControladorEcoBarreira:
    def __init__(self, controlador_sistema: "ControladorControladores"):
        self.__ecobarreiras = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_ecobarreira = TelaEcoBarreira()

    def cadastrar_ecobarreira(self):
        dados_ecobarreira = self.__tela_ecobarreira.pega_dados_ecobarreira()
        nova_ecobarreira = EcoBarreira(
            dados_ecobarreira["codigo"],
            dados_ecobarreira["cidade"],
            dados_ecobarreira["cep"],
            dados_ecobarreira["rua"],
            dados_ecobarreira["complemento"],
            dados_ecobarreira["estado"]
        )

        for ecobarreira in self.__ecobarreiras:
            if ecobarreira.codigo == nova_ecobarreira.codigo:
                self.__tela_ecobarreira.mostra_mensagem(
                    "Essa Ecobarreira já existe!")
                return

        self.__ecobarreiras.append(nova_ecobarreira)
        self.__tela_ecobarreira.mostra_mensagem(
            "Nova Ecobarreira criada com sucesso!")

    def buscar_ecobarreira_por_codigo(self, codigo: int):
        for ecobarreira in self.__ecobarreiras:
            if ecobarreira.codigo == codigo:
                return ecobarreira
        return None

    def altera_ecobarreira(self):
        self.listar_ecobarreiras()
        codigo = self.__tela_ecobarreira.busca_ecobarreira()
        ecobarreira = self.buscar_ecobarreira_por_codigo(codigo)

        if ecobarreira is not None:
            novos_dados_ecobarreira = self.__tela_ecobarreira.pega_dados_ecobarreira()
            ecobarreira.codigo = novos_dados_ecobarreira["codigo"]
            ecobarreira.cidade = novos_dados_ecobarreira["cidade"]
            ecobarreira.cep = novos_dados_ecobarreira["cep"]
            ecobarreira.rua = novos_dados_ecobarreira["rua"]
            ecobarreira.complemento = novos_dados_ecobarreira["complemento"]
            ecobarreira.estado = novos_dados_ecobarreira["estado"]
            self.listar_ecobarreiras()
            self.__tela_ecobarreira.mostra_mensagem(
                "Barreira alterada com sucesso!")
        else:
            self.__tela_ecobarreira.mostra_mensagem(
                "Atenção! essa ecobarreira não existe!")

    def excluir_ecobarreira(self):
        self.listar_ecobarreiras()
        codigo = self.__tela_ecobarreira.busca_ecobarreira()
        ecobarreira = self.buscar_ecobarreira_por_codigo(codigo)
        if ecobarreira:
            self.__ecobarreiras.remove(ecobarreira)
            self.__tela_ecobarreira.mostra_mensagem(
                "Ecobarreira excluída com sucesso!")
        else:
            self.__tela_ecobarreira.mostra_mensagem(
                "Ecobarreira não encontrada!")

    def listar_ecobarreiras(self):
        if not self.__ecobarreiras:
            self.__tela_ecobarreira.mostra_mensagem(
                "Nenhuma ecobarreira cadastrada.")
        else:
            for e in self.__ecobarreiras:
                self.__tela_ecobarreira.mostra_ecobarreira({
                    "codigo": e.codigo,
                    "cidade": e.cidade,
                    "cep": e.cep,
                    "rua": e.rua,
                    "complemento": e.complemento,
                    "estado": e.estado,
                    "sensores": [s.codigo for s in e.sensores]
                })

    def buscar_e_mostrar_ecobarreira(self):
        codigo = self.__tela_ecobarreira.busca_ecobarreira()
        ecobarreira = self.buscar_ecobarreira_por_codigo(codigo)
        if ecobarreira:
            self.__tela_ecobarreira.mostra_ecobarreira({
                "codigo": ecobarreira.codigo,
                "cidade": ecobarreira.cidade,
                "cep": ecobarreira.cep,
                "rua": ecobarreira.rua,
                "complemento": ecobarreira.complemento,
                "estado": ecobarreira.estado,
                "sensores": ecobarreira.sensores
            })
        else:
            self.__tela_ecobarreira.mostra_mensagem(
                "Ecobarreira não encontrada.")

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

    def get_ecobarreiras(self):
        return self.__ecobarreiras
