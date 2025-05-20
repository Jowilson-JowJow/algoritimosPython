#A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
lista=[0,1]
n=int(input('Digite quantos numeros deseja que a sequencia de fibonacci vai ter: '))
x=0
for i in range(1,n):
    x=lista[-1]+lista[-2]
    lista.append(x)
print(lista)
    