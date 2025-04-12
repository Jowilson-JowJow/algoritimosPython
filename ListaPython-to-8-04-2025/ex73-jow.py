#Crie uma lista de palavras e remova todas que tenham menos de 4 letras.
lista=['ana', 'lu', 'jo', 'amor', 'amores', 'flores','carros']
lista1=[x for x in lista if len(x)>=4]
print(lista1)
lista1=[x for x in lista if len(x)<=3]
print(lista1)