#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido
# por eles.
num1=int(input('Digite um numero: '))
num2=int(input('Digite um numero: '))
if num1>num2:
    for i in range(num2+1,num1):
        print(i)
elif num1==num2:
    print('não existe intervalo')
else:
    for i in range(num1+1, num2):
        print(i)