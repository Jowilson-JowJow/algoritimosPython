from Database import Database

class Mecanico:
    def __init__(self, nome=None, cpf=None, cod_mec=None, fone=None):
        self.nome = nome
        self.cpf = cpf
        self.cod_mec = cod_mec
        self.fone = fone

    def cadastrar_mec(self):
        self.db = Database()
        tupla = (self.nome, self.cpf, self.cod_mec, self.fone)
        result = self.db.insert_mec(tupla)
        return result
    
    def buscar_mec(self):
        self.db = Database()
        dados = self.db.select_mec()
        return dados

    def buscar_por_id_mec(self, id):
        self.db = Database()
        dados = self.db.select_by_id_mec(id)
        return dados
    
    def atualizar_mec(self, tupla):
        self.db = Database()
        dados = self.db.update_mec(tupla)
        return dados

    def excluir_mec(self,id):
        self.db = Database()
        dados = self.db.delete_mec(id)
        return dados
