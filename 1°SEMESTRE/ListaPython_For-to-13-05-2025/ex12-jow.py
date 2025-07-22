# #Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
# Foram obtidos os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). 

# Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
# Lista para armazenar dados das cidades
maior_indice = 9999999999999999999
menor_indice = -999999999999999999
cidade_maior = 0
cidade_menor = 0
total_veiculos = 0
total_acidentes = 0
contador = 0
for i in range(5):
    print(f"\n--- Cidade {i + 1} ---")
    codigo = int(input("Código da cidade: "))
    veiculos = int(input("Número de veículos de passeio (em 1999): "))
    acidentes = int(input("Número de acidentes com vítimas (em 1999): "))
    total_veiculos += veiculos
    if veiculos < 2000:
        total_acidentes += acidentes
        contador += 1
    if i == 0:
        maior_indice = acidentes
        menor_indice = acidentes
        cidade_maior = codigo
        cidade_menor = codigo
    else:
        if acidentes > maior_indice:
            maior_indice = acidentes
            cidade_maior = codigo
        if acidentes < menor_indice:
            menor_indice = acidentes
            cidade_menor = codigo
print("\n======= RESULTADOS =======")
print(f"Maior número de acidentes: {maior_indice} (Cidade {cidade_maior})")
print(f"Menor número de acidentes: {menor_indice} (Cidade {cidade_menor})")
print(f"Média de veículos nas 5 cidades: {total_veiculos / 5:.2f}")

if contador > 0:
    media_acidentes = total_acidentes / contador
    print(f"Média de acidentes nas cidades com menos de 2000 veículos: {media_acidentes:.2f}")
else:
    print("Nenhuma cidade com menos de 2000 veículos.")
