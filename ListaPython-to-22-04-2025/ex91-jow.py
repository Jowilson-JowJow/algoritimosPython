#Verifique se a soma de dois números é maior que 100 e múltiplo de 10.
num=int(input('Digite um numero: '))
if num>100 and num%10==0:
    print('O numero digitado se enquadra no exigido')
else:
    print('tente de novo')
    