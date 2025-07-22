#- Verifique se um número é múltiplo de 5 e 7.
num=int(input('Digite um numero: '))
num1=num%5
num2=num%7
if num1==0 and num2==0:
    print('O numero digitado é multiplo de 5 e 7')
else:
    print('Tente de novo')