import mysql.connector

class Database:
    def __init__(self, banco = "loja_on") -> None:
        self.banco = banco
        self.host = "localhost"
        self.user="root"
        self.password = ""

    def connect(self):
        self.conn =mysql.connector.connect(host=self.host, database=self.banco, user = self.user, password=self.password)
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado com Sucesso!!!")
        else:
            print("erro")

    def insert_cliente(self, tupla):
        self.connect()
        try:
            self.cursor.execute("INSERT INTO clientes (nome, email, fone) VALUES(%s, %s, %s)", tupla)
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def delete_cliente(self, id_cliente):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM clientes WHERE id_cliente = {id_cliente}")
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_cliente(self):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM clientes")
            result = self.cursor.fetchall()
            return result
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_by_id_cliente(self,id_cliente):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM clientes WHERE id_cliente = {id_cliente}")
            result = self.cursor.fetchone()
            return result
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def update_cliente(self, tupla):
        self.connect()
        try:
            self.cursor.execute(f"""UPDATE clientes SET nome = '{tupla[1]}', email = '{tupla[2]}', fone = '{tupla[3]}' WHERE id_cliente = {tupla[0]}""")
            self.conn.commit()
            return True
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()

if __name__=="__main__":
    db = Database()
    db.connect()
    print("Sendo executado pela main")