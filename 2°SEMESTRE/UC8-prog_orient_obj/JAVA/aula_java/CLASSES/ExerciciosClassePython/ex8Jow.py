# 8 - Classe Triangulo: Crie uma classe que modele um triangulo: 
# 	– Atributos: LadoA, LadoB, LadoC
# 	– Métodos: calcular Perímetro, getMaiorLado; 
# Crie instâncias desta classe. Ele deve pedir ao usuário que informe as medidas de um triangulo. Depois, deve criar um objeto com as medidas e imprimir sua área e maior lado.

class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA=ladoA
        self.ladoB=ladoB
        self.ladoC=ladoC

    def calcularPerimetro(self):
        return self.ladoA + self.ladoB + self.ladoC
    
    def get_MaiorLado(self):
        if (self.ladoA>self.ladoB and self.ladoA>self.ladoB):
            return self.ladoA
        elif (self.ladoB>self.ladoA and self.ladoB>self.ladoC):
            return self.ladoB
        else:
            return self.ladoC


trian1=Triangulo(10,12,5)
perimetro=trian1.calcularPerimetro()
maiorLado=trian1.get_MaiorLado()
print(f"O Triangulo dado tem perimetro = {perimetro} u.m")
print(f"O maior lado do Triangulo dado é = {maiorLado} u.m")