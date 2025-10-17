class Person:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar(self):
        print(f"{self.nome} está negociando.")

class Fisica(Person):
    def __init__(self, nome, telefone, email, endereco, cpf):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf

    def consultar_cpf(self):
        print(f"CPF de {self.nome}: {self.cpf}")

class Juridica(Person):
    def __init__(self, nome, telefone, email, endereco, cnpj):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj

    def consultar_cnpj(self):
        print(f"CNPJ de {self.nome}: {self.cnpj}")

pessoa_fisica = Fisica("Maria Silva", "1234-5678", "maria@email.com", "Rua das Flores, 123", "123.456.789-00")
pessoa_fisica.negociar()
pessoa_fisica.consultar_cpf()

pessoa_juridica = Juridica("Empresa X", "9876-5432", "contato@empresa.com", "Av. Central, 1000", "12.345.678/0001-99")
pessoa_juridica.negociar()
pessoa_juridica.consultar_cnpj()