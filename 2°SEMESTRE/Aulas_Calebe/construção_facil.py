# INÍCIO
#   ↓
# [Menu Principal]
#   ├──> (1) Cadastrar Produto
#   │       ↓
#   │   [Recebe código, nome, quantidade, valor]
#   │       ↓
#   │   [Adiciona ao dicionário "estoque"]
#   │       ↓
#   │   [Mensagem de sucesso]
#   │
#   ├──> (2) Entrada no Estoque
#   │       ↓
#   │   [Recebe código e quantidade a adicionar]
#   │       ↓
#   │   [Verifica se produto existe]
#   │       ├── Sim → Atualiza quantidade
#   │       └── Não → Mensagem de erro
#   │
#   ├──> (3) Cadastrar Cliente
#   │       ↓
#   │   [Recebe CPF e nome]
#   │       ↓
#   │   [Adiciona ao dicionário "clientes"]
#   │       ↓
#   │   [Mensagem de sucesso]
#   │
#   ├──> (4) Cadastrar Vendedor
#   │       ↓
#   │   [Recebe código, nome, comissão %]
#   │       ↓
#   │   [Adiciona ao dicionário "vendedores"]
#   │       ↓
#   │   [Mensagem de sucesso]
#   │
#   ├──> (5) Registrar Venda
#   │       ↓
#   │   [Recebe vendedor, cliente, produto, quantidade]
#   │       ↓
#   │   [Valida vendedor e cliente]
#   │       ↓
#   │   [Verifica se produto existe e tem estoque]
#   │       ├── Sim → Reduz estoque, calcula valor e comissão
#   │       │        Salva venda no dicionário e lista de vendas
#   │       └── Não → Mensagem de erro
#   │
#   ├──> (6) Relatórios
#   │       ↓
#   │   [Escolhe tipo: Estoque / Vendas por vendedor / Lucro mensal]
#   │       ├── Estoque → Exibe lista dos produtos e quantidades
#   │       ├── Vendas por vendedor → Soma vendas e comissões
#   │       └── Lucro mensal → Agrupa por ano-mês e soma valores
#   │
#   └──> (0) Sair
#           ↓
#        [FIM DO SISTEMA]



#CRIAR OS DICIONARIOS PARA QUE OS DADOS SEJAM SALVOS
estoque={}
clientes={}
vndedores={}
vendas={}

#CRIANDO AS FUNÇÕES

#função para cadastrar produto no estoque
def cadastrar_produto():
    codigo=input("Digite o codigo do produto: ")
    nome=input("digite o nome do produto: ")
    quantidade=int(input("Digite a quantidade inicial: "))
    valor=float(input("Digite o valor unitário: R$ "))
    estoque[codigo]={'nome':nome,'quantidade':quantidade,'valor':valor}
    print("Produto cadastrado com sucesso!\n")
    print(estoque)

#função para entrada de produtos no estoque
def entrada_estoque():
    codigo=input("Digite o codigo do produto: ")
    if codigo in estoque:
        quantidade=int(input("Digite Quantidade a adicionar: "))
        estoque[codigo]['quantidade']+=quantidade
        print("Estoque atualizado com sucesso!\n")
    else:
        print("produto não encontrado")
    print(estoque)

#função para dar saida do estoque
def saida_estoque(codigo,quantidade):
    if codigo not in estoque:
        print(f'Erro: produto com codigo "{codigo}" não encontrado no estoque.')
        return
    if estoque[codigo]['quantidade']<quantidade:
        print(f'Erro: quantidade insuficiente em estoque.\nDisponivel: {estoque[codigo]['quantidadade']} unidades do produto {estoque[codigo]['nome']}')
        return
    estoque[codigo]['quantidade']-=quantidade
    print(f'Saída realizada com sucesso.\nRestam {estoque[codigo]['quantidade']} unidades do produto {estoque[codigo]['nome']}')

def cadastra_cliente():
    cliente=input("Digie o cpf")
    
