# Crie uma classe que modele uma conta corrente
# (a) Atributos: n´umero da conta, nome do correntista e saldo
# (b) M´etodos: alterar nome, dep´ osito e saque; No construtor, saldo ´e opcional, com valor
# default zero e os demais atributos s˜ao obrigat ´ orios.

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo = self.saldo + valor

    def saque(self, valor):
        self.saldo = self.saldo - valor

    def mostrar_dados(self):
        print(f"Conta: {self.numero_conta}")
        print(f"Correntista: {self.nome_correntista}")
        print(f"Saldo: R$ {self.saldo}")
        print("------------------")



conta1 = ContaCorrente(12345, "Jow Jow", 100)
conta1.mostrar_dados()

conta1.alterar_nome("João Silva")
print("Nome alterado!")

conta1.deposito(200)
print("Depósito realizado!")

conta1.saque(50)
print("Saque realizado!")

conta1.mostrar_dados()
