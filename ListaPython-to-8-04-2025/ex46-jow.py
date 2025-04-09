#Crie uma lista e utilize max() para encontrar o segundo maior valor.
lista=[2,3,1,5,5,5,6,2,0]
maior=max(lista)
print (maior)
lista.remove(maior)
print(lista)
segundoMaior=max(lista)
print(segundoMaior)
