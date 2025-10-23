# - Classe Transporte: Você deve analisar a hierarquia do transporte tipo Terrestre e da Classe automóvel para criar as subclasses dos tipos de transporte Aéreo e Aquático. Instancie 3 objetos de cada classe e faça os testes nos atributos e métodos específicos de cada subclasse;
# Crie duas subclasses de Aquático e Aéreo, exemplo: 
# Lancha e Navio;
# AviaoMonomotor e AviaoComercial;
# Verifique os atributos e métodos específicos de cada subclasse


class Transporte:
    def __init__(self, modo_transporte):
        self.modo_transporte = modo_transporte

    def mostrar_modo(self):
        print(f"Modo de transporte: {self.modo_transporte}")

class Terrestre(Transporte):
    def __init__(self, modo_transporte, placa, modelo):
        super().__init__(modo_transporte)
        self.placa = placa
        self.modelo = modelo

    def ligar(self):
        print(f"O {self.modelo} com placa {self.placa} está ligado.")

    def desligar(self):
        print(f"O {self.modelo} com placa {self.placa} está desligado.")

class Aereo(Transporte):
    def __init__(self, modo_transporte, tipo_aviao):
        super().__init__(modo_transporte)
        self.tipo_aviao = tipo_aviao

    def decolar(self):
        print(f"O avião {self.tipo_aviao} está decolando.")

    def aterrissar(self):
        print(f"O avião {self.tipo_aviao} está aterrissando.")

class Aquatico(Transporte):
    def __init__(self, modo_transporte, tipo_embarcacao):
        super().__init__(modo_transporte)
        self.tipo_embarcacao = tipo_embarcacao

    def navegar(self):
        print(f"A embarcação {self.tipo_embarcacao} está navegando.")

    def ancorar(self):
        print(f"A embarcação {self.tipo_embarcacao} está ancorando.")

class Automovel(Terrestre):
    def __init__(self, placa, modelo, cor):
        super().__init__("Terrestre", placa, modelo)
        self.cor = cor

    def buzinar(self):
        print(f"O automóvel {self.modelo} com placa {self.placa} está buzinando.")

class AviaoMonomotor(Aereo):
    def __init__(self, tipo_aviao, capacidade):
        super().__init__("Aéreo", tipo_aviao)
        self.capacidade = capacidade

    def voar(self):
        print(f"O avião monomotor {self.tipo_aviao} está voando com capacidade para {self.capacidade} pessoas.")

class AviaoComercial(Aereo):
    def __init__(self, tipo_aviao, companhia_aerea):
        super().__init__("Aéreo", tipo_aviao)
        self.companhia_aerea = companhia_aerea

    def voar(self):
        print(f"O avião comercial {self.tipo_aviao} da companhia {self.companhia_aerea} está voando.")

class Lancha(Aquatico):
    def __init__(self, tipo_embarcacao, velocidade_maxima):
        super().__init__("Aquático", tipo_embarcacao)
        self.velocidade_maxima = velocidade_maxima

    def acelerar(self):
        print(f"A lancha {self.tipo_embarcacao} está acelerando a {self.velocidade_maxima} km/h.")

class Navio(Aquatico):
    def __init__(self, tipo_embarcacao, capacidade):
        super().__init__("Aquático", tipo_embarcacao)
        self.capacidade = capacidade

    def navegar(self):
        print(f"O navio {self.tipo_embarcacao} está navegando com capacidade para {self.capacidade} pessoas.")
