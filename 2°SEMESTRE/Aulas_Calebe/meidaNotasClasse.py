#criar uma classe media de notas de alunos com os atributos: nome, turma, nota1, nota2, nota3, nota4, sendo que a nota4 tem peso 2 e com o metodo de retornar a maior e a menor media com o nome e turma do aluno.

#criando a classe para o objeto media comm os atributos turma, nome, notas
class Media():
    def __init__(self, turma, nome, nota1, nota2, nota3, nota4):
        self.turma = turma
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
    #criando o metodo para bucar turma
    def get_turma(self):
        return self.turma

    #criando o metdo para buscar o nome
    def get_nome(self):
        return self.nome
    
    #criando metodo para gerar a media
    def media_aluno(self):
        media_alunos = (self.nota1+self.nota2+self.nota3+self.nota4*2)/5
        return media_alunos
    
lista_media=[]
for i in range(0,6):#cria os objetos da classe Media
    turma=input("Digite a truma do aluno: ")
    nome = input("Digite o nome do aluno: ")
    nota1 = int(input("Digite a nota 1 do aluno: "))
    nota2 = int(input("Digite a nota 2 do aluno: "))
    nota3 = int(input("Digite a nota 3 do aluno: "))
    nota4 = int(input("Digite a nota 4 do aluno: "))

    medias = Media(turma, nome, nota1, nota2, nota3, nota4) #cria o objeto e sala na variavel media

    lista_media.append(medias)# adiciona o objeto criado na lista de media

#é o teste de print para verificar se os objetos estavam na lista de media
# #printa os obetos da classe media que esta na lista de media
# for media in lista_media:
#     print(f"Turma: {media.turma} | Nome: {media.nome} |Media: {media.media_aluno():.2f}")

maior_media = lista_media[0].media_aluno()
turma_maior = lista_media[0].get_turma()
nome_maior = lista_media[0].get_nome()

menor_media = lista_media[0].media_aluno()
turma_menor = lista_media[0].get_turma()
nome_menor= lista_media[0].get_nome()


for media in lista_media:
    media_atual = media.media_aluno()
    turma_atual=media.get_turma()
    nome_atual = media.get_nome()

    if media_atual > maior_media:
        maior_media=media_atual
        turma_maior=turma_atual
        nome_maior = nome_atual
    
    if media_atual < menor_media:
        menor_media=media_atual
        turma_menor=turma_atual
        nome_menor = nome_atual

print(f"Maior Media\nTurma: {turma_maior} | Nome: {nome_maior} | Média: {maior_media:.2f}")
print(f"Menor Media\nTurma: {turma_menor} | Nome: {nome_menor} | Média: {menor_media:.2f}")


