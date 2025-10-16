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

class Conta




#tentei fazer mas esta errado
# class Cadastro():
#     def __init__(self, nome, agencia, conta_corrente, senha):
#         self.nome=nome
#         self.agencia=agencia
#         self.conta_corrente=conta_corrente
#         self.senha=senha
#         self.clientes=[]

# class Depositar():
#     def __init__(self,novo_deposito):
#         self.novo_deposito=novo_deposito
    
#     def deposito (self):

# class Consultar_saldo():
#     def __init__(self):
#         self.saldo = 0
#         if (self.deposito<0):
#             return self.saldo
#         elif (self.deposito>0):
#             self.saldo=self.saldo+self.deposito
#             return self.saldo
#         else:
#             return self.saldo


#parte do codigo de outro exercicio para ver como fazer herança de uma classe
# class Gerente(Funcionario):
#     def __init__(self, nome, login, senha, setor):
#         super().__init__(nome, login, senha)
#         self.setor =setor
#     def logar(self):##polimorfismo
#         confirm = input("digite o tokene")
#         if confirm:
#             print(f"Gerente {self.nome}logado com sucesso no setor: {self.setor}")
