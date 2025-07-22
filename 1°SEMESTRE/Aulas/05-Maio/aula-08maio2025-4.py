#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
#mostre no final a soma dos numeros desse intervalo
num1=int(input('Digite um numero: '))
num2=int(input('Digite um numero: '))
x=0
if num1>num2:
    for i in range(num2+1,num1):
        print(i,end='-')
        x=x+i
    print('\n',x)
elif num1==num2:
    print('não existe intervalo')
else:
    for i in range(num1+1, num2):
        print(i, end=' 5')
        x=x+i
    print('\n',x)
        
#ver esse codigo acho que ele esta errado