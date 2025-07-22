#Escreva uma função que identifique o segundo maior número em uma lista.
def segundo_maior(lista):
    lista_ordenada = sorted(set(lista), reverse=True)
    if len(lista_ordenada) < 2:
        return None
    return lista_ordenada[1]


lista = []
print('Digite números para a lista (digite "x" para parar):')
while True:
    entrada = input('Número: ')
    if entrada == 'x':
        break
    try:
        lista.append(int(entrada))
    except ValueError:
        print('Digite um número válido.')


resultado = segundo_maior(lista)
print(f'Segundo maior número: {resultado}')
