import mysql.connector

class Database:
    def __init__ (self, banco = "perkal") -> None:
        self.banco = banco
        self.host = "localhost"
        self.user = "root"
    
    def connect(self):
        self.conn = mysql.connector.connect(host=self.host, database=self.banco, user = self.user, password ="")
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("conectado com sucesso")
        else:
            print("erro")

db = Database()
db.connect()


