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

class Pessoa():
    def __init__(self, nome):
        self.nome=nome

class Conta(Pessoa):
    def __init__(self, num_conta, agencia, saldo, extrato, senha):
        self.num_conta = num_conta
        self.agencia = agencia
        self.saldo = saldo
        self.extrato = extrato
        self._senha = senha
        
    def depositar(self):





