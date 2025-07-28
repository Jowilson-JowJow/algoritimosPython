#Crie uma função que calcule juros compostos: montante = capital * (1 + taxa) ** tempo.
def juros_compostos(capital, taxa, tempo):
    return capital * ((1 + taxa) ** tempo)


capital = float(input('Digite o capital inicial: '))
taxa = float(input('Digite a taxa (em decimal, ex: 0.05 para 5%): '))
tempo = int(input('Digite o tempo em períodos: '))
resultado = juros_compostos(capital, taxa, tempo)
print(f'Montante final: {resultado:.2f}')
