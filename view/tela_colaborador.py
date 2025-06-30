import PySimpleGUI as sg


class TelaColaborador():
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

            for opcao in range(6):
                if values.get(str(opcao)):
                    return opcao

            sg.Popup("Erro", "Por favor, selecione uma opção válida.",
                     title="Opção inválida")

    def init_opcoes(self):
        sg.ChangeLookAndFeel("Green")
        layout = [
            [sg.Text(' ======== Colaboradores ======== ', font=("Arial", 25))],
            [sg.Text('Opções:', font=("Arial", 15))],
            [sg.Radio('1 - Cadastrar Colaborador', "RD1", key='1')],
            [sg.Radio('2 - Buscar Colaborador por CPF', "RD1", key='2')],
            [sg.Radio('3 - Alterar  Informações do Colaborador', "RD1", key='3')],
            [sg.Radio('4 - Excluir Colaborador', "RD1", key='4')],
            [sg.Radio('5 - Listar Colaboradores', "RD1", key='5')],
            [sg.Radio('0 - Retomar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('CastorEco').Layout(layout)

    def pega_dados_colaborador(self):
        sg.ChangeLookAndFeel('Green')

        estados_validos = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
                           'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN',
                           'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

        while True:
            layout = [
                [sg.Text(' ======= Dados do Colaborador ======== ', font=("Arial", 25))],
                [sg.Text('CPF: ', size=(15, 1)), sg.InputText('', key='cpf')],
                [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
                [sg.Text('Cidade:', size=(15, 1)), sg.InputText('', key='cidade')],
                [sg.Text('Cep:', size=(15, 1)), sg.InputText('', key='cep')],
                [sg.Text('Rua:', size=(15, 1)), sg.InputText('', key='rua')],
                [sg.Text('Complemento:', size=(15, 1)), sg.InputText('', key='complemento')],
                [sg.Text('Estado:', size=(15, 1)), sg.InputText('', key='estado')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('CastorEco').Layout(layout)

            button, values = self.__window.Read()
            self.__window.Close()

            if button == 'Cancelar' or values is None:
                return None

            cpf = values["cpf"]
            nome = values["nome"]
            cidade = values["cidade"]
            cep = values["cep"]
            rua = values["rua"]
            complemento = values["complemento"]
            estado = values["estado"]

            try:
                if not cpf.isdigit() or len(cpf) != 11:
                    raise ValueError(
                        "Cpf deve conter exatamente 11 dígitos numéricos.")

                cpf = int(cpf)

                if estado not in estados_validos:
                    raise ValueError("Estado inválido. Use a sigla!")

                for campo, valor in [('nome', nome), ('cidade', cidade), ('cep', cep),
                                     ('rua', rua), ('complemento', complemento)]:
                    if not valor:
                        raise ValueError(f"{campo} não pode estar vazio.")

                return {
                    "cpf": cpf,
                    "nome": nome,
                    "cidade": cidade,
                    "cep": cep,
                    "rua": rua,
                    "complemento": complemento,
                    "estado": estado
                }

            except ValueError as e:
                sg.Popup(
                    "Erro", f"Dados inválidos: {str(e)}", title="Erro de validação")

    def mostra_colaborador(self, dados_colaborador: dict):
        string = (
            f"CPF: {dados_colaborador['cpf']}\n"
            f"Nome: {dados_colaborador['nome']}\n"
            f"Cidade: {dados_colaborador['cidade']}\n"
            f"Cep: {dados_colaborador['cep']}\n"
            f"Rua: {dados_colaborador['rua']}\n"
            f"Complemento: {dados_colaborador['complemento']}\n"
            f"Estado: {dados_colaborador['estado']}\n"
        )
        sg.popup("Colaborador encontrado:", string)

    def mostra_colaboradores(self, lista_dados_colaboradores: list[dict]):
        string_todos_colaboradores = ""
        for colaborador in lista_dados_colaboradores:
            string_todos_colaboradores += (
                f"CPF: {colaborador['cpf']}\n"
                f"Nome: {colaborador['nome']}\n"
                f"Cidade: {colaborador['cidade']}\n"
                f"Cep: {colaborador['cep']}\n"
                f"Rua: {colaborador['rua']}\n"
                f"Complemento: {colaborador['complemento']}\n"
                f"Estado: {colaborador['estado']}\n\n"
            )
        sg.popup("Lista de Colaboradores", string_todos_colaboradores)

    def busca_colaborador(self):
        sg.ChangeLookAndFeel("Green")
        layout = [
            [sg.Text('-------- Buscar Colaborador ----------', font=("Arial", 25))],
            [sg.Text('Digite o cpf do colaborador: ', font=("Arial", 15))],
            [sg.Text('Cpf: ', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Busca Colaborador').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']
        self.close()
        return values["cpf"]

    def mostra_mensagem(self, mensagem):
        sg.popup("", mensagem)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
