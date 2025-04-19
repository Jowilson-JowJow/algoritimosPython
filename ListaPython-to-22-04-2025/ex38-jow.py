#Verifique se um número é múltiplo de 10.
num=int(input('Digite um numero: '))
num1=num%10
if num1==0:
    print('O numero digitado é multiplo de 10')
else:
    print('Tente de novo')
