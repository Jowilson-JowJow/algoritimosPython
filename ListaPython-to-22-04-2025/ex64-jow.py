#Verifique se a multiplicação de dois números é menor que 1000.
num=int(input('Digite um numero:'))
num1=int(input('Digite um numero:'))
mult=num*num1
if mult<1000:
    print('A multiplicação entre os numero é: %.0i'%mult)
else:
    print('tente de novo, a multiplicação é maior que 1000')