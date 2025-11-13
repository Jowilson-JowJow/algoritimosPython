from Database import Database

class Mecanico:
    def __init__(self, nome=None, cpf=None, cod_mec=None, fone=None):
        self.nome = nome
        self.cpf = cpf
        self.cod_mec = cod_mec
        self.fone = fone

    def cadastrar(self):
        self.db = Database()
        tupla = (self.nome, self.cpf, self.cod_mec, self.fone)
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
