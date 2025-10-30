
from Database import Database

class Cliente:
    def __init__(self, nome=None,cpf=None, fone=None, cidade=None):
        self.nome = nome
        self.cpf = cpf
        self.fone = fone
        self.cidade = cidade
        


    def cadastrar(self):
        self.db = Database()
        tupla = (self.nome, self.cpf, self.fone, self.cidade)
        self.db.insert(tupla)


    def buscar(self):
        self.db = Database()
        dados = self.db.select()
        return dados

    def deletar(self,id):
        self.db = Database()
        dados = self.db.delete(id)
        return dados

    def selecionar(self):
        self.db = Database()
        dados = self.db.select()
        return dados


cli = Cliente()
# cli.nome = input("digite seu nome: ")
# cli.cpf = input("digite seu cpf: ")
# cli.fone = input("digite seu fone: ")
# cli.cidade = input("digite seu cidade: ")
# cli.cadastrar()

# clientes = cli.buscar()
# print(clientes)

clientes = cli.deletar(5)
print(clientes)

# clientes = cli.selecionar()
# print (clientes)