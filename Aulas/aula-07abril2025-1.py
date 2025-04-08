idade=int(input('Digite a sua idade: '))
if idade >=16 and idade <18:# se verdadeiro
    print('pode votar')
elif idade <16:
    print('Apenas estude')
else:
    print('Pode dirigir')
