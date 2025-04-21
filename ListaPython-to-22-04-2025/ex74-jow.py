#Verifique se a média de três números é maior que 40.
num=int(input('Digite um numero: '))
num1=int(input('Digite um numero: '))
num2=int(input('Digite um numero: '))
media=(num+num1+num2)/3
if media>40:
    print('a média dos numeros digitados é maior que 40')
else:
    print('Tente de novo')
