import PySimpleGUI as sg


class TelaRelatorio():
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
                
            sg.Popup("Erro", "Por favor, selecione uma opção válida.", title="Opção inválida")

    def init_opcoes(self):
        sg.ChangeLookAndFeel("Green")
        layout = [
            [sg.Text(' ======== Relatório ======== ', font=("Arial", 25))],
            [sg.Text('Opções:', font=("Arial", 15))],
            [sg.Radio('1 - Relatório de Colaborador', "RD1", key='1')],
            [sg.Radio('2 - Relatório de Ecobarreira', "RD1", key='2')],
            [sg.Radio('3 - Relatório Melhor Colaborador', "RD1", key='3')],
            [sg.Radio('4 - Relatório Melhor Barreira', "RD1", key='4')],
            [sg.Radio('5 - Lixo total', "RD1", key='5')],
            [sg.Radio('0 - Retomar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('CastorEco').Layout(layout)

    def pega_codigo_ecobarreira(self):
        sg.ChangeLookAndFeel("Green")
        layout = [
            [sg.Text('-------- Buscar Ecobarreira ----------', font=("Arial", 25))],
            [sg.Text('Digite o código da ecobarreira: ', font=("Arial", 15))],
            [sg.Text('Código: ', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
    
        self.__window = sg.Window('Selecionar Ecobarreira').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo

    def pega_cpf_colaborador(self):
        sg.ChangeLookAndFeel("Green")
        layout = [
            [sg.Text('-------- Buscar Colaborador ----------', font=("Arial", 25))],
            [sg.Text('Digite o cpf do colaborador: ', font=("Arial", 15))],
            [sg.Text('CPF: ', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
    
        self.__window = sg.Window('Busca Sensor').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']
        self.close()
        return cpf

    def mostra_mensagem(self, mensagem):
        sg.popup("", mensagem)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values