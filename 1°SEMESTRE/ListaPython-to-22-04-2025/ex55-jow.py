#Verifique se um número é negativo e divisível por 5.
num=int(input('Digite um numero: '))
num1=num%5
if num<0 and num1==0:
    print('O numero esta nos parameros exigido')
else:
    print('tente de novo')
