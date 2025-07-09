#Crie uma função que receba uma lista de strings e retorne a maior delas.
def maior_string(lista):
    if not lista:
        return None
    return max(lista, key=len)


lista = []
print('Digite strings para a lista (digite "x" para parar):')
while True:
    entrada = input('String: ')
    if entrada == 'x':
        break
    lista.append(entrada)


resultado = maior_string(lista)
print(f'Maior string: {resultado}')
