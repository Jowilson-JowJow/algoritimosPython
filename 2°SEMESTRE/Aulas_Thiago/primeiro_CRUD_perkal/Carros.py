from Database import Database

class Carros:
    def __init__(self, nome_car=None, placa_car=None, estado_placa=None, chassi_car=None):
        self.nome_car = nome_car
        self.placa_car = placa_car
        self.estado_placa = estado_placa
        self.chassi_car = chassi_car

    def cadastrar_car(self):
        self.db = Database()
        tupla = (self.nome_car, self.placa_car, self.estado_placa, self.chassi_car)
        result = self.db.insert_car(tupla)
        return result
    
    def buscar_car(self):
        self.db = Database()
        dados = self.db.select_car()
        return dados

    def buscar_por_id_car(self, id):
        self.db = Database()
        dados = self.db.select_by_id_car(id)
        return dados
    
    def atualizar_car(self, tupla):
        self.db = Database()
        dados = self.db.update_car(tupla)
        return dados

    def excluir_car(self,id):
        self.db = Database()
        dados = self.db.delete_car(id)
        return dados
