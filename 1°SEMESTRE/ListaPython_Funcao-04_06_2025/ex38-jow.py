#Escreva uma função que calcule a distância entre dois pontos (x1, y1) e (x2, y2).
import math

def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


x1 = float(input('Digite x1: '))
y1 = float(input('Digite y1: '))
x2 = float(input('Digite x2: '))
y2 = float(input('Digite y2: '))


resultado = distancia(x1, y1, x2, y2)
print(f'Distância entre os pontos: {resultado:.2f}')
