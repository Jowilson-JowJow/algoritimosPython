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

cadastrar_produto()
entrada_estoque()

