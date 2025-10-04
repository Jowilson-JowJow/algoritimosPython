# 6 - Classe Círculo: crie uma classe que represente um círculo. Esta classe deve possuir o seguinte atributo:
# raio
# A classe deve ter os seguintes métodos:
# imprimir o valor do raio;
# calcular a área do círculo;
# calcular a circunferência do círculo.
import math
class Circulo:
    def __init__(self, raio):
        self.raio=raio

    def valorRaio(self):
        print(f"O Raio é: {self.raio} cm" )

    def areaCirculo(self):
        return math.pi*(self.raio**2)
    
    def perimetroCirculo(self):
        return 2*math.pi*self.raio
        
circ1=Circulo(30)
circ1.valorRaio()
print(f"A area do circulo é: {circ1.areaCirculo():.2f} cm²")
print(f"O perimetro do circulo é: {circ1.perimetroCirculo():.2f} cm")
