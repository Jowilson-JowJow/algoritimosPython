#Crie uma lista e transforme-a em uma string separada por vírgulas usando .join().
lista=[0,1,2,3,4,5,6,7,8,9]
print('lista',lista, '\n',len(lista),' elementos')
#lista= lista.join()#só posso usar assim se os elementos da lista forem string, como são inteiros devo transformar eles em string usando o comando map(str,lista)
lista1='-'.join(map(str,lista))
print(lista1)