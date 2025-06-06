#Crie uma função que calcule o fatorial de um número (sem usar recursão).
def fat (pos):
    resultado=1
    for n in range(1,pos+1):
        resultado=resultado*n
    return resultado
a=int(input('Enter number to get its factorial: '))
print(fat(a))