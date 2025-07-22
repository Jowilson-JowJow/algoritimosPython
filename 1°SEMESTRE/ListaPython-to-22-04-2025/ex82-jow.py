#Verifique se a multiplicação de dois números é ímpar.
num=int(input('Digite um numero: '))
num1=int(input('Digite um numero: '))
if (num*num1)%2!=0:
    print('O produto dos numeros é impar')
else:
    print('Tente de novo')