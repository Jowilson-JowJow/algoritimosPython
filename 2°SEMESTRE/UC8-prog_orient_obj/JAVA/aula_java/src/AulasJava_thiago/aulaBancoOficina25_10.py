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

    def insert(self, tupla):
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

    def delete(self,id_cli):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM cliente WHERE id_cli = {id_cli}")
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select(self):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM cliente")
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def selectById(self,id_cli):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM cliente WHERE id_cli = {id_cli}")
            result = self.cursor.fetchone()
            return result
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection

    def update(self, tupla):
        self.connect()
        
        try:
            self.cursor.execute(f"""
            UPDATE cliente SET nome = '{tupla[1]}',
            cpf= '{tupla[2]}',
            fone = '{tupla[3]}',
            cidade = '{tupla[4]}'
             WHERE id_cli = {tupla[0]}"""
             )
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
            print("Conexão encerrada com sucesso")

    




db = Database()
db.connect()
# dados = ("liana","12569874632","11999885522","Sorocaba")
# cadastro =db.insert(dados)
# if cadastro == True:
#     print("Cadastrado com sucesso!!!")

# id_cli=int(input("digite o id que vc queira deletar: "))
# x=db.delete(id_cli)
# if x:
#     print("deletado com sucesso")

# dados = db.select()
# for cliente in dados:
#     print(f"id: {cliente[0]} | Nome: {cliente[1]} | CPF: {cliente[2]} | Fone: {cliente[3]}")

# id_select = int (input ("QUAL CLIENTE DESEJA SELECIONAR? "))
# cli=db.selectById(id_select)
# print(cli)


dados = db.selectById(2)
dados = list(dados)

dados[1]=input("digite o novo nome: ")
dados[2]=input("digite o novo cpf: ")

dados=tuple(dados)
print(dados)
result = db.update(dados)

if result:
    print("DADOS ALTERADOS COM SUCESSO")

