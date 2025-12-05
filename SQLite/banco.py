import sqlite3
banco = sqlite3.connect('ADS2025.db')
cursor = banco.cursor()

nome=input("Digite o nome do produto: ")
qtd = input("Digite a quantidade do produto: ")
valor = input("Digite o valor do produto: ")
cursor.execute("CREATE TABLE IF NOT EXISTS produtos(nome text, qtd integer, valor float)")
cursor.execute("INSERT INTO produtos VALUES ('"+nome+"', "+str(qtd)+", "+str(valor)+")")
cursor.execute("SELECT * FROM produtos")
print(cursor.fetchall())
banco.commit()

#terceira interação
# import sqlite3
# banco = sqlite3.connect('ADS2025.db')
# cursor = banco.cursor()

# nome=input("Digite o nome do produto: ")
# qtd = input("Digite a quantidade do produto: ")
# valor = input("Digite o valor do produto: ")
# cursor.execute("INSERT INTO produtos VALUES ('"+nome+"', "+str(qtd)+", "+str(valor)+")")
# cursor.execute("SELECT * FROM produtos")
# print(cursor.fetchall())
# banco.commit()

# segunda interação
# import sqlite3
# banco = sqlite3.connect('ADS2025.db')
# cursor = banco.cursor()

# nome="Carnes"
# qtd = 2
# valor = 100.00
# cursor.execute("INSERT INTO produtos VALUES ('"+nome+"', "+str(qtd)+", "+str(valor)+")")
# cursor.execute("SELECT * FROM produtos")
# print(cursor.fetchall())
# banco.commit()


#primeira interação
# import sqlite3
# banco = sqlite3.connect('ADS2025.db')
# cursor = banco.cursor()
# #cursor.execute("CREATE TABLE produtos(nome text, qtd integer, valor float)") #depois de criar comenta para cada vez que executar não der erro
# cursor.execute("INSERT INTO produtos VALUES ('Fruta', 25, 10.00)")
# cursor.execute("SELECT * FROM produtos")
# print(cursor.fetchall())
# banco.commit()