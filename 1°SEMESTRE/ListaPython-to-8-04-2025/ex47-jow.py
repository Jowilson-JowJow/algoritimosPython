#Crie uma lista e utilize min() para encontrar o segundo menor valor.
lista=[2,3,1,5,5,5,6,2,0]
menor=min(lista)
print (menor)
lista.remove(menor)
print(lista)
segundoMenor=min(lista)
print(segundoMenor)