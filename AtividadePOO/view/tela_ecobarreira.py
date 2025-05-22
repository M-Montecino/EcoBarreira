class TelaEcoBarreira():
    def tela_opcoes(self):
        print(" ======= EcoBarreiras ======= ")
        print("Opções:")
        print("1 - Cadastrar EcoBarreira")
        print("2 - Buscar Ecobarreira por Código")
        print("3 - Alterar informações da EcoBarreira")
        print("4 - Excluir EcoBarreira")
        print("5 - Listar Ecobarreiras")
        print("0 - Retomar")

        while True:
            try:
                opcao = int(input("Escolha sua opção: "))
                if opcao in [0, 1, 2, 3, 4, 5]:
                    return opcao
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Por favor, digite um número válido.")

    def pega_dados_ecobarreira(self):
        print(" ===== Dados da Ecobarreira =====")
        while True:
            codigo = input("Código: ").strip()
            if codigo.isdigit() and int(codigo) > 0:
                codigo = int(codigo)
                break
            print("Código inválido")

        cidade = input("Cidade: ").strip()
        while not cidade:
            print("Cidade não pode estar vazio!")
            cidade = input("Cidade: ").strip()

        cep = input("Cep: ").strip()
        while not cep:
            print("Cep não pode estar vazio!")
            cep = input("Cep: ").strip()

        rua = input("Rua: ").strip()
        while not rua:
            print("Rua não pode estar vazio!")
            rua = input("Rua: ")

        complemento = input("Complemento: ").strip()
        while not complemento:
            print("Complemento não pode estár vazio!")
            complemento = input("Complemento: ").strip()

        estado = input("Estado: ").strip()
        while not estado:
            print("Estado não pode estar vazio!")
            estado = input("Estado: ").strip()

        return {"codigo": codigo,
                "cidade": cidade,
                "cep": cep,
                "rua": rua,
                "complemento": complemento,
                "estado": estado
                }

    def mostra_ecobarreira(self, dados_ecobarreira):
        print("Código: ", dados_ecobarreira["codigo"])
        print("Cidade: ", dados_ecobarreira["cidade"])
        print("Cep: ", dados_ecobarreira["cep"])
        print("Rua: ", dados_ecobarreira["rua"])
        print("Complemento: ", dados_ecobarreira["complemento"])
        print("Estado: ", dados_ecobarreira["estado"])
        print("--------------\n")

    def busca_ecobarreira(self):
        while True:
            codigo = input(
                "Código da Ecobarreira que deseja selecionar: ").strip()
            if codigo.isdigit() and int(codigo) > 0:
                return int(codigo)
            print("Código inválido. Digite apenas números")

    def mostra_mensagem(self, mensagem):
        print(mensagem)
