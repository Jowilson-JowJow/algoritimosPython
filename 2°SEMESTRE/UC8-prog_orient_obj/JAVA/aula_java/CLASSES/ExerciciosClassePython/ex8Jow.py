# 8 - Classe Triangulo: Crie uma classe que modele um triangulo: 
# 	– Atributos: LadoA, LadoB, LadoC
# 	– Métodos: calcular Perímetro, getMaiorLado; 
# Crie instâncias desta classe. Ele deve pedir ao usuário que informe as medidas de um triangulo. Depois, deve criar um objeto com as medidas e imprimir sua área e maior lado.

class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA=ladoA
        self.ladoB=ladoB
        self.ladoC=ladoC

    