# 19 - Classe Imóvel: Uma Imobiliária precisa de um sistema que controle o aluguel de seus Imóveis. Para isto você deve definir em um módulo a super classe Imóvel com os seguintes atributos:
# InscricaoMunicipal; Valor_aluguel; IPTU;
# Método:
# obter_parcela_IPTU();
# set_valor_aluguel();
# Subclasses:
# Defina as subclasses de Imóvel sendo: Casa, Apartamento; Terreno e Chácara;
# Defina os atributos específicos para cada sub classe, exemplo: piscina, sala_de_estar, 
# Quartos, churrasqueira, área m², elevador, área_de_lazer,   .

class Imovel:
    def __init__(self, inscricao_municipal, valor_aluguel, iptu):
        self.inscricao_municipal = inscricao_municipal
        self.valor_aluguel = valor_aluguel
        self.iptu = iptu

    def obter_parcela_iptu(self):
        parcela_mensal = self.iptu / 12
        return f"Parcela mensal do IPTU: R${parcela_mensal:.2f}"

    def set_valor_aluguel(self, novo_valor):
        self.valor_aluguel = novo_valor
        print(f"Novo valor do aluguel: R${self.valor_aluguel:.2f}")


class Casa(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, piscina, quartos, sala_de_estar):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.piscina = piscina
        self.quartos = quartos
        self.sala_de_estar = sala_de_estar

    def detalhes(self):
        return f"Casa - Piscina: {self.piscina}, Quartos: {self.quartos}, Sala de Estar: {self.sala_de_estar}"


class Apartamento(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, elevador, quartos, area_de_lazer):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.elevador = elevador
        self.quartos = quartos
        self.area_de_lazer = area_de_lazer

    def detalhes(self):
        return f"Apartamento - Elevador: {self.elevador}, Quartos: {self.quartos}, Área de Lazer: {self.area_de_lazer}"


class Terreno(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, area_m2):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.area_m2 = area_m2

    def detalhes(self):
        return f"Terreno - Área: {self.area_m2}m²"


class Chacara(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, churrasqueira, area_m2, quartos):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.churrasqueira = churrasqueira
        self.area_m2 = area_m2
        self.quartos = quartos

    def detalhes(self):
        return f"Chácara - Churrasqueira: {self.churrasqueira}, Área: {self.area_m2}m², Quartos: {self.quartos}"

casa = Casa("12345", 1500, 1800, True, 3, "Ampla")
print(casa.detalhes())
print(casa.obter_parcela_iptu())

casa.set_valor_aluguel(1800)

apartamento = Apartamento("67890", 2500, 1200, True, 2, "Salão de Festas")
print(apartamento.detalhes())