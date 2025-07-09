#Escreva uma função que receba uma lista e retorne um dicionário com a contagem de cada elemento.
# Função que conta os elementos da lista
def contar_elementos(lista):
    contagem = {}
    for elemento in lista:
        if elemento in contagem:
            contagem[elemento] += 1
        else:
            contagem[elemento] = 1
    return contagem

# Entrada de dados pelo usuário
lista = []  # Cria a lista vazia
print('Digite os elementos da lista. Quando quiser parar, digite "x":')

while True:
    entrada = input('Digite um elemento: ').lower()
    if entrada == 'x':
        break
    lista.append(entrada)

# Chama a função e exibe o resultado
resultado = contar_elementos(lista)
print(f'Resultado da contagem: {resultado}')

