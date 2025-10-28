#Exercício 2 - Sistema de Vendas (Loja Virtual)

class Clientes:
    def __init__ (self, id, nome, cpf, email,tel):
        self.id = id 
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.tel = tel
        self.pedidos=[]

    def cadastro(self):
        print(f"Cliente: {self.nome} | id: {self.id}\nCadastrado com Sucesso!!!")

    def atualizar(self, nome, email , tel):
        self.email = email
        self.tel = tel

class Produto:
    def __init__(self, codigo, nome, descricao, preco, qtd):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.preco =preco
        self.qtd = qtd

    def atualizar (self, novaQtd):
        self.qtd = novaQtd
        print(f"Estoque atualizado. Nova Quantidade: {self.qtd}.")

    def aplicarDesconto(self, percentual):
        preco_desc=self.preco - (self.preco*(percentual/100))
        return preco_desc
    

    def info(self):
        print(f"Nome do produto: {self.nome} | Preço: {self.preco:.2f} | Quantidade: {self.qtd}")

lista_clientes = []
cliente1 = Clientes(1, "jowjow","000000000000","aaaa@gmail.com", "67998745847" )

lista_clientes.append(cliente1)
print(lista_clientes[0])
lista_clientes[0].cadastro()

lista_produtos = []
produto1 = Produto(1,"vela","pacote com 6 velas de 10cm", 8.90, 5)

lista_produtos.append(produto1)
print(lista_produtos[0])
lista_produtos[0].atualizar(9)
novo_preco=lista_produtos[0].aplicarDesconto(10)
print(novo_preco)
lista_produtos[0].info()
