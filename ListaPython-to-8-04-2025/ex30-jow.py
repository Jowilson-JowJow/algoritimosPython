#Crie uma lista e use .extend() para adicionar vários elementos de outra lista.
lista1=[0,2,4,6,8]#cria a lista 1
lista2=[1,3,5,7,9]#cria a lista 2
print(lista1)#retorna na tela a lista 1
print(lista2)#retorna na tela a lista 2
lista1.extend(lista2)#coloca todos os elementos da lista 2 a partir do ultimo elemento da lista1
print(lista1)#printa a nova lista 1 apos a inseração dos elementos
print(lista2)#printa a lista 2 que não foi alterada
