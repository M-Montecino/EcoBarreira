from model.colaborador import Colaborador
from model.endereco import Endereco
from view.tela_colaborador import TelaColaborador


class ControladorColaborador:
    def __init__(self, controlador_sistema):
        self.__colaboradores = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_colaborador = TelaColaborador()

    def cadastrar_colaboradores(self):
        dados_colaborador = self.__tela_colaborador.pega_dados_colaborador()
        novo_colaborador = Colaborador(dados_colaborador["cpf"],
                                       dados_colaborador["nome"],
                                       dados_colaborador["cidade"],
                                       dados_colaborador["cep"],
                                       dados_colaborador["rua"],
                                       dados_colaborador["complemento"],
                                       dados_colaborador["estado"]
                                       )

        for colaborador in self.__colaboradores:
            if colaborador.cpf == novo_colaborador.cpf:
                self.__tela_colaborador.mostra_mensagem(
                    "Esse colaborador já existe!")
                return
        self.__colaboradores.append(novo_colaborador)
        self.__tela_colaborador.mostra_mensagem(
            "Colaborador adicionado com sucesso!")
        return

    def buscar_colaborador_por_cpf(self, cpf: int):
        for colaborador in self.__colaboradores:
            if colaborador.cpf == cpf:
                self.__tela_colaborador.mostra_mensagem(
                    "Colaborador encontrado!")
                return colaborador
        self.__tela_colaborador.mostra_mensagem("Colaborador não encontrado!")
        return None

    def altera_colaborador(self):
        self.listar_colaboradores()
        cpf_colaborador = self.__tela_colaborador.busca_colaborador()
        colaborador = self.buscar_colaborador_por_cpf(cpf_colaborador)

        if colaborador is not None:
            novos_dados_colaborador = self.__tela_colaborador.pega_dados_colaborador()
            colaborador.cpf = novos_dados_colaborador["cpf"]
            colaborador.nome = novos_dados_colaborador["nome"]
            colaborador.cidade = novos_dados_colaborador["cidade"]
            colaborador.cep = novos_dados_colaborador["cep"]
            colaborador.rua = novos_dados_colaborador["rua"]
            colaborador.complemento = novos_dados_colaborador["complemento"]
            colaborador.estado = novos_dados_colaborador["estado"]
            self.listar_colaboradores()
            self.__tela_colaborador.mostra_mensagem(
                "Colaborador alterado com sucesso!")
        else:
            self.__tela_colaborador.mostra_mensagem(
                "Colaborador não encontrado")

    def excluir_colaborador(self, cpf: int):
        self.listar_colaboradores()
        cpf = self.__tela_colaborador.busca_colaborador()
        colaborador = self.buscar_colaborador_por_cpf(cpf)

        if colaborador is not None:
            self.__colaboradores.remove(colaborador)
            self.listar_colaboradores
            self.__tela_colaborador.mostra_mensagem(
                "Colaborador excluido com sucesso!")
        else:
            self.__tela_colaborador.mostra_mensagem(
                "Colaborador não encontrado")

    def listar_colaboradores(self):
        for colaborador in self.__colaboradores:
            self.__tela_colaborador.mostra_colaborador({"Cpf": colaborador.cpf,
                                                        "Nome": colaborador.nome,
                                                        "Cidade": colaborador.cidade,
                                                        "Cep": colaborador.cep,
                                                        "Rua": colaborador.rua,
                                                        "Complemento": colaborador.complemento,
                                                        "Estado": colaborador.estado
                                                        })

    def retomar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_colaboradores, 2: self.buscar_colaborador_por_cpf,
                        3: self.altera_colaborador, 4: self.excluir_colaborador,
                        5: self.listar_colaboradores}

        continua = True
        while continua:
            lista_opcoes[self.__tela_colaborador.tela_opcoes()]()
