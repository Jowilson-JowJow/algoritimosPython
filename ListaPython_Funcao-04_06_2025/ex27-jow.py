#Escreva uma função que calcule a área de um triângulo (base × altura ÷ 2).
def area_triangulo (b,h):
    area=(b*h)/2
    print(f'O triangulo tem base {b} cm e sua altura é {h} cm\n a área do triangulo é {area:.2f} cm²')

x=float(input('Digite a altura do triangulo: '))
y=float(input('Digite a base do triangulo: '))
area_triangulo(x,y)
