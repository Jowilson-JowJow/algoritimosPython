#Verifique se um número é positivo e maior que 100.
num=int(input('Digite um numero: '))
if(num>0 and num>100):
    print('O numero digitado é positivo e maior que 100')
elif(num>0 and num<=100):
    print('O numero digitado é positovo, mas menor que 100')
else:
    print('O numero digitado é neutro ou negativo')
