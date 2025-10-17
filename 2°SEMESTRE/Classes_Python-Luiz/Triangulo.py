import math

class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        """Inicializa os atributos do triângulo"""
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcular_perimetro(self):
        """Calcula o perímetro do triângulo"""
        return self.ladoA + self.ladoB + self.ladoC

    def get_maior_lado(self):
        """Retorna o maior lado do triângulo"""
        return max(self.ladoA, self.ladoB, self.ladoC)

    def calcular_area(self):
        """Calcula a área do triângulo utilizando a fórmula de Herão"""
        s = self.calcular_perimetro() / 2 
        area = math.sqrt(s * (s - self.ladoA) * (s - self.ladoB) * (s - self.ladoC))
        return area


def main():
    ladoA = float(input("Informe o comprimento do Lado A: "))
    ladoB = float(input("Informe o comprimento do Lado B: "))
    ladoC = float(input("Informe o comprimento do Lado C: "))

    triangulo = Triangulo(ladoA, ladoB, ladoC)

    print(f"\nPerímetro do triângulo: {triangulo.calcular_perimetro():.2f}")
    print(f"Maior lado do triângulo: {triangulo.get_maior_lado():.2f}")
    print(f"Área do triângulo: {triangulo.calcular_area():.2f}")

if __name__ == "__main__":
    main()
