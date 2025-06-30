from model.coleta import Coleta
from daos.coleta_dao import ColetaDAO
from view.tela_coleta import TelaColeta
from model.lixo import *
from datetime import datetime

from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.controlador_controladores import ControladorControladores


class ControladorColeta:
    def __init__(self, controlador_sistema: "ControladorControladores"):
        self.__coleta_dao = ColetaDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_coleta = TelaColeta()

    def cadastrar_coleta(self):
        try:
            dados = self.__tela_coleta.pega_dados_coleta()

            colaborador = self.__controlador_sistema.controlador_colaborador.buscar_colaborador_por_cpf(
                dados["cpf_colaborador"]
            )
            ecobarreira = self.__controlador_sistema.controlador_ecobarreira.buscar_ecobarreira_por_codigo(
                dados["codigo_ecobarreira"]
            )

            if not colaborador:
                self.__tela_coleta.mostra_mensagem("Colaborador não encontrado.")
                return
            if not ecobarreira:
                self.__tela_coleta.mostra_mensagem("Ecobarreira não encontrada.")
                return

            id_coleta = int(dados["id"])

            nova = Coleta(
                id=id_coleta,
                data=dados["data"],
                colaborador=colaborador,
                ecobarreira=ecobarreira
            )

            for coleta in self.__coleta_dao.pega_todos():
                if coleta.id == nova.id:
                    raise ElementoRepetidoException()

            self.__coleta_dao.adiciona(nova)
            self.__tela_coleta.mostra_mensagem("Coleta adicionada com sucesso!")

        except ElementoRepetidoException as e:
            self.__tela_coleta.mostra_mensagem(str(e))
        except Exception as e:
            import traceback
            print("Erro completo:")
            traceback.print_exc()
            self.__tela_coleta.mostra_mensagem(f"Erro inesperado: {type(e).__name__}: {str(e)}")

    def buscar_coleta_por_id(self, id_input: int):
        try:
            id = int(id_input)
        except ValueError:
            self.__tela_coleta.mostra_mensagem("Id inválido")
            return None
        
        coleta = self.__coleta_dao.pega(id)
        if coleta is None:
            self.__tela_coleta.mostra_mensagem("Coleta não encontrada")
        return coleta

    def altera_coleta(self):
        try:
            id_coleta = self.__tela_coleta.busca_coleta()
            coleta = self.buscar_coleta_por_id(id_coleta)

            if coleta is None:
                raise ElementoNaoExisteException()

            novos_dados = self.__tela_coleta.pega_dados_coleta()

            id_antigo = coleta.id

            colaborador = self.__controlador_sistema.controlador_colaborador.buscar_colaborador_por_cpf(
                novos_dados["cpf_colaborador"]
            )
            if not colaborador:
                raise ElementoNaoExisteException()

            ecobarreira = self.__controlador_sistema.controlador_ecobarreira.buscar_ecobarreira_por_codigo(
                novos_dados["codigo_ecobarreira"]
            )
            if not ecobarreira:
                raise ElementoNaoExisteException()

            coleta.id = novos_dados["id"]
            coleta.data = novos_dados["data"]
            coleta.colaborador = colaborador
            coleta.ecobarreira = ecobarreira
            
            self.__coleta_dao.remove(id_antigo)
            self.__coleta_dao.adiciona(coleta)

            self.__tela_coleta.mostra_mensagem("Dados atualizados com sucesso!")

        except ElementoNaoExisteException as e:
            self.__tela_coleta.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_coleta.mostra_mensagem(f"Erro inesperado: {str(e)}")

    def excluir_coleta(self, id=None):
        try:
            id = self.__tela_coleta.busca_coleta()
            coleta = self.buscar_coleta_por_id(id)

            if coleta is None:
                raise ElementoNaoExisteException()
            
            self.__coleta_dao.remove(id)
            self.__tela_coleta.mostra_mensagem("Coleta excluida com sucesso!")

        except ElementoNaoExisteException as e:
            self.__tela_coleta.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_coleta.mostra_mensagem(f"Erro inesperado ao excluir colaborador: {str(e)}")

    def listar_coleta(self):
        try:
            coletas = self.__coleta_dao.pega_todos()

            if not coletas:
                self.__tela_coleta.mostra_mensagem("Nenhuma coleta cadastrada.")
                return
            
            lista_dados = []
            for coleta in coletas:
                data_str = coleta.data.strftime("%d/%m/%Y") if hasattr(coleta.data, 'strftime') else str(coleta.data)
                
                lista_dados.append({
                    "id": coleta.id,
                    "data": data_str,
                    "colaborador": coleta.colaborador.cpf,
                    "ecobarreira": coleta.ecobarreira.codigo
                })

            self.__tela_coleta.mostra_coletas(lista_dados)

        except Exception as e:
            self.__tela_coleta.mostra_mensagem(f"Erro ao listar coletas: {str(e)}")
    
    def buscar_e_mostrar_coleta(self):
        try:
            id = self.__tela_coleta.busca_coleta()
            coleta = self.buscar_coleta_por_id(id)

            if coleta is None:
                raise ElementoNaoExisteException()
            
            dados = {
                "id": coleta.id,
                "data": coleta.data,
                "colaborador": coleta.colaborador.cpf,
                "ecobarreira": coleta.ecobarreira.codigo
            }

            self.__tela_coleta.mostra_coleta(dados)

        except ElementoNaoExisteException as e:
            self.__tela_coleta.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_coleta.mostra_mensagem(f"Erro ao buscar colaborador: {str(e)}")

    def adicionar_lixo(self):
        dados_lixo = self.__tela_coleta.pega_dados_lixo()

        codigo_coleta = int(dados_lixo["id_coleta"])
        tipo = dados_lixo["tipo_lixo"]
        quantidade = float(dados_lixo["quantidade"])

        coleta = self.buscar_coleta_por_id(codigo_coleta)
        if coleta is None:
            self.__tela_coleta.mostra_mensagem("Coleta não encontrada!")
            return

        if tipo.lower() in ("plastico", "plástico"):
            lixo = Plastico(quantidade)

        elif tipo.lower() == "vidro":
            lixo = Vidro(quantidade)

        elif tipo.lower() == "metal":
            lixo = Metal(quantidade)

        elif tipo.lower() == "borracha":
            lixo = Borracha(quantidade)

        elif tipo.lower() == "organico":
            lixo = Organico(quantidade)

        elif tipo.lower() == "outros":
            lixo = Outros(quantidade)

        else:
            self.__tela_coleta.mostra_mensagem("Tipo não encontrado!")
            return

        coleta.lixos.append(lixo)
        self.__tela_coleta.mostra_mensagem("Lixo adicionado com sucesso!")

    def mostrar_lixos(self):
        codigo_coleta = self.__tela_coleta.busca_coleta()
        coleta = self.buscar_coleta_por_id(codigo_coleta)

        if coleta is None:
            self.__tela_coleta.mostra_mensagem("Coleta não encontrada!")
            return

        if not coleta.lixos:
            self.__tela_coleta.mostra_mensagem(
                "Nenhum lixo registrado nessa coleta.")
            return

        for i, lixo in enumerate(coleta.lixos, start=1):
            tipo = lixo.__class__.__name__
            self.__tela_coleta.mostra_mensagem(
                f"{i}) {tipo} - {lixo.quantidade} kg")

    def excluir_lixo(self):
        id = self.__tela_coleta.busca_coleta()
        coleta = self.buscar_coleta_por_id(id)

        if not coleta:
            self.__tela_coleta.mostra_mensagem("Coleta não encontrada!")
            return

        if not coleta.lixos:
            self.__tela_coleta.mostra_mensagem(
                "Nenhum lixo cadastrado nesta coleta.")
            return

        for i, lixo in enumerate(coleta.lixos, start=1):
            tipo = lixo.__class__.__name__
            self.__tela_coleta.mostra_mensagem(
                f"{i}) {tipo} - {lixo.quantidade} kg")

        indice = self.__tela_coleta.pega_indice_lixo()
        indice_real = indice - 1

        if 0 <= indice_real < len(coleta.lixos):
            removido = coleta.lixos.pop(indice_real)
            tipo_removido = removido.__class__.__name__
            self.__tela_coleta.mostra_mensagem(
                f"{tipo_removido} removido com sucesso.")
        else:
            self.__tela_coleta.mostra_mensagem(
                "Número inválido. Tente novamente.")

    def retomar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_coleta,
            2: self.buscar_e_mostrar_coleta,
            3: self.altera_coleta,
            4: self.excluir_coleta,
            5: self.listar_coleta,
            6: self.adicionar_lixo,
            7: self.excluir_lixo,
            8: self.mostrar_lixos,
            0: self.retomar
        }

        while True:
            try:
                opcao_escolhida = self.__tela_coleta.tela_opcoes()
                funcao_escolhida = lista_opcoes.get(opcao_escolhida)
                if funcao_escolhida:
                    funcao_escolhida()
                else:
                    self.__tela_coleta.mostra_mensagem(
                        "Opção inválida. Tente novamente")
            except Exception as e:
                self.__tela_coleta.mostra_mensagem(
                    f"Comando inesperado: {str(e)}")
