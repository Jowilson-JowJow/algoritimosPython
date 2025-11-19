from Database import Database

class Vendas:
    def __init__(self, id_venda=None, nome_card=None, qtde_venda=None, valor_total=None):
        self.id_venda=id_venda
        self.nome_card = nome_card
        self.qtde_venda = qtde_venda
        self.valor_total = valor_total

    def cadastrar_venda(self):
        self.db = Database()
        tupla = (self.nome_card, self.qtde_venda, self.valor_total)
        result = self.db.insert_venda(tupla)
        return result
    
    def buscar_venda(self):
        self.db = Database()
        dados = self.db.select_venda()
        return dados
    
    def buscar_por_id_venda(self, id):
        self.db = Database()
        dados = self.db.select_by_id_venda(id)
        return dados
    
    def atualizar_venda(self, tupla):
        self.db = Database()
        dados = self.db.update_venda(tupla)
        return dados
    
    def excluir_venda(self, id):
        self.db = Database()
        dados = self.db.delete_venda(id)
        return dados

