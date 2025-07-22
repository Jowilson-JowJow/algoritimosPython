#Verifique se a soma de três números é menor que 100.
num=int(input('Digite um numero: '))
num1=int(input('Digite um numero: '))
num2=int(input('Digite um numero: '))
print('Os numeros digitados foram: ',end=' ')
print(num,num1,num2, sep=' -- ')
soma=num+num1+num2
if soma<100:
    print('A soma dos numeros digitados é: ', soma)
else:
    print('Tente de novo a soma não passou de 100')