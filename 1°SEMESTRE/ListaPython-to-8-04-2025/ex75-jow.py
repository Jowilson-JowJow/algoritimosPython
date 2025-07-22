#Crie uma lista e divida-a ao meio em duas listas menores.
lista=['sol', 'casa','arvore','flor','chuva']
metade=len(lista)//2#/ --> divisão float porem para lista // --> divisão inteira
lista1=lista[:metade]
lista2=lista[metade:]
print(lista)
print(lista1)
print(lista2)
