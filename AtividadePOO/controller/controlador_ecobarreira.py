from model.ecobarreira import EcoBarreira
from model.endereco import Endereco
from model.sensor import Sensor
from view.tela_ecobarreira import TelaEcoBarreira


class ControladorEcoBarreira:
    def __init__(self, controlador_sistema):
        self.__ecobarreiras = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_ecobarreira = TelaEcoBarreira()

    def cadastrar_ecobarreira(self):
        dados_ecobarreira = self.__tela_ecobarreira.pega_dados_ecobarreira()
        nova_ecobarreira = EcoBarreira(dados_ecobarreira["codigo"],
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
                self.__tela_ecobarreira.mostra_mensagem(
                    "A Ecobarreira foi selecionada!")
                return ecobarreira
        self.__tela_ecobarreira.mostra_mensagem(
            "A Ecobarreira não foi encontrada!")
        return None

    def altera_ecobarreira(self):
        self.listar_ecobarreiras()
        codigo_ecobarreira = self.__tela_ecobarreira.busca_ecobarreira()
        ecobarreira = self.buscar_ecobarreira_por_codigo(codigo_ecobarreira)

    def excluir_ecobarreira(self, codigo: int):
        ecobarreira = self.buscar_ecobarreira_por_codigo(codigo)
        if ecobarreira in self.__ecobarreiras:
            self.__ecobarreiras.remove(ecobarreira)
            return ecobarreira
        else:
            return None

    def listar_ecobarreiras(self):
        if not self.__ecobarreiras:
            return None
        else:
            for ecobarreira in self.__ecobarreiras:
                print(f"Código: {ecobarreira.codigo}, \
                    Cidade: {ecobarreira.cidade}, \
                    Cep: {ecobarreira.cep}, \
                    Rua: {ecobarreira.rua}, \
                    Complemento: {ecobarreira.complemento}, \
                    Estado: {ecobarreira.estado}, \
                    Sensores: {ecobarreira.sensores}")
