#Exercício 2 - Sistema de Vendas (Loja Virtual)

class Cliente:
    def __init__(self, identificacao, nome, cpf, email, telefone):
        self.identificacao = identificacao
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

    def cadastrar(self):
        print(f"Cliente {self.nome} cadastrado com sucesso.")

    def atualizar_cadastro(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        print("Cadastro atualizado com sucesso.")

    def consultar_pedidos(self):
        print(f"Exibindo pedidos do cliente {self.nome}.")


class Produto:
    def __init__(self, codigo, nome, descricao, qtd_estoque, preco):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.qtd_estoque = qtd_estoque
        self.preco = preco

    def atualizar_estoque(self, quantidade):
        self.qtd_estoque += quantidade

    def aplicar_desconto(self, porcentagem):
        self.preco -= self.preco * (porcentagem / 100)

    def exibir_detalhes(self):
        print(f"Produto: {self.nome} | Preço: {self.preco:.2f} | Estoque: {self.qtd_estoque}")


class ItemPedido:
    def __init__(self, codigo, quantidade, preco_unitario):
        self.codigo = codigo
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.subtotal = self.calcular_subtotal()

    def calcular_subtotal(self):
        return self.quantidade * self.preco_unitario

    def atualizar_quantidade(self, nova_qtd):
        self.quantidade = nova_qtd
        self.subtotal = self.calcular_subtotal()

    def exibir_informacoes(self):
        print(f"Item: {self.codigo} | Quantidade: {self.quantidade} | SubTotal: {self.subtotal:.2f}")


class Pedido:
    def __init__(self, identificador, data, status):
        self.identificador = identificador
        self.data = data
        self.status = status
        self.valor_total = 0
        self.itens = []

    def adicionar_produto(self, item):
        self.itens.append(item)

    def remover_produto(self, codigo):
        for item in self.itens:
            if item.codigo == codigo:
                self.itens.remove(item)
                break

    def calcular_valor_total(self):
        total = 0
        for item in self.itens:
            total += item.subtotal
        self.valor_total = total
        return total


class Pagamento:
    def __init__(self, codigo, valor_pago, forma_pagamento, data):
        self.codigo = codigo
        self.valor_pago = valor_pago
        self.forma_pagamento = forma_pagamento
        self.data = data

    def processar_pagamento(self):
        print("Processando pagamento...")

    def confirmar_pagamento(self):
        print("Pagamento confirmado!")

    def emitir_recibo(self):
        print(f"Recibo emitido. Valor: {self.valor_pago:.2f} | Forma: {self.forma_pagamento}")




cliente = Cliente("001", "João", "111.222.333-44", "joao@email.com", "99999-0000")
cliente.cadastrar()

produto1 = Produto("P01", "Mouse Gamer", "Mouse RGB", 10, 150.00)
produto1.exibir_detalhes()

item1 = ItemPedido("P01", 2, produto1.preco)
pedido = Pedido("PED123", "10/11/2025", "Aberto")
pedido.adicionar_produto(item1)

pedido.calcular_valor_total()
print(f"Valor total do pedido: R$ {pedido.valor_total:.2f}")

pagamento = Pagamento("PG001", pedido.valor_total, "Cartão", "10/11/2025")
pagamento.processar_pagamento()
pagamento.confirmar_pagamento()
pagamento.emitir_recibo()
