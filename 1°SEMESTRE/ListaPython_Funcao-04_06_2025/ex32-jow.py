#Crie uma função que retorne os números pares de uma lista usando list comprehension.
def lista1():
    lista = []
    while True:
        menu = int(input('Digite:\n1 -- para iniciar a lista\n2 -- sair: '))
        if menu == 1:
            while True:
                entrada = input('Digite um numero para acrescentar na lista (quando quiser parar só digitar x): ').lower()
                if entrada == 'x':
                    print(lista)
                    break
                try:
                    num = int(entrada)
                    lista.append(num)
                except ValueError:
                    print('Por favor, digite um número válido ou "x" para sair.')
        elif menu == 2:
            break
        else:
            print("Digite 1 ou 2")
    return lista


def encontrar_pares(lista):
    pares = [num for num in lista if num % 2 == 0]
    return pares

def lista_pares():
    lista = lista1()
    pares = encontrar_pares(lista)
    print(f'Os números pares desta lista são: {pares}')


lista_pares()

