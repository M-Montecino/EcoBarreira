import PySimpleGUI as sg


class TelaSensor():
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
            [sg.Text(' ======== Sensores ======== ', font=("Arial", 25))],
            [sg.Text('Opções:', font=("Arial", 15))],
            [sg.Radio('1 - Cadastrar Sensor', "RD1", key='1')],
            [sg.Radio('2 - Buscar Sensor por Código', "RD1", key='2')],
            [sg.Radio('3 - Alterar Sensor', "RD1", key='3')],
            [sg.Radio('4 - Exclui Sensor', "RD1", key='4')],
            [sg.Radio('5 - Listar Sensores', "RD1", key='5')],
            [sg.Radio('0 - Retomar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('CastorEco').Layout(layout)

    def pega_dados_sensor(self):
        sg.ChangeLookAndFeel('Green')

        while True:
            layout = [
            [sg.Text(' ======= Dados do Sensor ======== ', font=("Arial", 25))],
            [sg.Text('Codigo', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Text('Tipo:', size=(15, 1)), sg.InputText('', key='tipo')],
            [sg.Text('Ativo:', size=(15, 1)), sg.InputText('', key='ativo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('CastorEco').Layout(layout)

            button, values = self.__window.Read()
            self.__window.Close()
                
            if button == 'Cancelar' or values is None:
                return None
            
            codigo = values["codigo"]
            tipo = values["tipo"]
            ativo = values["ativo"]

            try:
                    codigo = int(codigo)
                    if not isinstance(tipo, str) or tipo.strip() == "":
                        raise ValueError("Tipo deve ser uma string não vazia")
                    
                    ativo_str = ativo.strip().lower()
                    if ativo_str in ['true', '1', 'sim', 's']:
                        ativo = True
                    elif ativo_str in ['false', '0', 'não', 'nao', 'n']:
                        ativo = False
                    else:
                        raise ValueError("Ativo deve ser True ou False")

                    return {"codigo": codigo, "tipo": tipo, "ativo": ativo}

            except Exception as e:
                sg.Popup("Erro de entrada", f"Dados inválidos: {str(e)}", title="Erro")

    def mostra_sensor(self, dados_sensor: dict):
        string = (
            f"Codigo: {dados_sensor['codigo']}\n"
            f"Tipo: {dados_sensor['tipo']}\n"
            f"Ativo: {dados_sensor['ativo']}\n"
        )
        sg.popup("Sensor encontrado: ", string)

    def mostra_sensores(self, lista_dados_sensores: list[dict]):
        string_todos_sensores = ""
        for sensor in lista_dados_sensores:
            string_todos_sensores += (
            f"Codigo: {sensor['codigo']}\n"
            f"Tipo: {sensor['tipo']}\n"
            f"Ativo: {sensor['ativo']}\n"
            )
        sg.popup("Lista de sensores", string_todos_sensores)

    def busca_sensor(self):
        sg.ChangeLookAndFeel("Green")
        layout = [
            [sg.Text('-------- Buscar Sensor ----------', font=("Arial", 25))],
            [sg.Text('Digite o código do sensor: ', font=("Arial", 15))],
            [sg.Text('Código: ', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
    
        self.__window = sg.Window('Busca Sensor').Layout(layout)

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
