#
def aplicar_desconto(valor):
    return valor * 0.9


valor = float(input('Digite o valor da compra: '))
resultado = aplicar_desconto(valor)
print(f'Valor com 10% de desconto: {resultado:.2f}')
