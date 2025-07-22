#Verifique se um número é maior que 50, mas não é múltiplo de 5.
num=int(input('Digite um numero:'))
num1=num%5
if num>50 and num1!=0:
    print('Não é multiplo de 5 e maior que 50')
else:
    print('Tente de novo kkkkkk')