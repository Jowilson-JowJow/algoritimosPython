#Verifique se um número é divisível por 3 e 5.
num=int(input('Digite um numero: '))
if num%3==0 and num%5==0:
    print('O numero digitado é multiplo de 3 e 5')
else:
    print('tente de novo')