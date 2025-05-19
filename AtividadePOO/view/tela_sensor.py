class TelaSensor():
    def tela_opcoes(self):
        print(" ======== Sensores ======== ")
        print("Opções:")
        print("1 - Cadastrar Sensor")
        print("2 - Buscar Sensor por Código")
        print("3 - Alterar Sensor")
        print("4 - Exclui Sensor")
        print("5 - Listar Sensores")

        opcao = int(input("Escolha a opção:"))
        return opcao
    
    def pega_dados_sensor(self):
        print(" ======= Dados do Sensor ======== ")
        codigo = input("Código: ")
        tipo = input("Tipo: ")
        ativo = input("Ativo: (True ou False)")

        return {"codigo": codigo, "tipo": tipo, "ativo": ativo}
    
    def mostra_sensor(self, dados_sensor):
        print("Código: ", dados_sensor["codigo"])
        print("Tipo: ", dados_sensor["tipo"])
        print("Ativo:", dados_sensor["ativo"])
        print("\n")

    def busca_sensor(self):
        codigo = input("Código do sensor que deseja selecionar: ")
        return codigo
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)
