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

    #para o cliente
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

    #para o vendedor
    def insert_vendedor(self, tupla):
        self.connect()
        try:
            self.cursor.execute("INSERT INTO vendedores (nome, cod_vendedor, fone) VALUES(%s, %s, %s)", tupla)
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def delete_vendedor(self, id_vendedor):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM vendedores WHERE id_vendedor = {id_vendedor}")
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_vendedor(self):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM vendedores")
            result = self.cursor.fetchall()
            return result
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_by_id_vendedor(self,id_vendedor):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM vendedores WHERE id_vendedor = {id_vendedor}")
            result = self.cursor.fetchone()
            return result
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def update_vendedor(self, tupla):
        self.connect()
        try:
            self.cursor.execute(f"""UPDATE vendedores SET nome = '{tupla[1]}', cod_vendedor = '{tupla[2]}', fone = '{tupla[3]}' WHERE id_vendedor = {tupla[0]}""")
            self.conn.commit()
            return True
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()
    
    
    #para o card
    def insert_card(self, tupla):
        self.connect()
        try:
            self.cursor.execute("INSERT INTO cards (nome_card, preco_card, qtde_card, raridade_card, edicao_card) VALUES(%s, %s, %s, %s, %s)", tupla)
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def delete_card(self, id_card):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM cards WHERE id_card = {id_card}")
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_card(self):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM cards")
            result = self.cursor.fetchall()
            return result
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_by_id_card(self,id_card):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM cards WHERE id_card = {id_card}")
            result = self.cursor.fetchone()
            return result
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def update_card(self, tupla):
        self.connect()
        try:
            self.cursor.execute(f"""UPDATE cards SET nome_card = '{tupla[1]}', preco_card = '{tupla[2]}', qtde_card = '{tupla[3]}', raridade_card = '{tupla[4]}', edicao_card = '{tupla[5]}' WHERE id_card = {tupla[0]}""")
            self.conn.commit()
            return True
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    
    # registrar venda

    def insert_venda(self, tupla):
        self.connect()
        try:
            self.cursor.execute("INSERT INTO vendas (nome_card, qtde_venda, valor_total) VALUES(%s, %s, %s)", tupla)
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def delete_venda(self, id_venda):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM vendas WHERE id_venda = {id_venda}")
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_venda(self):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM vendas")
            result = self.cursor.fetchall()
            return result
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_by_id_venda(self,id_venda):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM vendas WHERE id_venda = {id_venda}")
            result = self.cursor.fetchone()
            return result
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def update_venda(self, tupla):
        self.connect()
        try:
            self.cursor.execute(f"""UPDATE vendas SET nome_card = '{tupla[1]}', qtde_venda = '{tupla[2]}', valor_total = '{tupla[3]}' WHERE id_venda = {tupla[0]}""")
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