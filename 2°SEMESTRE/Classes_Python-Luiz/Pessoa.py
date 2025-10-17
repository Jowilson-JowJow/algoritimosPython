class Pessoa:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, notas):
        super().__init__(matricula, nome, idade)
        self.notas = notas  
        self.media = 0      

    def calcular_media(self):
        if len(self.notas) > 0:
            self.media = sum(self.notas) / len(self.notas)
            print(f"Média do aluno {self.nome}: {self.media}")
        else:
            print("Nenhuma nota registrada.")

    def estudar(self):
        print(f"O aluno {self.nome} está estudando.")

class Professor(Pessoa):
    def __init__(self, matricula, nome, idade, formacao, disciplina, carga_horaria, salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.salario = salario

    def lecionar(self):
        print(f"O professor {self.nome} está lecionando {self.disciplina}.")

aluno1 = Aluno("A001", "Lucas", 16, [7.5, 8.0, 9.0])
aluno1.estudar()
aluno1.calcular_media()

professor1 = Professor("P001", "Carla", 40, "Matemática", "Álgebra", 20, 3500)
professor1.lecionar()