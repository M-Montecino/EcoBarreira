class TelaRelatorio():
    def tela_opcoes(self):
        print(" ======== Relatório ======== ")
        print("1 - Relatório de Colaborador")
        print("2 - Relatório de Ecobarreira")
        print("3 - Relatório Melhor Colaborador")
        print("4 - Relatório Melhor Barreira")
        print("5 - Lixo total")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3, 4, 5]:
                    return opcao
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Por favor, digite um valor válido.")

    def pega_codigo_ecobarreira(self):
        try:
            codigo = int(input("Digite o código da ecobarreira: "))
            return codigo
        except ValueError:
            print("Código inválido. Digite um número inteiro.")

    def pega_cpf_colaborador(self):
        cpf = input("Digite o CPF do colaborador (apenas números): ").strip()

        if not cpf.isdigit() or len(cpf) != 11:
            print("CPF inválido. Deve conter exatamente 11 dígitos numéricos.")
            return self.pega_cpf_colaborador()

        return cpf

    def mostra_mensagem(self, mensagem):
        print(mensagem)
