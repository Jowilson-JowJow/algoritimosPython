# 18 - Classe Brinquedos: Andy Davis precisa classificar seus brinquedos por Subclasses, sabemos que cada brinquedo tem atributos e métodos diferentes, exemplo Buzz Lightyear voa e Woody laça. Defina principais atributos:
# Nome, Cor, Tamanho, Preço;
# Método:
# brincar(); - fazer um print simples, estou brincando com {nome do brinquedo}
# Subclasses:
# Crie 5 sub classes de brinquedos com seus respectivos atributos e métodos.
# Utilize o polimorfismo para reescrever o método herdado da super classe


# Superclasse Brinquedo
class Brinquedo:
    def __init__(self, nome, cor, tamanho, preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        print(f"Estou brincando com o {self.nome}")

class Buzz(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, pode_voar):
        super().__init__(nome, cor, tamanho, preco)
        self.pode_voar = pode_voar

    def brincar(self):
        if self.pode_voar:
            print(f"Estou brincando com o {self.nome}. Prepare-se para decolar!")
        else:
            print(f"Estou brincando com o {self.nome}, mas não consigo voar.")

class Woody(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, pode_lacar):
        super().__init__(nome, cor, tamanho, preco)
        self.pode_lacar = pode_lacar

    def brincar(self):
        if self.pode_lacar:
            print(f"Estou brincando com o {self.nome}. Vamos laçar!")
        else:
            print(f"Estou brincando com o {self.nome}, mas não consigo laçar.")

class Boneca(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, pode_dancar):
        super().__init__(nome, cor, tamanho, preco)
        self.pode_dancar = pode_dancar

    def brincar(self):
        if self.pode_dancar:
            print(f"Estou brincando com a {self.nome}. Ela está dançando!")
        else:
            print(f"Estou brincando com a {self.nome}, mas ela não dança.")

class CarroDeCorrida(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, pode_acelerar):
        super().__init__(nome, cor, tamanho, preco)
        self.pode_acelerar = pode_acelerar

    def brincar(self):
        if self.pode_acelerar:
            print(f"Estou brincando com o {self.nome}. Vroom! Vamos acelerar!")
        else:
            print(f"Estou brincando com o {self.nome}, mas não posso acelerar.")

class UrsoDePelucia(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, pode_abraçar):
        super().__init__(nome, cor, tamanho, preco)
        self.pode_abraçar = pode_abraçar

    def brincar(self):
        if self.pode_abraçar:
            print(f"Estou brincando com o {self.nome}. Ele me dá um grande abraço!")
        else:
            print(f"Estou brincando com o {self.nome}, mas ele não consegue me abraçar.")

buzz = Buzz("Buzz Lightyear", "Branco e Verde", "30cm", 150, True)
woody = Woody("Woody", "Marrom", "35cm", 120, True)
boneca = Boneca("Boneca Barbie", "Rosa", "25cm", 80, False)
carro = CarroDeCorrida("Carro de Corrida", "Vermelho", "20cm", 100, True)
urso = UrsoDePelucia("Urso de Pelúcia", "Bege", "50cm", 60, True)

buzz.brincar()
woody.brincar()
boneca.brincar()
carro.brincar()
urso.brincar()