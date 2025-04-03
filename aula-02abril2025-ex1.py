#criar uma lista=[0,1,2,3,4,5,6,7,8,9,10] printar (intervalo de 1 a 9), (intervalo de 8 a 10), (numeros pares), (numeros impares), (lista reversa)
lista=[0,1,2,3,4,5,6,7,8,9,10]
print(lista[1:10])#para printar uma parte da lista por indice

print(lista[8:11])#nesse caso é codigo fica mais efetivo do que o modo da linha 6. tem a mesma função do comando na lina 3
print(lista[8:11:1])

print(lista[2::2]) #le apenas o elemento a partir do indice inicial pulando de 2 em 2, esse codigo é mais eficiente que o codigo da linha 9 
print(lista[2:11:2])

print(lista[1::2])

print(lista[::-1])#ele printa a lista de forma reversa. duvida por que ::
lista.sort(reverse=True)#comando para pegar a lista e fazer ela reversa isso muda a lista a partir deste comando
print(lista)
