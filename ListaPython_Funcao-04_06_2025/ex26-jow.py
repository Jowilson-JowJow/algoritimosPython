#Crie uma função que receba uma lista e um número n, e retorne os n maiores valores da lista.
def maiores_valores(lista, n):
    if n > len(lista):
        return "Erro: 'n' é maior que o tamanho da lista."
    return sorted(lista, reverse=True)[:n]


lista1=[]
while True:
    menu=int(input('Digite:\n1 -- para adicionar numero na lista\n2 -- para sair\n'))
    if menu==2:
        break
    elif menu==1:
        x=int(input('Digite um numero para adicionar a lista: '))
        lista1.append(x)
    else:
        print('Digite 1 ou 2')
    print(f'A lista é {lista1}')
y=int(input('Digite um numero (esse numero é os primeiros maiores numeros dessa lista): \n'))
print(f"Os {y} maiores valores são: {maiores_valores(lista1, y)}")


