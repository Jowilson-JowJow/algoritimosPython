# 17 - Classe Funcionário: Crie uma super classe que modele um Funcionário genérico. Esta classe deve possuir os seguintes atributos:
# Nome;
# Matricula;
# Salario;
# Método:
# Bater_ponto(): deve criar uma lista de pontos do funcionário, pode ser booleana 0 ou 1;
# Subclasses:
# Defina as subclasses de Funcionário, exemplo Vendedor e Gerente. Após a criação das subclasses você deve criar atributos e métodos específicos de cada subclasse;
# Ex: atributo comissão e método bater_meta() para Vendedor e atributo senha para o Gerente.

class Funcionario:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.pontos = []  

    def bater_ponto(self, ponto):
        if ponto in [0, 1]:
            self.pontos.append(ponto)
            print(f"Ponto registrado para {self.nome}: {'Presente' if ponto == 1 else 'Ausente'}")
        else:
            print("Erro: Ponto inválido. Use 0 para falta e 1 para presente.")

class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario, comissao):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao 

    def bater_meta(self, vendas):
        total_vendas = sum(vendas)
        if total_vendas >= 1000:
            print(f"{self.nome} bateu a meta com R${total_vendas} em vendas!")
        else:
            print(f"{self.nome} não bateu a meta. Vendas totais: R${total_vendas}")

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario, senha):
        super().__init__(nome, matricula, salario)
        self.senha = senha  

    def autenticar_senha(self, senha_digitada):
        if senha_digitada == self.senha:
            print(f"Autenticação bem-sucedida para o gerente {self.nome}.")
        else:
            print("Erro: Senha incorreta.")

funcionario1 = Funcionario("João", "F123", 2500)
funcionario1.bater_ponto(1)

vendedor1 = Vendedor("Carlos", "V456", 2000, 300)
vendedor1.bater_ponto(1)
vendedor1.bater_meta([300, 400, 350]) 

gerente1 = Gerente("Luciana", "G789", 5000, "1234")
gerente1.bater_ponto(1)
gerente1.autenticar_senha("1234")
gerente1.autenticar_senha("4321")