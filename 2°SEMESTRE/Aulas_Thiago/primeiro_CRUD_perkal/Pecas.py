from Database import Database

class Pecas:
    def __init__(self, nome_peca=None, preco=None, qtde_peca=None):
        self.nome_peca = nome_peca
        self.preco = preco
        self.qtde_peca = qtde_peca
        
    def cadastrar_peca(self):
        self.db = Database()
        tupla = (self.nome_peca, self.preco, self.qtde_peca)
        result = self.db.insert_peca(tupla)
        return result
    
    def buscar_peca(self):
        self.db = Database()
        dados = self.db.select_peca()
        return dados

    def buscar_por_id_peca(self, id):
        self.db = Database()
        dados = self.db.select_by_id_peca(id)
        return dados
    
    def atualizar_peca(self, tupla):
        self.db = Database()
        dados = self.db.update_peca(tupla)
        return dados

    def excluir_peca(self,id):
        self.db = Database()
        dados = self.db.delete_peca(id)
        return dados
