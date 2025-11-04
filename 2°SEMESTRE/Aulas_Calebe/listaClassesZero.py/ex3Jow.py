# Crie uma classe representando os alunos de um determinado curso. A classe deve
# conter os atributos matr´ıcula do aluno, nome, nota da primeira prova, nota da segunda
# prova e nota da terceira prova. Crie m´etodos para acessar o nome e a m´edia do aluno.
# (a) Permita ao usu´ ario entrar com os dados de 5 alunos.
# (b) Encontre o aluno com maior m´edia geral.
# (c) Encontre o aluno com menor m´edia geral
# (d) Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 6 para
# aprovac¸ ˜ao.

class Alunos:
    
    def __init__(self, nome, matricula, nota1,nota2, nota3):
        self.nome = nome
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def getnome(self):
        return self.nome
    
    def media(self):
        media_aluno = (self.nota1 + self.nota2 + self.nota3)/3  
        return media_aluno
    
     
lista_aluno =[]    
for i in range(0,2):
    nome = input("Infome o nome do aluno: ")
    matricula = input("Infome a matricula do aluno: ")
    nota1 = int(input("Infome a nota1 do aluno: "))
    nota2 = int(input("Infome a nota2 do aluno: "))
    nota3 = int(input("Infome a nota3 do aluno: "))
    aluno = Alunos(nome, matricula, nota1,nota2, nota3)
    lista_aluno.append(aluno)


nomes_de_alunos = []

for i in range(0, 2):
    media_do_aluno = lista_aluno[i].media()
    nome_de_aluno = lista_aluno[i].getnome()
    a= {"media": media_do_aluno, "nome": nome_de_aluno}
    nomes_de_alunos.append(a)

   
for i in range(0,2):##não deu certo
    print(nomes_de_alunos[i]["media"])
    print(nomes_de_alunos[i]["nome"])







