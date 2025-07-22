#Verifique se a soma de três números é maior que 100 e menor que 200.
num=int(input('Digite um numero: '))
num1=int(input('Digite um numero: '))
num2=int(input('Digite um numero: '))
if 100<(num+num1+num2)<200:
    print('A soma dos numeros ggitados esta no intervalo de 100 a 200')
else:
    print('Tente de novo')
