#Crie uma lista de 10 elementos e remova os 3 últimos.
lista=[0,1,2,3,4,5,6,7,8,9]
print('essa lista tem',len(lista), 'elementos e a lista é ', lista)
del lista[-3:]
print(lista)