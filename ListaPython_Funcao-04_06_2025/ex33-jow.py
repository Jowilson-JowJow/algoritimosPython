#Escreva uma função que recebe um número decimal e retorna sua representação binária.
def decimal_para_binario(numero):
    binario = bin(numero)[2:]
    return binario

decimal = int(input("Digite um número decimal: "))
resultado = decimal_para_binario(decimal)
print(f'O número {decimal} em binário é: {resultado}')
