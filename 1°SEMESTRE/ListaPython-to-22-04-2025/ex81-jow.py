#Verifique se a multiplicação de dois números é par.
num=int(input('Digite um numero: '))
num1=int(input('Digite um numero: '))
if (num*num1)%2==0:
    print('O produto dos numeros é par')
else:
    print('Tente de novo')