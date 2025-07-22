#Verifique se um número é múltiplo de 2 e 3.
num=int(input('Digite um numero: '))
print('O numero digitado foi: ', num)
num1=num%2
num2=num%3
if(num1==0 and num2==0):
    print('O numero digitado é multiplo de 2 e 3')
elif(num1==0 ):
    print('O numero digitado é multiplo apenas de 2')
elif (num2==0):
    print('O numero digitado é multiplo apenas de 3')
else:
    print('O numero digitado não é multiplo de 2 e 3')

    