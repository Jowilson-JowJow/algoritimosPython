#Verifique se um número é maior que 100 e múltiplo de 3.
num=int(input('Digite um numero: '))
num1=num%3
if num>100 and num1==0:
    print('O numero digitado se enquadra no exigido')
else:
    print('tente de novo')
    