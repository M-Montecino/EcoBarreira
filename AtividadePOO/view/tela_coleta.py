class TelaColeta():
    def tela_opcoes(self):
        print(" ======= Coleta ======= ")
        print("Opções: ")
        print("1 - Registrar nova Coleta")
        print("2 - Buscar Coleta por ID")
        print("3 - Alterar dados da Coleta")
        print("4 - Excluir Coleta")
        print("5 - Listar todas as Coletas")

        opcao = int(input("Escolha sua opção: "))
        return opcao

    def pega_dados_coleta(self):
        print(" ====== Dadods da Coleta ====== ")
        id_coleta = input("ID: ")
        data = input("Data (formato: DD/MM/AAAA)")
        cpf_colaborador = input("CPF do colaborador responsável: ")
        codigo_barreira = input("Código da Ecobarreira: ")

        return {"id": id,
                "data": data,
                "cpf_colaborador": cpf_colaborador,
                "codigo_barreira": codigo_barreira
                }
    
    def mostra_coleta(self, dados_coleta):
        print("ID: ", dados_coleta["id"])
        print("Data: ", dados_coleta["data"])
        print("Colaborador: ", dados_coleta["colaborador"])
        print("Ecobarreira: ", dados_coleta["ecobarreira"])
        print("\n")

    def busca_coleta(self):
        id = input("ID da coleta que deseja selecionar: ")
        return id
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)
