#Crie uma lista e multiplique todos os seus elementos por 2.
lista=[102, 202, 500]
lista1=[x*2 for x in lista]
print(lista1)
#outra forma
mult=3
lista2=list(map(lambda x: x*mult, lista))
print(lista2)
#outra forma
# import numpy as np
# lista3=np.array([16,32,64])
# lista4=lista3*2
# print(lista3,'\n',lista4)
