#Verifique se um número é maior que 0 e par.
num=int(input('Digite um numero: '))
num1=num%2
if num1==0 and num>0:
    print("O numero é maior que zero e par")
elif num1!=0 and num>0:
    print('O numero é maior que zero e impar')
elif num1!=0 and num<0:
    print('O numero é menor que zero e impar')
elif num1==0 and num<0:
    print('O numero é menor que zero e par')
else:
    print('O numer digitado é zero')
