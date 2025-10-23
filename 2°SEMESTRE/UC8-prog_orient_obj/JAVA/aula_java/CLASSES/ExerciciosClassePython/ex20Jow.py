# 20 - Classe Compra: Crie uma super classe que modele uma Venda. Esta classe deve possuir os seguintes atributos:
# Numero; Produto; Valor; Valor_total = 0;
# Método:
# calcular_valor_total(): deve somar ao valor_total o imposto de 17% do ICMS + o Frete de 5% sobre o valor do protudo;
# Subclasses:
# Defina as subclasses CompraAvista e CompraParcelada, na classe de CompraAvista  o método calcular_valor_total() deve ter o atributo desconto e na classe CompraParcelada criar o método simular_numero_de_parcelas.
# Em cada subclasse definir um métodos getters e setters para os seus atributos.

class Compra:
    def __init__(self, numero, produto, valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0

    def calcular_valor_total(self):
        icms = self.valor * 0.17
        frete = self.valor * 0.05
        self.valor_total = self.valor + icms + frete
        return f"Valor total da compra: R${self.valor_total:.2f}"


class CompraAvista(Compra):
    def __init__(self, numero, produto, valor, desconto):
        super().__init__(numero, produto, valor)
        self.desconto = desconto

    def calcular_valor_total(self):
        valor_total_com_impostos = super().calcular_valor_total()
        desconto_valor = self.valor_total * (self.desconto / 100)
        self.valor_total -= desconto_valor
        return f"{valor_total_com_impostos}\nDesconto aplicado: R${desconto_valor:.2f}\nValor final com desconto: R${self.valor_total:.2f}"

    def get_desconto(self):
        return self.desconto

    def set_desconto(self, novo_desconto):
        self.desconto = novo_desconto


class CompraParcelada(Compra):
    def __init__(self, numero, produto, valor, numero_parcelas):
        super().__init__(numero, produto, valor)
        self.numero_parcelas = numero_parcelas

    def simular_numero_de_parcelas(self):
        valor_parcela = self.valor_total / self.numero_parcelas
        return f"Valor por parcela (em {self.numero_parcelas}x): R${valor_parcela:.2f}"

    def get_numero_parcelas(self):
        return self.numero_parcelas

    def set_numero_parcelas(self, novo_numero):
        self.numero_parcelas = novo_numero

compra_avista = CompraAvista("1001", "Smartphone", 1500, 10)
print(compra_avista.calcular_valor_total())

compra_parcelada = CompraParcelada("1002", "Laptop", 2000, 12)
compra_parcelada.calcular_valor_total()  
print(compra_parcelada.simular_numero_de_parcelas()) 