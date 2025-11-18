import mysql.connector

class Database:
    def __init__(self, banco = "loja_on") -> None:
        self.banco = banco
        self.host = "Atividade_Python_POO_thiago"
        self.user="root"

    def connect(self):
        self.conn =mysql.connector.connect(host=self.host, database=self.banco, user = self.user, password="")
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado com Sucesso!!!")
        else:
            print("erro")

    def insert_cli(self, tupla):
        self.connect()
        try:
            self.cursor.execute("INSERT INTO Atividade_Python_POO_thiago (nome, email, fone) VALUES(%s, %s, %s)", tupla)
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def delete_cli(self, id_cliente):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM Atividade_Python_POO_thiago WHERE id_cliente = {id_cliente}")
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()