import math

class Circulo:
    def __init__(self, raio):
        """Inicializa o raio do círculo"""
        self.raio = raio

    def imprimir_raio(self):
        """Imprime o valor do raio"""
        print(f"Raio do círculo: {self.raio} unidades")

    def calcular_area(self):
        """Calcula e retorna a área do círculo"""
        area = math.pi * self.raio ** 2
        print(f"Área do círculo: {area:.2f} unidades quadradas")
        return area

    def calcular_circunferencia(self):
        """Calcula e retorna a circunferência do círculo"""
        circunferencia = 2 * math.pi * self.raio
        print(f"Circunferência do círculo: {circunferencia:.2f} unidades")
        return circunferencia

circulo1 = Circulo(5)

circulo1.imprimir_raio()
circulo1.calcular_area()
circulo1.calcular_circunferencia()
