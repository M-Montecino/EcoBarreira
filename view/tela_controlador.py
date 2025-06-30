import PySimpleGUI as sg


class TelaControlador:
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        while True:
            self.init_components()
            button, values = self.__window.Read()
            self.close()

            if button in (None, 'Cancelar'):
                return 0
            
            for opcao in range(6):
                if values.get(str(opcao)):
                    return opcao
                
            sg.Popup("Erro", "Por favor, selecione uma opção válida.", title="Opção inválida")

    def init_components(self):
        sg.ChangeLookAndFeel("Green")
        layout = [
            [sg.Text('------CastorEco-------', font=("Arial",25))],
            [sg.Text('Escolha sua opção:', font=("Arial",15))],
            [sg.Radio('1 --- Colaborador',"RD1", key='1')],
            [sg.Radio('2 --- EcoBarreira',"RD1", key='2')],
            [sg.Radio('3 --- Coleta',"RD1", key='3')],
            [sg.Radio('4 --- Sensor',"RD1", key='4')],
            [sg.Radio('5 --- Relatórios',"RD1", key='5')],
            [sg.Radio('0 --- Finalizar Sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Menu CastorEco', layout)

    def close(self):
        self.__window.Close()

    def mostra_mensagem(self, mensagem):
        sg.popup("", mensagem)
