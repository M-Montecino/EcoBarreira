class Relatorio:
    def __init__(self):
        pass

    def gerar_relatorio_colaborador(self, colaborador, lista_coletas):
        total_coletas = 0
        total_lixo = 0

        for coleta in lista_coletas:
            if coleta.colaborador == colaborador:
                total_coletas += 1
                total_lixo += sum(lixo.quantidade for lixo in coleta.lixos)

        return {
            "nome": colaborador.nome,
            "cpf": colaborador.cpf,
            "total_coletas": total_coletas,
            "total_lixo": total_lixo
        }

    def gerar_relatorio_ecobarreira(self, ecobarreira, lista_coletas):
        total_coletas = 0
        total_lixo = 0

        for coleta in lista_coletas:
            if coleta.ecobarreira == ecobarreira:
                total_coletas += 1
                total_lixo += sum(lixo.quantidade for lixo in coleta.lixos)

        return {
            "codigo": ecobarreira.codigo,
            "cidade": ecobarreira.cidade,
            "total_coletas": total_coletas,
            "total_lixo": total_lixo
        }

    def melhor_colaborador(self, lista_colaboradores, lista_coletas):
        melhor = None
        maior_lixo = -1

        for colaborador in lista_colaboradores:
            total = 0
            for coleta in lista_coletas:
                if coleta.colaborador == colaborador:
                    total += sum(lixo.quantidade for lixo in coleta.lixos)
            if total > maior_lixo:
                maior_lixo = total
                melhor = colaborador

        if melhor:
            return {
                "nome": melhor.nome,
                "cpf": melhor.cpf,
                "total_lixo": maior_lixo
            }
        return None

    def melhor_ecobarreira(self, lista_ecobarreiras, lista_coletas):
        melhor = None
        maior_lixo = -1

        for ecobarreira in lista_ecobarreiras:
            total = 0
            for coleta in lista_coletas:
                if coleta.ecobarreira == ecobarreira:
                    total += sum(lixo.quantidade for lixo in coleta.lixos)
            if total > maior_lixo:
                maior_lixo = total
                melhor = ecobarreira

        if melhor:
            return {
                "codigo": melhor.codigo,
                "cidade": melhor.cidade,
                "total_lixo": maior_lixo
            }
        return None

    def lixo_total(self, lista_coletas):
        total = 0
        for coleta in lista_coletas:
            total += sum(lixo.quantidade for lixo in coleta.lixos)
        return total
