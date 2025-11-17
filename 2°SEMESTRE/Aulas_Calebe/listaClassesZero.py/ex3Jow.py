# Crie uma classe representando os alunos de um determinado curso. 
# A classe deve conter os atributos matrícula do aluno, nome, nota da primeira prova,
# nota da segunda prova e nota da terceira prova. 
# Crie métodos para acessar o nome e a média do aluno.
# (a) Permita ao usuário entrar com os dados de 5 alunos.
# (b) Encontre o aluno com maior média geral.
# (c) Encontre o aluno com menor média geral
# (d) Para cada aluno diga se ele foi aprovado ou reprovado (mínimo 6)

class Alunos: 
    def __init__(self, nome, matricula, nota1, nota2, nota3):
        self.nome = nome
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    
    def getnome(self):
        return self.nome
    
    def media(self):
        media_aluno = (self.nota1 + self.nota2 + self.nota3) / 3
        return media_aluno


lista_aluno = []

for i in range(0, 5):
    nome = input("Informe o nome do aluno: ")
    matricula = input("Informe a matrícula do aluno: ")
    nota1 = int(input("Informe a nota da prova 1: "))
    nota2 = int(input("Informe a nota da prova 2: "))
    nota3 = int(input("Informe a nota da prova 3: "))
    
    aluno = Alunos(nome, matricula, nota1, nota2, nota3)
    lista_aluno.append(aluno)


maior_media = lista_aluno[0].media()
aluno_maior = lista_aluno[0].getnome()

menor_media = lista_aluno[0].media()
aluno_menor = lista_aluno[0].getnome()

print("\nMédias e situação dos alunos:\n")

for aluno in lista_aluno:
    media = aluno.media()
    nome = aluno.getnome()
    
    print(f"Aluno: {nome} | Média: {media:.2f}")
    
    if media >= 6:
        print("Situação: Aprovado\n")
    else:
        print("Situação: Reprovado\n")
    
    if media > maior_media:
        maior_media = media
        aluno_maior = nome
    
    if media < menor_media:
        menor_media = media
        aluno_menor = nome


print(f"Aluno com maior média: {aluno_maior} | Média = {maior_media:.2f}")
print(f"Aluno com menor média: {aluno_menor} | Média = {menor_media:.2f}")
