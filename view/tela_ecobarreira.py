import PySimpleGUI as sg


class TelaEcoBarreira():
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
            [sg.Text(' ======= EcoBarreiras ======= ', font=("Arial", 25))],
            [sg.Text('Opções:', font=("Arial", 15))],
            [sg.Radio('1 - Cadastrar EcoBarreira', "RD1", key='1')],
            [sg.Radio('2 - Buscar Ecobarreira por Código', "RD1", key='2')],
            [sg.Radio('3 - Alterar informações da EcoBarreira', "RD1", key='3')],
            [sg.Radio('4 - Excluir EcoBarreira', "RD1", key='4')],
            [sg.Radio('5 - Listar Ecobarreiras', "RD1", key='5')],
            [sg.Radio('6 - Adicionar Sensor na EcoBarreira', "RD1", key='6')],
            [sg.Radio('7 - Remover Sensor na EcoBarreira', "RD1", key='7')],
            [sg.Radio('8 - Checar Sensores na Ecobarreira', "RD1", key='8')],
            [sg.Radio('0 - Retomar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('CastorEco').Layout(layout)

    def pega_dados_ecobarreira(self):
        sg.ChangeLookAndFeel('Green')

        estados_validos = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
                           'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN',
                           'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

        while True:
            layout = [
                [sg.Text(' ======= Dados da Ecobarreira ======== ',
                         font=("Arial", 25))],
                [sg.Text('Codigo: ', size=(15, 1)), sg.InputText('', key='codigo')],
                [sg.Text('Cidade:', size=(15, 1)),
                 sg.InputText('', key='cidade')],
                [sg.Text('Cep:', size=(15, 1)), sg.InputText('', key='cep')],
                [sg.Text('Rua:', size=(15, 1)), sg.InputText('', key='rua')],
                [sg.Text('Complemento:', size=(15, 1)),
                 sg.InputText('', key='complemento')],
                [sg.Text('Estado:', size=(15, 1)),
                 sg.InputText('', key='estado')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('CastorEco').Layout(layout)

            button, values = self.__window.Read()
            self.__window.Close()

            if button == 'Cancelar' or values is None:
                return None

            codigo = values["codigo"]
            cidade = values["cidade"]
            cep = values["cep"]
            rua = values["rua"]
            complemento = values["complemento"]
            estado = values["estado"]

            try:
                if not codigo.isdigit():
                    raise ValueError(
                        "Código deve conter dígitos numéricos")
                
                codigo = int(codigo)

                if estado not in estados_validos:
                    raise ValueError("Estado inválido. Use a sigla!")

                for campo, valor in [('Cidade', cidade), ('CEP', cep),
                                     ('Rua', rua), ('Complemento', complemento)]:
                    if not valor:
                        raise ValueError(f"{campo} não pode estar vazio.")

                return {
                    "codigo": codigo,
                    "cidade": cidade,
                    "cep": cep,
                    "rua": rua,
                    "complemento": complemento,
                    "estado": estado
                }

            except ValueError as e:
                sg.Popup(
                    "Erro", f"Dados inválidos: {str(e)}", title="Erro de validação")

    def mostra_ecobarreira(self, dados_ecobarreira: dict):
        string = (
            f"Código: {dados_ecobarreira['nome']}\n"
            f"Cidade: {dados_ecobarreira['cidade']}\n"
            f"Cep: {dados_ecobarreira['cep']}\n"
            f"Rua: {dados_ecobarreira['rua']}\n"
            f"Complemento: {dados_ecobarreira['complemento']}\n"
            f"Estado: {dados_ecobarreira['estado']}\n"
        )
        sg.popup("Ecobarreira encontrada:", string)
    
    def mostra_ecobarreiras(self, lista_dados_ecobarreira: list[dict]):
        string_todas_ecobarreiras = ""
        for ecobarreira in lista_dados_ecobarreira:
            string_todas_ecobarreiras += (
                f"Nome: {ecobarreira['nome']}\n"
                f"Cidade: {ecobarreira['cidade']}\n"
                f"Cep: {ecobarreira['cep']}\n"
                f"Rua: {ecobarreira['rua']}\n"
                f"Complemento: {ecobarreira['complemento']}\n"
                f"Estado: {ecobarreira['estado']}\n\n"
            )
        sg.popup("Lista de Ecobarreiras", string_todas_ecobarreiras)

    def busca_ecobarreira(self):
        sg.ChangeLookAndFeel("Green")
        layout = [
            [sg.Text('-------- Buscar Ecobarreira ----------', font=("Arial", 25))],
            [sg.Text('Digite o código da Ecobarreira: ', font=("Arial", 15))],
            [sg.Text('Código: ', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
    
        self.__window = sg.Window('Busca Ecobarreira').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo

    def mostra_mensagem(self, mensagem):
        sg.popup("", mensagem)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def pega_codigo_sensor(self):
        sg.ChangeLookAndFeel("Green")

        while True:
            layout = [
                [sg.Text('Informe o código do sensor que deseja selecionar: ', font=("Arial", 15))],
                [sg.InputText('', key='codigo')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Selção de Sensor', layout)
            button, values = self.__window.Read()
            self.__window.Close()

            if button == 'Cancelar' or values is None:
                return None
            
            codigo = values['codigo'].strip()

            try:
                codigo = int(codigo)
                return codigo
            except ValueError:
                sg.Popup("Erro", "Entrada inválida! Digite um número inteiro", title="Erro de validação")