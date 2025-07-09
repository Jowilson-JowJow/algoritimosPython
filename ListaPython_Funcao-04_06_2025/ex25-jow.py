#Crie uma função que receba uma lista e retorne os elementos únicos (sem usar set).
def elementos_unicos(lista):
    unicos = []
    for item in lista:
        if item not in unicos:
            unicos.append(item)
    print(unicos)


lista1=[]
while True:
    menu=input('Digite:\n1 -- para acrescentar um numero a lista\n2 -- para sair.\n')
    if menu=='1':    
        x=int(input("digite um numero para acrescentar a lista.\n"))
        lista1.append(x)
    elif menu=='2':
        break
    else:
        print('Digite 1 ou 2')
print(lista1)

        
elementos_unicos(lista1)

