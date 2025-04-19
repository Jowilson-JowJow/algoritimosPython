#Verifique se um número é negativo ou menor que -10.
num=int(input('Digite um numero:'))
print('o numero digitado foi: ',num)
if(num<0):
    if(num<-10):
        print('O numero digitado é negativo e menor que -10 ')
    elif(num==-10):
        print('O numero digitado é negativo e igual a -10')
    else:
        print('O numeor digitado é negativo mas é maior que -10')
elif(num==0):
    print('O nuero digitado é neutro')
else:
    print('O numero digitado é positivo')
