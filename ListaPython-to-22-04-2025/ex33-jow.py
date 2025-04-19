#Verifique se a média de três números é menor que 20.
num=int(input('Digite um numero: '))
num1=int(input('Digite um numero: '))
num2=int(input('Digite um numero: '))
media=(num+num1+num2)/3
if media<20:
    print('a media é menor que 20')
else:
    print('tente de novo')
    