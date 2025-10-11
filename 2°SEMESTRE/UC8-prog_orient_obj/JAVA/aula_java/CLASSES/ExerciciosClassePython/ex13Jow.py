# 13 - Classe Pessoa: Crie uma super classe que modele uma Pessoa. Esta classe deve possuir os seguintes atributos:
# Matricula; Nome; Idade;  
# Subclasses:
# Defina as subclasses de Pessoa serão Aluno e Professor, estas devem conter além dos atributos herdados de Pessoa seus atributos identificadores, ex: Classe Aluno (NOTAS; MEDIA). 
# Classe Professor (Formacao, Disciplina, Carga Horária e Salario);
# Classe Aluno (Atrubuto NOTAS que deve ser uma Lista, Atributo média);
# Você deve criar métodos específicos para cada subclasse, ex: calcular_media, estudar, lecionar.

class Pessoa():
    def __init__(self, matricula, nome, idade):
        self.matricula=matricula
        self.nome=nome
        self.idade=idade
    

class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade):
        super().__init__(matricula, nome, idade)
        self.notas=[]
        self.media=0

    def lancar_notas(self,notas:list):
        self.notas = notas
        return self.__calcula_media()

    def __calcula_media(self):
        self.media = sum(self.notas) / len(self.notas)
        return self.media
        

class Professor(Pessoa):
    def __init__(self, matricula, nome, idade, formacao, disciplina, cargaHoraria, salario):
        super().__init__(matricula, nome, idade)
        self.formacao=formacao
        self.disciplina=disciplina
        self.cargaHoraria=cargaHoraria
        self.salario=salario

    
    

    

a1 = Aluno(123,"JOW",32)

media = a1.lancar_notas([9,8,7,5])

print(media)