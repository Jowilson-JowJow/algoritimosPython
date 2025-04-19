#Verifique se a soma de dois números é menor que 10 ou maior que 100.
num=int(input('Digite um numero:'))
num1=int(input('Digite um numero:'))
soma=num+num1
if soma<10 or soma>100:
    print('numeros no parametro exigido')
else:
    print('Tente de novo')
   