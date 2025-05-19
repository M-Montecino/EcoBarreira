class TelaControlador:
    def tela_opcoes(self):
        print("------CastorEco-------")
        print("Escolha sua opção:")
        print("1 --- Colaborador")
        print("2 --- EcoBarreira")
        print("3 --- Coleta")
        print("4 --- Sensor")
        print("0 --- Finalizar Sistema")
        opcao = int(input("Escolha sua opção:"))
        return opcao