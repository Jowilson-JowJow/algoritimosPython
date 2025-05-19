#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
#Não pode usar sum, media nem nada. Na Unha
num=int(input('Digite quantos numeros tem o conjunto: '))
x=0
for i in range(num):
    print('Digite',i+1,'° numero')
    x=int(input())
print(x, end=' ')

#esta errado