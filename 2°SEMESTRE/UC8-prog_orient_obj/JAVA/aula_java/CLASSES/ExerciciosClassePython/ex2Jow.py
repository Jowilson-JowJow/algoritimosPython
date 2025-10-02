# 2 - Classe Livro: Crie uma classe que modele um Livro. Esta classe deve possuir os seguintes atributos:
# Nome
# Autor
# Editora
# Páginas
# A classe deve ter o seguintes métodos:
# Alterar_editora()
# Listar_qtde_paginas()

class Livro:
    def __init__ (self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas
    
    def alterar_editora (self, nova_editora):
        self.editora=nova_editora

 
    def listar_qtde_paginas(self):
        return self.paginas
    
livro1 = Livro("O Hobit","J. R. R. Tolken","etica" , 600)
print("Editora Atual: ",livro1.editora)
livro1.alterar_editora("Harpercollins")
print("Editora nova: ", livro1.editora)

print("Quantidade de paginas: ", livro1.listar_qtde_paginas())

