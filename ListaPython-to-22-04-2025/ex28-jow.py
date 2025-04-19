#Verifique se uma pessoa é adulta (18-64 anos).
idade=int(input('Digite a sua idade'))
if idade>18 and idade<64:
    print('Você é um Adulto')
else:
    print('Você é adolescente ou idoso')
