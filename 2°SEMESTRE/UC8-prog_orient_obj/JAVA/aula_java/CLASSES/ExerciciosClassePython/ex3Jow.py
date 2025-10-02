# 3 - Classe Aluno: Crie uma classe que modele um aluno. Esta classe deve possuir os seguintes atributos:
# Nome;
# RA;
# Nota 1, nota 2, nota 3, nota 4;
# A classe deve ter o seguintes método:
# Mostrar_situacao: (APROVADO / EXAME / REPROVADO). Considere que, nesse caso, a média final é calculada pela média aritmética simples de todas as notas e que o aluno é aprovado somente se obtiver média maior ou igual a sete. Exame entre 5 e 6.9. Reprovado abaixo de 5
# A situação será retornada a partir das notas obtidas pelo aluno.


class Aluno:
    def __init__(self, nome, RA, n1, n2, n3, n4):
        self.nome = nome
        self.RA = RA
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.media = (n1+n2+n3+n4)/4
    def mostrar_situacao(self):
        if (self.media<5):
            return "Reprovado!!!"
        elif (self.media>=5 and self.media<7):
            return "Exame!!!"
        else:
            return "Aprovado"


aluno1=Aluno("joão",10234,8,7,6,7)
print(f"Nome: {aluno1.nome} \nMedia: {aluno1.media:.2f} \nSituação: {aluno1.mostrar_situacao()}")