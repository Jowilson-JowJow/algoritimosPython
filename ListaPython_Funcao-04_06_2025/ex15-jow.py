#Escreva uma função que receba uma palavra e retorne True se ela for um palíndromo.
def word():
    x=input('Digite uma palavra: ')
    inverter=x[::-1]
    print(x)
    print(inverter)
    if x==inverter:
        print('TRUE')
    else:
        print('FALSE')

word()