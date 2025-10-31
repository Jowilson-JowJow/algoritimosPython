# Crie uma classe representando os alunos de um determinado curso. A classe deve
# conter os atributos matr´ıcula do aluno, nome, nota da primeira prova, nota da segunda
# prova e nota da terceira prova. Crie m´etodos para acessar o nome e a m´edia do aluno.
# (a) Permita ao usu´ ario entrar com os dados de 5 alunos.
# (b) Encontre o aluno com maior m´edia geral.
# (c) Encontre o aluno com menor m´edia geral
# (d) Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 6 para
# aprovac¸ ˜ao.

class Alunos:
    
    def __init__(self, matricula, nome, nota1,nota2, nota3):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def getnome(self):
        return self.nome
    
    def media(self):
        media_aluno = (self.nota1 + self.nota2 + self.nota3)/3  
        return media_aluno
    
    
    
lista_aluno =[]    
for i in range(1,6):
    nome = input("Infome o nome do aluno: ")
    matricula = input("Infome a matricula do aluno: ")
    nota1 = input("Infome a nota1 do aluno: ")
    nota2 = input("Infome a nota2 do aluno: ")
    nota3 = input("Infome a nota3 do aluno: ")
    aluno = Alunos(matricula, nome, nota1,nota2, nota3)
    lista_aluno.append(aluno)







for i in range(0,5):
    al = lista_aluno[i] 
    print(al.media()) 

# aluno1=Alunos("1205-2025","jowjow",8,7,9)
# media_aluno=aluno1.media()
# print(f"A media do aluno {aluno1.getnome()} é: {media_aluno:.2f}") 
