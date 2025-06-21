#Crie uma função que calcule a área de um retângulo (base × altura)
def area(base,altura):
    print(f'{base}x{altura} = {base*altura}')

x=int(input('digite a base do retangulo: '))
y=int(input('digite a altura do retangulo: '))
area(x,y)