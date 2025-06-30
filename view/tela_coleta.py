import PySimpleGUI as sg
from datetime import datetime


class TelaColeta():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        while True:
            self.init_opcoes()
            button, values = self.__window.Read()
            self.close()

            if button in (None, 'Cancelar'):
                return 0

            for opcao in range(9):
                if values.get(str(opcao)):
                    return opcao

            sg.Popup("Erro", "Por favor, selecione uma opção válida.",
                     title="Opção inválida")

    def init_opcoes(self):
        sg.ChangeLookAndFeel("Green")
        layout = [
            [sg.Text(' ======= Coleta ======= ', font=("Arial", 25))],
            [sg.Text('Opções:', font=("Arial", 15))],
            [sg.Radio('1 - Registrar nova Coleta', "RD1", key='1')],
            [sg.Radio('2 - Buscar Coleta por ID', "RD1", key='2')],
            [sg.Radio('3 - Alterar dados da Coleta', "RD1", key='3')],
            [sg.Radio('4 - Excluir Coleta', "RD1", key='4')],
            [sg.Radio('5 - Listar todas as Coletas', "RD1", key='5')],
            [sg.Radio('6 - Adicionar Lixo', "RD1", key='6')],
            [sg.Radio('7 - Remover Lixo', "RD1", key='7')],
            [sg.Radio('8 - Mostrar Lixos', "RD1", key='8')],
            [sg.Radio('0 - Retomar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('CastorEco').Layout(layout)

    def pega_dados_coleta(self):
        sg.ChangeLookAndFeel("Green")

        while True:
            layout = [   
            [sg.Text(' ======= Dados da Coleta ======== ', font=("Arial", 25))],
            [sg.Text('Id: ', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Text('Data: ', size=(15, 1)), sg.InputText('', key='data')],
            [sg.Text('Código da ecobarreira: ', size=(15, 1)), sg.InputText('', key='codigo_ecobarreira')],
            [sg.Text('Cpf do colaborador: ', size=(15, 1)), sg.InputText('', key='cpf_colaborador')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('CastorEco').Layout(layout)

            button, values = self.__window.Read()
            self.__window.Close()
                
            if button == 'Cancelar' or values is None:
                return None
            
            id = values["id"]
            data = values["data"]
            codigo_ecobarreira = values["codigo_ecobarreira"]
            cpf_colaborador = values["cpf_colaborador"]

            try:
                if not id.isdigit():
                    raise ValueError("Id são apenas números")
                id = int(id)

                if not codigo_ecobarreira.isdigit():
                    raise ValueError("O código da Ecobarreira são apenas inteiros")
                codigo_ecobarreira = int(codigo_ecobarreira)

                if not cpf_colaborador.isdigit() or len(cpf_colaborador) != 11:
                    raise ValueError("CPF deve conter exatamente 11 dígitos")
                cpf_colaborador = int(cpf_colaborador)

                try:
                    data = datetime.strptime(data, "%d/%m/%Y")
                except ValueError:
                    raise ValueError("A data deve estar no formato DD/MM/AAAA")

                return {
                    "id": id,
                    "data": data,
                    "codigo_ecobarreira": codigo_ecobarreira,
                    "cpf_colaborador": cpf_colaborador
                }

            except ValueError as e:
                sg.Popup("Erro", f"Dados inválidos: {str(e)}", title="Erro de validação")

    def mostra_coleta(self, dados_coleta: dict):
        string = (
            f"id: {dados_coleta['id']}\n"
            f"Data: {dados_coleta['data']}\n"
            f"Colaborador: {dados_coleta['colaborador']}\n"
            f"Ecobarreira: {dados_coleta['ecobarreira']}\n"
        )
        sg.popup("Coleta encontrada:", string)
        
    def mostra_coletas(self, lista_dados_coletas: list[dict]):
        string_todas_coletas = ""
        for coleta in lista_dados_coletas:
            string_todas_coletas += (
            f"id: {coleta['id']}\n"
            f"Data: {coleta['data']}\n"
            f"Colaborador: {coleta['colaborador']}\n"
            f"Ecobarreira: {coleta['ecobarreira']}\n\n"   
        )
        sg.popup("Lista de Coletas", string_todas_coletas)

    def busca_coleta(self):
        sg.ChangeLookAndFeel("Green")
        layout = [
            [sg.Text('-------- Buscar Coleta ----------', font=("Arial", 25))],
            [sg.Text('Digite o id da Coleta: ', font=("Arial", 15))],
            [sg.Text('ID: ', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Busca Sensor').Layout(layout)

        button, values = self.open()
        id = values['id']
        self.close()
        return id

    def mostra_mensagem(self, mensagem):
        sg.popup("", mensagem)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def pega_dados_lixo(self):
        sg.ChangeLookAndFeel("Green")

        while True:
            layout = [
                [sg.Text(' ======= Dados do Lixo ======== ', font=("Arial", 25))],
                [sg.Text('ID da Coleta:', size=(20, 1)), sg.InputText('', key='id_coleta')],
                [sg.Text('Tipo de Lixo:', size=(20, 1)), sg.InputText('', key='tipo_lixo')],
                [sg.Text('Quantidade (kg):', size=(20, 1)), sg.InputText('', key='quantidade')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('CastorEco - Lixo', layout)
            button, values = self.__window.Read()
            self.__window.Close()

            if button == 'Cancelar' or values is None:
                return None

            id_str = values['id_coleta'].strip()
            tipo_lixo = values['tipo_lixo'].strip()
            qtd_str = values['quantidade'].strip()

            try:
                if not id_str.isdigit():
                    raise ValueError("ID da coleta deve ser um número inteiro.")
                id_coleta = int(id_str)

                if not tipo_lixo:
                    raise ValueError("Tipo de lixo não pode estar vazio.")

                quantidade = float(qtd_str)
                if quantidade <= 0:
                    raise ValueError("A quantidade deve ser maior que zero.")

                return {
                    "id_coleta": id_coleta,
                    "tipo_lixo": tipo_lixo,
                    "quantidade": quantidade
                }

            except ValueError as e:
                sg.Popup("Erro", f"Entrada inválida: {str(e)}", title="Erro de validação")

    def pega_indice_lixo(self):
        sg.ChangeLookAndFeel("Green")

        while True:
            layout = [
                [sg.Text('Informe o índice do lixo que deseja selecionar:', font=("Arial", 15))],
                [sg.InputText('', key='indice')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Seleção de Lixo', layout)
            button, values = self.__window.Read()
            self.__window.Close()

            if button == 'Cancelar' or values is None:
                return None

            indice = values['indice'].strip()

            try:
                indice = int(indice)
                return indice
            except ValueError:
                sg.Popup("Erro", "Entrada inválida! Digite um número inteiro", title="Erro de validação")