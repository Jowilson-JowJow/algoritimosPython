# Crie uma classe que modele uma aluno
# (a) Atributos: nome, n´umero de matr´ıcula e curso
# (b) M´etodos: mostrar curso e alterar curso

class Aluno:

    def __init__(self, nome, num_matricula, curso):
        self.nome = nome
        self.num_matricula = num_matricula
        self.curso = curso

    def mostrar_curso(self):
        return self.curso
    
    def alterar_curso(self):
        self.curso = input("Digite o novo curso: ")
        return self.curso


aluno1 = Aluno("jow",1,"ADS")
curso_aluno=aluno1.mostrar_curso()
print(curso_aluno)

novo_curso = aluno1.alterar_curso()
print(novo_curso)