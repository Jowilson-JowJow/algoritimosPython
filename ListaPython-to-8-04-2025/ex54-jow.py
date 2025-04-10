#Crie uma lista de 10 números e substitua os primeiros 5 por 0.
lista=[0,1,2,3,4,5,6,7,8,9]
print('tem', len(lista), 'elementos nessa lista')
lista[0:5]=[0]*5#cria uma lista com 5 elementos igual a zero e substitui na lista 
print(lista)