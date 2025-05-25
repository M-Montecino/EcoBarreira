class TelaColaborador():
    def tela_opcoes(self):
        print(" ======== Colaboradores ======== ")
        print("Opções:")
        print("1 - Cadastrar Colaborador")
        print("2 - Buscar Coaborador por CPF")
        print("3 - Alterar  Informações do Colaborador")
        print("4 - Excluir Colaborador")
        print("5 - Listar Colaboradores")
        print("0 - Retomar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3, 4, 5]:
                    return opcao
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Por favor, digite um valor válido.")

    def pega_dados_colaborador(self):
        print(" ======== Dados do Colaborador ======== ")

        while True:
            cpf_input = input("CPF: ").strip()
            cpf_limpo = "".join(filter(str.isdigit, cpf_input))

            if cpf_limpo.isdigit() and len(cpf_limpo) == 11:
                cpf = int(cpf_limpo)
                break
            print(
                "CPF inválido. Digite um CPF com 11 dígitos (com ou sem pontos e traço).")

        nome = input("Nome: ").strip()
        while not nome:
            print("Nome não pode estar vazio!")
            input("Nome: ").strip()

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

        estado = input("Estado: (digite a sigla) ").strip().lower()
        while True:
            if len(estado) == 2 and estado.isalpha:
                break
            print("Estado não pode estar vazio!")
            estado = input("Estado: ").strip()

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
        print("--------------\n")

    def busca_colaborador(self):
        while True:
            cpf_input = input(
                "CPF do colaborador que deseja selecionar: ").strip()
            cpf_limpo = "".join(filter(str.isdigit, cpf_input))
            if cpf_limpo.isdigit() and len(cpf_limpo) == 11:
                return int(cpf_limpo)
            print("CPF inválido. Digite novamente")

    def mostra_mensagem(self, mensagem):
        print(mensagem)
