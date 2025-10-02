# 4 - Classe Conta: Um banco mantém contas de clientes armazenando o número da conta, o nome do cliente e o saldo atual da conta. Crie uma classe que modele um Conta-Corrente.
# Nome;
# CPF;
# Numero;
# Saldo;
# A classe deve ter o seguintes métodos:
# Depositar()
# Sacar()  -  OBS: somente enquanto a conta possuir saldo positivo
# Imprimir saldo()

class Conta:
    def __init__(self, nome, CPF, numero, saldo):
        self.nome=nome
        self.CPF=CPF
        self.numero=numero
        self.saldo=saldo

    def depositar(self,novo_deposito):
        print(f"Saldo: {self.saldo}")
        self.saldo += novo_deposito
        print(f"Deposito: {novo_deposito:.2f} \nSaldo Atulizado: {self.saldo:.2f}")

    def sacar(self,novo_saque):
        print(f"Saldo: {self.saldo}")
        if (self.saldo>=novo_saque):
            self.saldo-=novo_saque
            print(f"Saque: {novo_saque:.2f}\nSaldo: {self.saldo}")
        else:
            print("Saldo insuficiente para saque!!!")

c1=Conta("joão","78955815-15","12569-9",125.36)
c1.depositar(500)
c1.sacar(400)