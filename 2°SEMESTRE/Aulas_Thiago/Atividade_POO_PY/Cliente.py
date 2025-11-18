from Database import Database

class Cliente:
    def __init__(self, nome = None, email = None, fone = None):
        self.nome = nome
        self.email = email
        self.fone = fone

    def cadastrar_cliente(self):
        self.db = Database()
        tupla = (self.nome, self.email, self.fone)
        result = self.db.insert_cliente(tupla)
        return result
    
    def buscar_cliente(self):
        self.db = Database()
        dados = self.db.select_cliente()
        return dados
    
    def buscar_por_id_cliente(self, id):
        self.db = Database()
        dados = self.db.select_by_id_cliente(id)
        return dados
    
    def atualizar_cliente(self, tupla):
        self.db = Database()
        dados = self.db.update_cliente(tupla)
        return dados
    
    def excluir_cliente(self, id):
        self.db = Database()
        dados = self.db.delete_cliente(id)
        return dados

