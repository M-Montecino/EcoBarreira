class TelaColaborador():
    def tela_opcoes(self):
        print(" ======== Colaboradores ======== ")
        print("Opções:")
        print("1 - Cadastrar Colaborador")
        print("2 - Buscar Coaborador por CPF")
        print("3 - Alterar  Informações do Colaborador")
        print("4 - Excluir Colaborador")
        print("5 - Listar Colaboradores")

        opcao = int(input("Escolha sua opção:"))
        return opcao

    def pega_dados_colaborador(self):
        print(" ======== Dados do Colaborador ======== ")
        cpf = input("CPF: ")
        nome = input("Nome: ")
        cidade = input("Cidade: ")
        cep = input("Cep: ")
        rua = input("Rua: ")
        complemento = input("Complemento: ")
        estado = input("Estado: ")

        return {"cpf": cpf,
                "nome": nome,
                "cidade": cidade,
                "cep": cep,
                "rua": rua,
                "complemento": complemento,
                "estado": estado
                }

    def mostra_colaborador(self, dados_colaborador):
        print("CPF: ", dados_colaborador["cpf"])
        print("Nome: ", dados_colaborador["nome"])
        print("Cidade: ", dados_colaborador["cidade"])
        print("Cep: ", dados_colaborador["cep"])
        print("Rua: ", dados_colaborador["rua"])
        print("Complemento: ", dados_colaborador["complemento"])
        print("Estado: ", dados_colaborador["estado"])

    def busca_colaborador(self):
        cpf = input("Cpf do colaborador que deseja buscar: ")
        return cpf

    def mostra_mensagem(self, mensagem):
        print(mensagem)
