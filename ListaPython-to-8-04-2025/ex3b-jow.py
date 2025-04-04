#Crie uma lista vazia e adicione os números 10, 20 e 30.
#outra forma de fazer
lista=[]#cria lista vazia
print(len(lista))#motra o numero de objetos dentro da lista, como a lista esta vazia deve retornar 0
lista.extend(('10',20,30))
print(lista)#permite adicionar varios elementos de uma vez a lista