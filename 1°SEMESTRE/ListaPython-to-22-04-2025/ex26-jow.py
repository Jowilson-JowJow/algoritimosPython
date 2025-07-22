#Verifique se um número é maior que 0, mas não é múltiplo de 5.
num=int(input('Digite um numero: '))
num1=num%5
if num>0 and num1!=0:
    print('O numero é maior que zero e não multiplo de 5')
else:
    print('tente de novo')
    