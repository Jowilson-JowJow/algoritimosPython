#Crie uma lista de palavras e converta todas para minúsculas.
lista=['ANA', 'CARLA', 'JOANA']
print('lista1',lista)
lista1=[]
for x in lista:
    lista1.append(x.lower())
print('lista1 minuscula',lista1)

#outra forma
lista2=['carlos', 'marcelo', 'joão']
print('lista2',lista2)
lista3=[x.lower() for x in lista2]
print('lista2 minuscula',lista3)