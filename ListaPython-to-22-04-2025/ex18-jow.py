#Verifique se a idade de uma pessoa permite votar (maior de 18 anos).
idade=int(input('Digite a sua idade: '))
if idade>=18:
    print('Parabéns, você pode votar')
else:
    print('Espere até ter 18 anos para poder votar')