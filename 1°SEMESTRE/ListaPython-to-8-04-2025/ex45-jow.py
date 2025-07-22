#Crie uma lista de números e calcule sua média com sum(lista) / len(lista).
lista=[1,2,3,5,8,11,8,5,3,2,1]
print('A lista é: ',lista)
soma=sum(lista)
print('A soma dos elementos da lista é: ', soma)
numElementos=len(lista)
print('O numero de elementos nessa lista é: ', numElementos)
media=soma/numElementos
print('A média dos elementos da lista é: %.2f' % media)