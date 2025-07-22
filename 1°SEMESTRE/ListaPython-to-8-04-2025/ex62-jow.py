#Crie uma lista de palavras e converta todas para maiúsculas.
lista=['ana', 'carla', 'joana']
print('lista1',lista)
lista1=[]
for x in lista:
    lista1.append(x.upper())
print('lista1 maiuscula',lista1)

#outra forma
lista2=['ana', 'carla', 'joana']
print('lista2',lista2)
lista3=[x.upper() for x in lista2]
print('lista2 maiuscula',lista3)
