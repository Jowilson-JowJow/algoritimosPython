# Crie uma classe que modele um carro
# (a) Atributos: marca, ano e prec¸o
# (b) M´etodos: mostrar prec¸o e de exibic¸ ˜ao dos dados
# Leia os dados de 5 carros e um valor p, Mostre as informac¸ ˜oes de todos os carros com
# prec¸o menor que p.

class Carro:

    def __init__(self, marca, ano, preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco

    def mostrar_preco(self):
        return f"R$ {self.preco:,.2f}"

    def exibir_dados(self):
        print("-" * 25)
        print(f"Marca: {self.marca}")
        print(f"Ano: {self.ano}")
        print(f"Preço: {self.mostrar_preco()}")
        print("-" * 25)
        
    def get_preco(self):
        return self.preco



def ler_carros(n_carros):
    lista_carros = []
    print("\n--- Cadastro de Carros ---")
    for i in range(n_carros):
        print(f"\nDados do {i+1}º Carro:")
        
        marca = input("Marca do carro: ")
        
        while True:
            try:
                ano = int(input("Ano do carro: "))
                break
            except ValueError:
                print("Ano inválido.")

        while True:
            try:
                preco_str = input("Preço do carro (Ex: 50000.00): ").replace(',', '.')
                preco = float(preco_str)
                break
            except ValueError:
                print("Preço inválido.")
        
        novo_carro = Carro(marca, ano, preco)
        lista_carros.append(novo_carro)
        
    return lista_carros


def filtrar_e_mostrar(lista_carros, valor_p):
    encontrados = 0
    print("\n" + "="*40)
    print(f"CARROS COM PREÇO ABAIXO DE R$ {valor_p:,.2f}")
    print("="*40)

    for carro in lista_carros:
        if carro.get_preco() < valor_p:
            carro.exibir_dados()
            encontrados += 1
    
    if encontrados == 0:
        print("Nenhum carro encontrado abaixo do preço limite.")
    
    print("="*40)



NUMERO_DE_CARROS = 5

colecao_carros = ler_carros(NUMERO_DE_CARROS)

print("\n--- Filtragem de Preço ---")
while True:
    try:
        valor_p_str = input("Digite o valor limite (P): ").replace(',', '.')
        valor_p = float(valor_p_str)
        break
    except ValueError:
        print("Valor P inválido.")

filtrar_e_mostrar(colecao_carros, valor_p)