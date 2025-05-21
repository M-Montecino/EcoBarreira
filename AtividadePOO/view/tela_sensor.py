class TelaSensor():
    def tela_opcoes(self):
        print(" ======== Sensores ======== ")
        print("Opções:")
        print("1 - Cadastrar Sensor")
        print("2 - Buscar Sensor por Código")
        print("3 - Alterar Sensor")
        print("4 - Exclui Sensor")
        print("5 - Listar Sensores")

        while True:
            try:
                opcao = int(input("Escolha a opção:"))
                if opcao in [1, 2, 3, 4, 5]:
                    return opcao
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Por favor, digite um número válido.")
    
    def pega_dados_sensor(self):
        print(" ======= Dados do Sensor ======== ")
        while True:
            codigo = input("Código").strip()
            if codigo.isdigit() and int(codigo) > 0:
                codigo = int(codigo)
                break
            print("Código inválido")

        tipo = input("Tipo do sensor: ").strip()
        while not tipo:
            print("Tipo não pode estar vazio!")
            tipo = input("Tipo do sensor: ").strip()
        
        while True:
            ativo_input = input("Está ativo? (True/False): ").strip().lower()
            if ativo_input in ["true","false"]:
                ativo = ativo_input == "true"
                break
            print("Valor inválido, digite 'True' ou 'False'.")

        return {"codigo": codigo, "tipo": tipo, "ativo": ativo}
    
    def mostra_sensor(self, dados_sensor):
        print("Código: ", {dados_sensor["codigo"]})
        print("Tipo: ", {dados_sensor["tipo"]})
        print("Ativo:", {'Sim' if dados_sensor['ativo'] else 'Não'})
        print("--------------\n")

    def busca_sensor(self):
        while True:
            codigo = input("Código do sensor que deseja selecionar: ").strip()
            if codigo.isdigit() and int(codigo) > 0:
                return int(codigo)
            print("Código inválido. Digite apenas números")

    def mostra_mensagem(self, mensagem):
        print(mensagem)
