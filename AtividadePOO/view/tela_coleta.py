class TelaColeta():
    def tela_opcoes(self):
        print(" ======= Coleta ======= ")
        print("Opções: ")
        print("1 - Registrar nova Coleta")
        print("2 - Buscar Coleta por ID")
        print("3 - Alterar dados da Coleta")
        print("4 - Excluir Coleta")
        print("5 - Listar todas as Coletas")
        print("6 - Adicionar Lixo")
        print("7 - Remover Lixo")
        print("8 - Mostrar Lixos")
        print("0 - Retomar")

        while True:
            try:
                opcao = int(input("Escolha a sua opção: "))
                if opcao in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                    return opcao
                print("Opção inválida.")
            except ValueError:
                print("Digite um número válido.")

    def pega_dados_coleta(self):
        print(" ====== Dadods da Coleta ====== ")
        while True:
            id_coleta = input("ID: ")
            if id_coleta.isdigit() and int(id_coleta) > 0:
                id_coleta = int(id_coleta)
                break
            print("ID inválido.")

        data = input("Data: (DD/MM/AAAA) ")
        while not data:
            print("Data não pode estar vazia!")
            data = input("Data: (DD/MM/AAAA) ")

        cpf_colaborador = input("CPF do colaborador: ").strip()
        cpf_colaborador = ''.join(filter(str.isdigit, cpf_colaborador))

        codigo_barreira = input("Código da ecobarreira: ")
        codigo_barreira = ''.join(filter(str.isdigit, codigo_barreira))

        return {"id": id_coleta,
                "data": data,
                "cpf_colaborador": cpf_colaborador,
                "codigo_barreira": codigo_barreira
                }

    def pega_dados_lixo(self):
        id_coleta = input("Digite o id da Coleta: ")
        tipo_lixo = input("Digite o tipo de lixo: ").strip()
        while True:
            quantidade = input("Digite a quantidade: ")
            if quantidade.isdigit and float(quantidade) > 0:
                return {"id_coleta": id_coleta,
                        "tipo_lixo": tipo_lixo,
                        "quantidade": quantidade}
            else:
                print("Quantidade inválida!")

    def pega_indice_lixo(self):
        try:
            return int(input("Informe o índice do lixo que deseja remover: "))
        except ValueError:
            self.mostra_mensagem("Entrada inválida. Digite um número inteiro.")
            return self.pega_indice_lixo()

    def mostra_coleta(self, dados_coleta):
        print("ID: ", dados_coleta["id"])
        print("Data: ", dados_coleta["data"])
        print("Colaborador: ", dados_coleta["colaborador"])
        print("Ecobarreira: ", dados_coleta["ecobarreira"])
        print("--------------\n")

    def busca_coleta(self):
        while True:
            id_str = input("ID da coleta: ")
            if id_str.isdigit():
                return int(id_str)
            print("ID inválido. Use apenas números.")

    def mostra_mensagem(self, mensagem):
        print(mensagem)
