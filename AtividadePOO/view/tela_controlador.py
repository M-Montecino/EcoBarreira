class TelaControlador:
    def tela_opcoes(self):
        print("------CastorEco-------")
        print("Escolha sua opção:")
        print("1 --- Colaborador")
        print("2 --- EcoBarreira")
        print("3 --- Coleta")
        print("4 --- Sensor")
        print("5 --- Relatórios")
        print("0 --- Finalizar Sistema")

        try:
            opcao = int(input("Escolha sua opção: "))
            return opcao
        except ValueError:
            return -1

    def mostra_mensagem(self, mensagem):
        print(mensagem)
