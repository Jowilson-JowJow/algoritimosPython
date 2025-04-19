#Verifique se a multiplicação de dois números é maior que 100.
num=int(input('Digite um numero: '))
num1=int(input('Digite um numero: '))
num2=int(input('Digite um numero: '))
media=num*num1*num2
if media>100:
    print('o produto entre os tres numeros é maior que 100')
else:
    print('tente de novo')
    