#Verifique se a média de dois números é maior que 50.
num=float(input('Digite um umero: '))
num1=float(input('Digite um umero: '))
print ("Os numeros digitados foram: ",num,' e ', num1 )
media=(num+num1)/2
if media>50:
    print('A média é maior que 50, a média é: %.2f'%media)
else:
    print('tente de novo, média menor que 50, a média é: %.2f'%media)