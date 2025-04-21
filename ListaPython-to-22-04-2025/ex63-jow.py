#Verifique se a multiplicação de dois números é maior que 500.
num=int(input('Digite um numero:'))
num1=int(input('Digite um numero:'))
mult=num*num1
if mult>500:
    print('A multiplicação entre os numero é: %.0i'%mult)
else:
    print('tente de novo, a multiplicação é menor que 500')