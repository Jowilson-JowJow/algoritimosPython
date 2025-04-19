#Verifique se um número é múltiplo de 7.
num=int(input('Digite um numero: '))
num1=num%7
if  num1==0:
    print('O numero é multiplo de 7')
else:
    print('Tente de novo')
