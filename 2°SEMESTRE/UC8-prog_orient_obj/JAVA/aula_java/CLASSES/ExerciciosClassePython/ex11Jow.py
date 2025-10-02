# 11 - Classe NF: Crie uma classe que modele uma Nota_Fiscal. Esta classe deve possuir os seguintes atributos:
# Numero; Tipo (Entrada/Saída); Série (1,2 ou 3); CNPJ; Razão Social; Data; Valor Produtos; ICMS; Frete; IPI; Valor total;
# A classe deve ter o seguintes métodos:
# obterNumero();
# obterDataEmissão();
# alterarRazaoSocial();
# calcularValorTotal() – somar valor do produto + frete e impostos e armazenar na variável valor_total.

class NF:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, valor_produto, icms, frete, ipi, valor_total):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.valor_produto = valor_produto
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_total = valor_total