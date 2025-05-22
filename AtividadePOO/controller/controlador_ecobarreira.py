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

    def excluir_ecobarreira(self, codigo: int):
        self.listar_ecobarreiras()
        codigo = self.__tela_ecobarreira.busca_ecobarreira()
        ecobarreira = self.buscar_ecobarreira_por_codigo(codigo)

        if ecobarreira is not None:
            self.__ecobarreiras.remove(ecobarreira)
            self.listar_ecobarreiras
            self.__tela_ecobarreira.mostra_mensagem(
                "Ecobarreira excluida com sucesso!")
        else:
            self.__tela_ecobarreira.mostra_mensagem(
                "Atenção! Essa Ecobarreira não existe")

    def listar_ecobarreiras(self):
        for ecobarreira in self.__ecobarreiras:
            self.__tela_ecobarreira.mostra_mensagem({
                "Código": ecobarreira.codigo,
                "Cidade": ecobarreira.cidade,
                "Cep": ecobarreira.cep,
                "Rua": ecobarreira.rua,
                "Complemento": ecobarreira.complemento,
                "Estado": ecobarreira.estado,
                "Sensores": ecobarreira.sensores
            })

    def retomar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_ecobarreira,
            2: self.buscar_ecobarreira_por_codigo,
            3: self.altera_ecobarreira,
            4: self.excluir_ecobarreira,
            5: self.listar_ecobarreiras,
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
