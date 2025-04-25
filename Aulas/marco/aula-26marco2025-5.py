#escreva uma função chamada que receba uma lista de numeros e retorne
# a soma cumulativa; isto é, uma nova lista onde o i-ésimo é a soma dos 
#dos primeiros i+1 elementos da lista origina. poe exemplo lista=[1,2,3] resulatdo [1,3,6]
lista=[1,2,3]
print([lista[0],lista[0]+lista[1],lista[0]+lista[1]+lista[2]])

#ou

lista1=[0,0,0]
lista1[0]=sum(lista[0:1])
lista1[1]=sum(lista[0:2])
lista1[2]=sum(lista[0:3])
print(lista1)