# 1 - Classe Pessoa: Crie uma classe que modele uma pessoa. Esta classe deve possuir os seguintes atributos:
# Nome
# Idade
# Endereço
# A classe deve ter os seguintes métodos:
# Mostrar nome;
# Alterar a idade;
# Imprimir endereço.

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_nome(self):
        print(f"Seu nome é: {self.nome}")

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def mostrar_endereco(self):
        print(f"O seu endereço é: {self.endereco}")


p1 = Pessoa("jowjow", 48, "rua francisco mario, 108")
p1.mostrar_nome()
print(f"Sua idade é: {p1.idade} anos")
p1.alterar_idade(22)
print(f"Idade corrigida: {p1.idade} anos")
p1.mostrar_endereco()