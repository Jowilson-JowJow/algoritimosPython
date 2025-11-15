
from Database import Database

class Cliente:
    def __init__(self, nome=None,cpf=None, fone=None, cidade=None):
        self.nome = nome
        self.cpf = cpf
        self.fone = fone
        self.cidade = cidade
        


    def cadastrar_cli(self):
        self.db = Database()
        tupla = (self.nome, self.cpf, self.fone, self.cidade)
        result = self.db.insert_cli(tupla)
        return result


    def buscar_cli(self):
        self.db = Database()
        dados = self.db.select_cli()
        return dados

    def buscar_por_id_cli(self, id):
        self.db = Database()
        dados = self.db.select_by_id_cli(id)
        return dados
    
    def atualizar_cli(self, tupla):
        self.db = Database()
        dados = self.db.update_cli(tupla)
        return dados

    def excluir_cli(self,id):
        self.db = Database()
        dados = self.db.delete_cli(id)
        return dados

   