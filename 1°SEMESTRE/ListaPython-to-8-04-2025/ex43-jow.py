#Crie uma lista com os números de 1 a 5 e eleve cada um ao quadrado.
lista=[1,2,3,4,5]
lista1=[x**2 for x in lista]
print(lista)
print(lista1)
#outra forma
lista2=list(map(lambda x: x**2, lista))
print(lista2) 