from model.colaborador import Colaborador
from model.endereco import Endereco
from view.tela_colaborador import TelaColaborador

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.controlador_controladores import ControladorControladores


class ControladorColaborador:
    def __init__(self, controlador_sistema: "ControladorControladores"):
        self.__colaboradores = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_colaborador = TelaColaborador()

    def cadastrar_colaboradores(self):
        dados_colaborador = self.__tela_colaborador.pega_dados_colaborador()
        novo_colaborador = Colaborador(
            dados_colaborador["cpf"],
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
                return colaborador
        return None

    def alterar_colaborador(self):
        cpf = self.__tela_colaborador.busca_colaborador()
        colaborador = self.buscar_colaborador_por_cpf(cpf)
        if colaborador:
            novos_dados = self.__tela_colaborador.pega_dados_colaborador()
            if novos_dados["cpf"] != cpf:
                self.__tela_colaborador.mostra_mensagem(
                    "Não é permitido alterar o CPF de um colaborador.")
                return

            colaborador.nome = novos_dados["nome"]
            colaborador.cidade = novos_dados["cidade"]
            colaborador.cep = novos_dados["cep"]
            colaborador.rua = novos_dados["rua"]
            colaborador.complemento = novos_dados["complemento"]
            colaborador.estado = novos_dados["estado"]
            self.__tela_colaborador.mostra_mensagem("Dados atualizados com sucesso!")
        else:
            self.__tela_colaborador.mostra_mensagem("Colaborador não encontrado.")

    def excluir_colaborador(self):
        cpf = self.__tela_colaborador.busca_colaborador()
        colaborador = self.buscar_colaborador_por_cpf(cpf)

        if colaborador is not None:
            self.__colaboradores.remove(colaborador)
            self.listar_colaboradores()
            self.__tela_colaborador.mostra_mensagem(
                "Colaborador excluído com sucesso!"
            )
        else:
            self.__tela_colaborador.mostra_mensagem(
                "Colaborador não encontrado.")

    def listar_colaboradores(self):
        if not self.__colaboradores:
            self.__tela_colaborador.mostra_mensagem(
                "Nenhum colaborador cadastrado.")
            return

        for colaborador in self.__colaboradores:
            self.__tela_colaborador.mostra_colaborador({
                "cpf": colaborador.cpf,
                "nome": colaborador.nome,
                "cidade": colaborador.cidade,
                "cep": colaborador.cep,
                "rua": colaborador.rua,
                "complemento": colaborador.complemento,
                "estado": colaborador.estado
            })

    def buscar_e_mostrar_colaborador(self):
        cpf = self.__tela_colaborador.busca_colaborador()
        colaborador = self.buscar_colaborador_por_cpf(cpf)
        if colaborador:
            self.__tela_colaborador.mostra_colaborador({
                "cpf": colaborador.cpf,
                "nome": colaborador.nome,
                "cidade": colaborador.cidade,
                "cep": colaborador.cep,
                "rua": colaborador.rua,
                "complemento": colaborador.complemento,
                "estado": colaborador.estado
            })

    def retomar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_colaboradores,
            2: self.buscar_e_mostrar_colaborador,
            3: self.alterar_colaborador,
            4: self.excluir_colaborador,
            5: self.listar_colaboradores,
            0: self.retomar
        }

        while True:
            try:
                opcao_escolhida = self.__tela_colaborador.tela_opcoes()
                funcao_escolhida = lista_opcoes.get(opcao_escolhida)
                if funcao_escolhida:
                    funcao_escolhida()
                else:
                    self.__tela_colaborador.mostra_mensagem(
                        "Opção inválida. Tente novamente.")
            except Exception as e:
                self.__tela_colaborador.mostra_mensagem(
                    f"Comando inesperado: {str(e)}")

    def get_colaboradores(self):
        return self.__colaboradores
