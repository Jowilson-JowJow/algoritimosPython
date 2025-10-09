# 10 - Classe Carro: Crie uma classe que modele um Carro. Esta classe deve possuir os seguintes atributos:
# Modelo, Marca, Cor, Ano, Valor, Nível (default 5) , Consumo
# A classe deve ter o seguintes métodos:
# ligar(); - para andar o carro deve estar ligado, use variável booleana.
# abastecer(); - deve incrementar no nível do tanque de combustível
# andar(); - recebe a distancia em km que o veículo andou
# verificar_nível(); - o deve criar uma forma de calcular quantos litros de comb. foram gasto por km
# calcular_imposto()  -  deve considerar o IPVA do carro em 2,5% do valor.

class Carro:
    def __init__(self, modelo, marca, cor, ano, valor, consumo):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = 5
        self.consumo = consumo
        self.status=False

    def ligar(self):
        if (self.status==False):
            self.status=True
            return self.status

    def abastecer(self):
        if(self.nivel==1):
            print("ABASTEÇA O CARRO")

    def andar(self,km):
        print(f"O carro andou {km} km")

    def verificar_nivel(self):
        print(f"O carro gastou {self.consumo} litros por km")

    def calcular_imoposto(self):
        ipva=self.valor*0.025
        print(f"O IPVA é R$ {ipva}")
        

carro1=Carro("uno","fiat","branco",2010,15000, 15)
if carro1.ligar():
    print("CARRO LIGADO")

carro1.abastecer()
carro1.andar(200)
carro1.verificar_nivel()
carro1.calcular_imoposto()