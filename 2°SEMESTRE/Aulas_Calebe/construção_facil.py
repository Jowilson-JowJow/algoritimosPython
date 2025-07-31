import os
import datetime

os.makedirs("2°SEMESTRE/Aulas_Calebe", exist_ok=True)# Garante que a pasta existe

def menu():# Menu principal
    while True:
        print('\n--- MENU PRINCIPAL ---')
        print('1 - Cadastrar Produto')
        print('2 - Entrada no Estoque')
        print('3 - Cadastrar Cliente')
        print('4 - Cadastrar Vendedor')
        print('5 - Registrar Venda')
        print('6 - Relatórios')
        print('0 - Sair')

        opcao = input('Escolha uma Opção:\n ')

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            entrada_estoque()
        elif opcao == '3':
            cadastrar_cliente()
        elif opcao == '4':
            cadastrar_vendedor()
        elif opcao == '5':
            registrar_venda()
        elif opcao == '6':
            gerar_relatorios()
        elif opcao == '0':
            print('Saindo do Sistema...')
            break
        else:
            print('Opção Inválida.\nTente novamente.\n')

def cadastrar_produto():#função para cadastrar o produto
    codigo = input('Digite o código do produto: ')
    nome = input('Digite o nome do produto: ')
    categoria = input('Digite a categoria (elétrica, hidráulica, etc): ')
    unidade_medida = input('Unidade de medida (kg, m², saco, etc): ')
    estoque_min = input('Estoque mínimo: ')
    estoque_max = input('Estoque máximo: ')
    preco_custo = input('Preço de custo: ')
    preco_venda = input('Preço de venda: ')
    quantidade = input('Quantidade inicial: ')

    with open('2°SEMESTRE/Aulas_Calebe/produtos.txt', 'a') as f:
        f.write(f'{codigo};{nome};{categoria};{unidade_medida};{estoque_min};{estoque_max};{preco_custo};{preco_venda};{quantidade}\n')

    print('Produto cadastrado com sucesso.\n')

def entrada_estoque():
    codigo = input('Digite o código do produto: ')
    quantidade_adicional = int(input('Digite a quantidade a adicionar ao estoque: '))
    linhas = []
    atualizado = False

    with open('2°SEMESTRE/Aulas_Calebe/produtos.txt', 'r') as f:
        for linha in f:
            dados = linha.strip().split(";")
            if dados[0] == codigo:
                dados[8] = str(int(dados[8]) + quantidade_adicional)
                atualizado = True
                print('Estoque atualizado com sucesso.')
            linhas.append(";".join(dados))

    if not atualizado:
        print('Produto não encontrado.')

    with open('2°SEMESTRE/Aulas_Calebe/produtos.txt', 'w') as f:
        for linha in linhas:
            f.write(f'{linha}\n')

def cadastrar_cliente():
    cpf = input('CPF do cliente: ')
    nome = input('Nome do cliente: ')
    telefone = input('Telefone: ')
    endereco = input('Endereço: ')

    with open('2°SEMESTRE/Aulas_Calebe/clientes.txt', 'a') as f:
        f.write(f'{cpf};{nome};{telefone};{endereco}\n')
    print('Cliente cadastrado com sucesso.\n')

def cadastrar_vendedor():
    codigo = input('Código do vendedor: ')
    nome = input('Nome do vendedor: ')

    with open('2°SEMESTRE/Aulas_Calebe/vendedores.txt', 'a') as f:
        f.write(f'{codigo};{nome}\n')
    print('Vendedor cadastrado com sucesso.')

def registrar_venda():
    data = datetime.datetime.now().strftime('%Y-%m-%d')
    cpf_cliente = input('CPF do cliente (ou deixe em branco se não cadastrado): ')
    codigo_vendedor = input('Código do vendedor: ')
    codigo_produto = input('Código do produto: ')
    quantidade = int(input('Quantidade vendida: '))
    desconto = float(input('Desconto aplicado (em R$): '))
    forma_pagamento = input('Forma de pagamento (dinheiro/pix/cartao): ').lower()

    with open('2°SEMESTRE/Aulas_Calebe/produtos.txt', 'r') as f:
        produtos = f.readlines()

    novo_estoque = []
    produto_encontrado = False
    valor_total = 0
    nome_produto = ""
    preco_unitario = 0

    for linha in produtos:
        dados = linha.strip().split(";")
        if dados[0] == codigo_produto:
            produto_encontrado = True
            if int(dados[8]) >= quantidade:
                dados[8] = str(int(dados[8]) - quantidade)
                preco_unitario = float(dados[7])
                nome_produto = dados[1]
                valor_total = quantidade * preco_unitario - desconto
            else:
                print('Estoque insuficiente.')
                return
        novo_estoque.append(";".join(dados))

    if not produto_encontrado:
        print('Produto não encontrado.')
        return

    with open('2°SEMESTRE/Aulas_Calebe/produtos.txt', 'w') as f:
        f.writelines([linha + '\n' for linha in novo_estoque])

    if forma_pagamento in ['dinheiro', 'pix']:
        comissao = 0.05 * valor_total
    elif forma_pagamento == 'cartao':
        comissao = 0.03 * valor_total
    else:
        print('Forma de pagamento inválida.')
        return

    with open('2°SEMESTRE/Aulas_Calebe/vendas.txt', 'a') as f:
        f.write(f'{data};{cpf_cliente};{codigo_vendedor};{codigo_produto};{nome_produto};{quantidade};{preco_unitario:.2f};{desconto:.2f};{valor_total:.2f};{forma_pagamento};{comissao:.2f}\n')

    print(f'Venda registrada com sucesso. Comissão: R$ {comissao:.2f}')

def gerar_relatorios():
    print("1 - Estoque atual")
    print("2 - Vendas por vendedor")
    print("3 - Lucro por mês")
    opcao = input("Escolha o relatório desejado: ")

    if opcao == "1":
        print("\n--- ESTOQUE ATUAL ---")
        with open("2°SEMESTRE/Aulas_Calebe/produtos.txt", "r") as f:
            for linha in f:
                dados = linha.strip().split(";")
                print(f'Produto: {dados[1]} | Quantidade: {dados[8]} | Preço Venda: R$ {dados[7]}')

    elif opcao == "2":
        print("\n--- VENDAS POR VENDEDOR ---")
        resumo = {}
        with open("2°SEMESTRE/Aulas_Calebe/vendas.txt", "r") as f:
            for linha in f:
                _, _, vendedor, _, _, _, _, _, valor, _, _ = linha.strip().split(";")
                resumo[vendedor] = resumo.get(vendedor, 0) + float(valor)
        for cod, total in resumo.items():
            print(f'Vendedor: {cod} | Total de Vendas: R$ {total:.2f}')

    elif opcao == "3":
        print("\n--- LUCRO POR MÊS ---")
        lucro_mes = {}
        with open("2°SEMESTRE/Aulas_Calebe/vendas.txt", "r") as f:
            for linha in f:
                data, _, _, _, _, _, _, _, valor, _, _ = linha.strip().split(";")
                mes = data[:7]
                lucro_mes[mes] = lucro_mes.get(mes, 0) + float(valor)
        for mes, total in sorted(lucro_mes.items()):
            print(f'Mês: {mes} | Lucro: R$ {total:.2f}')

    else:
        print("Opção inválida!")

# Executar o menu
menu()