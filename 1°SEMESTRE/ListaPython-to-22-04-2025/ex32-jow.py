#Verifique se a média de três números é maior que 50.
num=int(input('Digite um numero: '))
num1=int(input('Digite um numero: '))
num2=int(input('Digite um numero: '))
media=(num+num1+num2)/3
if media>50:
    print('a media é maior que 50')
else:
    print('tente de novo')
    