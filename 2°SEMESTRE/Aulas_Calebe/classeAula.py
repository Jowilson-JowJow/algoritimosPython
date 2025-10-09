
class Aluno:
    def __init__(self, nome , matricula):
        self.nome = nome
        self.matricula = matricula

    def exibirNome(self):
        return self.nome


aluno1=Aluno("JowJow","RA 20/2025")
nomeAluno=aluno1.exibirNome()
print(f"O nome do aluno é {nomeAluno}")