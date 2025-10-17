class NotaFiscal:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, icms, frete, ipi, valor_produto):
        """Inicializa os atributos da Nota Fiscal"""
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_produto = valor_produto
        self.valor_total = 0  

    def obterNumero(self):
        """Retorna o número da nota fiscal"""
        return self.numero

    def obterDataEmissao(self):
        """Retorna a data de emissão da nota fiscal"""
        return self.data

    def alterarRazaoSocial(self, nova_razao_social):
        """Altera a razão social da empresa"""
        self.razao_social = nova_razao_social
        print(f"A razão social foi alterada para: {self.razao_social}")

    def calcularValorTotal(self):
        """Calcula o valor total da nota fiscal (produto + frete + impostos)"""
        valor_impostos = self.icms + self.ipi
        self.valor_total = self.valor_produto + self.frete + valor_impostos
        return self.valor_total


def main():
    numero = int(input("Informe o número da nota fiscal: "))
    tipo = input("Informe o tipo (Entrada/Saída): ")
    serie = int(input("Informe a série (1, 2 ou 3): "))
    cnpj = input("Informe o CNPJ da empresa: ")
    razao_social = input("Informe a razão social da empresa: ")
    data = input("Informe a data de emissão (dd/mm/aaaa): ")
    icms = float(input("Informe o valor do ICMS: R$ "))
    frete = float(input("Informe o valor do frete: R$ "))
    ipi = float(input("Informe o valor do IPI: R$ "))
    valor_produto = float(input("Informe o valor do produto: R$ "))

    nota = NotaFiscal(numero, tipo, serie, cnpj, razao_social, data, icms, frete, ipi, valor_produto)

    print(f"\nNúmero da Nota Fiscal: {nota.obterNumero()}")
    print(f"Data de Emissão: {nota.obterDataEmissao()}")

    nova_razao_social = input("Informe a nova razão social: ")
    nota.alterarRazaoSocial(nova_razao_social)

    valor_total = nota.calcularValorTotal()
    print(f"O valor total da Nota Fiscal é: R$ {valor_total:.2f}")


if __name__ == "__main__":
    main()
