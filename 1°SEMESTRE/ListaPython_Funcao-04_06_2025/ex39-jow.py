#Crie uma função que receba o valor de uma compra e retorne o valor com 10% de desconto.
def aplicar_desconto(valor):
    return valor * 0.9


valor = float(input('Digite o valor da compra: '))
resultado = aplicar_desconto(valor)
print(f'Valor com 10% de desconto: {resultado:.2f}')
