class TelaControlador:
    def tela_opcoes(self):
        print("------CastorEco-------")
        print("Escolha sua opção:")
        print("1 --- Colaborador")
        print("2 --- EcoBarreira")
        print("3 --- Coleta")
        print("4 --- Sensor")
        print("0 --- Finalizar Sistema")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Por favor, digite um valor válido.")
