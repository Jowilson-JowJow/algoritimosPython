
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
        result = self.db.insert(tupla)
        return result


    def buscar(self):
        self.db = Database()
        dados = self.db.select()
        return dados

    def buscar_por_id(self, id):
        self.db = Database()
        dados = self.db.select_by_id(id)
        return dados
    
    def atualizar(self, tupla):
        self.db = Database()
        dados = self.db.update(tupla)
        return dados

    def excluir(self,id):
        self.db = Database()
        dados = self.db.delete(id)
        return dados

   


cli = Cliente()
# cli.nome = input("digite seu nome: ")
# cli.cpf = input("digite seu cpf: ")
# cli.fone = input("digite seu fone: ")
# cli.cidade = input("digite seu cidade: ")
# cli.cadastrar()

clientes = cli.buscar()

for item in clientes:
    print(item)

# id_excluir=int(input("Digite o id cliente você deseja excluir"))
# retorno = cli.excluir (id_excluir)
# if retorno == True:
#     print ("Cliente excluido com sucesso!!!")


id_atualizar = int(input("digite o id do cliente par atualizar"))
cli_atualizar = cli.buscar_por_id(id_atualizar)
print(cli_atualizar)
cli_atualizar=list(cli_atualizar)
cli_atualizar[1]=input("Digite o novo nome: ")
cli_atualizar[2]=input("Digite o novo cpf: ")
cli_atualizar[3]=input("Digite o novo fone: ")
cli_atualizar[4]=input("Digite o novo cidade: ")

cli_atualizar=tuple(cli_atualizar)

print(cli_atualizar)

resultado=cli.atualizar(cli_atualizar)
if resultado == True:
    print("atualizado com sucesso")