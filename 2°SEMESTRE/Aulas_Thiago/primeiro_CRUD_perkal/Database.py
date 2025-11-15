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
            # print("conectado com sucesso")
        else:
            print("erro")

    def insert_cli(self, tupla):
        self.connect()
        # tupla = ("Thiago","78965412398","67852147963","CG")
        try:
            self.cursor.execute("INSERT INTO cliente (nome,cpf,fone,cidade) VALUES(%s,%s,%s,%s)",tupla)
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def delete_cli(self,id_cli):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM cliente WHERE id_cli = {id_cli}")
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_cli(self):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM cliente")
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_by_id_cli(self,id_cli):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM cliente WHERE id_cli = {id_cli}")
            result = self.cursor.fetchone()
            return result
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def update_cli(self, tupla):
        self.connect()        
        try:
            self.cursor.execute(f"""
                UPDATE cliente SET nome = '{tupla[1]}', 
                cpf = '{tupla[2]}',
                fone = '{tupla[3]}',
                cidade = '{tupla[4]}'                
                WHERE id_cli = {tupla[0]}
            """)
            self.conn.commit()
            return True

        except Exception as err:
            print(err)
        
#fazer abaixo a parte do database para a classe mecanico
 

    def insert_mec(self, tupla):
        self.connect()
       
        try:
            self.cursor.execute("INSERT INTO cad_mecanico (nome,cpf, cod_mec, fone) VALUES(%s,%s,%s,%s)",tupla)
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def delete_mec(self,id_mec):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM cad_mecanico WHERE id_mec = {id_mec}")
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_mec(self):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM cad_mecanico")
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_by_id_mec(self,id_mec):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM cad_mecanico WHERE id_mec = {id_mec}")
            result = self.cursor.fetchone()
            return result
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def update_mec(self, tupla):
        self.connect()        
        try:
            self.cursor.execute(f"""
                UPDATE cad_mecanico SET nome = '{tupla[1]}', 
                cpf = '{tupla[2]}',
                cod_mec = '{tupla[3]}',
                fone = '{tupla[4]}'                
                WHERE id_mec = {tupla[0]}
            """)
            self.conn.commit()
            return True

        except Exception as err:
            print(err)

    def insert_peca(self, tupla):
        self.connect()
        
        try:
            self.cursor.execute("INSERT INTO pecas (nome_peca, preco, qtde_peca) VALUES(%s,%s,%s)",tupla)
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def delete_peca(self,id_peca):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM pecas WHERE id_peca = {id_peca}")
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_peca(self):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM pecas")
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_by_id_peca(self,id_peca):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM peca WHERE id_peca = {id_peca}")
            result = self.cursor.fetchone()
            return result
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def update_peca(self, tupla):
        self.connect()        
        try:
            self.cursor.execute(f"""
                UPDATE pecas SET nome_peca = '{tupla[1]}', 
                preco = '{tupla[2]}',
                qtde_peca = '{tupla[3]}'                
                WHERE id_peca = {tupla[0]}
            """)
            self.conn.commit()
            return True

        except Exception as err:
            print(err)

    def insert_car(self, tupla):
        self.connect()
       
        try:
            self.cursor.execute("INSERT INTO carros (nome_car, placa_car, estado_placa, chassi_car) VALUES(%s,%s,%s,%s)",tupla)
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def delete_car(self,id_car):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM carros WHERE id_car = {id_car}")
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_car(self):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM carros")
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_by_id_car(self,id_car):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM carros WHERE id_car = {id_car}")
            result = self.cursor.fetchone()
            return result
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def update_car(self, tupla):
        self.connect()        
        try:
            self.cursor.execute(f"""
                UPDATE carros SET nome_car = '{tupla[1]}', 
                placa_car = '{tupla[2]}',
                estado_placa = '{tupla[3]}',
                chassi_car = '{tupla[4]}'                
                WHERE id_car = {tupla[0]}
            """)
            self.conn.commit()
            return True

        except Exception as err:
            print(err)


#fazer abaixo a parte do database para a classe mecanico
        finally:
            self.close_connection()
        


    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            # print("Conexão encerrada com sucesso")

    


if __name__=="__main__":
    db = Database()
    db.connect()
    print("SENDO EXECUTADO PELA MAIN")



