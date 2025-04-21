#Verifique se a soma de dois números é maior que 50 e múltiplo de 3.
num=int(input('Digite um numero: '))
num1=int(input('Digite um numero: '))
soma=num+num1
if soma>50 and soma%3==0:
    print('A soma dos numeros é maior que 50 e multiplo de 3')
else:
    print('Tente de novo')