#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto 
# indeterminado de temperatura, bem como o mês e o ano que ocorreu essa temperatura, e informe ao final
# a menor e a maior temperaturas informadas, o mês e o ano em que elas ocorrera, bem como a média de todas
# as temperaturas.
# dados=int(input('Digite quantos dados de temperatura será informado:'))
# for i in  range(1,dados+1):
#     temp=float(input('Digite a temperatura:'))
#     mes=input('Digite o mês da medição (ex: jan. fev, ...):')
#     ano=int(input('Digite o ano (no formato aaaa) dessa medida:'))
#     print(lista)
temperaturas = []

quantidade = int(input("Quantas temperaturas deseja informar? "))

for i in range(quantidade):
    print(f"\nRegistro {i+1}:")
    temp = float(input("Digite a temperatura: "))
    mes = input("Digite o mês: ")
    ano = int(input("Digite o ano: "))
    temperaturas.append([temp, mes, ano])

# Processamento dos dados
menor = min(temperaturas, key=lambda x: x[0])
maior = max(temperaturas, key=lambda x: x[0])
media = sum(t[0] for t in temperaturas) / len(temperaturas)

# Exibição dos resultados
print("\n--- Resultados ---")
print(f"Menor temperatura: {menor[0]}°C em {menor[1]}/{menor[2]}")
print(f"Maior temperatura: {maior[0]}°C em {maior[1]}/{maior[2]}")
print(f"Média das temperaturas: {media:.2f}°C")

    
