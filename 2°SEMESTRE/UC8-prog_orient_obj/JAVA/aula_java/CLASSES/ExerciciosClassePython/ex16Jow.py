# 16 - Classe Passagem: Crie uma super classe que modele uma Passagem. Esta classe deve possuir os seguintes atributos:
# Preco;
# Assento;
# Método:
# alterar_preco() e escolher_assento();
# Subclasses:
# Defina a subclasse PassagemBus e PassagemAviao com os seguintes atributos: portaodeembarque e checkin para classe PassagemAviao, placa e leito par PassagemBus;
# Crie um novo método específico para cada subclasse. Ex: decolar() e abastecer()

class Passagem:
    def __init__(self, preco, assento):
        self.preco = preco
        self.assento = assento

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"Novo preço da passagem: R${self.preco}")

    def escolher_assento(self, novo_assento):
        self.assento = novo_assento
        print(f"Assento escolhido: {self.assento}")

class PassagemAviao(Passagem):
    def __init__(self, preco, assento, portaodeembarque, checkin):
        super().__init__(preco, assento)
        self.portaodeembarque = portaodeembarque
        self.checkin = checkin

    def decolar(self):
        if self.checkin:
            print(f"Decolando! Porta de embarque: {self.portaodeembarque}")
        else:
            print("Check-in não realizado. Não é possível decolar.")

class PassagemBus(Passagem):
    def __init__(self, preco, assento, placa, leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito

    def abastecer(self):
        print(f"Ônibus {self.placa} sendo abastecido!")

passagem_aviao = PassagemAviao(500, "10A", "Portão 5", True)
passagem_aviao.escolher_assento("12B")
passagem_aviao.decolar()  

passagem_bus = PassagemBus(150, "C10", "ABC1234", True)
passagem_bus.escolher_assento("C15")
passagem_bus.abastecer() 