#Verifique se um número é múltiplo de 2 e 5.
num=int(input('Digite um numero: '))
num1=num%2
num2=num%5
if num1==0 and num2==0:
    print('O numero digitado é multiplo de 2 e 5')
else:
    print('Tente de novo')