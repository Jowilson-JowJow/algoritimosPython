from Database import Database

class Cards:
    def __init__(self, nome_card = None, preco_card = None, qtde_card = None, raridade_card =None, edicao_card = None):
        self.nome_card = nome_card
        self.preco_card = preco_card
        self.qtde_card = qtde_card
        self.raridade_card = raridade_card
        self.edicao_card = edicao_card

    def cadastrar_card(self):
        self.db = Database()
        tupla = (self.nome_card, self.preco_card, self.qtde_card, self.raridade_card, self.edicao_card)
        result = self.db.insert_card(tupla)
        return result
    
    def buscar_card(self):
        self.db = Database()
        dados = self.db.select_card()
        return dados
    
    def buscar_por_id_card(self, id):
        self.db = Database()
        dados = self.db.select_by_id_card(id)
        return dados
    
    def atualizar_card(self, tupla):
        self.db = Database()
        dados = self.db.update_card(tupla)
        return dados
    
    def excluir_card(self, id):
        self.db = Database()
        dados = self.db.delete_card(id)
        return dados

