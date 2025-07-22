#Crie uma função que calcule a soma dos dígitos de um número inteiro.
def soma(x):
    texto=str(x)
    result=sum(int(digito) for digito in texto)
    print(result)
    
num=int(input('entered a number: '))
soma(num)