#Verifique se a média de três números é menor que 25.
num=int(input('Digite um numero: '))
num1=int(input('Digite um numero: '))
num2=int(input('Digite um numero: '))
media=(num+num1+num2)/3
if media<25:
    print('a média dos numeros digitados é menor que 25')
else:
    print('Tente de novo')
11