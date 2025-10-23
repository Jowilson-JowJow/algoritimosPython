# 14 - Classe Pessoa: Crie uma super classe que modele uma Pessoa. Esta classe deve possuir os seguintes atributos:
# Nome; Telefone; E-mail; Endereço;
# Métodos:
# negociar: deve printar uma mensagem de negociação;
# Subclasses:
# Defina as subclasses de Pessoa serão Física e Jurídica, estas devem conter além dos atributos herdados de Pessoa seus atributos identificadores, ex: CPF, CNPJ.
# Além de herdar o método negociar() crie métodos específicos para as subclasses;

class Pessoa:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar(self):
        print(f"{self.nome} está negociando.")

class Fisica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cpf):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf

    def consultar_cpf(self):
        print(f"CPF de {self.nome}: {self.cpf}")

class Juridica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cnpj):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj

    def consultar_cnpj(self):
        print(f"CNPJ de {self.nome}: {self.cnpj}")

pessoa_fisica = Fisica("Ana Maria Moura", "67 98999523", "mariamoura@email.com", "Rua primavera, 23", "123.456.000-00")
pessoa_fisica.negociar()
pessoa_fisica.consultar_cpf()

pessoa_juridica = Juridica("dungeon", "11 99877-3332", "dungeon@empresa.com", "Av. Capital, 2569", "11.222.778/0001-00")
pessoa_juridica.negociar()
pessoa_juridica.consultar_cnpj()