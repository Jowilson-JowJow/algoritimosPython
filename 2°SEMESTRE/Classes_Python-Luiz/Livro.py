class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def alterar_editora(self, nova_editora):
        """Altera o nome da editora do livro"""
        self.editora = nova_editora
        print(f"A editora foi alterada para: {self.editora}")

    def listar_qtde_paginas(self):
        """Exibe o número de páginas do livro"""
        print(f"O livro '{self.nome}' tem {self.paginas} páginas.")

livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "HarperCollins", 1200)

livro1.listar_qtde_paginas()  
livro1.alterar_editora("Penguin Random House")  
livro1.listar_qtde_paginas()  