from model.colaborador import Colaborador
from daos.colaborador_dao import ColaboradorDAO
from view.tela_colaborador import TelaColaborador

from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.controlador_controladores import ControladorControladores


class ControladorColaborador:
    def __init__(self, controlador_sistema: "ControladorControladores"):
        self.__colaborador_dao = ColaboradorDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_colaborador = TelaColaborador()

    def cadastrar_colaboradores(self):
        try:
            dados_colaborador = self.__tela_colaborador.pega_dados_colaborador()
            if dados_colaborador is None:
                return

            novo_colaborador = Colaborador(
                dados_colaborador["cpf"],
                dados_colaborador["nome"],
                dados_colaborador["cidade"],
                dados_colaborador["cep"],
                dados_colaborador["rua"],
                dados_colaborador["complemento"],
                dados_colaborador["estado"]
            )

            for colaborador in self.__colaborador_dao.pega_todos():
                if colaborador.cpf == novo_colaborador.cpf:
                    raise ElementoRepetidoException()

            self.__colaborador_dao.adiciona(novo_colaborador)
            self.__tela_colaborador.mostra_mensagem("Colaborador adicionado com sucesso!")

        except ElementoRepetidoException as e:
            self.__tela_colaborador.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_colaborador.mostra_mensagem(f"Erro inesperado: {str(e)}")

    def buscar_colaborador_por_cpf(self, cpf_input: int):
        try:
            cpf = int(cpf_input)
        except ValueError:
            self.__tela_colaborador.mostra_mensagem("CPF inválido")
            return None

        colaborador = self.__colaborador_dao.pega(cpf)
        if colaborador is None:
            self.__tela_colaborador.mostra_mensagem("Colaborador não encontrado")
        return colaborador

    def alterar_colaborador(self):
        try:
            cpf_input = self.__tela_colaborador.busca_colaborador()
            colaborador = self.buscar_colaborador_por_cpf(cpf_input)

            if colaborador is None:
                raise ElementoNaoExisteException()

            cpf_antigo = colaborador.cpf

            novos_dados = self.__tela_colaborador.pega_dados_colaborador()

            colaborador.cpf = novos_dados["cpf"]
            colaborador.nome = novos_dados["nome"]
            colaborador.cidade = novos_dados["cidade"]
            colaborador.cep = novos_dados["cep"]
            colaborador.rua = novos_dados["rua"]
            colaborador.complemento = novos_dados["complemento"]
            colaborador.estado = novos_dados["estado"]

            self.__colaborador_dao.remove(cpf_antigo)
            self.__colaborador_dao.adiciona(colaborador)

            self.__tela_colaborador.mostra_mensagem("Dados atualizados com sucesso!")

        except ElementoNaoExisteException as e:
            self.__tela_colaborador.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_colaborador.mostra_mensagem(f"Erro inesperado: {str(e)}")

    def excluir_colaborador(self):
        try:
            cpf_input = self.__tela_colaborador.busca_colaborador()
            cpf = int(cpf_input)
            colaborador = self.buscar_colaborador_por_cpf(cpf)

            if colaborador is None:
                raise ElementoNaoExisteException()

            self.__colaborador_dao.remove(cpf)
            self.__tela_colaborador.mostra_mensagem("Colaborador excluído com sucesso!")

        except ElementoNaoExisteException as e:
            self.__tela_colaborador.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_colaborador.mostra_mensagem(f"Erro inesperado: {str(e)}")

    def listar_colaboradores(self):
        try:
            colaboradores = self.__colaborador_dao.pega_todos()
            if not colaboradores:
                self.__tela_colaborador.mostra_mensagem("Nenhum colaborador cadastrado.")
                return

            lista_dados = []
            for colaborador in colaboradores:
                lista_dados.append({
                    "cpf": colaborador.cpf,
                    "nome": colaborador.nome,
                    "cidade": colaborador.cidade,
                    "cep": colaborador.cep,
                    "rua": colaborador.rua,
                    "complemento": colaborador.complemento,
                    "estado": colaborador.estado
                })

            self.__tela_colaborador.mostra_colaboradores(lista_dados)

        except Exception as e:
            self.__tela_colaborador.mostra_mensagem(f"Erro ao listar colaboradores: {str(e)}")

    def buscar_e_mostrar_colaborador(self):
        try:
            cpf = self.__tela_colaborador.busca_colaborador()
            colaborador = self.buscar_colaborador_por_cpf(cpf)

            if colaborador is None:
                raise ElementoNaoExisteException()

            dados = {
                "cpf": colaborador.cpf,
                "nome": colaborador.nome,
                "cidade": colaborador.cidade,
                "cep": colaborador.cep,
                "rua": colaborador.rua,
                "complemento": colaborador.complemento,
                "estado": colaborador.estado
            }

            self.__tela_colaborador.mostra_colaborador(dados)

        except ElementoNaoExisteException as e:
            self.__tela_colaborador.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_colaborador.mostra_mensagem(f"Erro ao buscar colaborador: {str(e)}")

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
