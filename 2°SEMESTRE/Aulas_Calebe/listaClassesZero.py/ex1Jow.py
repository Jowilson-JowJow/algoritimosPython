# 1. Crie uma classe que modele uma pessoa
# (a) Atributos: nome, idade e enderec¸o
# (b) M´etodos: mostrar enderec¸o e alterar enderec¸o

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_endereco(self):
        endereco_casa=self.endereco
        return endereco_casa
    
    def alterar_endereco(self):
        self.endereco = input("altere o enderço: ")
        return self.endereco


pessoa1 = Pessoa("joão", 23, "rua catanduva, n°203")
endereco = pessoa1.mostrar_endereco()
print(endereco)

novo_endereco = pessoa1.alterar_endereco()
print(novo_endereco)
