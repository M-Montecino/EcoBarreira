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

    def mostra_mensagem(self, mensagem):
        print(mensagem)
