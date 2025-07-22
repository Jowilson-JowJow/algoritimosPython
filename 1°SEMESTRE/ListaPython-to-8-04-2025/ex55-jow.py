#Crie uma lista e substitua seus elementos por seus valores absolutos com abs().
lista=[-3,-2,-1,0,1,2,3]
print(lista)
#tem dessa forma(precisei pesquisar)
for i in range(len(lista)):#len--pega o tamanho da lista, range--cria uma sequencia de indices e for i in -- percorre esse indice
    lista[i]=abs(lista[i]) #acessa o elementoa da lista  e pega o valor absoluto
print(lista)
#outra forma "compacta"
lista=[abs(x) for x in lista]
print(lista)