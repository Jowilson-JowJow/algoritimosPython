#Verifique se a média de dois números é menor que 30.
num=int(input('Digite um umero: '))
num1=int(input('Digite um umero: '))
print ("Os numeros digitados foram: ",num,' e ', num1 )
media=(num+num1)/2
if media<30:
    print('A média é menor que 30, a média é: %.2f'%media)
else:
    print('tente de novo, média maior que 30, a média é: %.2f'%media)