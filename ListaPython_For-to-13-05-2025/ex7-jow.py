#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
#Não pode usar sum, media nem nada. Na Unha
num=int(input('Digite quantos numeros tem o conjunto: '))
x=0
maior=-999999999999999999
menor=9999999999999999999
soma=0
for i in range(num):
    print('Digite',i+1,'° numero: ',end='')
    x=int(input())
    if x>maior:
        maior=x
    if x<menor:
        menor=x
soma=maior+menor
print(f'o maior numero é: {maior}\no menor dos numeros é: {menor}\na soma do maior com o menor numero é {soma}')
