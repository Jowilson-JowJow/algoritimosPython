#Verifique se um número é positivo e múltiplo de 3, mas não de 5.
num=int(input('Digite um numero: '))
num1=num%3
num2=num%5
if num>0 and num1==0 and num2!=0:
    print('Numeros nos parametros')
else:
    print('tente de novo')


