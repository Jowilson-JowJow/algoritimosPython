# 10 - Desenvolva um conjunto de classes para controlar o saldo, depósitos e retiradas de contas bancárias bem como os 
# dados do titular. Escreva inicialmente um diagrama modelando tanto contas corrente quanto contas poupança e 
# aplicações em fundo. Em seguida, implemente estas classes em Python.



class Titular:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def __str__(self):
        return f"Titular: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}"


class Conta:
    def __init__(self, titular, num_conta, saldo=0):
        self.titular = titular
        self.num_conta = num_conta
        self.saldo = saldo

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def retirada(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Retirada de R${valor:.2f} realizada com sucesso.")
        else:
            print("Saldo insuficiente para essa retirada.")

    def consultar_saldo(self):
        print(f"Saldo atual da conta {self.num_conta}: R${self.saldo:.2f}")


class ContaCorrente(Conta):
    def __init__(self, titular, num_conta, saldo=0, limite_cheque=1000):
        super().__init__(titular, num_conta, saldo)
        self.limite_cheque = limite_cheque

    def retirada(self, valor):
        if valor <= self.saldo + self.limite_cheque:
            self.saldo -= valor
            print(f"Retirada de R${valor:.2f} realizada com sucesso. Limite de cheque especial utilizado.")
        else:
            print("Saldo insuficiente para essa retirada, mesmo com o limite de cheque.")

    def consultar_limite(self):
        print(f"Limite de cheque especial: R${self.limite_cheque:.2f}")


class ContaPoupanca(Conta):
    def __init__(self, titular, num_conta, saldo=0, rendimento=0.05):
        super().__init__(titular, num_conta, saldo)
        self.rendimento = rendimento

    def aplicar_rendimento(self):
        rendimento = self.saldo * self.rendimento
        self.saldo += rendimento
        print(f"Rendimento de R${rendimento:.2f} aplicado. Novo saldo: R${self.saldo:.2f}")

    def consultar_rendimento(self):
        print(f"Rendimento mensal: {self.rendimento * 100}% ao mês.")


class FundoAplicacao:
    def __init__(self, nome_fundo, saldo_inicial, rendimento=0.02):
        self.nome_fundo = nome_fundo
        self.saldo = saldo_inicial
        self.rendimento = rendimento

    def aplicar_rendimento(self):
        rendimento = self.saldo * self.rendimento
        self.saldo += rendimento
        print(f"Rendimento de fundo aplicado: R${rendimento:.2f}. Novo saldo do fundo: R${self.saldo:.2f}")

    def consultar_saldo(self):
        print(f"Saldo atual do fundo {self.nome_fundo}: R${self.saldo:.2f}")

titular1 = Titular("João Silva", "123.456.789-00", "Rua das Flores, 123")

conta_corrente = ContaCorrente(titular1, "CC001", 2000, 1500)
conta_corrente.deposito(500)
conta_corrente.retirada(2500)
conta_corrente.consultar_saldo()
conta_corrente.consultar_limite()

conta_poupanca = ContaPoupanca(titular1, "CP001", 1000)
conta_poupanca.deposito(200)
conta_poupanca.aplicar_rendimento()
conta_poupanca.consultar_saldo()
conta_poupanca.consultar_rendimento()

fundo_aplicacao = FundoAplicacao("Fundo A", 5000)
fundo_aplicacao.aplicar_rendimento()
fundo_aplicacao.consultar_saldo()