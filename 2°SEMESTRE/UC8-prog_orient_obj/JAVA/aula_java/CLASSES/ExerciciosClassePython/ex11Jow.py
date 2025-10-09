# 11 - Classe NF: Crie uma classe que modele uma Nota_Fiscal. Esta classe deve possuir os seguintes atributos:
# Numero; Tipo (Entrada/Saída); Série (1,2 ou 3); CNPJ; Razão Social; Data; Valor Produtos; ICMS; Frete; IPI; Valor total;
# A classe deve ter o seguintes métodos:
# obterNumero();
# obterDataEmissão();
# alterarRazaoSocial();
# calcularValorTotal() – somar valor do produto + frete e impostos e armazenar na variável valor_total.

class NF:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, valor_produto, icms, frete, ipi):
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
        self.valor_total = 0

    def obterNumero(self):
        return self.numero
    
    def obterDataEmissao(self):
        return self.data
    
    def alterarRazaoSocial(self, novaRazaoSocial):
        self.razao_social = novaRazaoSocial
        return self.razao_social
    
    def calcularValorTotal(self):
        valor_icms = self.valor_produto * (self.icms / 100)
        valor_ipi = self.valor_produto * (self.ipi / 100)
        self.valor_total = self.valor_produto + self.frete + valor_icms + valor_ipi
        return self.valor_total
    

# ====== TESTE ======
notaFiscal1 = NF("00001", "entrada", 2, 1234567891000, "estoque", "22/10/2025", 2500, 17, 250, 5)

print(f"O número da nota fiscal é: {notaFiscal1.obterNumero()}")
print(f"A data da emissão é: {notaFiscal1.obterDataEmissao()}")
print(f"A razão social atual é: {notaFiscal1.razao_social}")
print(f"A razão social alterada é: {notaFiscal1.alterarRazaoSocial('venda')}")
print(f"O valor total da nota fiscal é: {notaFiscal1.calcularValorTotal():.2f}")
