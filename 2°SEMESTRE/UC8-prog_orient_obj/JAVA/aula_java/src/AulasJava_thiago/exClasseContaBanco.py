# Enunciado do exercício
# Sistema Bancário Orientado a Objetos
# Implemente um sistema bancário em Python usando orientação a objetos com as seguintes características:
# Crie uma classe Pessoa com propriedades básicas: nome.
# Crie uma classe Conta que herda de Pessoa e adiciona propriedades: número da conta, agência, saldo, extrato (lista de movimentações) e senha.
# Proteja a senha com encapsulamento (atributo privado) e métodos públicos para autenticação.
# A classe Conta deve ter métodos para:
# depositar (informando agência e conta, valor),
# sacar (informando agência, conta, senha e valor),
# consultar saldo (mediante conta, agência e senha),
# consultar extrato (mediante conta, agência e senha).
# O sistema deve validar a agência, conta e senha para operações que exigem autenticação.
# Crie um arquivo main.py que apresenta um menu para o usuário escolher entre:
# Cadastro de conta,
# Consultar saldo,
# Consultar extrato,
# Sacar dinheiro,
# Depositar dinheiro,
# Sair.
# Dica: Use listas para armazenar múltiplas contas e simule o banco.


class Pessoa:
    def __init__(self, nome):
        self.nome = nome



class Conta(Pessoa):
    def __init__(self, nome, agencia, numero_conta, senha):
        super().__init__(nome)
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.__senha = senha   
        self.saldo = 0
        self.extrato = []

  
    def autenticar(self, senha):
        return self.__senha == senha

  
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R$ {valor:.2f}")
        else:
            print("Valor inválido para depósito.")

    
    def sacar(self, valor, senha):
        if not self.autenticar(senha):
            print("Senha incorreta.")
            return

        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R$ {valor:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido.")

   
    def mostrar_saldo(self, senha):
        if self.autenticar(senha):
            print(f"Saldo atual: R$ {self.saldo:.2f}")
        else:
            print("Senha incorreta.")

   
    def mostrar_extrato(self, senha):
        if self.autenticar(senha):
            print("Extrato:")
            for mov in self.extrato:
                print(mov)
            print(f"Saldo final: R$ {self.saldo:.2f}")
        else:
            print("Senha incorreta.")



lista_contas = []


c1 = Conta("João", "001", "123", "1111")
c2 = Conta("Maria", "001", "456", "2222")

lista_contas.append(c1)
lista_contas.append(c2)


print("Testando conta do João")
c1.depositar(1000)
c1.sacar(200, "1111")
c1.mostrar_saldo("1111")
c1.mostrar_extrato("1111")

print("\nTestando conta da Maria")
c2.depositar(500)
c2.sacar(100, "2222")
c2.mostrar_saldo("2222")
c2.mostrar_extrato("2222")
