class TelaEcoBarreira():
    def tela_opcoes(self):
        print(" ======= EcoBarreiras ======= ")
        print("Opções:")
        print("1 - Cadastrar EcoBarreira")
        print("2 - Buscar Ecobarreira por Código")
        print("3 - Alterar informações da EcoBarreira")
        print("4 - Excluir EcoBarreira")
        print("5 - Listar Ecobarreiras")

        opcao = int(input("Escolha a sua opção: "))
        return opcao

    def pega_dados_ecobarreira(self):
        print(" ===== Dados da Ecobarreira =====")
        codigo = input("Código: ")
        cidade = input("Cidade: ")
        cep = input("Cep: ")
        rua = input("Rua: ")
        complemento = input("Complemento: ")
        estado = input("Estado: ")

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

    def busca_ecobarreira(self):
        codigo = input("Código da EcoBarreira que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, mensagem):
        print(mensagem)
