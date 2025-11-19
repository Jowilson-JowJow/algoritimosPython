from Database import Database

class Vendedores:
    def __init__(self, nome = None, cod_vendedor = None, fone = None):
        self.nome = nome
        self.cod_vendedor = cod_vendedor
        self.fone = fone

    def cadastrar_vendedor(self):
        self.db = Database()
        tupla = (self.nome, self.cod_vendedor, self.fone)
        result = self.db.insert_vendedor(tupla)
        return result
    
    def buscar_vendedor(self):
        self.db = Database()
        dados = self.db.select_vendedor()
        return dados
    
    def buscar_por_id_vendedor(self, id):
        self.db = Database()
        dados = self.db.select_by_id_vendedor(id)
        return dados
    
    def atualizar_vendedor(self, tupla):
        self.db = Database()
        dados = self.db.update_vendedor(tupla)
        return dados
    
    def excluir_vendedor(self, id):
        self.db = Database()
        dados = self.db.delete_vendedor(id)
        return dados

