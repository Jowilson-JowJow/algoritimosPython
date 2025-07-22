#Crie uma lista e some 10 a cada elemento.
lista=[202,52,63,78,987,100]
lista1=[x+10 for x in lista]
print(lista)
print(lista1)
#outra forma
mult=10
lista2=list(map(lambda x: x+mult, lista))
print(lista)
print(lista2)