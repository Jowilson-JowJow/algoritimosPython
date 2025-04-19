#Verifique se um número é menor que 100 e é par.
num=int(input('"digite um numero: '))
num1=num%2
if num<100 and num1==0:
    print('Numero dentro do exigido')
else:
    print('Tente de novo')