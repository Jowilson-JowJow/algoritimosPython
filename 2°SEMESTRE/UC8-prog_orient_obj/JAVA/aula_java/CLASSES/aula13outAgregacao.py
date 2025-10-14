class Aluno:
    def __init__(self, nome, ra):
        self.nome = nome
        self.ra = ra

class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno:object):
        self.alunos.append(aluno)

    def lista_alunos(self):
        for item in self.alunos:
            print(f"nome: {item.nome} | Ra: {item.ra}")



    
a1=Aluno("jowjow","12356")
a2=Aluno("jow","51235")
a3=Aluno("prof","235")
a4=Aluno("jowfisico","5135")

faculdade = Universidade("SENAC MS")
print (len(faculdade.alunos))
faculdade.adicionar_aluno(a1)
faculdade.adicionar_aluno(a2)
faculdade.adicionar_aluno(a3)
faculdade.adicionar_aluno(a4)
print(len(faculdade.alunos))

faculdade.lista_alunos()
